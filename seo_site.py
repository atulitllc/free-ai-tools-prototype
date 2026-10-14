"""AI for the Task SEO config. INDEXABLE gates robots meta and sitemap for the whole site."""
import os, shutil, sys
INDEXABLE = False
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT); import seo
LOGOS = "/workspace/atulit-logos/aiforthetask"

def hook(ctx):
    p, s, paths = ctx["path"], ctx["soup"], ctx["paths"]
    seg = p.strip("/").split("/") if p else []
    h1 = ctx["h1"]
    if p == "": return dict(titles=["Best Free AI Tools by Task, Tested Limits"])
    if seg[0] == "tools":
        task = [a["href"] for a in s.select("a.pill") if "task/" in a.get("href", "")]
        tk = task[0].split("task/")[1].strip("/") if task else ""
        sib = [q for q in paths if q.startswith("tools/") and q != p and f'task/{tk}/' in str(ctx["soups"][q].select("a.pill"))]
        rel = [f"task/{tk}/"] + sib[:5] + (["compare/resumerocket-vs-cvsmith/", "alternatives/resumerocket/"] if tk == "resumes" else [])
        name = h1.split(":")[0]
        return dict(titles=[h1, f"{name}: Free Plan, Limits & Uses", f"{name}: Free Plan & Limits"], related=rel)
    if seg[0] == "task":
        return dict(titles=[h1, h1.replace(" (2026)", "")])
    if seg[0] in ("compare", "alternatives"):
        rel = ["task/resumes/"] + [q for q in paths if q.startswith("tools/") and any(x in q for x in ("resumerocket", "cvsmith", "hiredraft", "lettera", "jobpolish"))] + [q for q in ("compare/resumerocket-vs-cvsmith/", "alternatives/resumerocket/") if q != p]
        return dict(titles=[h1], related=rel[:8])
    return dict(titles=[h1])

def build():
    for a, b in [(f"{LOGOS}/option-b-icon.svg", "favicon.svg"), (f"{ROOT}/img/brand/option-b-icon-32.png", "favicon-32.png"), (f"{ROOT}/img/brand/option-b-icon-180.png", "apple-touch-icon.png")]:
        shutil.copy(a, f"{ROOT}/img/brand/{b}")
    site = seo.Site(ROOT, "AI for the Task", "aiforthetask.com", "free-ai-tools-prototype", INDEXABLE, "Oct 13, 2026", "2026-10-13",
        "Sample data prototype by Atulit. Tools and numbers are made up. Some links are affiliate links marked sponsored.",
        f"{LOGOS}/option-b-wordmark-1200.png", "img/brand/option-b-icon-512.png",
        ["Free tier limits checked by hand.", "Sample data prototype.", "Updated Oct 2026.", "From AI for the Task.", "No ratings, just limits.", "Tested free plans."], hook)
    return seo.run(site)
if __name__ == "__main__": build()
