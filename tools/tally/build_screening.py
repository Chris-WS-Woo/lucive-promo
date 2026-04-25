"""Create the Lucive alpha-screening Tally form via API.

Usage:
    TALLY_KEY="tly-..." python build_screening.py

The API key is read from env var only. Never commit it.
Output: form ID + share URL (printed to stdout).
"""
import json
import os
import sys
import uuid
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

API_KEY = os.environ.get('TALLY_KEY')
if not API_KEY:
    sys.exit('[err] set TALLY_KEY env var')

BASE = 'https://api.tally.so'


def u() -> str:
    return str(uuid.uuid4())


# --- Block builders --------------------------------------------------------

def form_title(html: str) -> list:
    b = u()
    return [{
        'uuid': b, 'type': 'FORM_TITLE',
        'groupUuid': b, 'groupType': 'TEXT',
        'payload': {'html': html},
    }]


def title(html: str) -> list:
    b = u()
    return [{
        'uuid': b, 'type': 'TITLE',
        'groupUuid': b, 'groupType': 'TITLE',
        'payload': {'html': html},
    }]


def text(html: str) -> list:
    b = u()
    return [{
        'uuid': b, 'type': 'TEXT',
        'groupUuid': b, 'groupType': 'TEXT',
        'payload': {'html': html},
    }]


def long_text(label: str, *, required: bool = False) -> list:
    b = u()
    return [{
        'uuid': b, 'type': 'TEXTAREA',
        'groupUuid': b, 'groupType': 'TEXTAREA',
        'payload': {'isRequired': required, 'placeholder': label},
    }]


def multiple_choice(options: list[str], *, required: bool = True) -> list:
    group = u()
    blocks = []
    for i, opt in enumerate(options):
        blocks.append({
            'uuid': u(),
            'type': 'MULTIPLE_CHOICE',
            'groupUuid': group,
            'groupType': 'MULTIPLE_CHOICE',
            'payload': {
                'index': i,
                'text': opt,
                'isRequired': required,
            },
        })
    return blocks


def checkboxes(options: list[str], *, required: bool = False) -> list:
    group = u()
    blocks = []
    for i, opt in enumerate(options):
        blocks.append({
            'uuid': u(),
            'type': 'CHECKBOXES',
            'groupUuid': group,
            'groupType': 'CHECKBOXES',
            'payload': {
                'index': i,
                'text': opt,
                'isRequired': required if i == 0 else False,
            },
        })
    return blocks


# --- Assemble form ---------------------------------------------------------

blocks = []

# Cover / title
blocks += form_title('Lucive · 알파 테스터 선발 설문')
blocks += text(
    '8가지 짧은 질문이 있습니다. 약 2–3분 소요 · '
    '완주 시 Dip 500, 선발 시 +2,000. '
    '솔직하게 답해주시면 선발에 가장 큰 도움이 됩니다.'
)

# Q1 — usage duration
blocks += title('<strong>Q1.</strong> 얼마나 AI 캐릭터 챗을 써봤나요?')
blocks += multiple_choice([
    '안 써봤어요',
    '1개월 미만',
    '1–6개월',
    '6개월–1년',
    '1년 이상',
])

# Q1b — apps used
blocks += title('<strong>Q1b.</strong> 주로 어떤 앱을 썼나요? (복수 선택 가능)')
blocks += checkboxes([
    'Character.AI', '크랙', '제타', 'Replika',
    'Talkie', 'Janitor AI', 'SpicyChat', '기타',
])

# Q2 — frequency
blocks += title('<strong>Q2.</strong> 얼마나 자주 대화하세요?')
blocks += multiple_choice([
    '매일', '주 3–6회', '주 1–2회', '월 몇 번', '거의 안 함',
])

# Q3 — top frustration
blocks += title('<strong>Q3.</strong> 가장 답답했던 점 하나만 꼽는다면?')
blocks += multiple_choice([
    '대화를 기억 못 함',
    '답변이 반복되고 지루함',
    '캐릭터 깊이·서사 부족',
    '과금·광고 과도',
    '갑작스러운 검열·정지',
    '기타',
])

# Q4 — positive moments
blocks += title('<strong>Q4.</strong> 그래도 좋았던 순간은? (복수 선택)')
blocks += checkboxes([
    '공감받는 느낌이 좋았음',
    '재미있는 대화',
    '캐릭터가 마음에 들었음',
    '심심할 때 위로',
    '창작 소스로 활용',
    '스트레스 해소',
    '아직 인상적인 경험 없음',
], required=True)

# Q5 — creative experience
blocks += title('<strong>Q5.</strong> 창작 경험이 있으세요? (복수 선택)')
blocks += checkboxes([
    '웹소설·팬픽 써봄',
    '웹툰·그림 그려봄',
    '챗봇 봇메이킹',
    '게임·영상 시나리오',
    '블로그·에세이',
    'AI로 콘텐츠 만들어봄',
    '창작 경험 거의 없음',
], required=True)

# Q6 — game genres
blocks += title('<strong>Q6.</strong> 최근 1년간 즐긴 게임 장르는? (복수 선택)')
blocks += checkboxes([
    '비주얼 노벨·서사 게임',
    'JRPG·어드벤처',
    '오픈월드·RPG',
    '수집·방치형',
    'MMO·MOBA',
    '캐주얼·퍼즐',
    'FPS·액션',
    '게임 거의 안 함',
], required=True)

# Q7-A — webtoon frequency
blocks += title('<strong>Q7.</strong> 웹툰·웹소설은 얼마나 즐기세요?')
blocks += multiple_choice([
    '매일', '주 여러 번', '주 1회', '가끔', '거의 안 봄',
])

# Q7-B — genres
blocks += title('주로 보는 장르는? (복수 선택)')
blocks += checkboxes([
    '로맨스·로판', '판타지',
    '빙의물·환생물', '헌터물',
    '무협', '스릴러·미스터리',
    '일상·힐링', 'SF',
])

# Q8 — spend
blocks += title('<strong>Q8.</strong> 최근 6개월, AI 챗·게임·웹소설에 돈 써본 적 있나요?')
blocks += multiple_choice([
    '10만 원 이상', '5–10만 원', '1–5만 원', '1만 원 미만', '과금 경험 없음',
])

# Q9 — time slots
blocks += title('<strong>Q9.</strong> 알파 테스트 참여 가능한 시간대는? (복수 선택)')
blocks += checkboxes([
    '평일 아침', '평일 낮', '평일 저녁',
    '주말 아침', '주말 낮', '주말 저녁',
], required=True)

# Q10 — bonus wishlist
blocks += title('<strong>Q10.</strong> (보너스) 알파에서 꼭 시험해보고 싶은 게 있나요?')
blocks += text('한두 문장이면 충분해요. 작성 시 <strong>우선 선발 가산점</strong>.')
blocks += long_text('예: 메모리 유지가 진짜 되는지 3일 뒤 확인해보고 싶어요 (200자 이내)')


# --- POST ------------------------------------------------------------------

body = {
    'status': 'PUBLISHED',
    'blocks': blocks,
    'settings': {
        'language': 'ko',
    },
}

req = urllib.request.Request(
    f'{BASE}/forms',
    data=json.dumps(body).encode('utf-8'),
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'User-Agent': 'lucive-tally-bootstrap/1.0',
    },
    method='POST',
)

try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode('utf-8'))
        print(f'[ok] HTTP {r.status}')
        print(f"[form] id      = {data.get('id')}")
        print(f"[form] name    = {data.get('name')}")
        print(f"[form] status  = {data.get('status')}")
        print(f"[form] blocks  = {len(blocks)}")
        print(f"[share url]    = https://tally.so/r/{data.get('id')}")
        print(f"[admin url]    = https://tally.so/forms/{data.get('id')}/edit")
except urllib.error.HTTPError as e:
    print(f'[err] HTTP {e.code}')
    print(e.read().decode('utf-8')[:1200])
    sys.exit(1)
