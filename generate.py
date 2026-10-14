import json,os,html
B="AI for the Task"; SITE_ORIGIN="https://aiforthetask.com"; BASE=SITE_ORIGIN+"/"; MON="Oct 2026"; CSSV="20261013logos"
CATS=[("resumes","Resumes","#6366f1","Write and polish CVs and cover letters"),("logos","Logos","#ec4899","Generate brand marks and icons"),("video","Video","#f97316","Create and edit short clips"),("homework","Homework","#10b981","Step by step study help"),("writing","Writing","#0ea5e9","Drafts, rewrites and grammar"),("images","Images","#a855f7","Text to image and photo edits"),("voice","Voice","#ef4444","Text to speech and voice cloning"),("coding","Coding","#14b8a6","Autocomplete, debugging, explainers"),("presentations","Presentations","#eab308","Slides from a prompt or doc"),("research","Research","#3b82f6","Cited answers and paper summaries")]
CD={c[0]:c for c in CATS}
def page(path,title,desc,crumbs,body,ld=[]):
  r="../"*path.count("/")
  L=[{"@context":"https://schema.org","@type":"Organization","name":B,"url":BASE,"logo":BASE+"img/brand/option-b-icon-512.png","parentOrganization":{"@type":"Organization","name":"Atulit"}},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate([("Home","")]+crumbs)]}]+ld
  cr=" / ".join([f'<a href="{r}">Home</a>']+[f'<a href="{r}{u}">{html.escape(n)}</a>' for n,u in crumbs])
  crumb_block=f'<div class="w"><div class="crumb">{cr}</div></div>' if crumbs else ''
  o=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><meta name="robots" content="noindex, nofollow"><link rel="canonical" href="{BASE}{path}"><link rel="icon" href="{r}img/brand/option-b-icon.svg" type="image/svg+xml"><link rel="icon" href="{r}img/brand/option-b-icon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="{r}img/brand/option-b-icon-180.png"><link rel="stylesheet" href="{r}style.css?v={CSSV}"><script type="application/ld+json">{json.dumps(L)}</script></head><body>
<div class="sample">Prototype by Atulit. Free tier facts are real, read from official pricing pages on Oct 13, 2026. Not indexed.</div>
<header><div class="w nav"><a class="logo" href="{r}"><img src="{r}img/brand/option-b-wordmark.svg" alt="{B}" height="34"></a><nav><a href="{r}#tasks">Tasks</a><a href="{r}task/resumes/">Resumes</a><a href="{r}task/images/">Images</a><a href="{r}task/coding/">Coding</a><a href="{r}how-we-test/">How we test</a><a href="{r}about/">About</a></nav></div></header>
{crumb_block}{body}
<footer><div class="w"><p><a class="logo" href="{r}"><img src="{r}img/brand/option-b-wordmark.svg" alt="{B}" height="28"></a><br>by Atulit. Free AI tools for the task.</p><a href="{r}#tasks">All tasks</a><a href="{r}how-we-test/">How we test</a><a href="{r}disclosure/">Affiliate disclosure</a><a href="{r}about/">About</a><p>Funded by affiliate links. We never rank by payout.</p></div></footer>
<script src="{r}app.js"></script></body></html>'''
  os.makedirs(path or ".",exist_ok=True); open(path+"index.html","w").write(o)
mono=lambda t,sz="":f'<div class="mono" style="background:{CD[t["task"]][2]};{sz}">{t["name"][:2]}</div>'
def catgrid(r): return '<div class="grid">'+"".join(f'<a class="cat" href="{r}task/{s}/"><div class="mono" style="background:{c}">{n[:2]}</div><b>{n}</b><small>{d}</small></a>' for s,n,c,d in CATS)+'</div>'
NEWS='''<div class="w"><div class="news"><div><h2>The 5 best new free tools, every Friday</h2><p style="opacity:.85;margin:6px 0 0">No spam. Unsubscribe anytime. From AI for the Task.</p></div><form id="nl"><input type="email" required placeholder="you@example.com" aria-label="Email"><button class="btn">Subscribe</button></form><div class="ok" id="nlok">You are in! Check your inbox to confirm.</div></div></div>'''
DISC=lambda r:f'<div class="disc">Disclosure: "Try it" buttons are affiliate links (marked sponsored). We may earn a commission at no cost to you. We never rank by payout. <a href="{r}disclosure/">Learn more</a></div>'

from tools_data import T,CHECKED
ALL={t["slug"]:t for t in T}
def tools(s): return [t for t in T if t["task"]==s]
CATS=[c for c in CATS if tools(c[0])]
CD={c[0]:c for c in CATS}
SRC=lambda t:f'<a href="{t["url"]}" rel="nofollow">official pricing page</a>'
NOTE='<p style="font-size:13px;color:var(--mut)">Facts come only from each tool\'s official pricing page, checked '+CHECKED+'. "Not stated" means the page did not say. Plans change often, so confirm on the official page before you sign up.</p>'
page("",f"{B}: Free AI Tools by Task, Real Free Tier Limits","Free AI tools sorted by task with free tier limits taken from official pricing pages.",[],f'''
<section class="hero"><div class="w"><span class="stamp">● Last checked {CHECKED}</span><h1>Every <span class="grad">free AI tool</span>,<br>for the task.</h1><p class="lead">Free tier limits taken from each tool's official pricing page, with a source link and check date on every entry.</p></div></section>
<div class="w"><h2 id="tasks">Pick a task</h2>{catgrid("")}<h2>All {len(T)} tools</h2>
<div class="trend">{"".join(f'<a class="tc" href="tools/{t["slug"]}/">{mono(t)}<div><b style="color:var(--ink)">{t["name"]}</b><br><small>{CD[t["task"]][1]}</small></div></a>' for t in T)}</div>{NOTE}</div>''',
[{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":BASE+f"task/{c[0]}/","name":c[1]} for i,c in enumerate(CATS)]}])
for s,n,c,d in CATS:
  ts=tools(s); r="../../"
  rows="".join(f'<tr><td><a href="{r}tools/{t["slug"]}/"><b>{t["name"]}</b></a></td><td>{t["free"]}</td><td>{t["paid"]}</td><td>{t["card"]}</td><td><a href="{t["url"]}" rel="nofollow">Source</a><br><small>{CHECKED}</small></td></tr>' for t in ts)
  page(f"task/{s}/",f"Free AI {n} Tools: Real Free Tier Limits",d,[(n,f"task/{s}/")],f'''
<div class="w"><main><span class="stamp">● Last checked {CHECKED}</span><h1>Free AI tools for {n.lower()}</h1><p class="lead" style="margin:0 0 18px">{d}. {len(ts)} tool{"s" if len(ts)>1 else ""}, listed in no ranked order. We have not hands on tested them yet.</p>
<h2 style="margin-top:20px">Free limits compared</h2><div class="tw"><table><thead><tr><th>Tool</th><th>Free tier</th><th>Cheapest paid plan</th><th>Card needed</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>{NOTE}
<h2>Other tasks</h2><div class="sort">{"".join(f'<a href="{r}task/{x[0]}/">{x[1]}</a>' for x in CATS if x[0]!=s)}</div></main></div>''',
  [{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":t["name"],"url":BASE+f'tools/{t["slug"]}/'} for i,t in enumerate(ts)]}])
for t in T:
  r="../../"; n=CD[t["task"]][1]; alts=[x for x in tools(t["task"]) if x["slug"]!=t["slug"]]
  com=f'<tr><th>Commercial use</th><td>{t["com"]}</td></tr>' if t.get("com") else ''
  page(f'tools/{t["slug"]}/',f'Is {t["name"]} Free? Free Plan Limits (Checked {CHECKED})',f'{t["name"]} free plan limits from the official pricing page.',[(n,f'task/{t["task"]}/'),(t["name"],f'tools/{t["slug"]}/')],f'''
<div class="w"><main><div style="display:flex;gap:16px;align-items:center;margin-top:18px">{mono(t,"width:64px;height:64px;font-size:22px")}<div><h1 style="margin:0">Is {t["name"]} free?</h1><a class="pill" href="{r}task/{t["task"]}/">{n}</a> <span class="pill">Last checked {CHECKED}</span></div></div>
<p style="font-size:18px">{"No free plan." if t.get("nofree") else "Yes, there is a free plan."} {t["free"]}.</p>
<p><a class="btn ac" href="{t["url"]}" rel="nofollow" target="_blank">Open the official {t["name"]} pricing page</a></p>
<h2>Free tier facts</h2><div class="tw"><table><tr><th>Free tier</th><td>{t["free"]}</td></tr><tr><th>Cheapest paid plan</th><td>{t["paid"]}</td></tr><tr><th>Card needed</th><td>{t["card"]}</td></tr>{com}<tr><th>Source</th><td>{SRC(t)}, checked {CHECKED}</td></tr></table></div>{NOTE}
{"<h2>Other "+n.lower()+" tools</h2><div class=trend>"+"".join(f'<a class="tc" href="{r}tools/{a["slug"]}/">{mono(a)}<div><b style="color:var(--ink)">{a["name"]}</b></div></a>' for a in alts)+"</div>" if alts else ""}</main></div>''')
for p,tl,txt in [("how-we-test/","How we check",f"<p>Each free tier entry is read from the tool's official pricing page. We record only what the page states, link to it, and show the date we checked ({CHECKED}). Where a page does not say something, we write Not stated.</p><h2>Not yet done</h2><p>We have not hands on tested output quality, watermarks or privacy for these tools, so we do not rank them.</p>"),
 ("disclosure/","Affiliate disclosure",f"<p>{B} plans to be funded by affiliate links. Right now no links on this site are affiliate links. Any future ones will be marked sponsored and will never affect what we list.</p>"),
 ("about/","About "+B,f"<p>{B} is a project by Atulit. Everyone deserves to know which AI tools are actually free, and what the catch is, before signing up.</p>")]:
  page(p,tl,tl,[(tl,p)],f'<div class="w prose"><h1>{tl}</h1>{txt}</div>')
import seo_site; seo_site.build()
print("ok", B, BASE, "pages", sum(1 for _ in __import__('pathlib').Path('.').rglob('index.html')))
