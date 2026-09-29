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
  .swatch {{ display:inline-block; width:14px; height:14px; border-radius:3px; vertical-align:-2px; margin-right:6px; border:1px solid var(--line); }}
</style>
</head>
<body>
<main id="doc"></main>
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
