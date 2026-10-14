# Real free tier facts, each read from the official pricing page on Oct 13, 2026.
# Only what the page states. "Not stated" means the page did not say.
CHECKED="Oct 13, 2026"
T=[
 dict(name="Teal",task="resumes",url="https://www.tealhq.com/pricing",free="Free Forever plan: unlimited resumes, unlimited job tracking, 10 AI credits for resume bullets",paid="Teal+ from $13 per week",card="Not stated"),
 dict(name="Rezi",task="resumes",url="https://www.rezi.ai/pricing",free="Free plan: 1 resume, 1 AI interview, 3 PDF downloads, AI resume writer and editor",paid="Pro $29; Lifetime $149 one time",card="No (page says no card required)"),
 dict(name="Kickresume",task="resumes",url="https://www.kickresume.com/en/pricing/",free="Free as long as you do not pick paid customization; 4 free resume templates. Free for students verified with ISIC, ITIC or UNiDAYS",paid="Premium (price not captured)",card="Not stated"),
 dict(name="Ideogram",task="logos",url="https://ideogram.ai/pricing",free="Free plan $0: weekly slow credits for eligible accounts, 1 running generation, images are public. No free trials of paid plans",paid="Plus $15 per month billed annually",card="Not stated",com="Page says you may use generated images for any purpose, including commercial use"),
 dict(name="CapCut",task="video",url="https://www.capcut.com/pricing",free="Free plan USD 0: free templates and basic editing tools",paid="Pro USD 19.99 per month",card="Not stated"),
 dict(name="Runway",task="video",url="https://runwayml.com/pricing",free="Free forever: 125 one time credits that do not expire, 5GB asset storage",paid="Standard $12 per month billed annually ($15 monthly)",card="Not stated"),
 dict(name="Descript",task="video",url="https://www.descript.com/pricing",free="Free plan $0: 60 media minutes per month, 720p export, 5GB cloud storage, 1 GB max file size",paid="Hobbyist $16 per month billed annually ($24 monthly)",card="No (FAQ says no card needed for the Free plan)"),
 dict(name="Khanmigo",task="homework",url="https://www.khanmigo.ai/pricing",free="Free for teachers. Learners and parents pay",paid="$4 per month or $44 per year for learners and parents",card="Not stated"),
 dict(name="Grammarly",task="writing",url="https://www.grammarly.com/plans",free="Free plan $0: spelling and grammar fixes, tone detection, 100 AI prompts",paid="Pro $12 USD per month, 7 day free trial",card="Not stated"),
 dict(name="Notion",task="writing",url="https://www.notion.com/pricing",free="Free plan $0 for individuals: includes a trial of Notion AI, basic forms and sites",paid="Plus $10 per member per month",card="Not stated"),
 dict(name="Claude",task="writing",url="https://claude.com/pricing",free="Free plan $0: chat on web, desktop and mobile, web search, file creation, code runs, memory",paid="Pro $17 per month with annual billing",card="Not stated"),
 dict(name="Leonardo.Ai",task="images",url="https://leonardo.ai/pricing/",free="Free plan $0: 150 fast tokens per day, public creations only, basic quality settings",paid="Essential $12 per month",card="Not stated",com="Free tier gets a non exclusive, royalty free licence for commercial use; Leonardo holds rights to the images"),
 dict(name="Gemini",task="images",url="https://gemini.google/subscriptions/",free="Free with a Google Account: Flash-Lite model, image generation and editing, Deep Research",paid="Paid tiers give 2x or 4x usage (price not captured)",card="Not stated"),
 dict(name="ElevenLabs",task="voice",url="https://elevenlabs.io/pricing",free="Free plan $0: 10k credits per month, text to speech, speech to text, sound effects, 3 Studio projects",paid="Starter $6 per month (first month offer shown)",card="Not stated",com="Commercial license starts on Starter, not Free"),
 dict(name="Speechify",task="voice",url="https://speechify.com/pricing/",free="Free plan: listen at up to 1.5x, 10 basic voices, text to speech only",paid="Premium $29 per month billed monthly",card="Not stated"),
 dict(name="GitHub Copilot",task="coding",url="https://github.com/features/copilot/plans",free="Free plan $0: limited chat and agent usage, supports CLI and agent mode",paid="Pro $10 per month",card="Not stated"),
 dict(name="Cursor",task="coding",url="https://cursor.com/pricing",free="Free plan $0 per month: limited agent requests and limited chat requests",paid="Plus $8 per month",card="Not stated"),
 dict(name="Windsurf",task="coding",url="https://windsurf.com/pricing",free="Free plan $0: light agent quota, limited models, unlimited Tab completions and inline edits",paid="Pro $20 per month",card="Not stated"),
 dict(name="Beautiful.ai",task="presentations",url="https://www.beautiful.ai/pricing",free="No free plan. 14 day free trial of Pro or Team",paid="Pro $14.50 per month billed annually",card="Not stated",nofree=True),
 dict(name="Elicit",task="research",url="https://elicit.com/pricing",free="Basic plan free: unlimited search across 138 million papers, unlimited summaries and chat with papers, limited Research Agent and Reports",paid="Plus $11 per user per month billed annually",card="Not stated"),
]
for t in T: t["slug"]=t["name"].lower().replace(".","").replace(" ","-")
