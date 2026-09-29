#!/usr/bin/env python3
"""Build browser-viewable HTML pages from docs/*.md.

Usage:  python3 scripts/build-docs.py
Output: docs/<name>.html next to each .md file (open in any browser).
Markdown is rendered in the browser with marked.js (CDN).
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  :root {{ --red:#a72a2c; --ink:#1a1a1a; --gray:#5a5a5f; --line:#e4e4e7; --soft:#f6f6f7; --bg:#fff; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --ink:#ececee; --gray:#a1a1a6; --line:#2e2e32; --soft:#1c1c1f; --bg:#121214; --red:#e0585a; }}
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.65 Inter, system-ui, sans-serif; }}
  main {{ max-width:880px; margin:0 auto; padding:40px 20px 80px; }}
  h1, h2, h3 {{ font-family:"Space Grotesk", sans-serif; line-height:1.2; letter-spacing:-0.01em; }}
  h1 {{ font-size:34px; margin:0 0 8px; }}
  h2 {{ font-size:24px; margin:48px 0 14px; padding-top:24px; border-top:1px solid var(--line); }}
  h3 {{ font-size:19px; margin:28px 0 10px; }}
  a {{ color:var(--red); }}
  hr {{ border:0; margin:0; }}
  code {{ font:14px/1.4 ui-monospace, Menlo, monospace; background:var(--soft); padding:2px 6px; border-radius:5px; word-break:break-all; }}
  blockquote {{ margin:16px 0; padding:12px 16px; border-left:4px solid var(--red); background:var(--soft); border-radius:0 8px 8px 0; }}
  blockquote p {{ margin:0; }}
  .table-wrap {{ overflow-x:auto; margin:16px 0; }}
  table {{ border-collapse:collapse; width:100%; font-size:15px; }}
  th, td {{ text-align:left; padding:10px 12px; border-bottom:1px solid var(--line); vertical-align:top; }}
  th {{ background:var(--soft); font-weight:600; }}
  li {{ margin:4px 0; }}
  .tag {{ display:inline-block; font:600 11px/1 Inter, sans-serif; letter-spacing:.04em; padding:4px 7px; border-radius:999px; vertical-align:middle; }}
  .tag-client {{ background:#a72a2c; color:#fff; }}
  .tag-draft {{ background:#e4e4e7; color:#1a1a1a; }}
  .tag-placeholder {{ background:#fff3cd; color:#7a5a00; }}
  .toolbar {{ position:sticky; top:0; z-index:5; display:flex; gap:10px; align-items:center; justify-content:space-between; padding:12px 20px; background:var(--bg); border-bottom:1px solid var(--line); }}
  .toolbar strong {{ font-family:"Space Grotesk", sans-serif; font-size:15px; }}
  .btn {{ display:inline-flex; align-items:center; gap:6px; padding:8px 14px; border:1px solid var(--line); border-radius:999px; background:var(--bg); color:var(--ink); font:600 13px/1 Inter, sans-serif; cursor:pointer; white-space:nowrap; }}
  .btn:hover {{ border-color:var(--red); color:var(--red); }}
  .btn-primary {{ background:var(--red); border-color:var(--red); color:#fff; }}
  .btn-primary:hover {{ color:#fff; filter:brightness(1.1); }}
  .toc {{ margin:24px 0 8px; padding:18px 20px; background:var(--soft); border-radius:12px; }}
  .toc p {{ margin:0 0 8px; font:600 12px/1 Inter, sans-serif; letter-spacing:.06em; text-transform:uppercase; color:var(--gray); }}
  .toc ol {{ margin:0; padding-left:20px; columns:2; column-gap:28px; }}
  .toc a {{ text-decoration:none; }}
  .toc a:hover {{ text-decoration:underline; }}
  @media (max-width:600px) {{ .toc ol {{ columns:1; }} }}
  .doc-section {{ position:relative; scroll-margin-top:64px; }}
  .doc-section > h2 {{ display:flex; align-items:center; justify-content:space-between; gap:12px; }}
  .doc-section > h2 .btn {{ font-size:12px; padding:6px 12px; }}
  .toast {{ position:fixed; left:50%; bottom:24px; transform:translate(-50%, 20px); opacity:0; padding:10px 18px; border-radius:999px; background:#1a1a1a; color:#fff; font:600 14px/1 Inter, sans-serif; transition:all .2s ease; pointer-events:none; white-space:nowrap; }}
  .toast.show {{ opacity:1; transform:translate(-50%, 0); }}
  .swatch {{ display:inline-block; width:14px; height:14px; border-radius:3px; vertical-align:-2px; margin-right:6px; border:1px solid var(--line); }}
</style>
</head>
<body>
<div class="toolbar">
  <strong>{title}</strong>
  <button class="btn btn-primary" type="button" id="copy-all">Copy entire doc</button>
</div>
<main id="doc"></main>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
  const md = {md};
  const el = document.getElementById('doc');
  el.innerHTML = marked.parse(md);
  // Wrap tables for mobile scrolling
  el.querySelectorAll('table').forEach(t => {{ const w = document.createElement('div'); w.className = 'table-wrap'; t.replaceWith(w); w.appendChild(t); }});
  // Colour-code [CLIENT] / [DRAFT] / [PLACEHOLDER] labels
  el.innerHTML = el.innerHTML
    .replace(/<strong>\\[CLIENT\\]<\\/strong>/g, '<span class="tag tag-client">CLIENT</span>')
    .replace(/<strong>\\[DRAFT([^\\]]*)\\]<\\/strong>/g, '<span class="tag tag-draft">DRAFT$1</span>')
    .replace(/<strong>\\[PLACEHOLDER\\]<\\/strong>/g, '<span class="tag tag-placeholder">PLACEHOLDER</span>');
  // Colour swatches next to hex codes
  el.querySelectorAll('code').forEach(c => {{
    if (/^#[0-9a-f]{{6}}$/i.test(c.textContent)) c.insertAdjacentHTML('beforebegin', '<span class="swatch" style="background:' + c.textContent + '"></span>');
  }});

  // Group each H2 and its content into a <section>; build contents list
  const slug = t => t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const toc = document.createElement('nav');
  toc.className = 'toc';
  toc.innerHTML = '<p>Jump to</p><ol></ol>';
  el.querySelectorAll('h2').forEach(h2 => {{
    const sec = document.createElement('section');
    sec.className = 'doc-section';
    sec.id = slug(h2.textContent);
    h2.before(sec);
    let n = h2.nextSibling;
    sec.appendChild(h2);
    while (n && !(n.nodeType === 1 && n.tagName === 'H2')) {{ const next = n.nextSibling; if (!(n.nodeType === 1 && n.tagName === 'HR')) sec.appendChild(n); else n.remove(); n = next; }}
    toc.querySelector('ol').insertAdjacentHTML('beforeend', '<li><a href="#' + sec.id + '">' + h2.textContent + '</a></li>');
    const btn = document.createElement('button');
    btn.className = 'btn';
    btn.type = 'button';
    btn.textContent = 'Copy section';
    btn.addEventListener('click', () => copyNode(sec, 'Section copied'));
    h2.appendChild(btn);
  }});
  const firstSection = el.querySelector('.doc-section');
  if (firstSection) firstSection.before(toc);

  // Copy as rich text (keeps headings, bold, tables) with plain-text fallback
  function cleanClone(node) {{
    const c = node.cloneNode(true);
    c.querySelectorAll('button, .swatch, .toc').forEach(x => x.remove());
    return c;
  }}
  async function copyNode(node, msg) {{
    const c = cleanClone(node);
    const html = c.innerHTML, text = c.innerText || c.textContent;
    try {{
      await navigator.clipboard.write([new ClipboardItem({{
        'text/html': new Blob([html], {{ type: 'text/html' }}),
        'text/plain': new Blob([text], {{ type: 'text/plain' }})
      }})]);
    }} catch (e) {{
      // Fallback: select a hidden copy and use execCommand
      const tmp = document.createElement('div');
      tmp.style.cssText = 'position:fixed;left:-9999px;top:0';
      tmp.appendChild(c);
      document.body.appendChild(tmp);
      const r = document.createRange(); r.selectNodeContents(tmp);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
      document.execCommand('copy');
      sel.removeAllRanges(); tmp.remove();
    }}
    const t = document.getElementById('toast');
    t.textContent = msg + ' — paste into your doc';
    t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 2200);
  }}
  document.getElementById('copy-all').addEventListener('click', () => copyNode(el, 'Entire doc copied'));
</script>
</body>
</html>
"""

for md_path in sorted(DOCS.glob("*.md")):
    text = md_path.read_text(encoding="utf-8")
    first = next((l for l in text.splitlines() if l.startswith("# ")), md_path.stem)
    title = first.lstrip("# ").strip()
    # json.dumps gives a safe JS string; escape "</" so it can't close the <script> tag
    md_js = json.dumps(text).replace("</", "<\\/")
    out = md_path.with_suffix(".html")
    out.write_text(TEMPLATE.format(title=html.escape(title), md=md_js), encoding="utf-8")
    print(f"built {out.relative_to(ROOT)}")
