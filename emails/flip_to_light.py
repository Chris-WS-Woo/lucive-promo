"""Flip email templates from dark cinematic to v9 light (product canonical).

Converts:
- color-scheme dark → light
- deep navy backgrounds → white / light-gray surfaces
- light gray text → dark slate
- white-on-dark borders → light slate borders
- default link color → product blue
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).parent
FILES = [
    '00_kr_등록_확인.html',
    '01_설문완료_로스터대기.html',
    '02_알파_선발.html',
    '03_알파_대기자.html',
    '04_알파_이용가이드_오픈전날.html',
    '90_순위상승_알림.html',
]

# Order matters: more-specific multi-token patterns first, raw hex last.
SUBS = [
    # color-scheme meta
    ('name="color-scheme" content="dark"',
     'name="color-scheme" content="light"'),
    ('name="supported-color-schemes" content="dark"',
     'name="supported-color-schemes" content="light"'),
    # Default anchor color → product blue
    ('a { color: #06B6D4;',   'a { color: #2563EB;'),
    ('a{color:#06B6D4;',      'a{color:#2563EB;'),
    # White-on-dark borders / dividers → light slate (Tailwind slate-200/300)
    ('rgba(255,255,255,0.06)', '#E2E8F0'),
    ('rgba(255,255,255,0.08)', '#E2E8F0'),
    ('rgba(255,255,255,0.1)',  '#CBD5E1'),
    ('rgba(255,255,255,0.12)', '#CBD5E1'),
    ('rgba(255,255,255,0.14)', '#CBD5E1'),
    ('rgba(255,255,255,0.2)',  '#94A3B8'),
    ('rgba(255,255,255,0.25)', '#94A3B8'),
    ('rgba(255,255,255,0.35)', '#64748B'),
    # Dark surface hexes → light surface hexes
    # (order: deepest bg first so later replacements don't collide)
    ('#08090C', '#F8FAFC'),   # body / outermost canvas
    ('#0F1117', '#FFFFFF'),   # main container
    ('#161822', '#F1F5F9'),   # elevated card surface
    ('#1C1F2E', '#F1F5F9'),   # inline code / small chip bg
    # Dark-theme text ramp → light-theme text ramp
    ('#F1F3F8', '#1E293B'),   # text primary
    ('#8B92A8', '#64748B'),   # text secondary
    ('#5A6178', '#94A3B8'),   # text tertiary
]


def flip(text: str) -> tuple[str, int]:
    total = 0
    for a, b in SUBS:
        n = text.count(a)
        if n:
            text = text.replace(a, b)
            total += n
    return text, total


for name in FILES:
    p = HERE / name
    if not p.exists():
        print(f'[skip] {name} not found')
        continue
    before = p.read_text(encoding='utf-8')
    after, n = flip(before)
    p.write_text(after, encoding='utf-8')
    print(f'[ok] {name}: {n} substitutions')

print('[done]')
