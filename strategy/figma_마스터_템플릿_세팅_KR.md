# 🎨 LUCIVE Figma 마스터 템플릿 세팅 가이드

> **목표:** 30-60분 투자해서 이후 모든 홍보 에셋을 "변형만으로" 뽑아낼 수 있는 마스터 파일 구축.
>
> **산출물:** `LUCIVE_MASTER.fig` 파일 1개 (로컬 스타일 + 5가지 비율 프레임 + 재사용 컴포넌트 12개)

---

## 0. 준비

- [ ] Figma 무료 계정 로그인 (figma.com)
- [ ] 새 파일 생성 → 이름 `LUCIVE_MASTER`
- [ ] Google Fonts에서 아래 4종 확인 (Figma가 자동 로드):
  - Inter
  - Noto Sans KR
  - Instrument Serif
  - JetBrains Mono

---

## 1. 페이지 구조 만들기 (5분)

좌측 Pages 패널에서 `+` 눌러 4개 페이지 생성:

```
📄 00 — Design System
📄 01 — Components
📄 02 — Frames (Ready to Export)
📄 03 — Archive
```

각 페이지 역할:
- **00 Design System:** 색상·타이포·그라디언트 정의
- **01 Components:** 재사용 블록 (마스터 컴포넌트)
- **02 Frames:** 실제 내보낼 이미지들 (5비율)
- **03 Archive:** 쓰지 않는 오래된 버전

---

## 2. 로컬 스타일 등록 (10분)

### 🎨 색상 스타일 (Color Styles)

**작업:** `00 — Design System` 페이지에서 작업

1. `R` 키로 Rectangle 하나 그림
2. 우측 Fill 색상 클릭 → HEX 입력
3. Fill 색상 팔레트 옆 `...` → `Create style` → 이름 지정
4. 아래 전체 반복 (총 13개)

| 스타일 이름 | HEX | 용도 |
|------------|-----|------|
| `bg/deep` | `#08090C` | 베이스 배경 |
| `bg/surface` | `#0F1117` | 2단계 배경 |
| `bg/card` | `#161822` | 카드 |
| `bg/elevated` | `#1C1F2E` | 입력·버튼 호버 |
| `text/primary` | `#F1F3F8` | 주 텍스트 |
| `text/secondary` | `#8B92A8` | 보조 텍스트 |
| `text/tertiary` | `#5A6178` | 흐린 텍스트 |
| `brand/cyan` | `#06B6D4` | 주 브랜드 |
| `brand/blue` | `#2563EB` | 보조 브랜드 |
| `brand/purple` | `#8B5CF6` | 강조 |
| `brand/pink` | `#EC4899` | 감정·핫 |
| `brand/gold` | `#F59E0B` | 1위·희귀 |
| `state/green` | `#10B981` | 성공 |
| `state/red` | `#EF4444` | 긴급 |
| `border/subtle` | `rgba(255,255,255,0.06)` | 약한 선 |
| `border/medium` | `rgba(255,255,255,0.10)` | 보통 선 |

### 🌈 그라디언트 스타일 (복제해서 쓸 수 있게 저장)

Rectangle 3개 그리고 Linear Gradient 설정 → Create style:

| 이름 | 설정 |
|------|------|
| `grad/primary` | Linear 135°, `#06B6D4` → `#2563EB` |
| `grad/warm` | Linear 135°, `#EC4899` → `#8B5CF6` |
| `grad/aurora` | Linear 135°, `#06B6D4` 0% → `#8B5CF6` 50% → `#EC4899` 100% |

### 🔤 타이포그래피 스타일 (Text Styles)

텍스트 박스(`T` 키) 만들고 속성 설정 후 Text 스타일로 저장 (총 8개):

| 스타일 이름 | Font | Weight | Size | Line-Height | Letter-Spacing |
|------------|------|:-----:|:----:|:-----------:|:--------------:|
| `display/XL` | Inter | 900 | 72 | 110% | -3% |
| `display/L` | Inter | 800 | 48 | 115% | -2% |
| `h1` | Inter | 800 | 32 | 120% | -2% |
| `h2` | Inter | 700 | 24 | 130% | -1% |
| `body/L` | Inter | 500 | 17 | 170% | 0 |
| `body/M` | Inter | 400 | 15 | 160% | 0 |
| `caption` | Inter | 500 | 13 | 150% | 0 |
| `serif/italic` | Instrument Serif | 400 Italic | 28 | 120% | -2% |
| `mono` | JetBrains Mono | 600 | 11 | 150% | 10% (UP) |

> Inter 미설치 시 Noto Sans KR을 fallback으로 추가 설정. Font에서 `Inter, Noto Sans KR` 순서로 지정.

---

## 3. 5가지 비율 프레임 세팅 (5분)

`02 — Frames` 페이지로 이동. `F` 키 눌러 Frame tool 활성화. 커스텀 사이즈 입력:

| 프레임 이름 | 크기 | 용도 |
|------------|------|------|
| `01_square_1080` | 1080 × 1080 | 디시·아카·X 정사각 |
| `02_portrait_4-5` | 1080 × 1350 | 에타·네이버 카페 |
| `03_vertical_9-16` | 1080 × 1920 | 숏폼·스토리 |
| `04_landscape_16-9` | 1600 × 900 | X 가로·블로그 |
| `05_og_1200x630` | 1200 × 630 | 카카오·메타 공유 |

각 프레임 생성 후:
1. 프레임 선택 → Fill 색상 → `bg/deep` 스타일 적용
2. 프레임 이름 앞에 번호 붙여 정렬 순서 고정

---

## 4. 재사용 컴포넌트 만들기 (25-30분)

`01 — Components` 페이지에서 작업. 각 컴포넌트 만든 후 우클릭 → `Create component` (단축키 `Ctrl+Alt+K` / `Cmd+Opt+K`).

### 4.1 Logo (2분)

- Text tool `T` → "Lucive"
- 스타일: `h1`
- Fill: `grad/primary`
- 컴포넌트화 → 이름 `logo/wordmark`

### 4.2 Hero Typo Card (5분)

1080×1080 사각형 안에 배치:

```
[배경: bg/deep]

  ┌─ Ambient Orb (Ellipse, Fill: brand/cyan, Opacity 15%, Blur 120) ─┐
  │                                                                   │
  │  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                                │
  │  ┃  ▪ PRE-LAUNCH · NEW AI       ┃  ← mono 스타일 뱃지            │
  │  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                │
  │                                                                   │
  │  기억하는 AI,                     ← display/L (text/primary)      │
  │  서사가 있는 AI                   ← display/L (grad/aurora)       │
  │                                                                   │
  │  챗봇을 넘어선 비주얼 노벨형       ← body/L (text/secondary)      │
  │  AI 동반자를 만나보세요.                                            │
  │                                                                   │
  │  [ 지금 사전 등록 → ]              ← 버튼 (grad/primary fill)     │
  │                                                                   │
  └──────────────────────────────────────────────────────────────────┘
       lucive.app · [QR 또는 링크]       ← caption (text/tertiary)
```

- Ambient Orb: 원형 `W:500 H:500`, Opacity 15%, Effect → Layer blur 120
- Padding: 60px 모든 방향
- Rectangle 모서리 0 (풀 블리드)
- 컴포넌트화 → `card/hero-typo`

**Auto layout 설정**: 텍스트 묶음 선택 → `Shift + A` → 수직, Gap 16, Padding 동일

### 4.3 Matrix Row (재사용 핵심) (5분)

매트릭스 비교표의 한 행 컴포넌트:

```
[Feature 이름]      [Lucive ✓]  [C.AI ✗]  [크랙 ✗]  [제타 ✗]  [Replika ✗]  [Talkie ✗]
  설명 한 줄
```

- Auto layout 수평, Gap 14
- 각 셀: 120×60 (정렬 유지)
- `Variant` 기능 사용해서 Lucive 컬럼은 항상 초록 ✓, 타사는 기본 ✗/▲ 토글
- Component Properties로 `feature name`, `feature desc`을 외부에서 조작 가능하게

**Variants 만들기:**
1. 매트릭스 Row 컴포넌트 선택
2. 우측 `Add variant` → `competitor-1-state: pass / partial / fail`
3. 같은 방식으로 각 경쟁사별 state variant 추가

Variants 완성 시 외부에서 편하게 ✓/▲/✗ 전환 가능.

### 4.4 VN Chat Bubble (LP·User) (5분)

채팅 버블 컴포넌트 2종:

**LP 버블 (`bubble/lp`):**
- 배경: `bg/elevated`
- Border-radius: 16 16 16 4 (왼쪽 하단만 각짐)
- Border: 1px solid `border/subtle`
- Padding: 11 16
- 내부 텍스트: `body/M` + `text/primary`
- 상단 label: `caption` + `brand/pink` (LP 이름)

**User 버블 (`bubble/me`):**
- 배경: `grad/primary`
- Border-radius: 16 16 4 16 (오른쪽 하단만)
- Padding: 11 16
- 텍스트: white

Auto layout 수직 + Gap 10으로 여러 버블 쌓기 가능하게.

### 4.5 VN Scene Frame (2분)

9:14 세로 비율 프레임 (290×450 권장):

- 배경: `grad/warm` 또는 `grad/aurora`
- Opacity 오버레이: 검정 10%
- 하단 1/3 영역: `bg/deep` 반투명 (rgba 15,17,23,0.82) + backdrop blur 16
- 상단 Label: 둥근 pill, mono 폰트, "Visual Novel" 텍스트
- 컴포넌트화 → `frame/vn-scene`

### 4.6 Countdown Strip (2분)

```
┌─────────┬─────────┬─────────┬─────────┐
│   75    │   14    │   23    │   09    │
│  Days   │ Hours   │ Minutes │ Seconds │
└─────────┴─────────┴─────────┴─────────┘
```

- 각 유닛: 100×100, bg/card, border-radius 14
- 숫자: `display/L`, fill: `grad/aurora`
- 라벨: `mono`, color: `text/tertiary`
- 컴포넌트화 → `strip/countdown`

### 4.7 CTA Button (3분)

```
[ 지금 사전 등록 → ]
```

**Primary:**
- Fill: `grad/primary`
- Text: Inter 600, 15px, white
- Padding: 15 × 30
- Border-radius: 100 (pill)
- 컴포넌트화 → `btn/primary`

**Ghost:**
- Fill: transparent
- Border: 1px solid `border/medium`
- Text color: `text/primary`
- 나머지 동일
- 컴포넌트화 → `btn/ghost`

### 4.8 Pill Badge (2분)

```
▪ MEMORY
```

- Background: rgba(6,182,212,0.15) 또는 각 브랜드 색 15% opacity
- Border: 1px solid 해당 색 35% opacity
- Text: mono 폰트, 해당 색 100%
- Padding: 4 × 10, Border-radius 100
- Variants로 5종: cyan / purple / pink / gold / green

### 4.9 Tier Card (3분)

혜택 섹션용 카드 3종 (gold / silver / bronze):
- 배경: `bg/card` + 해당 tier 색 8% 그라디언트 오버레이
- Border: 해당 tier 색 35% opacity
- 상단 tag: pill badge
- 제목: `h2`
- 본문: `body/M`
- 하단: 점선 구분선 + `caption`

---

## 5. 프레임별 템플릿 채우기 (10분)

`02 — Frames` 페이지의 5개 프레임에 컴포넌트 인스턴스 배치:

### 5.1 `01_square_1080` (디시·아카·X 정사각 기본)

```
┌────────────────────────────────────┐
│                                    │
│  [card/hero-typo] 인스턴스 복사    │ ← 720×900 정중앙
│                                    │
│  또는                               │
│                                    │
│  [Matrix Row × 8줄]                 │ ← 매트릭스 비교 버전
│                                    │
│  로고 하단 [logo/wordmark]          │
└────────────────────────────────────┘
```

### 5.2 `02_portrait_4-5` (에타·네이버 카페)

```
┌────────────────────────────┐
│  [frame/vn-scene] 320×440  │ ← 상단 60%
│                            │
│  "기억하는 AI,              │
│   서사가 있는 AI"           │ ← display/L
│                            │
│  [body/L 3줄]              │
│                            │
│  [btn/primary]              │
│                            │
│  [logo/wordmark]            │
└────────────────────────────┘
```

### 5.3 `03_vertical_9-16` (숏폼 9:16)

```
┌──────────────────┐
│  ▪ MEMORY        │ ← Pill badge
│                  │
│  어제 한 말을     │ ← display/XL
│  기억합니다.     │
│                  │
│  [bubble/lp]     │ ← 채팅 데모 3-4줄
│  [bubble/me]     │
│  [bubble/lp]     │
│                  │
│  [btn/primary]   │
│                  │
│  lucive.app      │ ← caption
└──────────────────┘
```

### 5.4 `04_landscape_16-9` (X 가로·블로그 헤더)

```
┌──────────────────────────────────────┐
│  [logo] ← 좌상단                     │
│                                      │
│    기억하는 AI,                       │ ← display/XL 중앙
│    서사가 있는 AI.                    │
│                                      │
│  [캐릭터 일러스트 오른쪽]              │
│  [btn/primary]                       │
│                                      │
│  [strip/countdown 하단]              │
└──────────────────────────────────────┘
```

### 5.5 `05_og_1200x630` (카카오 공유·메타 OG)

```
┌────────────────────────────────────────┐
│                                        │
│  Lucive                                │ ← logo 좌상단
│                                        │
│  기억하는 AI, 서사가 있는 AI.           │ ← display/XL 좌측 2/3
│  비주얼 노벨로 만나는 AI 동반자.         │ ← body/L
│                                        │
│                          [캐릭터 일러]  │ ← 우측 1/3 (AI 생성 이미지 배치)
│                                        │
│  [사전 등록 · lucive.app]               │ ← caption 하단
└────────────────────────────────────────┘
```

**주의:** OG 이미지는 텍스트가 **왼쪽 2/3 영역**에만 와야 함. 카카오·페이스북이 오른쪽을 자르는 경우 있음.

---

## 6. 내보내기 세팅 (5분)

### Export Presets

각 프레임 선택 → 우측 하단 `Export` → `+` 추가:

| 용도 | 포맷 | 배율 | 설정 |
|------|:----:|:---:|------|
| 웹 업로드 | PNG | 1x | 투명 배경 필요시 |
| 소셜 공유 | JPG | 1x | 파일 크기 작을 때 |
| 인쇄물 | PNG | 2x | 고해상도 |

### 일괄 내보내기

1. 프레임 여러 개 선택 (Shift+클릭)
2. 오른쪽 Export 패널에서 + 버튼 → 포맷 추가
3. 하단 `Export 5 items` 버튼 → 폴더 선택
4. 자동으로 프레임 이름대로 저장됨

**파일 이름 컨벤션 추천:**
```
lucive_ogimg_v1_20260416.png
lucive_matrix_square_v1.png
lucive_hero_9x16_v2.png
```

---

## 7. 응용 예시 — 5분 안에 새 에셋 만들기

### 예: "기억 유지" 강조 카드 (1:1)

1. `01_square_1080` 프레임 복사 → 이름 `01_square_memory`
2. Hero Typo Card 인스턴스 선택
3. 제목 텍스트만 "기억하는 AI" → "17일 전을 기억해요"로 변경
4. 하단 Pill Badge 추가: `▪ MEMORY` (purple variant)
5. 옆에 채팅 Bubble 3개 (메모리 증명 대사)
6. Export

→ **5분 만에 디시·X용 짤방 완성**

---

## 8. 컴포넌트 사용 팁

### Auto Layout 핵심
- 자식 요소 선택 → `Shift + A`로 AutoLayout 적용
- 수직/수평, Gap, Padding 모두 속성 패널에서 조정
- **크기 자동 조정** 덕분에 텍스트 길이 바뀌어도 레이아웃 안 깨짐

### 컴포넌트 인스턴스 분리
- 컴포넌트 인스턴스 → 우클릭 → `Detach instance`
- 분리 후에는 원본 영향 안 받음 (임시 수정 시 유용)

### Override 우선순위
- 컴포넌트 변수(Component Properties) > Text content > Fill 색상
- Text content만 override 허용하려면 나머지는 `Preserve override` 체크

---

## 9. 런칭 전 체크리스트

### 마스터 파일 품질
- [ ] 색상 스타일 13개 모두 등록됨
- [ ] 그라디언트 스타일 3개 등록됨
- [ ] 텍스트 스타일 9개 등록됨
- [ ] 컴포넌트 12개 생성 완료
- [ ] 5개 프레임 모두 배경 `bg/deep` 적용
- [ ] 폰트 (Inter, Noto Sans KR, Instrument Serif, JetBrains Mono) 로드 완료

### 에셋별 내보내기 전
- [ ] 텍스트 오타 검사 (네이버 맞춤법 검사기)
- [ ] 이미지 2MB 이하
- [ ] OG 이미지 텍스트가 왼쪽 2/3에 배치
- [ ] 각 프레임별 UTM 링크 포함 여부

---

## 10. 무료 Figma 커뮤니티 템플릿 (보조)

직접 만들기 귀찮을 때 **시작점**으로 쓸 수 있는 무료 템플릿:

- [Figma Community — Social Media Template](https://www.figma.com/community/search?resource_type=files&q=social%20media%20template%20dark)
- [Mobile App Landing Template](https://www.figma.com/community/search?resource_type=files&q=mobile%20landing)
- [Product Hunt Launch Kit](https://www.figma.com/community/search?resource_type=files&q=product%20hunt)

템플릿을 복제한 뒤 색상·폰트만 Lucive 값으로 교체하면 1시간 절약 가능.

---

## 11. 다음 단계 — 제작 우선순위 (D-2 오후 시작)

1. ✅ `00 — Design System` 페이지 세팅 (15분)
2. ✅ 5개 Frame 생성 (5분)
3. ✅ Component 12개 중 **우선 6개만** 먼저 (20분):
   - `logo/wordmark`, `card/hero-typo`, `btn/primary`,
   - `bubble/lp`, `bubble/me`, `matrix-row`
4. ✅ `05_og_1200x630` 만들기 (15분)
5. ✅ `01_square_1080` 매트릭스 버전 (15분)
6. ✅ `02_portrait_4-5` 에타용 (15분)
7. Tier 2 컴포넌트는 D+1 이후 필요해지면 추가 제작

**총 소요: 약 90분** → D-2 오후 블록에 배치 가능.

---

> **💡 Pro Tip:** 한 번 만든 마스터 파일을 **복사**해서 채널별 variant 파일로 운영:
> - `LUCIVE_MASTER.fig` (원본)
> - `LUCIVE_MASTER_X.fig` (X 전용 — 짤방·GIF 중심)
> - `LUCIVE_MASTER_ETA.fig` (에타 전용 — 소프트 톤)
>
> 변형은 자유롭게, 원본은 정상 유지.
