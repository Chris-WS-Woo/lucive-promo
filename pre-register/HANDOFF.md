# LUCIVE 프리런치 사이트 · 개발팀 핸드오프

> 작성일: 2026-04-30
> 담당: wonseok.woo@gmail.com
> 저장소: github.com/Chris-WS-Woo/lucive-promo
> 배포: GitHub Pages (https://chris-ws-woo.github.io/lucive-promo/pre-register/v38-lp-wide.html)

---

## 0. 한 페이지 요약

- 정적 HTML/CSS/JS 사이트 (빌드 없음, 바닐라)
- 알파 사전등록 + 데모 체험 + 핵심 사용자 설문 3개 기능
- 알파 **선발 컨셉 없음** (모두에게 오픈, 핵심 사용자는 별도 안내/혜택)
- 현재 모든 폼·공유는 클라이언트 mock. 백엔드 미연결
- GitHub Pages 자동 배포 (main 브랜치 push)

---

## 1. 활성 파일 (Canonical)

개발팀이 다룰 실 운영 페이지는 다음 6개입니다. 그 외 `v1*–v37*` 파일은 모두 archived 이력 (참조용).

| 파일 | 역할 | 진입점 |
|---|---|---|
| `v38-lp-wide.html` | **메인 랜딩** | ✅ 사이트 진입점 |
| `v34-kr-lucive.html` | 캐릭터 체험 데모 (35 캐릭터 grid + chat + VN) | 메인의 "체험" CTA |
| `v35-signup.html` | 사전등록 폼 + 성공 화면 (프로모/공유) | 메인의 "사전등록" CTA |
| `screening.html` | 핵심 사용자 설문 (8 + 1 문항) | signup 성공 화면 CTA |
| `terms.html` | 이용약관 | footer |
| `privacy.html` | 개인정보 처리방침 | footer |

기타 자산:
- `lp-data/lp_demo_data_{sunrise,neon,underground,velvet,indie}.js` — 35 캐릭터 데이터 (LP_FULL 빌드)
- 이미지 자산: 외부 CDN (`https://cdn.deepintothe.xyz/lucive/`)

---

## 2. 유저 플로우

```
                    ┌──────────────────────────────────┐
                    │  v38-lp-wide.html  (메인 랜딩)    │
                    │  hero → 4 phases → lineup → CTA  │
                    └──────────────────────────────────┘
                              │             │
                  체험        │             │  사전등록
                              ▼             ▼
            ┌──────────────────────┐   ┌────────────────────┐
            │ v34-kr-lucive.html   │   │ v35-signup.html    │
            │ (select grid →       │   │ (이메일 폼)        │
            │  profile → chat/VN)  │   │                    │
            └──────────────────────┘   └────────────────────┘
                                                │
                                                │ 사전등록 완료
                                                ▼
                                       ┌────────────────────┐
                                       │ 성공 화면          │
                                       │ - 프로모 코드      │
                                       │ - 카톡/X/링크 공유 │
                                       │ - 추천 1위 / 2-5위 │
                                       │ - 설문 CTA →       │
                                       └────────────────────┘
                                                │
                                                ▼
                                       ┌────────────────────┐
                                       │ screening.html     │
                                       │ (8문항 + 1 옵션)   │
                                       │ - Dip 500 즉시     │
                                       │ - 핵심 테스터 안내 │
                                       └────────────────────┘
```

---

## 3. 페이지별 상세 스펙

### 3.1 메인 랜딩 — `v38-lp-wide.html`

**구조** (스크롤 스냅 단위로 5개 섹션 + lineup + pre-cta + footer):

| 섹션 | 디스트릭트 색 | 역할 |
|---|---|---|
| HERO (100vh) | gold | 강렬한 첫 인상 |
| PHASE 02 살아있는 세계 | velvet | 5 캐릭터 첫 챗 (FIRST CONTACT) sequential reveal |
| PHASE 03 비주얼 노블 | sunrise | 5 캐릭터 VN 화면 cycling |
| PHASE 04 분기 | velvet | 5 캐릭터 + 선택지 cycling |
| PHASE 05 LINKED 기억들 | indie | 5 캐릭터 linked chat sequential reveal |
| LINEUP | neutral | 35 known + 10 mystery 캐릭터 그리드 |
| PRE-CTA | neutral | "먼저 한 번 만나보세요" + 체험/사전등록 |
| FOOTER | neutral | LUCIVE / 이용약관 / 개인정보 |

**고정 UI**:
- 상단: LUCIVE 워드마크 (좌, 클릭시 top scroll) + 사전등록 (우, gold pill)
- 우하단 floating CTA 가로 3버튼: `↑ 처음으로` / `체험하러 가기 ▶` / `바로 사전등록하러 가기 →` (gold)

**Phase 02 / 05 핵심 인터랙션** (개발 시 주의):

- 슬라이드 cycle 30s · 각 슬라이드 6s 노출 (hard-cut 전환)
- 슬라이드별 `--sd` CSS 변수로 base offset (0/6/12/18/24s)
- 메시지 sequential reveal: `.mock-body > *:not(.mock-input):nth-child(N)` 으로 `animation-delay: calc(var(--sd) + offset)` 적용
- 입력창은 항상 노출, 안쪽 텍스트만 typewriter (max-width 0→200px)
- 슬라이드 간 hard-cut: `@keyframes slideCycle{0%,19.8%{opacity:1}20%,100%{opacity:0}}`

**말풍선 폭 구조 (중요!)**:

```html
<div class="mock-msg lp">
  <div class="mock-msg-inner">      <!-- 핵심: inline-flex wrapper -->
    <div class="mock-mini">avatar</div>
    <div class="mock-bubble">text</div>
  </div>
</div>
```

```css
.mock-msg{display:block;width:100%}              /* block 레벨 */
.mock-msg-inner{display:inline-flex;...}         /* inline-flex (content sized) */
.mock-bubble{...max-width:240px}                 /* 픽셀 cap */
```

이 구조를 깨지 않아야 함. nested flex 만들면 cross-axis 사이징이 min-content로 fallback되는 브라우저 이슈 있음 (이전 시행착오 다수).

### 3.2 캐릭터 체험 — `v34-kr-lucive.html`

**Stage 머신**:
- `select-stage` (LP grid 35명, 카테고리 탭)
- `profile-stage` (캐릭터 프로필 + entry 화면)
- `chat-stage` (Pre-Link Chat / Linked Chat)
- `vn-stage` (선택지 분기 비주얼 노블)
- `final-overlay` (체험 종료, 사전등록/다른 캐릭터 선택)

**상단 UI**:
- 좌: 이전으로 (history.back, 직전 페이지가 v38)
- 우: 사전등록 escape (어느 stage에서든 노출)

**데이터 소스**: `lp-data/lp_demo_data_*.js` 5개 디스트릭트 LP_FULL 객체.

각 캐릭터 데이터 형식:
```js
LP_FULL.taeo = {
  name: '태오', district: 'sunrise',
  profileBg: 'img/lp/taeo_entry/profile_bg.png',
  entryThumb: 'img/lp/taeo_entry/scene1.png',
  bg: [...],  // 멀티 BG 시나리오
  preLinkChat: [...],  // 첫 만남 메시지
  vn: [...],           // 비주얼 노블 컷
  linked: [...]        // 재방문 시 기억 메시지
}
```

**asset 경로 변환**:
- 데이터 파일 안 경로는 `img/lp/...` 상대 경로
- 런타임에 `resolveAsset()` 헬퍼로 CDN URL 변환:
  `https://cdn.deepintothe.xyz/lucive/img/lp/...`

### 3.3 사전등록 — `v35-signup.html`

**입력 폼**:
- `email` (required)
- `agreedToTerms` (checkbox, required)
- `marketingConsent` (checkbox, optional)
- `referralCode` (URL `?r=XXXX` 자동 캡처 — **현재 미구현, 백엔드 필요**)

**제출 시 (현재 mock)**:
- 이메일 hash로 promoCode 생성 (예: `LUCIVE·A8X7B2`)
- 초대 URL 생성: `lucive.app/r/{promoCode}`
- 성공 화면 표시

**성공 화면 컴포넌트**:
1. `promo-block` — 내 코드 + 초대 링크 + 카톡/X/링크 공유
2. `tier-block` — 추천 보너스 (1위 / 2-5위)
3. `next-block` — 설문 CTA + 다이브 보상 안내

**친구 초대 보상**: 초대자/피초대자 둘 다 +100 다이브.

### 3.4 핵심 사용자 설문 — `screening.html`

**구성**:
- intro 화면 (목적 안내)
- 9개 질문 페이지 (q01 ~ q10, q10은 옵션)
  - 객관식 single, 객관식 multi, 척도, 텍스트, 텍스트영역
- complete 화면 (보상 안내 + 카톡 채널 invite)

**진행 UI**: 상단 progress bar + dot + 시간 pill (남은 시간 추정).

**완료 보상**: Dip 500 즉시 + 핵심 테스터 활동 시 추가 다이브 + 별도 혜택 (구체 미정).

### 3.5 약관 / 개인정보 — `terms.html`, `privacy.html`

- 정적 텍스트 (사전 공개 초안, 시행일 2026-04-22)
- 상단 돌아가기 버튼: `history.back()` (없으면 root로 fallback)

---

## 4. 데이터 모델 (백엔드 명세 제안)

### 4.1 사전등록 (POST /api/preregister)

**Request**:
```json
{
  "email": "user@example.com",
  "agreedToTerms": true,
  "marketingConsent": true,
  "referralCode": "LUCIVE·X8K2A0"
}
```

**Response**:
```json
{
  "success": true,
  "promoCode": "LUCIVE·A8X7B2",
  "inviteUrl": "https://lucive.app/r/A8X7B2",
  "registeredAt": "2026-04-30T01:23:45Z"
}
```

### 4.2 설문 응답 (POST /api/survey)

**Request**:
```json
{
  "email": "user@example.com",
  "answers": {
    "q01": "value",
    "q02": ["choice1", "choice2"],
    ...
    "q10": "free text optional"
  },
  "completedAt": "2026-04-30T01:30:00Z"
}
```

**Response**:
```json
{
  "success": true,
  "rewardDip": 500,
  "totalDip": 600,
  "isCoreUser": true   // 응답 분석 후 핵심 사용자 분류
}
```

### 4.3 추천 관계 / 순위 (GET /api/leaderboard/{email})

**Response**:
```json
{
  "myInviteCount": 7,
  "myRank": 12,
  "topPrize": "기본 서비스 평생 무료",
  "topRanks": [
    {"rank": 1, "count": 47, "anonymous": "k**@example.com"},
    ...
  ]
}
```

### 4.4 이메일 발송 트리거

- 사전등록 환영 (즉시)
- 설문 완료 보상 (즉시, Dip 적립)
- 알파 오픈 안내 (운영팀 수동)
- 추천 보상 알림 (친구 가입 시 양쪽)
- 핵심 테스터 안내 (운영팀 수동)

---

## 5. 자산 / 외부 의존성

### 5.1 CDN 자산 (필수)

Base: `https://cdn.deepintothe.xyz/lucive/`

```
img/lp/
├── {key}.png                         # 캐릭터 아바타 (작은 원형)
└── {key}_entry/
    ├── profile_bg.png                # 풀 atmospheric 배경
    ├── header.png                    # 와이드 헤더 배경
    ├── scene1.png, scene2.png, ...   # 시나리오 BG
    └── char_{key}.png                # 캐릭터 컷아웃 (투명 배경)
```

35 캐릭터 키 (5 디스트릭트):
- **sunrise**: taeo, ihana, minjun_sr, maria, seha, ryo
- **neon**: haejun, kai, jian, damya, lise, nia, levi, lana
- **underground**: sebin, or_, raon, ella, yujin, changsik
- **velvet**: yun_ara, stella, adel, leon, sia, inis, seraphine, myur, kael
- **indie**: ruon, piera, nova, haru, juhyuk, seoyul

### 5.2 폰트 (Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,700&display=swap">
```

- **Cormorant Garamond** (display, italic) — 헤드라인, 캐치프레이즈
- **Inter** (sans) — 본문, UI
- **JetBrains Mono** (mono) — 라벨, 카운터, 코드

### 5.3 자바스크립트 라이브러리

- **없음**. 모든 인터랙션 vanilla JS
- 카카오 공유는 현재 alert mock — 정식은 [Kakao JS SDK](https://developers.kakao.com/docs/latest/ko/kakaotalk-sharing/js) 필요

---

## 6. 디자인 토큰

### 6.1 컬러 (v38 기준 통일)

```css
--bg: #FFF9F7              /* 크림 배경 */
--card: #fff
--elevated: #FAEFE8
--text-1: #2A1A22          /* 진한 본문 */
--text-2: #6B5560          /* 보조 본문 */
--text-3: #9C8893          /* 흐린 메타 */
--accent: #C97B89          /* 로즈 핑크 (em, hover) */
--gold: #D6B07C            /* 골드 primary CTA */
--gold-deep: #b8945e
--divider: rgba(63,38,52,.08)

/* 디스트릭트 */
--d-sunrise: #FFB56B
--d-neon: #5EC8FF
--d-underground: #D45877
--d-velvet: #C084FC
--d-indie: #7EE5B8
```

### 6.2 타이포 스케일

| 용도 | 폰트 | 사이즈 |
|---|---|---|
| Hero h1 | Cormorant 700 italic | clamp(38, 6.2vw, 80) |
| Phase h | Cormorant 700 italic | clamp(34, 4.6vw, 60) |
| Section h (signup tier) | Cormorant 700 | 19px |
| 본문 | Inter 400 | 14-15px |
| 라벨 / mono | JetBrains Mono 800 | 9.5-12px |

### 6.3 인터랙션 표준

- 버튼 transition: `.2s var(--ease)`, `var(--ease) = cubic-bezier(.22,1,.36,1)`
- 호버 lift: `transform: translateY(-1~2px)`
- 골드 primary 그림자: `0 6-14px ... rgba(214,176,124,.32)`
- 폼 focus ring: 3px rgba(201,123,137,.15)

---

## 7. 백엔드 연동 TODO (우선순위 순)

### P0 — 알파 오픈 전 필수

| # | 항목 | 현재 상태 | 필요 작업 |
|---|---|---|---|
| 1 | 사전등록 폼 → DB | localStorage mock | POST API + 이메일 검증 + dedup |
| 2 | 환영 이메일 발송 | 없음 | SES/Sendgrid + 템플릿 |
| 3 | 프로모 코드 발급 | 클라이언트 hash | 서버 측 발급 (충돌 방지) |
| 4 | 추천 관계 추적 | 없음 | URL `?r=` 캡처 + DB join |

### P1 — 캠페인 운영용

| # | 항목 | 현재 상태 | 필요 작업 |
|---|---|---|---|
| 5 | 설문 응답 저장 | 클라이언트만 | POST /api/survey |
| 6 | Dip 적립 시스템 | 표시만 | 사용자별 Dip 잔액 + 트랜잭션 |
| 7 | Top 5 순위 계산 | 없음 | 추천 카운트 집계 + 순위 API |
| 8 | 카카오 공유 SDK | alert mock | Kakao JS SDK 통합 |

### P2 — 정식 오픈 전

| # | 항목 | 현재 상태 | 필요 작업 |
|---|---|---|---|
| 9 | 이용약관/개인정보 정식본 | 사전 공개 초안 | 법무 검토 후 최종본 |
| 10 | 핵심 테스터 분류 로직 | 미정 | 설문 응답 기반 분류 알고리즘 |
| 11 | 다국어 지원 | 한국어만 | i18n 구조 (영문 우선?) |

---

## 8. 알려진 이슈 / 주의사항

### 8.1 브라우저 호환성

- `width:max-content`, `:not(.foo):nth-child(N)` 사용 — Chrome/Safari/Firefox 최신 OK, IE 미지원
- `backdrop-filter: blur` — Safari 9+, Chrome 76+ (구형 모바일 fallback 필요할 수 있음)
- `scroll-snap-type: y proximity` — iOS Safari에서 가끔 미세 ghost (방향성에 따라)

### 8.2 모바일 최적화

- Phase 02/05 phone mockup이 작은 화면에서 좁아질 수 있음 (max-width:340px)
- floating CTA 가로 3버튼은 ≤640px에서 wrap (max-width: calc(100vw - 36px))
- screening.html survey는 모바일 우선 디자인

### 8.3 접근성 (a11y)

- 폼 label 연결 OK
- 진행 progress bar에 `role="progressbar"` 미부여 (TODO)
- 키보드 nav: 일부 stage에서 focus trap 미구현
- Reduced motion (`prefers-reduced-motion`) 미대응 — 추가 권장

### 8.4 SEO

- `<meta name="robots" content="noindex">` 거의 모든 페이지에 설정됨 (사전 등록 단계라 의도적)
- 정식 오픈 시 메인 랜딩만 `index, follow` 로 변경

---

## 9. 빌드 / 배포

- **빌드 없음** — vanilla HTML/CSS/JS
- **GitHub Pages** 자동 배포: main 브랜치 push 시 1분 내 반영
- **Netlify 설정** (`netlify.toml`) 도 있음 — Netlify 배포로 전환 시 사용
- 배포 URL: `https://chris-ws-woo.github.io/lucive-promo/pre-register/v38-lp-wide.html`

### Custom domain 연결 시

- DNS A 레코드 → GitHub Pages IP 또는 CNAME → `chris-ws-woo.github.io`
- 별도 `CNAME` 파일 필요 (`pre-register/CNAME` 또는 root)
- HTTPS는 GitHub Pages 자동 발급 (Let's Encrypt)

---

## 10. 변경 이력 (최근)

| 버전 | 주요 변경 |
|---|---|
| v38 | 메시지 sequential reveal, 입력창 typewriter, 알파 선발 컨셉 제거, "캐릭터 챗" 강조 |
| v37 | 말풍선 폭 구조 수정 (.mock-msg-inner 도입) |
| v36 | "살아있는 세계" phase 신규, FIRST CONTACT 챗 시연 |
| v35 | cream/gold 톤 통일, signup 페이지 최초 |
| v34 | 와이드 데모 + 35 캐릭터 데이터 통합 |

---

## 11. 문의

- 전체 기획/디자인: wonseok.woo@gmail.com
- 슬랙/카카오 채널: 별도 안내
- 긴급: GitHub Issues (`Chris-WS-Woo/lucive-promo`)
