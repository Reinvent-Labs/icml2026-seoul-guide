from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1200, 630
bg       = (250, 250, 248)
accent   = (37,  99,  235)
text_col = (26,  26,  26)
muted    = (107, 107, 107)
border   = (229, 229, 229)

img  = Image.new("RGB", (W, H), bg)
draw = ImageDraw.Draw(img)

# Fonts
font_bold   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 62)
font_med    = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
font_small  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
font_tag    = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)

# Top accent bar
draw.rectangle([0, 0, W, 8], fill=accent)

# Accent left stripe
draw.rectangle([72, 80, 80, H - 80], fill=accent)

# Title
draw.text((108, 90), "Seoul Guide", font=font_bold, fill=accent)
draw.text((108, 165), "for ICML 2026", font=font_bold, fill=text_col)

# Subtitle
draw.text((108, 258), "A practical guide for AI researchers attending", font=font_med, fill=muted)
draw.text((108, 298), "ICML in Seoul — places, apps, events, and tips.", font=font_med, fill=muted)

# Tags row
tags = ["Apps", "Events", "Korean Phrases", "Work Cafes", "Places"]
x = 108
y = 380
for tag in tags:
    bbox = draw.textbbox((0, 0), tag, font=font_tag)
    tw = bbox[2] - bbox[0]
    pad = 20
    rx0, ry0, rx1, ry1 = x, y, x + tw + pad*2, y + 42
    draw.rounded_rectangle([rx0, ry0, rx1, ry1], radius=8, fill=(239, 246, 255))
    draw.text((rx0 + pad, ry0 + 9), tag, font=font_tag, fill=accent)
    x = rx1 + 12

# Author section
try:
    avatar = Image.open("/home/user/dolist/icml2026/salomon.jpg").convert("RGB")
    size = 72
    avatar = avatar.resize((size, size))
    mask  = Image.new("L", (size, size), 0)
    from PIL import ImageDraw as ID2
    md = ID2.Draw(mask)
    md.ellipse([0, 0, size, size], fill=255)
    avatar.putalpha(mask)
    img.paste(avatar, (108, 490), avatar)
    ax = 196
except Exception:
    ax = 108

draw.text((ax, 495), "Salomon Diei", font=font_tag, fill=text_col)
draw.text((ax, 525), "KOREATECH DICE Lab  ·  salomon.reinvent-labs.com", font=font_small, fill=muted)

# Domain watermark bottom right
draw.text((W - 420, H - 52), "icml.reinvent-labs.com", font=font_small, fill=muted)

img.save("/home/user/dolist/icml2026/og-image.jpg", "JPEG", quality=92)
print("OG image saved.")
