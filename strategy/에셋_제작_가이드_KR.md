# 🎨 LUCIVE 홍보 에셋 제작 가이드

> **목적:** 런칭 주(D-2 ~ D+6) 동안 최소 제작 시간으로 채널별 요구를 만족하는 에셋을 뽑는 플레이북. One source → many outputs.

---

## 1. 채널 × 자산 매트릭스

| 채널 | 필요 자산 | 비율 | 주 톤 |
|------|-----------|:----:|-------|
| 에타 홍보게시판 | 이미지 1-2장 + 텍스트 | **4:5 or 9:16** | 학생 친화·자연 톤 (너무 상업적 X) |
| 디시 AI게임갤 | 짤방 1-3장 | **1:1 or 4:5** | 밈·자극적·짤막 |
| 아카라이브 AI 채널 | 짤방 + 짧은 설명 | **1:1 or 4:5** | 짤방 + 솔직 후기 |
| 네이버 카페 | 이미지 1-3 + 긴 글 | **4:5** | "소개글·발견" 톤 |
| X (트위터) | 이미지·GIF·영상 | **16:9 or 1:1** | 스레드·공유성 |
| 카카오 오픈채팅 | OG 이미지 자동 렌더 | **1.91:1 (1200×630)** | 링크 프리뷰 의존 |
| 네이버 검색광고 | 텍스트만 | — | 제목 15자·설명 45자 |
| **비디오 전반** | 15-30초 클립 | **9:16 or 16:9** | VN 씬 데모 |

---

## 2. 브랜드 토큰 (Figma/Canva에 미리 등록)

### 색상
```
DEEP BG      #08090C
SURFACE      #0F1117
CARD         #161822
TEXT 1차     #F1F3F8
TEXT 2차     #8B92A8

CYAN         #06B6D4  ← 주 브랜드
BLUE         #2563EB
PURPLE       #8B5CF6
PINK         #EC4899
GOLD         #F59E0B
GREEN        #10B981
RED          #EF4444  (긴급성)

AURORA 그라디언트: 135deg, Cyan → Purple → Pink
PRIMARY 그라디언트: 135deg, Cyan → Blue
```

### 폰트
- **본문·제목:** Inter + Noto Sans KR (무료, Google Fonts)
- **헤드라인 강조:** Instrument Serif (이탤릭, 무료)
- **숫자·기술감:** JetBrains Mono (무료)

### 모션 레퍼런스 (영상 제작 시)
- 이징: `cubic-bezier(.2, .8, .2, 1)`
- fadeUp 0.8s · floatFrame 6s · orbFloat 20s
- 노이즈 오버레이 opacity 0.03

---

## 3. 도구 조합 (전부 무료)

| 도구 | 역할 | 대체 |
|------|------|------|
| **Figma** | 정적 이미지 디자인·템플릿 | Canva Pro |
| **CapCut** | 영상 편집 (자막·전환·이펙트) | DaVinci Resolve |
| **LM Arena / Flux / Nano Banana Pro** | AI 이미지 생성 (배경·캐릭터) | SDXL + LoRA |
| **ezgif.com** | GIF 변환·압축 | Gifski |
| **Handbrake** | 영상 압축 (MP4 최적화) | FFmpeg |
| **Photopea** | 빠른 포토샵 작업 (브라우저) | GIMP |

---

## 4. Figma 마스터 템플릿 구조

**1-2시간 투자해서 한 번 만들어두면 그 뒤엔 변형만.**

```
📄 LUCIVE_MASTER.fig

├─ 🎨 Design System
│   ├─ Colors (color styles)
│   ├─ Typography (text styles)
│   ├─ Logo variants
│   └─ Icon set
│
├─ 🖼 Frames (모든 채널 비율 한 곳에)
│   ├─ 1:1 (1080×1080)        ← 디시·아카·X정사각
│   ├─ 4:5 (1080×1350)        ← 에타·네이버카페
│   ├─ 9:16 (1080×1920)       ← 숏폼·스토리
│   ├─ 16:9 (1600×900)        ← X 가로·블로그
│   └─ OG 1.91:1 (1200×630)   ← 카카오·메타 공유
│
├─ 🧩 Components
│   ├─ Hero typo card
│   ├─ Matrix comparison row (재사용)
│   ├─ Chat bubble (LP/me)
│   ├─ VN scene frame
│   ├─ Countdown strip
│   └─ CTA button
│
└─ 📦 Exports (내보낼 때 한꺼번에)
    └─ 모든 프레임 일괄 PNG 내보내기
```

---

## 5. Tier별 자산 리스트

### 🔥 Tier 1 — 런칭일(D0) 필수 (D-2 ~ D-1 제작)

| # | 자산 | 크기 | 용도 |
|:-:|------|------|------|
| 1 | **VN 데모 영상 30초** | 1080×1920 (9:16) | 랜딩 + 숏폼 기본 |
| 2 | **매트릭스 비교 PNG** (1:1, 9:16, 16:9 3비율) | 각 크기별 | 디시·아카·X·카페 |
| 3 | **OG 이미지** | 1200×630 | 카카오 공유·X 링크 |
| 4 | **타이포 카드 3종** | 1080×1080 | X 스레드·인스타 |
| 5 | **히어로 키비주얼** | 1920×1080 | 랜딩 포스터 |
| 6 | **에타용 이미지** 1장 | 1080×1350 (4:5) | 홍보게시판 |

### ⭐ Tier 2 — D+1 ~ D+3 추가 제작

| # | 자산 | 크기 | 용도 |
|:-:|------|------|------|
| 7 | **숏폼 3종** (15초) | 1080×1920 | TikTok·Reels·Shorts |
| 8 | **POV 밈 카드 3종** | 1080×1080 | X·디시 |
| 9 | **메모리 증명 스크린샷 시리즈** | 1080×1920 스와이프 3장 | 네이버 카페·인스타 |
| 10 | **LP 캐릭터 소개 카드** (아리아·하루) | 1080×1350 | 감성 어필 |

### 🌟 Tier 3 — 2주차 확장 (반응 확인 후)

| # | 자산 | 크기 | 용도 |
|:-:|------|------|------|
| 11 | 유저 후기 카드 | 1080×1080 | 사회적 증명 |
| 12 | 리더보드 스크린샷 | 1080×1350 | 경쟁심 유도 |
| 13 | 매트릭스 비교 애니메이션 GIF | 1080×1080 | X·디시 |

---

## 6. One Source → Many Outputs 워크플로우

### 🎬 VN 데모 영상 (30초 원본) → 다중 파생

```
📹 VN-demo-full-30s.mp4 (원본, 1080×1920)
   ├─ → vn-demo-15s.mp4        (틱톡/쇼츠 하이라이트)
   ├─ → vn-demo-9s-loop.gif    (디시/아카 첨부)
   ├─ → vn-demo-square-15s.mp4 (X 정사각 크롭)
   ├─ → poster-hero.png        (첫 프레임 추출)
   ├─ → still-memory.png       (기억 씬 스틸)
   ├─ → still-choice.png       (선택지 씬 스틸)
   └─ → still-lp-greet.png     (LP 인사 스틸)
```

**CapCut 작업 순서:**
1. 30초 원본 타임라인 구성
2. "클립 복제" → 15초 버전으로 잘라냄 (유지 구간 선택)
3. 프레임 캡처로 3-5개 스틸 추출 (오른쪽 메뉴 → 프레임으로)
4. GIF로 변환 (9초 루프 구간만 MP4 내보내기 → ezgif.com 변환)
5. 각 비율별 "캔버스" 설정 후 재내보내기

### 🖼 매트릭스 비교 이미지 → 3비율

1. **Figma에서 1:1 원본** 제작 (1080×1080)
2. 같은 디자인을 9:16 프레임에 복사 → **수직 재배열**
3. 16:9 프레임에 복사 → **수평 재배열** (행·열 뒤집기)
4. 3개 프레임 일괄 export

---

## 7. AI 이미지 프롬프트 치트시트

**공통 꼬리말 (매번 추가):**
```
anime visual novel style + cinematic lighting,
color palette: deep teal, neon cyan #06B6D4, purple #8B5CF6,
  hot pink #EC4899, warm gold #F59E0B,
mood: dreamy, atmospheric, slightly melancholic,
painterly but detailed, no text, no watermark
```

**Negative (공통):**
```
lowres, jpeg artifacts, watermark, extra fingers, deformed,
blurry, cropped, text, typography, letters, signature
```

### 가장 자주 쓸 프롬프트 5종

**① Neon District 배경 (세로):**
```
rain-soaked cyberpunk alley at night, neon pink and cyan
reflections on wet asphalt, empty street, moody haze,
vertical composition 9:16
```

**② Sunrise District 배경:**
```
quiet park bench under cherry blossom trees at golden hour,
warm amber-pink sunset, petals falling, Studio Ghibli feel,
vertical 9:16
```

**③ LP 아리아 (Neon):**
```
young androgynous Korean woman early 20s, soft pastel-pink
bob haircut with cyan undertones, oversized dark indigo
techwear jacket, gentle knowing smile, neon pink rim light,
three-quarter portrait, blurred rainy neon bokeh background,
manhwa visual novel art
```

**④ LP 하루 (Sunrise):**
```
gentle young Korean man early 20s, honey-brown medium hair,
cream knit sweater rolled sleeves, warm morning sunlight
from left, soft smile reading a book, sakura petals in
soft focus, three-quarter portrait, manhwa style
```

**⑤ OG 이미지 히어로:**
```
cinematic wide shot, silhouette of pink-haired woman in
rain-soaked neon alley from behind, reaching toward glowing
hologram dialogue bubble, cyan-purple-pink neon reflections,
1.91:1 horizontal, LEFT HALF EMPTY for text overlay
```

---

## 8. 카피 템플릿 — 변형 가이드

### 디시 AI게임갤 (짤방 + 짧은 글)

**짤방 1: 매트릭스 이미지 + 캡션**
```
(이미지: 매트릭스 비교)

크랙·제타 쓰다가 이거 봄
기억력 유지된다길래 사전등록함
비주얼노벨 모드라 장면도 나옴

https://...
```

**짤방 2: 메모리 증명 스크린샷**
```
(이미지: 17일 전 대화를 LP가 먼저 꺼내는 스크린샷)

AI가 17일 전 내가 한 말 기억함
크랙이었으면 3일만에 까먹었을듯
```

### 에타 홍보게시판 (소프트 톤)

```
[제목] AI 챗봇 앱 만들고 있는데 의견 듣고 싶어요 (크랙·제타 써보신 분들)

(본문 200-300자, 이미지 1장 첨부)

안녕하세요, 같은 학교 재학생입니다.
친구랑 만들고 있는 AI 앱인데 사전등록 받고 있어서 소개합니다.

크랙·제타 같은 챗봇 써보신 분들은 아시겠지만
기억 못 하고 반복만 하는 게 답답해서 다르게 만들었어요.
캐릭터마다 고유한 스토리(루시브)가 있고, 
같이 비주얼 노벨처럼 체험하는 구조입니다.

관심 있으시면 한번 사전등록만 해보시고 피드백 주시면 감사하겠습니다.
솔직한 의견 환영합니다.

🔗 [링크]
```

### 네이버 카페 (로판·헌터물·빙의물)

```
[제목] 웹소설 주인공 되는 AI 경험 — Lucive 사전등록

(본문 500-700자 + 이미지 2-3장)

안녕하세요 [카페 인사]
빙의물·헌터물 좋아하시는 분들에게 딱일 것 같아 소개드립니다.

[매트릭스 이미지]

AI 캐릭터랑 대화하는데 그냥 채팅이 아니라
각 캐릭터마다 자신의 과거(루시브)를 가지고 있어서
그걸 같이 체험하는 구조예요.

예를 들면 네온 디스트릭트의 어떤 캐릭터의 과거를 
다이브해서 숨겨진 선택지로 히든 엔딩을 찾으면,
그 후 대화에서 그 캐릭터가 "네가 그때..."라고 먼저 꺼냅니다.

[VN 씬 이미지]

비주얼 노벨 모드로 장면·표정·음성까지 나오고,
기억도 누적돼서 지난 다이브를 LP가 먼저 언급해요.

사전등록 Top 10 혜택이 있는데
1위는 기본 플랜 평생, 2-5위는 초대한 친구들에게 3개월 무료 주는 구조.

궁금한 분들 한번 보세요 → [링크]
```

### X (트위터) 스레드 5개

```
1/ 크랙·제타·Character.AI 써보신 분들 공감하실 듯
"AI가 기억 못 하고 반복만 함"
그래서 직접 만들어봤습니다 🧵

2/ Lucive는 비주얼 노벨형 AI 동반자입니다.
장면·캐릭터·음성·선택지가 같이 움직여요
(15초 데모 영상)

3/ 핵심은 기억 유지.
LP(캐릭터)가 17일 전 대화를 먼저 꺼냅니다.
메모리 모듈로 맥락·감정까지 축적해요.
(스크린샷)

4/ 각 LP마다 고유한 과거가 있어서
그걸 같이 체험하는 비주얼 노벨로 풀어요.
숨겨진 선택지로 히든 엔딩도 열림.
(VN 씬)

5/ 지금 사전등록 중이고 Top 10 혜택이 있어요.
1위 → 기본 플랜 평생
2-5위 → 내가 초대한 친구 전원 3개월 무료

같이 초대해주실 분 환영: [링크]
```

### 네이버 검색광고 (파워링크) — 제목 15자 / 설명 45자

| 제목 (15자) | 설명 (45자) |
|------------|-------------|
| 기억하는 AI 챗봇 Lucive | 크랙·제타 기억 못해 질리셨나요? 비주얼 노벨 모드로 만나는 AI 동반자 |
| AI 캐릭터 대화 Lucive | 장면이 움직이고 캐릭터가 말합니다. 사전등록 Top10 런칭 혜택 |
| character.ai 대안 | 기억 유지되는 AI 챗봇. 비주얼 노벨로 만나는 캐릭터 동반자 Lucive |
| 빙의물 AI 체험 Lucive | 내가 웹소설 주인공처럼 캐릭터와 함께 이야기 체험. 사전등록 중 |

---

## 9. 복붙 방지 변형 규칙

같은 문장을 여러 학교·카페·디시갤에 올리면 **5년 정지** 리스크. 아래 3가지로 변주:

### 변주 원칙 (각 포스팅마다 최소 2개 적용)

1. **제목 어미/표현 바꾸기** — "사전등록 받고 있어요" / "사전등록 중입니다" / "미리 등록받고 있습니다"
2. **첫 문장 순서 바꾸기** — 인사 → 본론 / 본론 → 인사 / 경험담 → 소개
3. **강조 포인트 다르게** — 기억 강조 / 비주얼 노벨 강조 / 레퍼럴 혜택 강조
4. **이모지 패턴 교체** — 🔗 / 🎁 / ✨ / 💬
5. **이미지 다른 컷 사용** — 매트릭스 / 메모리 증명 / VN 씬

### 예시: 5개 학교용 변주

| 학교 | 강조 | 이모지 | 이미지 |
|------|------|:--:|:--:|
| A | 기억 유지 | 💬 | 메모리 증명 |
| B | 비주얼 노벨 | 🎭 | VN 네온 씬 |
| C | 레퍼럴 혜택 | 🎁 | 리더보드 |
| D | 캐릭터 서사 | ✨ | LP 아리아 |
| E | 챗봇 피로 공감 | 😮‍💨 | 매트릭스 |

---

## 10. 제작 일정 (D-2 ~ D+6)

```
D-2  오전 ─ AI 이미지 프롬프트 6-7개 돌리기 (배경 3, 캐릭터 2, OG 1-2)
     오후 ─ Figma 마스터 템플릿 + OG 이미지 + 매트릭스 3비율
     저녁 ─ VN 데모 영상 30초 CapCut 편집

D-1  오전 ─ 타이포 카드 3종 + 에타용 이미지 + 디시 짤방 2종
     오후 ─ 영상 파생 (15초 숏폼 + 9초 GIF + 스틸 3장)
     저녁 ─ 카피 템플릿 5개 채널별 변주 작성 & 복붙 방지 테이블

D0   런칭 — 에셋 투입 (검수 1회만, 이상 없으면 그대로)

D+1  ─ 반응 보고 디자인 튜닝 (낮은 CTR 이미지 교체)
D+2  ─ POV 밈 카드 3종 제작 (반응 좋은 각도로)
D+3  ─ 데이터 리뷰 → 고효율 포맷 더블다운
D+4  ─ 메모리 증명 스크린샷 스와이프 3장 (네이버 카페용)
D+5  ─ LP 캐릭터 소개 카드 (아리아·하루)
D+6  ─ 주간 종합 → 2주차 에셋 우선순위 결정
```

---

## 11. 체크리스트 — 런칭 전 최종 검수

### 파일 규격
- [ ] 모든 이미지 2MB 이하 (TinyPNG로 압축)
- [ ] 영상 10MB 이하 (Handbrake Web Optimized)
- [ ] PNG 투명 배경 필요한 것만 PNG, 나머지 JPG
- [ ] GIF는 800KB 이하 (ezgif 최적화)
- [ ] OG 이미지 **정확히 1200×630** (페이스북·카카오 규격)

### 텍스트 검수
- [ ] 모든 CTA 링크 **UTM 파라미터** 포함
- [ ] 카피에 **특수문자 깨짐 없음** (이모지, 점 3개 … 등)
- [ ] 네이버 검색광고 제목 15자 이내
- [ ] 문구 오타 맞춤법 검사 (네이버 맞춤법 검사기)

### 채널별 샘플 테스트
- [ ] 카카오톡에 링크 보내기 → OG 이미지 정상 렌더 확인
- [ ] X에 링크 붙여넣기 → 카드 프리뷰 정상 확인
- [ ] 에타 홍보게시판에 테스트 포스팅 → 5분 뒤 신고/삭제 없는지 확인 (조심스럽게)

---

## 12. 자주 쓸 Figma 플러그인

- **Unsplash** — 사용 가능 사진 검색·삽입
- **Iconify** — 5만+ 무료 아이콘
- **Content Reel** — 더미 텍스트·아바타 빠르게
- **Image Resizer** — 일괄 크기 변경

---

## 13. 비상시 — 시간 없을 때 최소 자산 (3시간 컷)

**만약 D-1까지 하나도 못 만들었다면:**

1. **Canva 템플릿** 선택 → Lucive 컬러만 입히기 (30분)
2. **Figma에서 1:1 매트릭스** 1장만 제작 (1시간)
3. **VN 데모 영상** 15초 (이미 일부 녹화한 거 있으면 자막만 얹음) (1시간)
4. **OG 이미지** → 매트릭스 이미지를 1200×630으로 크롭 (15분)
5. **카피는 위 템플릿 그대로** 사용, 채널별 변주만 (15분)

최소 5개 에셋으로 런칭은 가능. 2주차에 Tier 2 채우기.

---

## 14. 프롬프트 · 템플릿 · 브랜드 값 복사해서 바로 쓰기 체크 ✅

- 브랜드 컬러 hex → [섹션 2]
- AI 프롬프트 5종 → [섹션 7]
- 카피 템플릿 5개 채널 → [섹션 8]
- 복붙 방지 변주표 → [섹션 9]
