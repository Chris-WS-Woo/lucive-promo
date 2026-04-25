"""v8-{jp,en}-unified.html → v9-{jp,en}-unified.html

Converts dark theme to v9 light product-canonical palette + new manifesto copy.
Keeps regional copy (JP/EN) already translated in v8 variants.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).parent
V9_KR = HERE / 'v9-kr-unified.html'

# ── 1. Extract v9-kr canonical tokens + VN stage block ────────────────────
kr = V9_KR.read_text(encoding='utf-8')

m = re.search(r':root\{[^}]*\}', kr, re.DOTALL)
if not m: sys.exit('[err] v9-kr :root not found')
V9_ROOT = m.group(0)

# Font import line (one of the <link href="...googleapis.../css2?family=...">)
m = re.search(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
    kr,
)
if not m: sys.exit('[err] v9-kr font link not found')
V9_FONTS_BASE = m.group(0)

# VN stage CSS (two rules: .v8-stage and .v8-stage::before)
v9_stage_match = re.search(
    r'\.v8-stage\{[^}]*\}\s*\.v8-stage::before\{[^}]*\}',
    kr, re.DOTALL,
)
if not v9_stage_match: sys.exit('[err] v9-kr VN stage CSS not found')
V9_STAGE = v9_stage_match.group(0)


# ── 2. Region font variants ───────────────────────────────────────────────
FONT_JP = (
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Inter:wght@400;500;600;700;800&'
    'family=Space+Grotesk:ital,wght@0,400;0,500;0,600;0,700&'
    'family=Noto+Sans+JP:wght@400;500;600;700;800;900&'
    'family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">'
)
FONT_EN = (
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Inter:wght@400;500;600;700;800&'
    'family=Space+Grotesk:ital,wght@0,400;0,500;0,600;0,700&'
    'family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">'
)


# ── 3. Dark→light rgba / hex substitutions (shared with emails) ──────────
DARK_TO_LIGHT = [
    # color-scheme meta
    ('name="color-scheme" content="dark"', 'name="color-scheme" content="light"'),
    # Hard-coded dark surface hexes (v8-jp used dark sakura, v8-en used dark indigo)
    # Base surfaces
    ('#0A0812', '#F8FAFC'),  # v8-jp bg
    ('#141020', '#F1F5F9'),  # v8-jp bg-soft
    ('#1A1426', '#FFFFFF'),  # v8-jp bg-card
    ('#231A35', '#F1F5F9'),  # v8-jp bg-elevated
    ('#0A0A0F', '#F8FAFC'),  # v8-en bg
    ('#111118', '#F1F5F9'),  # v8-en bg-soft
    ('#15151E', '#FFFFFF'),  # v8-en bg-card
    ('#1C1C28', '#F1F5F9'),  # v8-en bg-elevated
    # Text ramps
    ('#F8F5F0', '#1E293B'),  # v8-jp ink
    ('#C8C0D4', '#334155'),  # v8-jp ink-soft
    ('#9088A0', '#64748B'),  # v8-jp muted
    ('#5A5068', '#94A3B8'),  # v8-jp muted-2
    ('#F5F5F7', '#1E293B'),  # v8-en ink
    ('#C8C8D0', '#334155'),  # v8-en ink-soft
    ('#8B8B96', '#64748B'),  # v8-en muted
    ('#55555F', '#94A3B8'),  # v8-en muted-2
    # White-on-dark borders → slate
    ('rgba(255,255,255,.07)', '#E2E8F0'),
    ('rgba(255,255,255,.08)', '#E2E8F0'),
    ('rgba(255,255,255,.13)', '#CBD5E1'),
    ('rgba(255,255,255,.14)', '#CBD5E1'),
    # Hover / overlay on dark → light equivalents
    ('rgba(255,255,255,.05)', 'rgba(15,23,42,.04)'),
    ('rgba(255,255,255,.06)', 'rgba(15,23,42,.04)'),
    ('rgba(255,255,255,.1)',  'rgba(15,23,42,.08)'),
    ('rgba(255,255,255,.12)', 'rgba(15,23,42,.1)'),
    ('rgba(255,255,255,.25)', 'rgba(15,23,42,.18)'),
    ('rgba(255,255,255,.35)', 'rgba(15,23,42,.28)'),
    # Floating jump-nav dark bg → light glass
    ('background:rgba(10,8,18,.85)',  'background:rgba(248,250,252,.85)'),
    ('background:rgba(10,10,15,.85)', 'background:rgba(248,250,252,.85)'),
]


# ── 4. Manifesto copy per region ─────────────────────────────────────────
# (Old v8 kicker/manifesto/subhead) → (new v9)
JP_MANIFESTO_OLD = re.compile(
    r'<div class="v8-head rv">\s*'
    r'<div class="kicker">[^<]*</div>\s*'
    r'<h2 class="v8-manifesto">.*?</h2>\s*'
    r'<p class="v8-subhead">.*?</p>\s*'
    r'</div>',
    re.DOTALL,
)
JP_MANIFESTO_NEW = (
    '<div class="v8-head rv">\n'
    '      <div class="kicker">AI コンパニオン・アプリを見てきて</div>\n'
    '      <h2 class="v8-manifesto">道具じゃなく、<br><em>存在を</em> 作ります。</h2>\n'
    '      <p class="v8-subhead">Google Play レビュー <b>1,200 件に繰り返し現れる 4 つの失望</b>。'
    'Lucive は最初から違う質感から始まります。</p>\n'
    '    </div>'
)

EN_MANIFESTO_OLD = JP_MANIFESTO_OLD  # same regex
EN_MANIFESTO_NEW = (
    '<div class="v8-head rv">\n'
    '      <div class="kicker">WHAT WE SAW IN AI COMPANION APPS</div>\n'
    '      <h2 class="v8-manifesto">Not a tool —<br><em>a presence.</em></h2>\n'
    '      <p class="v8-subhead"><b>4 familiar disappointments that repeat across 1,200+ Google Play reviews</b>. '
    'With Lucive, the texture is different from the very first message.</p>\n'
    '    </div>'
)


# ── 5. Build pipeline ────────────────────────────────────────────────────
def build(src_name: str, dst_name: str, fonts_link: str, manifesto_new: str):
    src = HERE / src_name
    dst = HERE / dst_name

    text = src.read_text(encoding='utf-8')

    # 5a. Replace :root block with v9-kr canonical
    text = re.sub(r':root\{[^}]*\}', V9_ROOT, text, count=1, flags=re.DOTALL)

    # 5b. Replace the Inter/Space Grotesk font <link> (if present) with region variant
    text = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
        fonts_link,
        text,
    )
    # Also replace any legacy font <link> (v8 used Gowun/Zen-Kaku etc.)
    text = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=(?!Inter)[^"]*" rel="stylesheet">',
        fonts_link,
        text,
    )

    # 5c. Dark → light substitutions
    for a, b in DARK_TO_LIGHT:
        text = text.replace(a, b)

    # 5d. VN stage background (v8 had purple/sakura; v9 uses navy→cyan)
    text = re.sub(
        r'\.v8-stage\{[^}]*\}\s*\.v8-stage::before\{[^}]*\}',
        V9_STAGE,
        text, count=1, flags=re.DOTALL,
    )

    # 5e. Manifesto copy
    text = JP_MANIFESTO_OLD.sub(manifesto_new, text, count=1) if dst_name.endswith('-jp-unified.html') \
           else EN_MANIFESTO_OLD.sub(manifesto_new, text, count=1)

    dst.write_text(text, encoding='utf-8')
    print(f'[ok] {dst_name}  ({len(text):,} chars)')


if __name__ == '__main__':
    build('v8-jp-unified.html', 'v9-jp-unified.html', FONT_JP, JP_MANIFESTO_NEW)
    build('v8-en-unified.html', 'v9-en-unified.html', FONT_EN, EN_MANIFESTO_NEW)
    print('[done]')
