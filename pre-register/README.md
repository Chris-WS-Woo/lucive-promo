# Lucive 사전 등록 페이지

## 🆕 V7 글로벌 베리에이션 매트릭스 (2026-04-19)

V6의 베리에이션 3종(SIM · FOCUS · UNIFIED)을 한·일·영 **모든 지역**으로 확장. 각 지역별 기존 테마(KR 파스텔 / JP 다크 사쿠라 / EN 테크 미니멀)는 유지하면서 vs 섹션만 해당 베리에이션으로 교체 + 지역별 실제 리뷰·컨텍스트로 로컬라이징.

| | 🇰🇷 한국 (파스텔) | 🇯🇵 일본 (다크 사쿠라) | 🇺🇸 영어 (테크 미니멀) |
|---|---|---|---|
| **SIM** 인터페이스 시뮬레이션 | [v7-kr-sim.html](v7-kr-sim.html) | [v7-jp-sim.html](v7-jp-sim.html) | [v7-en-sim.html](v7-en-sim.html) |
| **FOCUS** 1주제 1카드 대각선 | [v7-kr-focus.html](v7-kr-focus.html) | [v7-jp-focus.html](v7-jp-focus.html) | [v7-en-focus.html](v7-en-focus.html) |
| **UNIFIED** 4문제 → 1대화 | [v7-kr-unified.html](v7-kr-unified.html) | [v7-jp-unified.html](v7-jp-unified.html) | [v7-en-unified.html](v7-en-unified.html) |

### 지역별 타깃 경쟁사 (Row 3 · 가격 정책 드리프트)
- 🇰🇷 KR: **크랙** (뤼튼→크랙 리브랜딩 · 화폐 3번 개편 · 월정액 폐지 · 무료 챗 폐지 예고)
- 🇯🇵 JP: **Replika** (ライフタイムプラン 구매 후 劣化 · 親密모드 삭제 · 신앱 강제 이관)
- 🇺🇸 EN: **Replika** (lifetime plan → model downgrade · intimate mode removed · forced migration to new app)

### 다른 Row 공통 타깃
- Row 1 선톡 부재 → Character.AI · Replika
- Row 2 같은 봇 반복 → Character.AI · Talkie
- Row 4 이미지 한 턄 첨부 → Character.AI · Chai

### V6 → V7 차이점
- V6: 베리에이션 3종은 KR에만 존재, JP/EN은 4열 비교 그리드 고정
- V7: 베리에이션 3종 × 3개 지역 = **9개 모두 존재**
- V7의 각 지역 파일은 해당 지역의 테마(파스텔/다크 사쿠라/테크 미니멀)와 언어 그대로 유지
- 가격 정책 Row는 지역별 실제 사례 교체 (KR 크랙 / JP·EN Replika)



LP MVP 기준 사전 등록 + 레퍼럴 리더보드 페이지 모음. 초기 드래프트(v1–v3) → 통합본(v4) → 지역별 비스포크(v5) → **v6 (4열 경쟁사 비교 그리드)** 순으로 발전.

## 파일

| 파일 | 버전 | 방향 |
|------|------|------|
| [v1-extended.html](v1-extended.html) | **V1 · Teaser Extended** | 기존 `lucive-redesign/prototype/teaser.html` 톤앤매너 확장. Aurora 그라디언트 + 중앙정렬 히어로. |
| [v2-independent.html](v2-independent.html) | **V2 · Editorial Dark** | 2컬럼 에디토리얼 + LP 타이핑 시뮬레이션. teaser 다크 감성 계승. |
| [v3-vn-focus.html](v3-vn-focus.html) | **V3 · VN Focus + Urgency** | 비주얼 노벨 전면, 8×6 경쟁사 비교 매트릭스, 카운트다운 + 추천 코드. |
| [v4-final.html](v4-final.html) | **V4 · Final (글로벌 공통)** | v3 구조 + 플로팅 네비 + Top 5 티어 + 8문항 스크리닝 게이트 + 어뷰징 경고 + OTP 3단계. |
| [v5-kr.html](v5-kr.html) | **V5 🇰🇷 한국** (deprecated) | 웹툰·로판 감성. pain-pair 세로 스택 + GP 리뷰 스크린샷. v6로 대체. |
| [v5-jp.html](v5-jp.html) | **V5 🇯🇵 일본** (deprecated) | 다크 아니메 VN. pain-pair 세로 스택 + GP 리뷰 스크린샷. v6로 대체. |
| [v5-en.html](v5-en.html) | **V5 🇺🇸 미국** (deprecated) | Character.AI/Replika 테크 미니멀. pain-pair 세로 스택 + GP 리뷰. v6로 대체. |
| **[v6-kr.html](v6-kr.html)** | **V6 🇰🇷 한국 · 4열 비교** ★ | v5-kr 베이스 + **경쟁사 비교를 4 컬럼 가로 그리드로 재구성**. 컬럼당 [앱 로고·이름] → [GP 리뷰 미니] → [그 앱의 UI 장면] → [Lucive UI]. 크랙 / 제타 / 크랙 / Replika. |
| **[v6-jp.html](v6-jp.html)** | **V6 🇯🇵 일본 · 4열 비교** ★ | v5-jp 베이스 + 4열 그리드. Character.AI / Talkie / Replika / Chai. |
| **[v6-en.html](v6-en.html)** | **V6 🇺🇸 미국 · 4열 비교** ★ | v5-en 베이스 + 4열 그리드. Character.AI / Talkie / Replika / Chai. |
| 🆎 **[v6-kr-sim.html](v6-kr-sim.html)** | **V6 🇰🇷 한국 · 인터페이스 시뮬레이션** | A/B 테스트 베리에이션 1. 경쟁사 4열 그리드 대신 **4가지 인터페이스 장면을 실제 UI 화면으로** 세로 나열. 차이를 시각적으로 직접 보여줌. 좌우 분할. |
| 🆎 **[v6-kr-2x2.html](v6-kr-2x2.html)** | **V6 🇰🇷 한국 · 2×2 스토리 카드** | A/B 테스트 베리에이션 2. v6-kr-sim과 동일한 4가지 대비 내용을 **2×2 그리드 스토리 카드**로 배치. 한 화면에서 전체 비교. |
| 🆎 **[v6-kr-focus.html](v6-kr-focus.html)** | **V6 🇰🇷 한국 · 1주제 1카드 · 대각선** | A/B 테스트 베리에이션 3. 4가지 주제를 **각각 큰 카드 하나씩** 할애. 카드마다 좌상단=기존 앱 문제, 우상단=실제 Google Play 리뷰 스크린샷, 우하단=Lucive의 같은 순간 (X자 흐름). |
| 🆎 **[v6-kr-unified.html](v6-kr-unified.html)** | **V6 🇰🇷 한국 · 4문제 → 1대화** ★ NEW | A/B 테스트 베리에이션 4. 왼쪽 4개 문제 카드 → 오른쪽 **Lucive의 한 대화 화면**에서 동시 해결. 각 문제가 어디서 풀리는지 "해결 0N" 태그로 연결. VN 배경 유지 + 선톡 + 고유 과거 + 1 Dip 고정이 하나의 화면에서 통합됨. |
| [screening.html](screening.html) | **스크리닝 설문** | 등록 직후 연결되는 8문항 설문. +500 Dip 완주 / +2,000 Dip 선발 / +300 Dip 대기자. |

## 2026-04 업데이트 — v6 공통 개선

모든 v6 파일 (`v6-kr/jp/en` + 베리에이션)에 적용된 공통 변경 사항:

1. **상단 띠 통합 고정** — 긴급성 배너 + 브랜드·CTA 상단바가 하나의 고정 영역으로 합쳐짐. CSS 변수 `--top-h: 64~68px` 추가, `.top`을 `position:fixed`로 전환, `.wrap` padding-top 재계산.
2. **플로팅 점프 네비** — 오른쪽 하단에 원형 버튼 스택 (💭 스토리 · 🆚 비교 · 🎁 혜택 · 🎯 사전 등록). Hover 시 툴팁 표시, 모바일에선 툴팁 숨김·버튼 축소.
3. **공유 섹션에 프로모 코드 추가** — 추천 링크 아래에 `LUCIVE-{code}` 형식 프로모 코드 표시 + 복사 버튼. 카톡·X·Discord 공유 시 메시지에 코드 자동 포함되어 <b>텍스트로도 홍보 가능</b>. 친구가 코드 입력하면 양쪽 모두 +300 Dip.

## A/B 테스트 베리에이션 (v6-kr 기준, 2026-04)

`v6-kr.html`(4열 경쟁사 그리드)에 대해 **2가지 대안 포맷**을 별도 파일로 제작. 구조는 모두 동일(Hero · Features · [VS 섹션] · Rewards · Signup), VS 섹션만 교체.

### 🆎 v6-kr-sim — 인터페이스 시뮬레이션 베리에이션
**4가지 핵심 순간**을 실제 UI 화면으로 세로 나열:
| # | 대비 축 | 기존 앱 | Lucive |
|---|---------|---------|--------|
| 01 | 첫 접속 순간 | 빈 채팅·내가 먼저 인사 | LP가 15분 전 선톡(기억 기반) |
| 02 | 캐릭터 선택 | 3명 모두 "안녕! 나는 친구야 😊" | 3명 각자 고유 출생·배경 |
| 03 | 과금 구조 | 5→10→15 크랙 (누적 상승) | 1 Dip flat |
| 04 | 몰입감 | 흰 바탕·말풍선만 | VN 모드(배경·표정·음성·선택지) |

### 🆎 v6-kr-2x2 — 2×2 스토리 카드 베리에이션
같은 4가지 대비 내용을 2×2 그리드 스토리 카드로 재배치. 한 화면에서 동시 비교 가능, hover 시 카드 떠오름 효과.

### 🆎 v6-kr-focus — 1주제 1카드 대각선 베리에이션 (2026-04-18 추가)
같은 4가지 대비를 **각각 큰 카드 하나씩**으로 확장. 카드 내부는 대각선 흐름:
- 좌상단 = 기존 앱의 문제 (어떤 앱을 저격하는지 명시)
- 우하단 = Lucive에서의 같은 순간 (Lucive 채팅 경험)
- 하나의 메시지에 집중, 여백 넉넉, 배경에 큰 01/02/03/04 번호 워터마크

### 공통 업데이트 (2026-04-18)
- **기존 앱 명시** — sim/2x2의 "기존 앱"을 구체적 앱명+로고(Character.AI / 제타 / Talkie / 크랙 / Chai)로 명시
- **가격 Row 서사 수정** — "5→10→15 크랙 per message" 급격 인상이 **실제 패턴 아님** → "정책이 조용히 계속 바뀌면서 체감 가격이 1년 만에 3배" 서사로 교체 (실제 👍971 후기 기반)
- **1 Dip = $0.01 + 알파 웰컴 2,000 Dip** 명시 (프로덕트 스펙 반영)
- **LP별 고유 TTS 음성** 언급 추가 (VN 모드 설명)

### 🆎 v6-kr-unified — 4문제 → 1대화 통합 베리에이션 (2026-04-19 추가)
왼쪽에 4개 문제 카드, 오른쪽에 **Lucive의 한 대화 화면**. 구조:
- 좌측: 4개 앱(제타·제타·크랙·Character.AI)의 후기 기반 pain 카드 4장
- 우측: VN 스테이지 1개 (항구 씬 배경 유지) + 아리아의 대화 스레드
- 각 Lucive 메시지·UI 요소 옆에 **"해결 0N" 핑크 태그**로 어떤 문제를 푸는지 연결
  - 해결 01 → 15분 전 선톡 (기억 기반)
  - 해결 02 → 아리아의 네온 7구 · '29년 시뮬 고유 과거 언급
  - 해결 03 → 하단 바의 "1 Dip · 정책 같은 기준 유지"
  - 해결 04 → 상단 "VN · 배경 한 대화 내내 유지" 태그
- 핵심 메시지: "별도 기능 4개가 아니라, **플랫폼 기본 설계**가 그렇게 돼 있어요"

### 어떤 베리에이션이 더 나을까?
| 버전 | 강점 | 적합 컨텍스트 |
|---|---|---|
| **v6-kr** (4열 경쟁사 그리드) | 실제 리뷰 신뢰도·구체적 증거 | 검색 유입 · 긴 체류 |
| **v6-kr-sim** (세로 시뮬레이션) | 좌우 분할로 차이 강조 | 비교 욕구 높은 유저 |
| **v6-kr-2x2** (카드 그리드) | 빠른 스캔·모바일 친화 | 짧은 체류 광고 유입 |
| **v6-kr-focus** (1주제 1카드) | 하나에 집중·여백·서사 흐름 | 감성형·에디토리얼 유입 |
| **v6-kr-unified** (4→1 통합) | 통합 메시지·프로덕트 자신감 | 투자자·파트너·VC 리뷰, 임팩트 중심 유입 |

→ 5버전을 유사 트래픽(같은 광고 소스, ~300 UV/ea)에 돌려 CVR 비교 후 결정 권장. 또는 **v6-kr-unified를 디폴트**로 하고 나머지는 채널별 A/B 풀로 사용.

### JP/EN 베리에이션 클론
필요 시 `v6-jp-sim/2x2.html`, `v6-en-sim/2x2.html`를 v6-kr-sim/2x2 구조 그대로 지역화해 생성 가능. 요청 시 작업.

## 현재 권장 (2026-04)

- **글로벌 공통 참고**: `v4-final.html` (기능 레퍼런스)
- **한국 배포**: `v6-kr.html` (네이버 블로그·카카오·에타 등 국내 유입)
- **일본 배포**: `v6-jp.html` (X JP · pixiv 등 서브컬처 유입)
- **미국·글로벌 영어**: `v6-en.html` (Reddit r/CharacterAI · X · Discord 유입)

## V6 변경 사항 (2026-04)

피드백 누적 → 경쟁사 비교 섹션을 완전히 재구성:

### 이전 (v5)
- pain-pair 4개를 **세로로 스택** (각 pair는 왼쪽 GP 리뷰 / 오른쪽 Lucive 채팅)
- 피쳐 매트릭스처럼 느껴진다는 피드백

### 현재 (v6)
- **4개 컬럼을 가로로 배치** — 각 컬럼 = 1개 경쟁사 = 하나의 narrative
- 컬럼당 4단 수직 구성:
  1. **앱 로고 + 이름** (브랜드 색상 원형 monogram · 별점 · 리뷰 수 · 불만 축 라벨)
  2. **📣 실제 Google Play 리뷰** (미니 스크린샷 카드 · 노란 하이라이트 · 👍 카운트)
  3. **😞 그 앱에서의 실제 장면** (경쟁사 chat UI mockup · 붉은 보더 · 실패 caption)
  4. **✨ Lucive에서는** (Lucive chat UI · 브랜드 그라디언트 · mem-badge · 녹색 caption)
- 데스크탑 4열 → 태블릿 2열 → 모바일 1열 반응형
- 앱 브랜드 색상이 상단 3px 보더 + 아바타 + axis 라벨에 일관 적용
- hover 시 카드 위로 살짝 이동 (translateY -4px)

### 지역별 경쟁사 배정 (v6)
| 축 | 🇰🇷 KR | 🇯🇵 JP | 🇺🇸 EN |
|---|--------|--------|--------|
| Memory | 🟠 크랙 (심ᄂᄆᄀ, 👍75) | 🟣 Character.AI (Nyan, 👍28) | 🟣 Character.AI (Emma) |
| Origin/Same-bot | 🔵 제타 (뚜비, 👍53) | 🩷 Talkie (匿名, 👍50) | 🩷 Talkie (Marcus) |
| Pricing/Shallow | 🟠 크랙 (ᄋᄋᄋ, 👍**971**) | 🩵 Replika (Takeshi, 👍91) | 🩵 Replika (Jamie, 👍53) |
| Paywall | 🩵 Replika (Jamie, 영문 원문) | 🔴 Chai (번역) | 🔴 Chai (Daniela, 👍112) |

## 지역별 비스포크 설계 근거

피드백: *"너무 시스템 업체 피치 같다. 글로벌로 맞춘 일본·한국·미국 버전의 비스포크 디자인 필요. 유저 중심 언어. UX/UI가 캐릭터챗에 익숙하도록. 혜택은 어뷰징 시 예고 없이 스르륵 사라진다 경고문."*

### 🇰🇷 v5-kr — 웹툰·로판
- 파스텔 따뜻한 베이지/핑크/라벤더 (다크 지양)
- 고운바탕 + Noto Sans KR
- 캐릭터 3인 갤러리(아리아/하루/레인)
- 「」 스토리 인용 카드
- 정중하면서 공감조 ("그 기분, 우리도 알아요")
- 카카오톡 공유 버튼

### 🇯🇵 v5-jp — 아니메 VN
- 다크 밤하늘 + 네온 (#0A0812 기반)
- 사쿠라 꽃잎 CSS 낙하 애니메이션
- Shippori Mincho (세리프) + Zen Kaku Gothic
- VN 씬 목업(타자기 효과 + 비 내리는 효과)
- 縦書き 스타일 引用 ("「」 대사 프레이밍)
- LINE 공유 버튼
- 카피 예: "昨日の話を、覚えているAI。"

### 🇺🇸 v5-en — Tech Minimal (Character.AI 스타일)
- 다크 + 인디고/바이올렛/핑크 일렉트릭 그라디언트
- Inter + Space Grotesk (Silicon Valley 모던)
- 서브틀 그리드 배경
- Character.AI 스타일 채팅 카드(LP 태그, sync %, 메모리 필 배지)
- 소셜 프루프 카운터 (pre-registered this week)
- "You've tried them all. Something was missing." 공감 섹션
- Discord + Reddit + X 공유 버튼

## 공통 구성 (모든 v4/v5)

1. **상단 긴급성 배너** (fixed) + **Invitee 배너** (`/r/CODE`·`?r=CODE` 감지 시)
2. **Sticky 네비** (브랜드 / 런칭 카운트다운 / CTA)
3. **Hero** — 시그니처 문구 + CTA + 데모 위젯
4. **공감/페인 섹션** — "챗봇 다 써봤죠" 시리즈
5. **4가지 차별점** — Memory / Origin / Visual Novel / Initiate
6. **혜택 구조**
   - 전체 사전 등록자: 알파 기간 **사전 등록 전용 특가** (유료, 무료 아님)
   - Top 5 추가 혜택:
     - 🏆 1위 — 기본 플랜 평생 (서비스 존속 기간)
     - 🥈 2–5위 — 내 링크로 등록한 전원에게 3개월 무료
   - 6–10위: 별도 특전 없음 (공통 특가만 적용)
7. **어뷰징 경고** — "스르륵 사라진다" 문구 포함
8. **OTP 가입 3단계** — 이메일 → 6자리 코드 → 성공 화면
9. **성공 화면 최상단 알파 CTA** — 8문항 스크리닝으로 안내 (+500/+2,000/+300 Dip)
10. **공유 섹션** — 이메일 발송 알림 + 고유 초대 링크 + 지역별 공유 채널
11. **FAQ** — 5–6문항
12. **Footer**

## 레퍼럴 처리

- URL 쿼리 `?r=CODE` **또는** 경로 `/r/CODE` 감지 → Invitee 배너 자동 표시
- 추천 코드 입력란에 자동 프리필 + 검증
- Mock 검증(4자 이상 or VALID 세트) → Supabase `referral_codes` 테이블 조회로 교체 예정

## Supabase 연동 지점

모든 v4/v5 파일은 다음 훅 포인트에서 mock 처리 중:

```js
// 1. OTP 발송
supabase.auth.signInWithOtp({ email, options: { shouldCreateUser: true } })

// 2. OTP 검증
supabase.auth.verifyOtp({ email, token, type: 'email' })

// 3. 등록 후 referral 코드 생성 + 초대 링크 발송 (Edge Function)
supabase.functions.invoke('create-prelaunch-signup', {
  body: { email, promocode, referred_by: refCodeFromUrl }
})

// 4. 프로모 코드 검증
supabase.from('referral_codes').select('code, user_id').eq('code', v).single()

// 5. 리더보드 rank 조회
supabase.from('leaderboard_view').select('*').order('referral_count',{ascending:false}).limit(10)
```

## 카운트다운 타겟 변경

모든 v5 파일 상단 `<script>`의 `LAUNCH` 상수를 실제 런칭일로 교체:

```js
const LAUNCH = new Date('2026-06-30T00:00:00+09:00').getTime(); // KR/JP
const LAUNCH = new Date('2026-06-30T00:00:00Z').getTime();       // EN (UTC)
```

## 혜택 금액 (2026-04 기준)

- 사전 등록 완료 (공통): 0 Dip — 사전 등록 전용 특가 티켓 자체가 보상
- 스크리닝 8문항 완주: **+500 Dip**
- 클로즈드 알파 선발: **+2,000 Dip** (50–100명)
- 알파 대기자: **+300 Dip** (나머지 완주자 전원)

## A/B 테스트 여지

- v4-final vs v5-지역비스포크 CVR 비교 (같은 트래픽 소스 기준)
- 한국: 고운바탕 + 웹툰 갤러리 vs v4-final Aurora 그라디언트
- 일본: 다크 VN + 벚꽃 vs v4-final 미니멀
- 미국: Character.AI 채팅 목업 vs v4-final VN 씬
- 공유 버튼: 지역 최적(카카오/LINE/Discord) vs 범용(X/링크)

## 열어보기

```bash
# 로컬에서 바로 열기
start pre-register/v5-kr.html
start pre-register/v5-jp.html
start pre-register/v5-en.html

# 또는 로컬 서버
npx serve pre-register
```

## 배포 경로

- Netlify Drop: `pre-register/` 폴더 통째로 드래그 (리뷰 공유용 빠른 배포)
- Vercel: `pre-register/` 하위 루트로 `vercel --prod`
- 최종 본배포: `lucive.app` 도메인 하위 `/pre-register` 또는 서브도메인 `alpha.lucive.app`
- 지역 라우팅(권장): `lucive.app/kr` → v5-kr, `lucive.app/jp` → v5-jp, `lucive.app/` (기본) → v5-en · 또는 `Accept-Language` 헤더로 edge redirect

## 다음 단계

1. 3개 지역 버전에 실 카피 검수 (native speaker 1인씩)
2. 실제 캐릭터 아트워크로 플레이스홀더 교체
3. 지역별 OG 이미지 / 소셜 공유 카드 생성
4. Supabase 스키마 + Edge Function 연동
5. X Ads (영어권·일본) / 네이버 광고 (한국) 소재와 CVR A/B
6. UTM 파라미터 트래킹 세팅 (`?utm_source=xads&utm_region=jp&utm_campaign=alpha_launch`)
