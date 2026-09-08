#!/usr/bin/env python3
"""Render tmp/hlist-<date>-overnight.html from tmp/overnight-<date>/*/status.json.
Safe to run concurrently: it regenerates the whole page from files each time.
Usage: scripts/overnight_hlist.py 20260906
"""
import json, sys, html, datetime as dt
from pathlib import Path
date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().strftime("%Y%m%d")
root = Path(__file__).resolve().parent.parent
src = root / "tmp" / f"overnight-{date}"
out = root / "tmp" / f"hlist-{date}-overnight.html"
e = html.escape
items = []
for f in sorted(src.glob("*/status.json")):
    try:
        items.append(json.loads(f.read_text()))
    except Exception as ex:
        items.append({"repo": f.parent.name, "status": "error", "recap": f"unreadable status.json: {ex}", "plan": []})

def dot(s):
    return {"done": "#2e9e5b", "working": "#d9930d", "blocked": "#d64545", "planning": "#d9930d"}.get(s, "#9aa3ad")

def hrs(x):
    return f"{x:g}h" if isinstance(x, (int, float)) else ""

def dur(it):
    est = sum(p.get("est_hours") or 0 for p in it.get("plan", []))
    act = sum(p.get("actual_hours") or 0 for p in it.get("plan", []))
    if it.get("status") == "done":
        return f"{act:g}h" + (f" / ~{est:g}h est" if est else "")
    return f"{act:g}h elapsed / ~{est:g}h est" if act else f"~{est:g}h est"

rows = []
for it in items:
    plan = "".join(
        f'<li><span class="d" style="background:{dot(p.get("status"))}"></span>{e(p.get("item",""))}'
        f'<span class="m">{hrs(p.get("est_hours"))}{(" → " + hrs(p.get("actual_hours"))) if p.get("actual_hours") else ""}</span>'
        f'{("<div class=v>" + e(p["verification"]) + "</div>") if p.get("verification") else ""}</li>'
        for p in it.get("plan", []))
    prs = " ".join(f'<a href="{e(u)}">{e(u.rsplit("/",1)[-1] if "/" in u else u)}</a>' for u in it.get("prs", []))
    need = "".join(f"<li>{e(x)}</li>" for x in it.get("needs_user", []))
    rows.append(f'''<details><summary><span class="d" style="background:{dot(it.get("status"))}"></span>
<b>{e(it.get("repo",""))}</b> <span class="t">{e(it.get("title",""))}</span><span class="r">{e(dur(it))}</span></summary>
<div class="b">{("<p class=rc>" + e(it.get("recap","")) + "</p>") if it.get("recap") else ""}
{("<ol class=p>" + plan + "</ol>") if plan else "<p class=rc>plan not written yet</p>"}
{("<p><b>PRs:</b> " + prs + "</p>") if prs else ""}{("<p><b>Needs you:</b></p><ul>" + need + "</ul>") if need else ""}
<p class="m">updated {e(it.get("updated",""))}</p></div></details>''')

out.write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Overnight {date}</title><style>
:root{{--bg:#f4f5f2;--card:#fcfcfa;--ink:#1c1f1a;--mute:#626a5e;--line:#dfe2da}}
@media(prefers-color-scheme:dark){{:root{{--bg:#121410;--card:#1a1d17;--ink:#e6e8e0;--mute:#99a191;--line:#2a2e26}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;overflow-x:hidden}}
main{{max-width:720px;margin:0 auto;padding:14px 10px 40px}}h1{{font-size:19px;margin:6px 0 2px}}.sub{{color:var(--mute);font-size:13px;margin-bottom:12px}}
details{{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:8px 0}}summary{{list-style:none;cursor:pointer;padding:11px 12px;display:flex;align-items:center;gap:8px}}
summary::-webkit-details-marker{{display:none}}.d{{width:10px;height:10px;border-radius:50%;flex:none;display:inline-block}}
.t{{color:var(--mute);font-size:13px;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.r{{color:var(--mute);font-size:12px;white-space:nowrap;font-variant-numeric:tabular-nums}}
.b{{padding:0 12px 12px;border-top:1px solid var(--line);font-size:14px}}.rc{{margin:10px 0}}.p{{margin:0;padding-left:18px}}.p li{{margin:5px 0}}.p .d{{width:8px;height:8px;margin-right:6px}}
.m{{color:var(--mute);font-size:12px;margin-left:6px}}.v{{color:var(--mute);font-size:12px;margin-left:14px}}a{{color:#2f6fed;text-decoration:none}}
</style></head><body><main><h1>Overnight run {date[:4]}-{date[4:6]}-{date[6:]}</h1>
<div class="sub">{len(items)} repos · {sum(1 for i in items if i.get("status")=="done")} done · {sum(1 for i in items if i.get("status") in ("working","planning"))} in progress · {sum(1 for i in items if i.get("status")=="blocked")} blocked · rendered {dt.datetime.now().strftime("%H:%M")}</div>
{"".join(rows) or "<p>no status files yet</p>"}</main></body></html>''')
print(out)
