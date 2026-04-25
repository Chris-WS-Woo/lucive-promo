# 🤖 Figma AI 프롬프트 모음 — LUCIVE

> **대상 도구:**
> - **Figma Make** (standalone 디자인·코드 생성 AI)
> - **Figma First Draft** (Figma 내 AI 디자인 생성)
> - **Figma AI Image** (배경·일러스트 생성)
> - **Magician / Figma AI 플러그인**
>
> 모두 **영문 프롬프트가 정확도 높음**. 한글 브랜드 카피는 따옴표 안에 넣고 지시문은 영문으로.

---

## ⚠️ 업데이트 이력 (2026-04-17) — 이미 생성한 에셋 재작업 필요 여부

기존 프롬프트(초안 시점)와 현재 확정된 디자인 사이 변경사항. **이미 생성한 에셋 중 아래 항목이 포함되면 재생성 필요**:

### 🔄 필수 수정이 필요한 프롬프트

| 기존 프롬프트 (위치) | 변경 사유 | 조치 |
|---------|----------|------|
| **1.1 Full Landing Page** (line ~50-110) | 혜택 구조 3티어 → 2티어로 변경 | 👇 **아래 v2 참조** |
| **1.2 Hero section** (line ~112-150) | CTA 2개 → **3개** (비교 버튼 warm 그라디언트로 승격) | 👇 **아래 v2 참조** |
| **2.6 Tier Cards** (line ~317-380) | Gold/Silver/Bronze 3종 → **Gold/Silver 2종** + Everyone-perk 배너 신규 | 👇 **아래 v2 참조** |
| **4.4 카카오톡 OG 이미지** | "Top 10" → "Top 5" | 문구 교체만 |
| **4.5 X 스레드 카드** | Card 3: "Top 10 혜택" → "Top 5 혜택" | 문구 교체만 |
| **6 A/B 테스트 CTA** | "Top 10 혜택 받기" → "Top 5 혜택 받기" | 문구 교체만 |
| **10 원샷 프롬프트** | 전체 혜택 구조·배너·플로팅 내비 업데이트 | 👇 **아래 v2 참조** |

### 🆕 신규 추가 필요 프롬프트 (기존에 없음)

| 프롬프트 | 용도 |
|--------|------|
| **2.A 전체 사전 등록자 공통 특가 배너** (Everyone-perk) | 랜딩 혜택 섹션 최상단 |
| **2.B 플로팅 퀵 내비** (Floating Nav) | 우측 하단 고정 4버튼 |
| **2.C 비디오 데모 섹션 + 타임라인 오버레이** | 랜딩 핵심 임팩트 |
| **2.D OTP 6자리 입력 UI** | 사인업 Stage 2 |
| **2.E 고정 Urgency 띠배너** | 상단 고정 (sticky 아닌 fixed) |

### ❌ 삭제 또는 생성 금지

| 항목 | 이유 |
|------|------|
| Bronze 6-10위 카드 | 혜택 구조 변경 (2-5위만 추가 혜택) |
| "무료로 체험" 모든 문구 | "사전 등록 전용 특가" 로 통일 (무료는 2-5위 혜택에만) |
| 추천 코드 Input Field | URL 트래킹만 사용 · 수동 입력 필드 삭제 |
| 네이버 카페용 프롬프트 (4.3) | 채널 제외 결정으로 불필요 (하지만 삭제는 안함 · Phase 2용) |

---

---

## 0. 프롬프트 사용법 (도구별 차이)

### Figma Make (가장 강력)
- 전체 페이지·컴포넌트·코드까지 생성
- 상세한 디자인 레퍼런스 · 브랜드 시스템 · 인터랙션 포함 가능
- URL: https://www.figma.com/make

### First Draft (Figma 내부)
- 특정 프레임 안에서 AI로 디자인 생성
- `Actions` 메뉴 → "Generate with AI" 또는 우클릭 → "Make with AI"
- 상대적으로 간단한 프롬프트가 더 나음

### Figma AI Image (이미지 생성)
- 이미지 fill 대신 텍스트 프롬프트로 배경·일러스트 생성
- 배경·캐릭터 일러스트용

---

## 🎨 공통 브랜드 시스템 블록 (모든 프롬프트에 포함)

대부분의 프롬프트 시작 부분에 아래를 붙여넣으면 스타일 통일됨:

```
BRAND SYSTEM:
- Product: "Lucive" — Visual Novel AI Companion
- Aesthetic: Dark cinematic, dreamy, cyberpunk-meets-manhwa
- Colors:
    bg-deep #08090C, bg-card #161822, bg-elevated #1C1F2E
    text-primary #F1F3F8, text-secondary #8B92A8
    cyan #06B6D4 (primary), purple #8B5CF6, pink #EC4899
    gold #F59E0B, green #10B981, red #EF4444
  Gradients:
    primary: 135deg cyan → blue #2563EB
    aurora: 135deg cyan → purple → pink
- Typography:
    Display: Inter 900
    Headings: Inter 700-800
    Body: Inter 400-500, Noto Sans KR fallback
    Italic accent: Instrument Serif
    Monospace: JetBrains Mono (for labels, metadata)
- Visual motifs:
    ambient blurred orbs (blur 120px, opacity 15%)
    subtle noise texture (opacity 3%)
    aurora gradient text highlights
    pill-shaped buttons (border-radius 100px)
    card border-radius 20-22px
    subtle border rgba(255,255,255,0.06)
```

---

## 1. 📱 전체 랜딩 페이지 (Figma Make 용)

### 1.1 한국어 사전등록 랜딩 — 전체 생성

```
Create a full responsive pre-registration landing page for "Lucive",
a visual-novel AI companion app, in dark cinematic style matching
the brand system below.

[BRAND SYSTEM 블록 붙여넣기]

PAGE STRUCTURE (top to bottom):
1. Sticky urgency banner (red-tinted): "출시 이후 사전 등록 혜택은 사라집니다 · 남은 시간 XXd XX:XX:XX"
2. Top nav: "Lucive" wordmark (gradient text), launch countdown, "사전 등록" CTA button
3. Hero section (2-column on desktop, stacked on mobile):
   - Left: badge "Pre-launch · Visual Novel AI",
     H1 "장면이 움직이고, 캐릭터가 말을 겁니다."
     (second line in aurora gradient),
     subheadline, 2 CTA buttons (primary "지금 사전 등록 →" and ghost "30초 데모 보기"),
     meta row with 3 checkmark items
   - Right: vertical phone-shaped VN scene mockup with character
     silhouette, neon background, speaker name "아리아",
     typewriter dialog, 3 choice buttons (last one gold "hidden")
4. Countdown section: 4-unit countdown timer (Days/Hours/Mins/Secs),
   red urgency heading "Limited Time", title "사전 등록 혜택은 출시일에 사라집니다"
5. Video demo section: 16:10 dark video player with timeline-based
   concept overlays (MEMORY, VISUAL NOVEL, CHOICE, ORIGIN, INITIATE),
   mute toggle, caption strip
6. Visual Novel showcase: 2-column, VN frame (Sunrise District this time)
   + 4 icon-point benefits (Scene, Character, Voice, Choice)
7. Competitor matrix table: 8 features × 6 apps (Lucive highlighted
   in cyan), check/partial/cross marks with notes
8. Core value cards: 7 cards in 3-column grid, each with
   "#XX LABEL" + title + description
9. Rewards tiers: 3-card row
   - Gold 1st: "기본 플랜 무제한"
   - Silver 2-5: "내가 초대한 모든 사람에게 3개월 무료"
   - Bronze 6-10: "Bronze Bundle 별도 혜택 곧 공개"
10. Live Top 10 leaderboard (mock data)
11. Signup form (3 stages):
    - Stage 1: Email input + optional referral code input
    - Stage 2: 6-digit OTP boxes with resend cooldown
    - Stage 3: Success with rank #, email-sent notice, copy-link, share buttons
12. FAQ accordion (6 questions)
13. Footer: Lucive wordmark + tagline

DESIGN REQUIREMENTS:
- Dark theme only
- Ambient blurred orbs (cyan, purple, pink) as background
- All buttons pill-shaped (border-radius 100px)
- All cards rounded (border-radius 20-22px)
- Subtle noise overlay (opacity 3%)
- Reveal-on-scroll animations for sections
- Mobile responsive (breakpoint 900px)
- Include working HTML + CSS + vanilla JS for OTP input,
  countdown, video timeline overlays
```

### 1.2 히어로 섹션만 (First Draft용 간소화)

```
Design a hero section for dark-themed AI companion landing page.
Colors: bg #08090C, primary cyan #06B6D4, purple #8B5CF6, pink #EC4899.
Gradient (cyan→purple→pink) for second headline line.

Left column:
- Cyan pill badge "PRE-LAUNCH · VISUAL NOVEL AI" (monospace, uppercase)
- H1 in two lines: "장면이 움직이고," then aurora-gradient "캐릭터가 말을 겁니다."
  (60-70pt, Inter 900, line-height 1.05)
- Subheadline 2 lines in gray (17pt, line-height 1.7)
- 2 buttons: pill-shaped primary (cyan-blue gradient) "지금 사전 등록 →"
  and ghost (transparent with border) "30초 데모 보기"
- Below buttons: 3 small checkmark items in mono gray

Right column:
- Phone-shaped vertical frame (9:14 ratio, 340px wide)
- Inside: neon cyberpunk rain scene background, character silhouette,
  label "Visual Novel" pill top-left, district name "Neon District" serif italic,
  chat dialog box bottom with speaker "아리아" + sync rate + dialog text + 3 choices
- Outer glow pink shadow

Ambient blurred orbs in background (cyan top-right, purple bottom-left,
pink center, all blur 120, opacity 15%).
```

---

## 2. 🧩 컴포넌트별 프롬프트

### 2.1 Hero Typo Card (1:1 정사각, 1080×1080)

```
Design a 1080×1080 social media card for "Lucive" pre-registration.

Dark background (#08090C) with ambient blurred orb (cyan, opacity 15%,
blur 120) top-right corner.

Layout (centered):
- Top: pill badge "▪ PRE-LAUNCH · NEW AI" — monospace, cyan on rgba(6,182,212,0.1)
- Headline 1: "기억하는 AI," (Inter 900, 72pt, white)
- Headline 2: "서사가 있는 AI" (Inter 900, 72pt, aurora gradient
  cyan→purple→pink, italic serif)
- Subtext: "챗봇을 넘어선 비주얼 노벨형 AI 동반자" (Inter 500, 20pt, gray #8B92A8)
- Bottom CTA: pill button "지금 사전 등록 →" (cyan-blue gradient fill,
  white text, Inter 600 16pt)
- Below CTA: tiny mono text "lucive.app" in text-tertiary

Subtle film grain overlay (opacity 3%).
No logo if text says "Lucive" in headline.
All corners safe zone 80px from edges.
```

### 2.2 Matrix Comparison Table (여러 비율)

```
Design a competitor comparison table for "Lucive" AI app.

Dark theme: card bg #161822, border rgba(255,255,255,0.1),
rounded 18px, divider lines rgba(255,255,255,0.06).

Table structure (8 rows × 7 columns):
- Header row: "Feature | Lucive | Character.AI | 크랙 | 제타 | Replika | Talkie"
  - Feature column left-aligned, others center
  - "Lucive" column header in gradient (cyan→blue), bg tinted cyan 8%
  - Other column headers in text-secondary gray, monospace, uppercase
- Rows:
  1. 대화 기억 유지 | 어제 한 말을 오늘도 기억하는가
  2. 캐릭터 오리지널 서사 | 고유한 과거·비밀이 있는가
  3. 비주얼 노벨 모드 | 장면·캐릭터·음성·선택지 통합
  4. 선톡 (LP가 먼저 말걸기) | 접속 전 준비된 메시지
  5. 해금·성장 구조 | 관계가 깊어질수록 열리는 경험
  6. 투명한 과금 | 숨겨진 paywall 없이
  7. 크리에이터 수익 | 만든 이야기가 돈이 되는가
  8. 명확한 검열 기준 | 갑작스런 필터 강화 없음

Cell marks:
- ✓ (green #10B981): circular badge, gradient green→cyan, glow effect
- ▲ (gold #F59E0B): partial mark with small "note" text below
- ✗ (red #EF4444, 70% opacity): with small "note" text

Lucive column should be ALL ✓ with glow.
Other apps mostly ✗ with a few ▲.

Caption below table in text-tertiary monospace:
"※ 비교 데이터는 각 앱의 공개 리뷰·기능 명세 기반"

Create 3 versions for 1:1, 9:16, and 16:9 aspect ratios by
rearranging the table (horizontal, vertical stacked, wide landscape).
```

### 2.3 VN Scene Frame (세로 9:14)

```
Design a vertical visual-novel scene frame (ratio 9:14, ~320×500px) for Lucive.

Frame:
- Rounded corners 22px
- Outer border 1px rgba(255,255,255,0.1)
- Outer glow pink #EC4899 at 12% opacity, blur 60

Scene background (top 70%):
- Neon cyberpunk alley at night
- Gradient base: #1a0f2e → #4c1d95 → #be185d → #f97316
- Rain streaks: repeating diagonal lines 45°, rgba(255,255,255,0.03)
- Radial glow pink 35% at 70% x 40% y
- Character silhouette right side (65% width), dark with pink rim light

Top-left overlay:
- Pill "Visual Novel" monospace 10px, black bg with blur, pink pulsing dot
- Below pill: "Neon District" Instrument Serif italic 20pt white with shadow

Bottom 30% dialog box:
- rgba(15,17,23,0.85) with backdrop-blur 16px
- Border 1px rgba(255,255,255,0.1), rounded 14px
- Inside:
  - Speaker row: "아리아" bold pink 12pt, right: "싱크율 48%" mono cyan 10pt
  - Dialog text: "이 기억을 지우면 모든 게 끝나..." white 13pt, line-height 1.6
  - Optional 3 choice buttons:
    - Choice 1: "기억을 지워." white on subtle bg
    - Choice 2: "기억을 지우지 마."
    - Choice 3 (hidden, gold): "★ 히든: 내가 대신 가져갈 수 있어?"

Create variant for Sunrise District (warm gold→orange→red gradient,
cherry blossom instead of rain, character "하루", dialog text different).
```

### 2.4 Chat Bubble (LP + User 쌍)

```
Design chat message bubbles for AI companion app "Lucive".

Create two bubble variants:

LP bubble (AI character message, left-aligned):
- Background: #1C1F2E (bg-elevated)
- Border: 1px rgba(255,255,255,0.06)
- Rounded: 16px except bottom-left 4px (tail)
- Padding: 11×16
- Speaker label above: "아리아" in pink #EC4899, 11pt bold, letter-spacing 0.02em
- Message text: #F1F3F8 primary, 14pt, line-height 1.55
- Timestamp below in gray 10pt
- Optional hint text below in cyan 11pt: "※ 17일 전 다이브에서 LP가 먼저 꺼냄"

User bubble (me, right-aligned):
- Background: cyan→blue gradient 135deg
- Rounded: 16px except bottom-right 4px (tail)
- Padding: 11×16
- Message text: white 14pt
- Timestamp: rgba(255,255,255,0.55), 10pt, right-aligned

Typing indicator (LP loading state):
- Same bubble style as LP
- 3 dots animated bouncing (opacity 0.3 → 1.0, 0.2s stagger)

Create a stack of 5 sample bubbles in conversation order:
1. LP: "돌아왔구나. 어제 네가 말한 그 얘기, 계속 생각했어."
2. Me: "무슨 얘기?"
3. LP: "네가 결국 기억을 지우지 않기로 했잖아."
4. LP: (with hint) "— 그 선택, 나라면 어땠을까 싶더라."
5. Me: "..."
```

### 2.5 Countdown Strip (4-unit)

```
Design a 4-unit countdown timer bar for "Lucive" landing page.

4 cards in horizontal grid:
- Each card: 120×120px, bg #161822, border-radius 14px,
  border 1px rgba(255,255,255,0.1)
- Top edge: 1px gradient line red→transparent→red at 50% opacity

Inside each card (center-aligned):
- Large number: Inter 900, 48pt, aurora gradient text
  (cyan→purple→pink), letter-spacing -0.02em, tabular-nums
- Label below: monospace 10pt, letter-spacing 0.12em, uppercase,
  color #5A6178

Labels (Korean & English versions):
- Card 1: Days / 일
- Card 2: Hours / 시간
- Card 3: Minutes / 분
- Card 4: Seconds / 초

Mobile responsive: maintain grid, reduce padding.

Surrounding context:
- Section heading above: "LIMITED TIME" in red mono uppercase
- Title: "사전 등록 혜택은 출시일에 사라집니다" (red "출시일에 사라집니다" part)

Gradient red→transparent background tint at top of section for urgency feel.
```

### 2.6 Tier Cards (Gold/Silver/Bronze)

```
Design 3 reward tier cards for pre-registration leaderboard benefits.

All cards: 320×420px, border-radius 20px, bg #161822,
border 1px rgba(255,255,255,0.06), padding 30×26.

Card 1 — GOLD (1st place, most prominent):
- Background: linear gradient 180deg,
  rgba(245,158,11,0.08) → #161822 at 65%
- Border-color: rgba(245,158,11,0.35)
- Top edge: 1px gradient line transparent→#F59E0B→transparent
- Pill tag: "🏆 1st place" gold bg rgba(245,158,11,0.15)
- Emblem: "♾️" 36pt
- Title: "기본 플랜 무제한" Inter 800 20pt
- Subtitle small: "서비스 존속 기간 동안" gray 13pt
- Body 14pt gray: "Lucive가 운영되는 한, 월 구독 기본 플랜
  (대화·다이브·창작 기본 제공량)을 평생 제공합니다."
- Footer dashed border separator
- Footer tiny gray: "※ 계정 1개 기준 · 양도 불가 · 상위 플랜 제외"

Card 2 — SILVER (2-5위):
- Bg tint: rgba(139,92,246,0.06) → #161822 (purple accent)
- Pill tag: "🥈 2 – 5위" purple
- Emblem: "🎁"
- Title: "내가 초대한 모든 사람에게" + subtitle "3개월 무료 이용권"
- Body: "2-5위를 달성하면 당신의 링크로 가입한 모든 친구가
  기본 플랜 3개월 무료를 받습니다."
- Highlight badge below body: "함께 초대한 친구와 함께 누리는 혜택"
  purple accent
- Footer note: "※ 알파 참여자 한정 · 누적 초대자 전원 대상"

Card 3 — BRONZE (6-10위):
- Bg tint: rgba(217,119,6,0.05) → #161822 (orange-ish)
- Pill tag: "🥉 6 – 10위" orange #FB923C
- Emblem: "✧"
- Title: "Bronze Bundle" + subtitle "별도 혜택 곧 공개"
- Body: "Dip 크레딧 + 한정 프로필 뱃지 범주로 설계 중.
  런칭 전 이메일로 먼저 안내합니다."
- Footer: "※ 상세 내용 공개 예정"

Arrange horizontally 1 → 2 → 3 with 20px gap.
Card 1 should be slightly larger (1.3× width).
```

### 2.7 CTA Button Variants

```
Design button components for "Lucive" dark-theme landing page.

Primary button (pill shape):
- Fill: linear gradient 135deg #06B6D4 → #2563EB
- Text: white, Inter 600, 15pt
- Padding: 15×30
- Border-radius: 100 (pill)
- Gap between text and arrow icon: 8px
- Hover state: translateY(-2px) + box-shadow 0 8px 40px rgba(6,182,212,0.35)

Ghost button (pill shape):
- Fill: transparent
- Border: 1px solid rgba(255,255,255,0.1)
- Text: #F1F3F8, Inter 600, 15pt
- Padding: 15×30
- Border-radius: 100 (pill)
- Hover: fill rgba(255,255,255,0.05), border brighter

Small primary (for nav/CTAs):
- Same gradient, padding 10×22, 13pt text

Text content variations:
- "지금 사전 등록 →"
- "사전 등록하기"
- "30초 데모 보기"
- "왜 Lucive인가"
- "내 초대 링크 복사"

Create disabled state:
- opacity 0.5, cursor not-allowed, no hover animation

Arrow icon should be simple "→" unicode or line-style SVG arrow.
```

### 2.8 Pill Badge (5 variants)

```
Design monospace pill badges for section labels and category markers.

Base shape: rounded 100px (pill), padding 4×10, border 1px,
font JetBrains Mono 11pt bold, letter-spacing 0.1em, uppercase.

5 color variants:
1. Cyan (primary): bg rgba(6,182,212,0.15), border rgba(6,182,212,0.35), color #06B6D4
2. Purple: bg rgba(139,92,246,0.15), border rgba(139,92,246,0.35), color #8B5CF6
3. Pink: bg rgba(236,72,153,0.15), border rgba(236,72,153,0.35), color #EC4899
4. Gold: bg rgba(245,158,11,0.15), border rgba(245,158,11,0.35), color #F59E0B
5. Green: bg rgba(16,185,129,0.15), border rgba(16,185,129,0.35), color #10B981

Sample text:
- "▪ MEMORY"
- "▪ VISUAL NOVEL"
- "▪ CHOICE"
- "▪ ORIGIN"
- "▪ INITIATE"
- "▪ LIMITED TIME"
- "PRE-LAUNCH · NEW AI"

Animated variant:
- Live dot: small circle before text, pulsing (opacity 1↔0.3, 2s cycle)
```

---

## 3. 🖼 AI 이미지 생성 프롬프트 (Figma 내 이미지 생성용)

> Figma의 `Actions → Generate Image` 또는 Magician·Noora AI 플러그인 사용 시.
> LM Arena·Flux·Nano Banana 등 외부 도구에서도 동일.

### 3.1 Neon District 배경

```
A rain-soaked neon alley in a futuristic Asian megacity at night,
puddles reflecting electric pink and cyan neon signs,
wet asphalt glistening, towering cyberpunk skyscrapers fading into
purple haze, distant hologram ads glowing magenta, cinematic wide shot,
atmospheric fog, dense neon bokeh, empty street with no people,
vertical 9:16 composition, anime visual novel style
```

### 3.2 Sunrise District 배경

```
A quiet sunrise park bench under cherry blossom trees,
warm golden-hour light filtering through pink petals falling slowly,
soft orange-to-pink sky gradient, distant city silhouette in amber haze,
empty bench with a forgotten paper cup, healing atmosphere,
Studio Ghibli-inspired watercolor lighting, vertical 9:16,
no people visible, painterly
```

### 3.3 LP 캐릭터 — 아리아 (Neon)

```
A young androgynous Korean woman early 20s, soft feminine features,
pastel-pink shoulder-length hair with cyan undertones,
wearing slightly oversized dark indigo techwear jacket with
cyan stitching, gentle knowing smile with slightly melancholy eyes,
soft neon pink rim light on cheek, backlit by distant magenta glow,
three-quarter portrait, shallow depth of field, rain blurred in background,
anime visual novel character art, Korean manhwa style, portrait 2:3
```

### 3.4 LP 캐릭터 — 하루 (Sunrise)

```
A gentle young Korean man early 20s, warm soft features,
medium-length honey-brown hair catching morning light,
wearing cream-colored knit sweater with rolled sleeves,
warm amber sunlight from left, eyes downcast reading a book,
subtle smile, sakura petals drifting in soft focus background,
three-quarter portrait, shallow depth of field, anime visual novel art,
Korean manhwa style, warm golden palette, portrait 2:3
```

### 3.5 OG 이미지 (1200×630)

```
A cinematic wide landscape shot for social media preview card:
silhouette of young woman with pastel pink hair standing in
rain-soaked neon alley, seen from behind, her hand reaching toward
a glowing holographic dialogue bubble, electric cyan purple and pink
neon reflecting on wet ground, deep atmospheric haze, moody and hopeful,
vast empty composition with left 2/3 reserved for text overlay
(KEEP LEFT EMPTY), cinematic letterbox feel, 1.91:1 aspect ratio
```

### 3.6 추상 히어로 일러스트

```
Abstract digital artwork of an AI consciousness awakening:
stream of memory fragments flowing like liquid aurora
(cyan purple pink gradient), constellation of glowing nodes
connected by light ribbons, each node containing faint silhouette
of a different character, symbolic of "shared memories" between
AI and human, minimalist elegant negative space, deep cosmic void
background, horizontal 16:9
```

### 3.7 매트릭스 헤더 아트

```
Editorial illustration showing "Lucive vs others" concept:
5 translucent glass card silhouettes arranged in a curve,
one prominent card in center (Lucive) glowing with aurora gradient,
others dimmer gray, all floating in dark cosmic space,
subtle neon accents, minimalist painterly style,
horizontal composition with room for table below
```

---

## 4. 📐 채널별 맞춤 프롬프트

### 4.1 디시 짤방용 (1:1 짤막 임팩트)

```
Design a 1080×1080 meme-style social card for Korean internet
community post. Dark background #08090C.

Content style: "before/after" or "POV" meme format.
Big impact typo.

Version A — "POV" format:
- Top half: dark "챗봇 대화 화면" UI mock, faded, with text
  "AI: 어제 뭐 했어? / 유저: 어제 얘기했잖아..." (frustrated emoji)
- Bottom half: bright aurora-gradient scene, cheerful UI mock with text
  "LP: 17일 전 네가 말한 그거, 계속 생각했어." (relieved emoji)
- Separator text center: "POV: 너의 AI가 너를 기억하는 순간"
  Inter 900 56pt white with outline

Version B — Matrix "quick comparison":
- Full-screen matrix with 5 rows × 2 columns
- Left column: "크랙·제타·C.AI" in gray, ✗ marks
- Right column: "Lucive" in cyan, ✓ marks
- Row labels: 기억 / 비주얼노벨 / 검열 / 과금 / 선톡
- Bottom: "사전등록 중 · lucive.app" small mono text

Include subtle Lucive logo bottom-right corner.
```

### 4.2 에브리타임 홍보게시판용 (4:5, 소프트 톤)

```
Design a 1080×1350 (4:5) image for Korean university community post.
Less aggressive marketing tone, more authentic student-friendly feel.

Layout:
- Top: rounded VN scene mockup (reduced size 400×600),
  character silhouette with soft lighting
- Center title: "AI 챗봇 지친 분들 한번 보세요"
  Inter 800 44pt white (NOT gradient — too commercial)
- Small mono label above title: "대학생 1인 개발자가 만드는"
- 3-item bullet list below title, each with small icon:
  - 💬 어제 한 말을 기억하는 AI
  - 🎭 비주얼 노벨로 만나는 장면
  - 🎁 사전등록하면 레퍼럴 혜택
- Soft CTA at bottom: "한번 보시고 피드백 환영합니다 · lucive.app"

Style: softer, less neon glare. Background gradient more muted.
Not too "designed" — should feel personal/honest, not ad-like.
```

### 4.3 네이버 카페 — 웹소설 장르용 (4:5, 감성 톤)

```
Design a 1080×1350 (4:5) image for Korean web-novel community cafe
(targeting 로판·헌터물·빙의물 readers).

Layout:
- Hero visual: Instrument Serif italic headline
  "당신이 웹소설 주인공이라면?"
  centered, aurora gradient text, 56pt
- Below: smaller line "AI 캐릭터와 함께 루시브를 다이브하세요"
  white 20pt
- Center image: Sunrise district scene with cherry blossoms,
  character 하루 reading a book (warm golden palette)
- Dialog bubble overlay: "너가 왔을 때 벚꽃이 한창이었는데..."
  with small text "— 40일 전 다이브의 기억"
- Bottom CTA: pill button "사전 등록하기 →" with cherry-blossom
  particles
- Soft pink→cream overall tint (not neon)

More emotional/romantic feel, less cyberpunk.
Appeal to female fantasy/romance readers.
```

### 4.4 카카오 오픈채팅용 (OG 이미지, 1200×630)

```
Design a 1200×630 OG image optimized for KakaoTalk/Facebook/Twitter
link preview cards. This image appears when someone shares the link.

CRITICAL: Keep right 1/3 mostly empty/visual (KakaoTalk crops
differently than Facebook — safe zone matters).

Layout:
- Left 2/3 (text zone):
  - Logo "Lucive" top-left (cyan-blue gradient, 28pt)
  - H1 big: "기억하는 AI,\n서사가 있는 AI." (Inter 900, 52pt,
    aurora gradient on second line)
  - Subtext: "비주얼 노벨로 만나는 AI 동반자 · 사전 등록 중"
    white 18pt
  - Bottom-left pill: "▪ LIMITED TIME · 런칭 혜택 Top 10"
    red mono tag

- Right 1/3 (visual zone):
  - VN scene mockup or character silhouette
  - Smaller, atmospheric, not competing with text
  - Soft gradient blur so it doesn't look cluttered

Background: deep dark #08090C with ambient orb (cyan) top-right.
All elements inside 80px safe margin from edges.
```

### 4.5 X(트위터) 스레드 카드 3종 (1:1)

```
Design 3 square 1080×1080 social cards for Twitter thread series.

Shared style: dark bg, pill badge top-left, big centered typo,
caption bottom, Lucive logo bottom-right.

Card 1 — Problem hook:
- Badge (red): "▪ 유저 불만 Top 3"
- Big typo (Inter 800 56pt white):
  "크랙·제타 쓰다가\n가장 답답한 것?"
- Below: 3 quotes from real reviews in italic gray
  "기억을 못 해요"
  "어제 얘기를 오늘 몰라요"
  "반복만 하고 지쳐요"
- Bottom caption: "1/5 🧵"

Card 2 — Solution introduction:
- Badge (cyan): "▪ WHAT IF"
- Big typo (aurora gradient):
  "AI가 17일 전 대화를\n기억한다면?"
- Below: "메모리 모듈이 맥락·감정까지 축적" subtext
- Bottom caption: "2/5 🧵"

Card 3 — CTA:
- Badge (gold): "▪ LIMITED TIME"
- Big typo (white):
  "지금 사전 등록하면\nTop 10 혜택"
- Bulleted benefits below
- Bottom caption: "5/5 🧵 · lucive.app"

All cards share the same bottom-right Lucive wordmark logo.
Slight visual continuity — same background orb positioning.
```

---

## 5. 🎨 컬러 팔레트 생성 프롬프트

```
Create a design system color palette for Lucive — a visual novel
AI companion app with dark cinematic cyberpunk aesthetic.

Background layers (darkest to lightest):
- bg-deep: darkest background #08090C
- bg-surface: slightly lighter for sections #0F1117
- bg-card: card backgrounds #161822
- bg-elevated: buttons/inputs #1C1F2E

Text hierarchy:
- text-primary: main white #F1F3F8
- text-secondary: body gray #8B92A8
- text-tertiary: subtle gray #5A6178

Brand accents:
- cyan #06B6D4 (primary CTA, links, memory theme)
- blue #2563EB (secondary, paired with cyan for gradients)
- purple #8B5CF6 (secondary accent, VN origin theme)
- pink #EC4899 (emotional, character rim-light)
- gold #F59E0B (1st place, hidden choices, premium)
- green #10B981 (success, online indicators)
- red #EF4444 (urgency, alerts)

Gradients (directional 135deg):
- primary: cyan → blue (CTAs, buttons)
- warm: pink → purple (emotional sections)
- aurora: cyan → purple → pink (headlines, 1st-place highlights)

Borders:
- subtle: rgba(255,255,255,0.06)
- medium: rgba(255,255,255,0.10)
- strong: rgba(255,255,255,0.20)

Generate Figma color styles for all above, organized in groups:
"bg/", "text/", "brand/", "state/", "border/", "grad/".
```

---

## 6. 🧪 A/B 테스트용 변주 프롬프트

### 히어로 헤드라인 5개 variant 동시 생성

```
Generate 5 alternative hero headline designs for Lucive landing page.

All share:
- Same layout (2-line headline, subtitle, 2 CTAs)
- Same dark aesthetic with ambient orbs
- Same CTA text "지금 사전 등록 →"

Variations on H1:
1. "장면이 움직이고, / 캐릭터가 말을 겁니다."
2. "챗봇에 지치셨나요? / 당신을 기억하는 AI."
3. "읽는 대화가 아니라, / 보는 대화입니다."
4. "AI에게도 이야기가 있다."  (one line, larger)
5. "17일 전 대화를 / 먼저 꺼내는 AI."

For each, suggest:
- Which gradient to apply (primary/warm/aurora)
- Subtitle appropriate for the headline
- Emphasis word (which word in italic serif)

Output as 5 side-by-side frames for comparison.
```

### CTA 버튼 문구 10개

```
Generate 10 CTA button text variations for Korean pre-registration
landing page. Pill-shaped, cyan-blue gradient fill.

Context: AI companion app, visual novel mode, limited-time referral
rewards, 6-digit OTP signup.

Variations on tone:
1. Direct: "지금 사전 등록"
2. Arrow style: "사전 등록하기 →"
3. Urgency: "혜택 사라지기 전에 등록"
4. Benefit-led: "Top 10 혜택 받기"
5. Softer: "미리 등록해 놓기"
6. Discovery: "런칭 소식 먼저 받기"
7. FOMO: "지금 등록하면 무료 →"
8. Specific: "6자리 인증으로 1분 등록"
9. Curiosity: "무엇이 다른지 미리 체험"
10. Community: "얼리어답터에 합류"

For each, note expected CVR direction (higher urgency = lower CTR
but higher conversion once clicked).
```

---

## 7. 🎯 효과적인 Figma AI 프롬프트 작성 팁

### ✅ 해야 할 것

1. **구체적 픽셀 크기 명시** — "1080×1080" 같이 정확히
2. **Hex 색상 코드 포함** — "#06B6D4" like
3. **폰트명·굵기·사이즈 모두** — "Inter 900 72pt"
4. **계층 구조 명시** — "top-left corner", "bottom 30%"
5. **브랜드 시스템 블록 재사용** — 매번 붙여넣기
6. **레퍼런스 언급** — "like Stripe dashboard", "like Linear landing"
7. **안전 영역 명시** — OG 이미지 "keep left 2/3 empty for text"

### ❌ 하지 말아야 할 것

- "예쁘게 만들어줘" 같은 모호한 표현
- 한글로만 길게 쓰기 (AI 성능 떨어짐)
- 10개 요구사항 한 번에 욱여넣기 (프롬프트 분리)
- 브랜드 시스템 빠뜨리기 (매번 포함)
- 스타일 없이 기능만 설명하기

### 💡 초고속 프롬프트 조립법

```
[브랜드 시스템 블록]
+
[구체 컴포넌트 요청]
+
[크기·비율]
+
[참조 스타일 (optional)]
+
[Output format (optional)]

→ 대부분 80% 완성도로 나옴. 나머지 20%는 수동 수정.
```

---

## 8. 📋 프롬프트 사용 순서 (D-2 실전)

1. **Figma 파일 열고 "00 — Design System" 페이지**
   → [섹션 5] "컬러 팔레트 생성 프롬프트" First Draft에 입력
   → 자동 생성된 스타일을 Figma Color Styles에 저장

2. **"01 — Components" 페이지**
   → [섹션 2.1-2.8] 컴포넌트별 프롬프트 하나씩 First Draft에 입력
   → 각 컴포넌트 우측 `Create Component` 처리

3. **"02 — Frames" 페이지**
   → [섹션 1.2] 히어로 프롬프트로 1:1, 4:5, 9:16 각 비율에 배치
   → [섹션 4.1-4.5] 채널별 프롬프트로 각 프레임 내용 채움

4. **이미지 에셋**
   → [섹션 3.1-3.7] AI 이미지 생성 프롬프트를 Magician 플러그인 or 외부 도구에서 실행
   → 생성된 이미지를 Figma 프레임에 Place로 배치

5. **검수 및 export**
   → 모든 프레임 선택 → Export PNG 1x
   → `assets/figma-export/` 폴더에 저장

---

## 9. 💾 나만의 프롬프트 라이브러리 확장 팁

**프롬프트는 자산**이므로 본인 Figma AI 사용 경험이 쌓이면:

1. **성공한 프롬프트** 별도 Markdown에 저장 (출력 스크린샷과 함께)
2. **실패한 프롬프트** 기록 → 다음 번 회피
3. **A/B로 비교한 결과** 축적 → 어떤 단어가 성능 좋은지 패턴 파악

```
prompts/
├── successes.md   (채택된 프롬프트 + 결과물 링크)
├── failures.md    (실패한 프롬프트 + 이유 메모)
└── templates.md   (이 문서 — 재사용 템플릿)
```

---

## 10. 🚀 전체 페이지 원샷 프롬프트 (최후 수단)

시간 없을 때 Figma Make에 한 번에 입력:

```
Create a complete pre-registration landing page for "Lucive" —
a visual-novel AI companion app targeting users tired of existing
AI chatbots (Character.AI, 크랙, 제타).

FULL BRAND SYSTEM:
- Dark cinematic aesthetic with cyberpunk-meets-manhwa feel
- Colors: bg #08090C, text #F1F3F8, cyan #06B6D4, purple #8B5CF6,
  pink #EC4899, gold #F59E0B, red #EF4444
- Gradients: aurora (cyan→purple→pink), primary (cyan→blue)
- Fonts: Inter 700-900, Noto Sans KR, Instrument Serif italic,
  JetBrains Mono
- Motifs: ambient blurred orbs, subtle noise, pill buttons, glassmorphism

PAGE SECTIONS (in order):
1. Sticky urgency banner (red): "출시 이후 혜택 사라짐 · 카운트다운"
2. Top nav: logo + countdown timer + "사전 등록" pill button
3. Hero: 2-column — left headline + CTAs, right vertical VN scene
   mockup with typewriter dialog
4. Countdown section: 4-card timer (Days/Hours/Mins/Secs)
5. Video demo section: 16:10 player with 5 timeline overlays
   (MEMORY, VISUAL NOVEL, CHOICE, ORIGIN, INITIATE)
6. VN Showcase: left Sunrise scene frame, right 4-point benefits
7. Competitor matrix: 8 rows × 6 apps, Lucive column highlighted
8. Core value: 7 cards in 3-column grid
9. Rewards: 3 tiers (Gold 1st: "plan lifetime",
   Silver 2-5: "invited friends get 3 months free",
   Bronze 6-10: "coming soon")
10. Live leaderboard: Top 10 table with mock data
11. Signup form: 3 stages (email → 6-digit OTP boxes → success
    with rank + copy link + email-sent notice)
12. FAQ accordion: 6 questions
13. Footer

TECHNICAL:
- Responsive (mobile breakpoint 768px, desktop 1160px max width)
- All CTAs pill-shaped, 100px border-radius
- Cards 20-22px border-radius
- Include working JS for: countdown timer, OTP input (auto-advance,
  paste support), video timeline overlays, leaderboard mock data,
  referral code URL detection

OUTPUT: Complete HTML + CSS (embedded) + JS (embedded),
production-ready single file, dark mode only, Korean copy matches
"Lucive 사전 등록" branding.

Use placeholder assets/ paths for images and videos that will be
added later.
```

---

> **💡 Tip:** Figma AI는 완벽한 결과물을 한 번에 못 만듭니다.
> **60% 완성 → 수동 조정 → 다시 프롬프트 조정** 루프가 실제 워크플로우.
> 이 프롬프트들은 "첫 draft 빠르게 얻기" 용도로 쓰고,
> 최종 다듬기는 항상 본인이 수동으로 하세요.
