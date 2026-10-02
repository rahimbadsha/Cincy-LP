#!/usr/bin/env node
// Full-page, high-resolution JPG capture of a page using local Google Chrome (no dependencies).
//
// Usage:
//   node scripts/capture.mjs <url> <out.jpg> [width=1440] [scale=2] [mobile=0]
// Example:
//   node scripts/capture.mjs http://localhost:5500/versions/v7/ exports/v7-desktop.jpg 1440 2
//   node scripts/capture.mjs http://localhost:5500/versions/v7/ exports/v7-mobile.jpg 390 3 1

import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, mkdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';

const [url, out, width = '1440', scale = '2', mobile = '0'] = process.argv.slice(2);
if (!url || !out) { console.error('Usage: node scripts/capture.mjs <url> <out.jpg> [width] [scale] [mobile]'); process.exit(1); }

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = 9333 + Math.floor(Math.random() * 500);
const profile = mkdtempSync(join(tmpdir(), 'cc-capture-'));
const sleep = ms => new Promise(r => setTimeout(r, ms));

const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
  `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`, 'about:blank'
], { stdio: 'ignore' });

async function main() {
  // Wait for DevTools endpoint
  let target;
  for (let i = 0; i < 50 && !target; i++) {
    try { target = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json(); }
    catch { await sleep(200); }
  }
  if (!target) throw new Error('Chrome DevTools did not start');

  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r, { once: true }));
  let id = 0; const pending = new Map(); const events = [];
  ws.addEventListener('message', e => {
    const m = JSON.parse(e.data);
    if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
    else if (m.method) events.push(m.method);
  });
  const send = (method, params = {}) => new Promise((res, rej) => {
    const i = ++id; pending.set(i, m => m.error ? rej(new Error(method + ': ' + m.error.message)) : res(m.result));
    ws.send(JSON.stringify({ id: i, method, params }));
  });
  const evaluate = async expr => (await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })).result.value;

  const w = Number(width), dpr = Number(scale), isMobile = mobile === '1';
  await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: isMobile ? 844 : 900, deviceScaleFactor: dpr, mobile: isMobile });
  await send('Page.navigate', { url });
  for (let i = 0; i < 100 && !events.includes('Page.loadEventFired'); i++) await sleep(100);

  // Scroll through the page so lazy content (video, HubSpot calendar) loads, then wait for it
  await evaluate(`(async () => {
    document.documentElement.style.scrollBehavior = 'auto';
    for (let y = 0; y < document.documentElement.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 250)); }
    scrollTo(0, document.documentElement.scrollHeight);
  })()`);
  const calendarReady = await evaluate(`(async () => {
    for (let i = 0; i < 60; i++) {
      const c = document.querySelector('.cc-calendar');
      if (!c || c.classList.contains('is-loaded')) return true;
      await new Promise(r => setTimeout(r, 500));
    }
    return false;
  })()`);
  await evaluate('scrollTo(0, 0)');

  // Make the viewport as tall as the page so cross-origin iframes (video, calendar) actually paint.
  // Settle twice: the calendar iframe may resize the page once it renders.
  let height = await evaluate('document.documentElement.scrollHeight');
  for (let pass = 0; pass < 2; pass++) {
    await send('Emulation.setDeviceMetricsOverride', { width: w, height, deviceScaleFactor: dpr, mobile: isMobile });
    await sleep(3000);
    height = await evaluate('document.documentElement.scrollHeight');
  }
  // Headless Chrome can't paint YouTube video frames: show the video's poster image instead,
  // and hide the fixed mobile sticky bar (it would land mid-page in a single tall image).
  await evaluate(`(() => {
    const p = document.querySelector('.cc-player[data-youtube-id]');
    if (p) {
      const img = new Image();
      img.src = 'https://i.ytimg.com/vi/' + p.dataset.youtubeId + '/maxresdefault.jpg';
      img.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:1';
      p.querySelector('.cc-player__frame').appendChild(img);
      const b = p.querySelector('.cc-player__sound'); if (b) { b.hidden = false; b.style.zIndex = 2; }
    }
    const s = document.querySelector('.cc-sticky'); if (s) s.style.display = 'none';
  })()`);
  await sleep(2000);

  const shot = await send('Page.captureScreenshot', {
    format: 'jpeg', quality: 92,
    clip: { x: 0, y: 0, width: w, height, scale: 1 }
  });
  mkdirSync(dirname(out), { recursive: true });
  writeFileSync(out, Buffer.from(shot.data, 'base64'));
  console.log(`saved ${out}  ${w * dpr}x${height * dpr}px  calendar ${calendarReady ? 'loaded' : 'NOT loaded'}`);
  ws.close();
}

main().catch(e => { console.error(e.message); process.exitCode = 1; })
  .finally(() => { chrome.kill('SIGKILL'); try { rmSync(profile, { recursive: true, force: true }); } catch {} });
