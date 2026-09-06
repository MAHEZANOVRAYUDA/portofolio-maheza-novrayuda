import os
import math
from PIL import Image, ImageDraw, ImageFilter

def create_favicon_suite():
    os.makedirs('static', exist_ok=True)
    os.makedirs('staticfiles_build/static', exist_ok=True)

    # 1. GENERATE VECTOR SVG FAVICON
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#020617"/>
            <stop offset="100%" stop-color="#0f172a"/>
        </linearGradient>
        <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#38bdf8"/>
            <stop offset="50%" stop-color="#6366f1"/>
            <stop offset="100%" stop-color="#0ea5e9"/>
        </linearGradient>
        <linearGradient id="mnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#38bdf8"/>
            <stop offset="50%" stop-color="#818cf8"/>
            <stop offset="100%" stop-color="#06b6d4"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#38bdf8" flood-opacity="0.45"/>
        </filter>
        <filter id="nodeGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#38bdf8" flood-opacity="0.8"/>
        </filter>
    </defs>

    <!-- Base Squircle -->
    <rect x="20" y="20" width="472" height="472" rx="112" fill="url(#bgGrad)" stroke="url(#borderGrad)" stroke-width="12"/>

    <!-- Subtle Tech Circuit Grid lines -->
    <g opacity="0.12" stroke="#38bdf8" stroke-width="2">
        <line x1="80" y1="20" x2="80" y2="492"/>
        <line x1="432" y1="20" x2="432" y2="492"/>
        <line x1="20" y1="80" x2="492" y2="80"/>
        <line x1="20" y1="432" x2="492" y2="432"/>
    </g>

    <!-- Modern Interlocking M-N Monogram -->
    <g filter="url(#glow)">
        <!-- Letter M -->
        <path d="M 120 372 L 120 148 L 212 284 L 300 148 L 300 372" 
              stroke="url(#mnGrad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round"/>
        
        <!-- Letter N -->
        <path d="M 300 372 L 300 148 L 392 372 L 392 148" 
              stroke="url(#mnGrad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- Glowing AI / Data Vertices -->
    <g filter="url(#nodeGlow)">
        <!-- V1: Center M node -->
        <circle cx="212" cy="284" r="14" fill="#38bdf8"/>
        <circle cx="212" cy="284" r="7" fill="#ffffff"/>
        
        <!-- V2: N Apex node -->
        <circle cx="392" cy="148" r="14" fill="#06b6d4"/>
        <circle cx="392" cy="148" r="7" fill="#ffffff"/>

        <!-- V3: M Apex node -->
        <circle cx="120" cy="148" r="10" fill="#38bdf8"/>
    </g>
</svg>
'''
    with open('static/favicon.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    with open('staticfiles_build/static/favicon.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created static/favicon.svg")

    # 2. GENERATE HIGH-RES RASTER WITH PILLOW (1024x1024 supersampled)
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background squircle
    margin = 44
    radius = 240
    # Draw dark slate rounded rectangle
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=radius,
        fill=(2, 6, 23, 255),  # Slate-950
        outline=(56, 189, 248, 220),  # Sky-400
        width=24
    )

    # Subtle grid accent lines
    draw.line([(160, margin), (160, size - margin)], fill=(56, 189, 248, 30), width=4)
    draw.line([(size - 160, margin), (size - 160, size - margin)], fill=(56, 189, 248, 30), width=4)
    draw.line([(margin, 160), (size - margin, 160)], fill=(56, 189, 248, 30), width=4)
    draw.line([(margin, size - 160), (size - margin, size - 160)], fill=(56, 189, 248, 30), width=4)

    # Draw Monogram M and N
    # Points
    p_m_start = (240, 744)
    p_m_top1  = (240, 296)
    p_m_mid   = (424, 568)
    p_mn_top  = (600, 296)
    p_mn_bot  = (600, 744)
    p_n_bot   = (784, 744)
    p_n_top   = (784, 296)

    # Outer glow layer for monogram
    glow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_img)
    glow_color = (56, 189, 248, 120)
    glow_width = 96

    # Draw lines on glow layer
    for p1, p2 in [
        (p_m_start, p_m_top1),
        (p_m_top1, p_m_mid),
        (p_m_mid, p_mn_top),
        (p_mn_top, p_mn_bot),
        (p_mn_top, p_n_bot),
        (p_n_bot, p_n_top),
    ]:
        glow_draw.line([p1, p2], fill=glow_color, width=glow_width, joint='round')
    glow_img = glow_img.filter(ImageFilter.GaussianBlur(16))
    img = Image.alpha_composite(img, glow_img)
    draw = ImageDraw.Draw(img)

    # Core high-contrast monogram strokes
    stroke_w = 72
    cyan_sky = (56, 189, 248, 255)
    indigo_sky = (99, 102, 241, 255)
    cyan_teal = (6, 182, 212, 255)

    # M left pillar
    draw.line([p_m_start, p_m_top1], fill=cyan_sky, width=stroke_w, joint='round')
    # M left diagonal
    draw.line([p_m_top1, p_m_mid], fill=cyan_sky, width=stroke_w, joint='round')
    # M right diagonal
    draw.line([p_m_mid, p_mn_top], fill=indigo_sky, width=stroke_w, joint='round')
    # Shared pillar
    draw.line([p_mn_top, p_mn_bot], fill=indigo_sky, width=stroke_w, joint='round')
    # N diagonal
    draw.line([p_mn_top, p_n_bot], fill=cyan_teal, width=stroke_w, joint='round')
    # N right pillar
    draw.line([p_n_bot, p_n_top], fill=cyan_teal, width=stroke_w, joint='round')

    # Draw rounded endpoints for maximum craftsmanship
    for pt, col in [
        (p_m_start, cyan_sky),
        (p_m_top1, cyan_sky),
        (p_m_mid, cyan_sky),
        (p_mn_top, indigo_sky),
        (p_mn_bot, indigo_sky),
        (p_n_bot, cyan_teal),
        (p_n_top, cyan_teal),
    ]:
        r = stroke_w // 2
        draw.ellipse([(pt[0] - r, pt[1] - r), (pt[0] + r, pt[1] + r)], fill=col)

    # Glowing AI Vertices / Nodes
    # Node 1: M Center vertex
    r_outer = 32
    draw.ellipse([(p_m_mid[0] - r_outer, p_m_mid[1] - r_outer), (p_m_mid[0] + r_outer, p_m_mid[1] + r_outer)], fill=(56, 189, 248, 255))
    r_inner = 16
    draw.ellipse([(p_m_mid[0] - r_inner, p_m_mid[1] - r_inner), (p_m_mid[0] + r_inner, p_m_mid[1] + r_inner)], fill=(255, 255, 255, 255))

    # Node 2: N Top vertex
    draw.ellipse([(p_n_top[0] - r_outer, p_n_top[1] - r_outer), (p_n_top[0] + r_outer, p_n_top[1] + r_outer)], fill=(6, 182, 212, 255))
    draw.ellipse([(p_n_top[0] - r_inner, p_n_top[1] - r_inner), (p_n_top[0] + r_inner, p_n_top[1] + r_inner)], fill=(255, 255, 255, 255))

    # Node 3: M Top vertex
    r_small = 20
    draw.ellipse([(p_m_top1[0] - r_small, p_m_top1[1] - r_small), (p_m_top1[0] + r_small, p_m_top1[1] + r_small)], fill=(255, 255, 255, 230))

    # Save multi-size PNGs
    sizes_map = {
        'static/favicon-16x16.png': (16, 16),
        'static/favicon-32x32.png': (32, 32),
        'static/favicon-48x48.png': (48, 48),
        'static/apple-touch-icon.png': (180, 180),
        'static/android-chrome-192x192.png': (192, 192),
        'static/android-chrome-512x512.png': (512, 512),
        'staticfiles_build/static/favicon-16x16.png': (16, 16),
        'staticfiles_build/static/favicon-32x32.png': (32, 32),
        'staticfiles_build/static/favicon-48x48.png': (48, 48),
        'staticfiles_build/static/apple-touch-icon.png': (180, 180),
        'staticfiles_build/static/android-chrome-192x192.png': (192, 192),
        'staticfiles_build/static/android-chrome-512x512.png': (512, 512),
    }

    for path, (w, h) in sizes_map.items():
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        resized.save(path, format='PNG')
        print(f"Created {path}")

    # Generate multi-resolution ICO file
    ico_img = img.resize((256, 256), Image.Resampling.LANCZOS)
    ico_img.save(
        'static/favicon.ico',
        format='ICO',
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
    )
    ico_img.save(
        'staticfiles_build/static/favicon.ico',
        format='ICO',
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
    )
    print("Created static/favicon.ico")

    # 3. GENERATE SITE.WEBMANIFEST
    manifest = '''{
  "name": "Maheza Novrayuda Portfolio",
  "short_name": "Maheza Portfolio",
  "icons": [
    {
      "src": "/static/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/static/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#020617",
  "background_color": "#020617",
  "display": "standalone"
}'''
    with open('static/site.webmanifest', 'w', encoding='utf-8') as f:
        f.write(manifest)
    with open('staticfiles_build/static/site.webmanifest', 'w', encoding='utf-8') as f:
        f.write(manifest)
    print("Created static/site.webmanifest")

if __name__ == '__main__':
    create_favicon_suite()
