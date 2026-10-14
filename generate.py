import json,os,html
B="AI for the Task"; SITE_ORIGIN="https://aiforthetask.com"; BASE=SITE_ORIGIN+"/"; MON="Oct 2026"; CSSV="20261013logos"
CATS=[("resumes","Resumes","#6366f1","Write and polish CVs and cover letters"),("logos","Logos","#ec4899","Generate brand marks and icons"),("video","Video","#f97316","Create and edit short clips"),("homework","Homework","#10b981","Step by step study help"),("writing","Writing","#0ea5e9","Drafts, rewrites and grammar"),("images","Images","#a855f7","Text to image and photo edits"),("voice","Voice","#ef4444","Text to speech and voice cloning"),("coding","Coding","#14b8a6","Autocomplete, debugging, explainers"),("presentations","Presentations","#eab308","Slides from a prompt or doc"),("research","Research","#3b82f6","Cited answers and paper summaries")]
CD={c[0]:c for c in CATS}
N={"resumes":["ResumeRocket","CVSmith","HireDraft","Lettera","JobPolish"],"logos":["MarkMint","Glyphly","BrandSprout","IconForge","LogoLoom"],"video":["ClipCraft","Reelio","FrameFox","CutPilot","Vidwave"],"homework":["StudyOwl","MathMentor","Quizzy","Explainr","TutorBee"],"writing":["Proseful","Draftly","Wordsmith Pro","Tonely","EditBird"],"images":["Pixora","Dreamcanvas","Lumen Art","Snapforge","Hueify"],"voice":["Voxa","SpeakEasy AI","Narrato","Tonewave","Echolab"],"coding":["CodeCompass","Bugbuster","Stackmate","Syntaxa","DevPilot"],"presentations":["Slidewise","Deckly","Pitchcraft","Showpad AI","Keynova"],"research":["Citely","Scholarly","Factfinder","PaperPal X","Insightly"]}
REL={"resumes":["writing","presentations","research"],"images":["logos","video","presentations"],"writing":["resumes","research","homework"],"coding":["research","writing","homework"]}
def tools(s):
  L=[]
  for i,x in enumerate(N[s]):
    L.append(dict(name=x,slug=x.lower().replace(" ","-"),mono=x[:2],task=s,limit=["10 generations/day","3 exports/month","Unlimited drafts","50 credits/month","5 projects"][i],
     wm=[False,False,True,False,True][i],signup=["Email","None","Email","Google","Email"][i],card=[False,False,True,False,False][i],dev=["Upload","On-device","Upload","Upload","On-device"][i],
     com=[True,True,False,True,False][i],good=["Fast, clean templates","Best output quality","Great for beginners","Strong customization","Private by design"][i],
     bad=["Limited exports","Slow at peak hours","Watermark on free plan","Fewer templates","Basic editing only"][i],checked=f"Oct {12-i}, 2026",gone=(x=="JobPolish")))
  return L
ALL={t["slug"]:t for s in N for t in tools(s)}
yn=lambda v,good=True:f'<b class="{"y" if v==good else "n"}">{"Yes" if v else "No"}</b>'
def page(path,title,desc,crumbs,body,ld=[]):
  r="../"*path.count("/")
  L=[{"@context":"https://schema.org","@type":"Organization","name":B,"url":BASE,"logo":BASE+"img/brand/option-b-icon-512.png","parentOrganization":{"@type":"Organization","name":"Atulit"}},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate([("Home","")]+crumbs)]}]+ld
  cr=" / ".join([f'<a href="{r}">Home</a>']+[f'<a href="{r}{u}">{html.escape(n)}</a>' for n,u in crumbs])
  crumb_block=f'<div class="w"><div class="crumb">{cr}</div></div>' if crumbs else ''
  o=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><meta name="robots" content="noindex, nofollow"><link rel="canonical" href="{BASE}{path}"><link rel="icon" href="{r}img/brand/option-b-icon.svg" type="image/svg+xml"><link rel="icon" href="{r}img/brand/option-b-icon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="{r}img/brand/option-b-icon-180.png"><link rel="stylesheet" href="{r}style.css?v={CSSV}"><script type="application/ld+json">{json.dumps(L)}</script></head><body>
<div class="sample">Sample data. Prototype by Atulit. Tools and numbers are made up.</div>
<header><div class="w nav"><a class="logo" href="{r}"><img src="{r}img/brand/option-b-wordmark.svg" alt="{B}" height="34"></a><nav><a href="{r}#tasks">Tasks</a><a href="{r}task/resumes/">Resumes</a><a href="{r}task/images/">Images</a><a href="{r}compare/resumerocket-vs-cvsmith/">Compare</a><a href="{r}how-we-test/">How we test</a><a href="{r}about/">About</a></nav></div></header>
{crumb_block}{body}
<footer><div class="w"><p><a class="logo" href="{r}"><img src="{r}img/brand/option-b-wordmark.svg" alt="{B}" height="28"></a><br>by Atulit. Free AI tools for the task.</p><a href="{r}#tasks">All tasks</a><a href="{r}how-we-test/">How we test</a><a href="{r}disclosure/">Affiliate disclosure</a><a href="{r}about/">About</a><p>Funded by affiliate links. We never rank by payout.</p></div></footer>
<script src="{r}app.js"></script></body></html>'''
  os.makedirs(path or ".",exist_ok=True); open(path+"index.html","w").write(o)
mono=lambda t,sz="":f'<div class="mono" style="background:{CD[t["task"]][2]};{sz}">{t["mono"]}</div>'
def catgrid(r): return '<div class="grid">'+"".join(f'<a class="cat" href="{r}task/{s}/"><div class="mono" style="background:{c}">{n[:2]}</div><b>{n}</b><small>{d}</small></a>' for s,n,c,d in CATS)+'</div>'
NEWS='''<div class="w"><div class="news"><div><h2>The 5 best new free tools, every Friday</h2><p style="opacity:.85;margin:6px 0 0">No spam. Unsubscribe anytime. From AI for the Task.</p></div><form id="nl"><input type="email" required placeholder="you@example.com" aria-label="Email"><button class="btn">Subscribe</button></form><div class="ok" id="nlok">You are in! Check your inbox to confirm.</div></div></div>'''
DISC=lambda r:f'<div class="disc">Disclosure: "Try it" buttons are affiliate links (marked sponsored). We may earn a commission at no cost to you. We never rank by payout. <a href="{r}disclosure/">Learn more</a></div>'
tr=[tools(s)[0] for s in ["images","writing","video","coding","voice","research","logos","presentations"]]
page("","Best Free AI Tools by Task, Tested Limits","Free AI tools sorted by task with tested free tier limits.",[],f'''
<section class="hero"><div class="w"><span class="stamp">● Updated this week . Oct 12, 2026</span><h1>Every <span class="grad">free AI tool</span>,<br>for the task.</h1><p class="lead">Free limits, watermarks, signup and commercial use, verified by hand so you know the catch first.</p>
<form class="search" action="task/resumes/"><input name="q" placeholder="Try: make a resume, remove background, write code"><button class="btn ac">Search</button></form></div></section>
<div class="w"><h2 id="tasks">Pick a task</h2>{catgrid("")}<h2>Trending this week</h2>
<div class="trend">{"".join(f'<a class="tc" href="tools/{t["slug"]}/">{mono(t)}<div><b style="color:var(--ink)">{t["name"]}</b><br><small>{CD[t["task"]][1]} . {t["limit"]}</small></div></a>' for t in tr)}</div></div>{NEWS}''',
[{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":BASE+f"task/{c[0]}/","name":c[1]} for i,c in enumerate(CATS)]}])
for s,n,c,d in CATS:
  ts=tools(s); r="../../"; cards=""
  for i,t in enumerate(ts):
    cards+=f'''<article class="card">{mono(t)}<div><div class="rank">#{i+1}{" BEST OVERALL" if i==0 else ""}</div><h3><a href="{r}tools/{t["slug"]}/" style="color:var(--ink)">{t["name"]}</a>{' <span class="pill" style="color:#b91c1c">No longer free since Sep 30, 2026</span>' if t["gone"] else ''}</h3>
<div class="facts"><div><span>Free tier:</span> {t["limit"]}</div><div><span>Card needed:</span> {yn(t["card"],False)}</div><div><span>Good at:</span> {t["good"]}</div><div><span>Not good at:</span> {t["bad"]}</div></div></div>
<div class="cta"><a class="btn ac" href="https://example.com/go/{t["slug"]}" rel="sponsored nofollow" target="_blank">Try it</a><small>Last verified {t["checked"]}</small></div></article>'''
  rows="".join(f'<tr><td><a href="{r}tools/{t["slug"]}/"><b>{t["name"]}</b></a></td><td>{"Paid only" if t["gone"] else t["limit"]}</td><td>{yn(t["wm"],False)}</td><td>{t["signup"]}</td><td>{t["dev"]}</td><td>{yn(t["com"])}</td><td>{t["checked"]}</td></tr>' for t in ts)
  faq=[(f"Are these AI tools for {n.lower()} really free?","Every listed tool has a free tier today, except any marked no longer free. Limits are in the table."),("How is the order decided?","By our test results only. Affiliate payouts never affect ranking.")]
  rel=REL.get(s,["writing","images","research"])
  page(f"task/{s}/",f"Best Free AI Tools for {n} (2026)",d,[(n,f"task/{s}/")],f'''
<div class="w"><main><span class="stamp">● Updated Oct 12, 2026</span><h1>Best Free AI Tools for {n} (2026)</h1><p class="lead" style="margin:0 0 18px">{d}. {len(ts)} free tiers tested hands on.</p>{DISC(r)}
<div class="sort"><a class="on" href="?sort=tested">Best tested</a><a href="?sort=nocard">No card</a><a href="?sort=ondevice">On-device</a><a href="?sort=commercial">Commercial use</a></div>
<h2 style="margin-top:20px">Free limits compared</h2><div class="tw"><table><thead><tr><th>Tool</th><th>Free limit</th><th>Watermark</th><th>Signup</th><th>On-device / upload</th><th>Commercial use</th><th>Last verified</th></tr></thead><tbody>{rows}</tbody></table></div>
<p style="font-size:13px;color:var(--mut)">How we verify these limits: <a href="{r}how-we-test/">our testing method</a>.</p>
<h2>Ranked picks</h2>{cards}
{(chr(60)+"h2>Head to head"+chr(60)+"/h2><p><a href=\""+r+"compare/resumerocket-vs-cvsmith/\">ResumeRocket vs CVSmith</a> . <a href=\""+r+"alternatives/resumerocket/\">ResumeRocket alternatives</a></p>") if s=="resumes" else ""}
<h2>Related tasks</h2><div class="sort">{"".join(f'<a href="{r}task/{x}/">{CD[x][1]}</a>' for x in rel)}</div>
<h2>FAQ</h2>{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)}</main></div>''',
  [{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":t["name"],"url":BASE+f'tools/{t["slug"]}/'} for i,t in enumerate(ts)]},
   {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}])
for t in ALL.values():
  r="../../"; n=CD[t["task"]][1]; alts=[x for x in tools(t["task"]) if x["slug"]!=t["slug"]][:4]
  gone='<div class="disc" style="background:#fef2f2;border-color:#fecaca;color:#991b1b;margin-top:16px"><b>No longer free since Sep 30, 2026.</b> The free plan was removed. See <a href="../../alternatives/resumerocket/">free alternatives</a>.</div>' if t["gone"] else ''
  page(f'tools/{t["slug"]}/',f'{t["name"]}: Free Plan, Limits & Best Uses',f'{t["name"]} free plan limits.',[(n,f'task/{t["task"]}/'),(t["name"],f'tools/{t["slug"]}/')],f'''
<div class="w"><main><div style="display:flex;gap:16px;align-items:center;margin-top:18px">{mono(t,"width:64px;height:64px;font-size:22px")}<div><h1 style="margin:0">{t["name"]}: Free Plan, Limits &amp; Best Uses</h1><a class="pill" href="{r}task/{t["task"]}/">{n}</a> <span class="pill">Last verified {t["checked"]}</span></div></div>{gone}
<p style="font-size:18px">Is {t["name"]} free? {"No, not anymore." if t["gone"] else "Yes. "+t["limit"]+", "+("with" if t["wm"] else "no")+" watermark."}</p>
{DISC(r)}<p><a class="btn ac" href="https://example.com/go/{t["slug"]}" rel="sponsored nofollow" target="_blank">Try {t["name"]}</a> &nbsp;<a href="https://example.com/{t["slug"]}/pricing" rel="nofollow">Official pricing page</a></p>
<h2>Free tier limits</h2><div class="tw"><table><tr><th>Category</th><td>{n} AI tool</td></tr><tr><th>Price</th><td>{"Paid plans only" if t["gone"] else "Free plan, $0"}</td></tr><tr><th>Free limit</th><td>{"Paid only" if t["gone"] else t["limit"]}</td></tr><tr><th>Watermark</th><td>{yn(t["wm"],False)}</td></tr><tr><th>Signup</th><td>{t["signup"]}</td></tr><tr><th>Card needed</th><td>{yn(t["card"],False)}</td></tr><tr><th>On-device / upload</th><td>{t["dev"]}</td></tr><tr><th>Commercial use</th><td>{yn(t["com"])}</td></tr></table></div>
<p style="font-size:13px;color:var(--mut)">Limits verified per <a href="{r}how-we-test/">how we test</a>.</p>
<div class="prose"><h2>What we tested</h2><p>Fresh free account, three real {n.lower()} tasks, exports checked for watermark and quality. Good at: {t["good"].lower()}. Not good at: {t["bad"].lower()}.</p>
<h2>Privacy notes</h2><p>{"Runs on your device; files are not uploaded." if t["dev"]=="On-device" else "Files are uploaded to the vendor. Sample policy says inputs may be used to improve models unless you opt out."}</p></div>
<h2>Alternatives</h2><div class="trend">{"".join(f'<a class="tc" href="{r}tools/{a["slug"]}/">{mono(a)}<div><b style="color:var(--ink)">{a["name"]}</b><br><small>{a["limit"]}</small></div></a>' for a in alts)}</div>
{"<p><a href=\""+r+"alternatives/resumerocket/\">See all ResumeRocket alternatives</a> . <a href=\""+r+"compare/resumerocket-vs-cvsmith/\">ResumeRocket vs CVSmith</a></p>" if t["task"]=="resumes" else ""}<p><a href="{r}task/{t["task"]}/">All free AI tools for {n.lower()}</a></p></main></div>''',
  [{"@context":"https://schema.org","@type":"SoftwareApplication","name":t["name"],"applicationCategory":f"{n} AI tool","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}] if not t["gone"] else [])
a,b=ALL["resumerocket"],ALL["cvsmith"]; r="../../"
rows="".join(f'<tr><th>{k}</th><td>{f(a)}</td><td>{f(b)}</td></tr>' for k,f in [("Free limit",lambda t:t["limit"]),("Watermark",lambda t:yn(t["wm"],False)),("Signup",lambda t:t["signup"]),("On-device / upload",lambda t:t["dev"]),("Commercial use",lambda t:yn(t["com"])),("Good at",lambda t:t["good"]),("Not good at",lambda t:t["bad"]),("Last verified",lambda t:t["checked"])])
page("compare/resumerocket-vs-cvsmith/","ResumeRocket vs CVSmith: Free Plans Compared","ResumeRocket vs CVSmith free plans.",[("Resumes","task/resumes/"),("ResumeRocket vs CVSmith","compare/resumerocket-vs-cvsmith/")],f'''
<div class="w"><h1>ResumeRocket vs CVSmith: Free Plans Compared</h1><p class="lead" style="margin:0 0 18px">Same three resumes, both free plans. Here is how they compare.</p>{DISC(r)}
<h2>Free plan side by side</h2><div class="tw"><table><thead><tr><th></th><th><a href="{r}tools/resumerocket/">ResumeRocket</a></th><th><a href="{r}tools/cvsmith/">CVSmith</a></th></tr></thead><tbody>{rows}</tbody></table></div>
<p style="font-size:13px;color:var(--mut)"><a href="{r}how-we-test/">How we test</a></p>
<div class="prose"><h2>Verdict</h2><p>Pick ResumeRocket for speed and templates. Pick CVSmith if you want no signup and on-device privacy.</p></div>
<p><a class="btn ac" href="https://example.com/go/resumerocket" rel="sponsored nofollow">Try ResumeRocket</a> <a class="btn" href="https://example.com/go/cvsmith" rel="sponsored nofollow">Try CVSmith</a></p>
<p><a href="{r}task/resumes/">All free resume tools</a> . <a href="{r}alternatives/resumerocket/">ResumeRocket alternatives</a></p></div>''')
alts=[x for x in tools("resumes") if x["slug"]!="resumerocket"]
page("alternatives/resumerocket/","Free ResumeRocket Alternatives (2026)","Free ResumeRocket alternatives.",[("Resumes","task/resumes/"),("ResumeRocket alternatives","alternatives/resumerocket/")],f'''
<div class="w"><h1>Free ResumeRocket Alternatives (2026)</h1><p class="lead" style="margin:0 0 18px">Hit the export limit? These free tools do the same job.</p>{DISC(r)}
{"".join(f'<article class="card">{mono(t)}<div><h3><a href="{r}tools/{t["slug"]}/" style="color:var(--ink)">{t["name"]}</a></h3><div class="facts"><div><span>Free limit:</span> {"Paid only" if t["gone"] else t["limit"]}</div><div><span>Watermark:</span> {yn(t["wm"],False)}</div><div><span>Good at:</span> {t["good"]}</div><div><span>Not good at:</span> {t["bad"]}</div></div></div><div class="cta"><a class="btn ac" href="https://example.com/go/{t["slug"]}" rel="sponsored nofollow">Try it</a><small>Last verified {t["checked"]}</small></div></article>' for t in alts)}
<p><a href="{r}compare/resumerocket-vs-cvsmith/">ResumeRocket vs CVSmith</a> . <a href="{r}tools/resumerocket/">ResumeRocket free plan</a></p></div>''',
[{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":t["name"],"url":BASE+f'tools/{t["slug"]}/'} for i,t in enumerate(alts)]}])
for p,tl,txt in [("how-we-test/","How we test","<p>Every tool is tested on a brand new free account, on real tasks, by a human. We record the free limit, watermark, signup, on-device vs upload, commercial use terms, and capture a dated screenshot of the pricing page.</p><h2>Ranking</h2><p>Output quality, free tier generosity, ease of use and privacy. Never by affiliate payout.</p><h2>Rechecks</h2><p>Monthly at least. If a free plan disappears we mark it 'No longer free since' with the date.</p>"),
 ("disclosure/","Affiliate disclosure",f"<p>{B} is funded by affiliate links. When you click a \"Try it\" button and later upgrade, we may earn a commission at no extra cost to you.</p><p>Affiliate links are marked sponsored. Neither affects rankings.</p>"),
 ("about/","About "+B,f"<p>{B} is a project by Atulit. Everyone deserves to know which AI tools are actually free, and what the catch is, before signing up.</p>")]:
  page(p,tl,tl,[(tl,p)],f'<div class="w prose"><h1>{tl}</h1>{txt}</div>')
import seo_site; seo_site.build()
print("ok", B, BASE, "pages", sum(1 for _ in __import__('pathlib').Path('.').rglob('index.html')))
