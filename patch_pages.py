import os, re

BASE_URL = "https://icml.reinvent-labs.com"
OG_IMAGE = f"{BASE_URL}/og-image.jpg"

META = """\
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="A practical guide for AI researchers attending ICML 2026 in Seoul — events, apps, places, Korean phrases, and tips." />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="A practical guide for AI researchers attending ICML 2026 in Seoul — events, apps, places, Korean phrases, and tips." />
  <meta name="twitter:image" content="{og_image}" />"""

SHARE = """\
  <div class="share-bar">
    <span class="share-label">Share</span>
    <a class="share-btn wa" href="https://wa.me/?text=ICML%202026%20Seoul%20Guide%20%7C%20Events%2C%20places%20%26%20tips%20for%20researchers%20{url}" target="_blank" rel="noopener">
      WhatsApp
    </a>
    <a class="share-btn x" href="https://twitter.com/intent/tweet?text=ICML%202026%20Seoul%20Guide%20%E2%80%94%20events%2C%20apps%2C%20places%20%26%20tips%20for%20researchers&url={url}" target="_blank" rel="noopener">
      𝕏 Post
    </a>
    <a class="share-btn li" href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener">
      LinkedIn
    </a>
  </div>"""

pages = {
    "index.html":          ("Seoul Guide for ICML 2026", f"{BASE_URL}/"),
    "socials.html":        ("ICML 2026 Events & Socials · Seoul", f"{BASE_URL}/socials.html"),
    "must-visit.html":     ("Must-Visit Places in Seoul · ICML 2026", f"{BASE_URL}/must-visit.html"),
    "explore-seoul.html":  ("Explore Seoul · ICML 2026 Guide", f"{BASE_URL}/explore-seoul.html"),
    "work-cafes.html":     ("Work Cafes Near COEX · ICML 2026", f"{BASE_URL}/work-cafes.html"),
    "apps.html":           ("Essential Apps for Seoul · ICML 2026", f"{BASE_URL}/apps.html"),
    "korean-phrases.html": ("Useful Korean Phrases · ICML 2026", f"{BASE_URL}/korean-phrases.html"),
    "other-tips.html":     ("Practical Tips for Seoul · ICML 2026", f"{BASE_URL}/other-tips.html"),
    "coex-guide.html":     ("COEX Venue Guide · ICML 2026", f"{BASE_URL}/coex-guide.html"),
    "workshops.html":      ("ICML 2026 Workshops · Seoul", f"{BASE_URL}/workshops.html"),
}

for fname, (title, url) in pages.items():
    path = f"/home/user/dolist/icml2026/{fname}"
    html = open(path).read()

    # Skip if meta already patched
    if "og:url" not in html:
        meta_block = META.format(url=url, title=title, og_image=OG_IMAGE)
        html = html.replace("</head>", f"{meta_block}\n</head>", 1)

    # Add share bar before </footer> if not already there
    if "share-bar" not in html:
        share_block = SHARE.format(url=url)
        html = html.replace("<footer>", f"{share_block}\n  <footer>", 1)

    open(path, "w").write(html)
    print(f"Patched: {fname}")
