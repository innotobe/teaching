#!/usr/bin/env python3
"""Regenerate index.html: one section per course folder, linking every PDF in it.

Course folder:  <year>-<term>-<name>/   e.g. 2026-fall-circuits/
Optional title: <folder>/TITLE  (first line is shown instead of the folder name)
"""
import html
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent


def course_dirs():
    dirs = [d for d in ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")]
    return sorted(dirs, key=lambda d: d.name, reverse=True)  # newest semester first


def section(d):
    title_file = d / "TITLE"
    title = title_file.read_text().splitlines()[0].strip() if title_file.exists() else d.name
    pdfs = sorted(d.rglob("*.pdf"))
    items = "\n".join(
        f'      <li><a href="{quote(p.relative_to(ROOT).as_posix())}">'
        f"{html.escape(p.relative_to(d).with_suffix('').as_posix())}</a></li>"
        for p in pdfs
    ) or "      <li class=empty>(아직 자료 없음)</li>"
    return f"""  <section>
    <h2>{html.escape(title)}</h2>
    <ul>
{items}
    </ul>
  </section>"""


page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>강의자료</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 760px; margin: 2rem auto; padding: 0 1rem; line-height: 1.6; }}
  h1 {{ border-bottom: 2px solid #333; padding-bottom: .3rem; }}
  h2 {{ margin-top: 2rem; }}
  li {{ margin: .25rem 0; }}
  a {{ text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .empty {{ color: #888; }}
</style>
</head>
<body>
  <h1>강의자료</h1>
{chr(10).join(section(d) for d in course_dirs())}
</body>
</html>
"""
(ROOT / "index.html").write_text(page)
print(f"index.html updated ({len(course_dirs())} courses)")
