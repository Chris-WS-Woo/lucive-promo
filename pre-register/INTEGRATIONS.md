# LUCIVE 운영 통합 가이드 · Klaviyo + GA4 + Zapier

> 정적 사이트(GitHub Pages) 환경에서 백엔드 없이 SaaS 만으로
> 사전등록 리스트 / 설문 응답 / 이메일 / 분석 운영 가능.

## 0. TL;DR — 5분 셋업

1. **Klaviyo** 가입 → 리스트 생성 → 공개 API 키 + List ID 복사
2. **GA4** 속성 생성 → Measurement ID 복사
3. (선택) **Zapier** Catch Webhook 만들고 URL 복사
4. `pre-register/_integrations.js` 상단의 `CONFIG` 4개 값 채워넣기
5. 끝. 모든 페이지가 자동 연동됨.

---

## 1. 아키텍처

```
                    ┌─ 사용자 브라우저 ─┐
                    │                  │
   사전등록 폼 ────►│  Klaviyo Subscribe │ → 리스트 + 프로필 properties
                    │                  │
   설문 제출 ──────►│  Klaviyo Identify│ → 답변을 프로필 속성에 저장
                    │  + Track Event   │ → 'Survey Completed' Flow 트리거
                    │                  │
   모든 페이지 ────►│  gtag.js (GA4)   │ → page_view, sign_up, share, cta_click
                    │                  │
   (선택) ─────────►│  Zapier Webhook  │ → Slack 알림 / Sheet 백업
                    └──────────────────┘

   Klaviyo Flow (서버 측)
   ─────────────────────
   • Pre-registered 이벤트 트리거 → 환영 메일 발송
   • Survey Completed 이벤트 트리거 → 감사 메일 + Dip 적립 안내
   • 알파 오픈 시 → Pre-register 리스트 일괄 캠페인 (Top 5 결과 포함)
```

**왜 Resend 빠졌나?**
- Klaviyo 가 트랜잭셔널(환영, 감사) + 마케팅(알파 오픈) 모두 처리
- 오픈/클릭 트래킹도 Klaviyo 기본 제공
- Resend 는 정식 오픈 후 transactional 분리 필요할 때 추가하면 됨 (Zapier 경유)

---

## 2. Klaviyo 셋업 (필수)

### 2.1 계정 + 리스트 생성

1. https://www.klaviyo.com/ 가입 (Free 250명까지)
2. **Account** → **Settings** → **API Keys** → **Public API Key** 복사
   - 6자 영숫자 (예: `AbC123`)
   - ⚠️ Private 키는 사용하지 않음 (브라우저 노출 위험)
3. **Audience** → **Lists & Segments** → **Create List**
   - 이름: `LUCIVE Pre-register`
   - List ID: 리스트 클릭 → Settings 탭에서 6자 영숫자 (예: `XyZ789`) 복사

### 2.2 발신 도메인 설정

1. **Account** → **Settings** → **Domains** → **Add Domain**
2. 발신 도메인 입력 (예: `lucive.app` 또는 `mail.lucive.app`)
3. DNS 레코드 (DKIM, SPF, Return-Path) 도메인 호스팅에 추가
4. 검증 완료 후 발신 주소 등록 (예: `hello@lucive.app`)

### 2.3 환영 메일 Flow 만들기

**목표**: 사전등록 직후 자동으로 환영 메일 발송 (프로모 코드 포함).

#### 옵션 A — 템플릿 자동 업로드 (권장)

저장소에 미리 디자인된 반응형 HTML 템플릿이 포함되어 있어요:
- `pre-register/_email_templates/01-welcome.html` (cream/gold 톤, Outlook/Gmail/iOS 호환)

**업로드 (한 번만)**:
1. 프로젝트 루트 `.env` 에 `KLAVIYO_PRIVATE_KEY=pk_xxxxx` 추가 (Klaviyo Account → Settings → API Keys → Private Key 만들고 권한 설정)
2. 터미널에서:
   ```bash
   cd pre-register/_email_templates
   # macOS / Linux / Git Bash (jq 필요)
   ./upload-to-klaviyo.sh "Welcome — Pre-register" 01-welcome.html
   # 또는 Windows / 어디서든 (Python 3 표준 라이브러리만)
   python upload-to-klaviyo.py "Welcome — Pre-register" 01-welcome.html
   ```
3. 콘솔에 Template ID 출력됨. Klaviyo → Content → Templates 에 동일 이름으로 즉시 등장.

**Flow 만들기**:
1. **Flows** → **Create Flow** → **Create from Scratch**
2. **Trigger**: Metric → `Pre-registered`
3. **Action**: Email → 즉시 발송
4. Email 편집 화면 → **Use existing template** → 방금 업로드한 `Welcome — Pre-register` 선택
5. 발신자/주소 확인 후 **Live ON**

#### 옵션 B — 직접 카피 복붙

UI 에서 새 템플릿 생성 후 아래 카피를 직접 입력:

```
Subject: LUCIVE 사전등록 완료 — 당신만의 코드입니다

안녕하세요,

LUCIVE 사전등록을 완료해 주셔서 감사합니다.

▸ 당신의 프로모 코드: {{ event.promo_code }}
▸ 친구 초대 링크: {{ event.invite_url }}
   친구가 이 링크로 가입하면 둘 다 +100 다이브

다음 단계 (선택):
2분 설문 → Dip 500 즉시 지급
{{ organization.web_view_url }}/screening.html

알파 오픈 시점에 다시 안내드립니다.

— LUCIVE 팀
```

5. Live 활성화

### 2.4 설문 완료 Flow

1. Trigger: `Survey Completed`
2. Email 액션:
```
Subject: 설문 완료 감사합니다 · Dip 500 적립

답변 감사합니다.

알파 오픈 시점에 핵심 테스터 안내를 별도로 드립니다.

— LUCIVE
```

### 2.5 프로필 속성 (자동 저장됨)

`_integrations.js` 가 다음 속성을 자동으로 Klaviyo 프로필에 저장합니다:

**사전등록 시**:
| Property | 예시 | 용도 |
|---|---|---|
| `promo_code` | `LUCIVE·A8X7B2` | 환영 메일 변수 |
| `invite_url` | `https://lucive.app/r/A8X7B2` | 환영 메일 변수 |
| `referral_code` | `LUCIVE·X8K2A0` | 추천인 그룹화 |
| `marketing_consent` | `true` / `false` | 캠페인 발송 필터 |
| `signup_source` | `v35-signup` | 유입 경로 분석 |
| `signup_at` | `2026-04-30T01:23:45Z` | 코호트 분석 |

**설문 완료 시 추가**:
| Property | 예시 |
|---|---|
| `survey_completed` | `true` |
| `survey_completed_at` | `2026-04-30T01:30:00Z` |
| `survey_q01` | `enthusiast` |
| `survey_q02` | `chatbot, novel` (다중 선택은 콤마) |
| `survey_q05` | (척도 응답 숫자) |
| ... | (각 질문별로 자동 저장) |

### 2.6 세그먼트 만들기 (운영 활용)

**핵심 사용자 세그먼트** (예시):
- `survey_completed = true`
- AND `survey_q01 in [enthusiast, power_user]`
- AND `marketing_consent = true`
→ 별도 캠페인 / Dip 추가 적립 안내

**Top 추천인 세그먼트**:
- 추천 카운트는 별도 집계 필요 (Zapier + Sheet 또는 Klaviyo Custom Property 업데이트)

---

## 3. GA4 셋업 (필수)

### 3.1 속성 생성

1. https://analytics.google.com/ → Admin → Create Property
2. **Property name**: `LUCIVE Pre-launch`
3. **Time zone**: Asia/Seoul, **Currency**: KRW
4. **Industry**: Internet/Telecom
5. **Business size**: Small
6. Property 만든 후 → Data Streams → Web → URL 입력
7. **Measurement ID** 복사 (`G-XXXXXXXXXX`)

### 3.2 자동 트래킹되는 이벤트

`_integrations.js` 로드만으로 자동:
- `page_view` (모든 페이지)
- `scroll` (90% 도달)
- `click` (외부 링크)
- `file_download`

### 3.3 커스텀 이벤트 (이 사이트가 발사하는 것)

| Event | 발사 시점 | 파라미터 |
|---|---|---|
| `sign_up` | 사전등록 폼 제출 | `method`, `has_referral`, `marketing_consent` |
| `survey_complete` | 설문 8문항 제출 | `answer_count`, `has_email` |
| `share` | 카톡/X/링크 공유 클릭 | `method`, `content_type` |
| `cta_click` | 상단 네브 / pre-cta / floating CTA 클릭 | `cta` (`signup`/`demo`), `position` |

### 3.4 컨버전(Key Event) 마킹

Admin → Events → 마킹할 이벤트 옆 토글 ON:
- `sign_up` → 핵심 컨버전
- `survey_complete` → 보조 컨버전

### 3.5 권장 Custom Dimensions

Admin → Custom Definitions:
- `has_referral` (event scope, boolean) — 추천인 가입 여부
- `cta_position` (event scope, string) — CTA 위치 분석

---

## 4. Zapier 셋업 (선택)

Klaviyo 외 자동화가 필요할 때만 사용. 예: Slack 실시간 알림, Google Sheet 백업.

### 4.1 Catch Webhook 만들기

1. https://zapier.com/ 가입 (Free 100 task/월)
2. **Create Zap** → Trigger: **Webhooks by Zapier** → **Catch Hook**
3. URL 생성됨 (예: `https://hooks.zapier.com/hooks/catch/12345/abcdef/`)
4. URL 복사

### 4.2 페이로드 형식

`_integrations.js` 가 두 가지 type 으로 POST:

**signup**:
```json
{
  "type": "signup",
  "email": "user@example.com",
  "promo_code": "LUCIVE·A8X7B2",
  "invite_url": "https://lucive.app/r/A8X7B2",
  "referral_code": "",
  "marketing_consent": true,
  "ts": "2026-04-30T01:23:45Z"
}
```

**survey_complete**:
```json
{
  "type": "survey_complete",
  "email": "user@example.com",
  "answers": { "q01": "...", "q02": [...] },
  "ts": "2026-04-30T01:30:00Z"
}
```

### 4.3 Action 예시

**Slack 알림**:
- Zapier → Slack → Send Channel Message
- Channel: `#alpha-signup`
- Text: `🎯 새 사전등록 · {{email}} (referral: {{referral_code}})`

**Google Sheet 백업**:
- Zapier → Google Sheets → Create Spreadsheet Row
- Spreadsheet: `LUCIVE Pre-register Backup`
- Worksheet: `Signups` / `Surveys`
- 컬럼 매핑: type, email, promo_code, ...

---

## 5. 통합 헬퍼 (`_integrations.js`)

### 5.1 CONFIG 채우기

```js
// pre-register/_integrations.js
const CONFIG = {
  KLAVIYO_PUBLIC_KEY: 'AbC123',         // ← Klaviyo Public API Key
  KLAVIYO_LIST_ID: 'XyZ789',            // ← Pre-register 리스트 ID
  GA4_MEASUREMENT_ID: 'G-XXXXXXXXXX',   // ← GA4 Measurement ID
  ZAPIER_WEBHOOK: '',                   // (선택) Zapier Catch URL
  DEBUG: false,                         // 테스트 시 true 로 (실제 호출 안 함)
};
```

### 5.2 페이지 통합 상태

| 페이지 | 자동 연동 |
|---|---|
| `v38-lp-wide.html` | GA4 page_view + cta_click (사전등록/체험/floating) |
| `v34-kr-lucive.html` | GA4 page_view |
| `v35-signup.html` | sign_up + Klaviyo subscribe + share + Zapier |
| `screening.html` | survey_complete + Klaviyo identify + track + Zapier |
| `terms.html` | GA4 page_view |
| `privacy.html` | GA4 page_view |

### 5.3 디버그 모드

```js
DEBUG: true,
```
→ API 호출 안 하고 콘솔에만 로그 (개발 시 안전 검증용).

CONFIG 값이 비어 있으면 자동으로 no-op (페이지는 정상 동작).

---

## 6. 운영 체크리스트

### 알파 오픈 전

- [ ] Klaviyo 계정 + 리스트 생성
- [ ] 발신 도메인 DKIM/SPF 검증
- [ ] 환영 메일 Flow 활성화 (Pre-registered 트리거)
- [ ] GA4 속성 생성 + Measurement ID 발급
- [ ] (선택) Zapier 알림 셋업
- [ ] `_integrations.js` CONFIG 4개 값 채움
- [ ] 본인 이메일로 사전등록 테스트 → Klaviyo 리스트 등록 + 환영 메일 수신 확인
- [ ] 본인 이메일로 설문 완료 테스트 → Klaviyo 프로필 속성 갱신 확인
- [ ] GA4 실시간 보고서에서 이벤트 확인

### 알파 기간 중

- [ ] Klaviyo 일일 리스트 증가 모니터링
- [ ] 환영 메일 오픈율/클릭률 점검 (Klaviyo Dashboard)
- [ ] 설문 완주율 (GA4 funnels: page_view → form_start → survey_complete)
- [ ] 핵심 사용자 세그먼트 추출 → 별도 안내 메일 발송
- [ ] Top 추천인 집계 (Zapier + Sheet 또는 수동)

### 알파 오픈 시점

- [ ] Klaviyo Campaign 생성: 알파 오픈 안내
- [ ] Top 5 추천인 별도 결과 안내 메일
- [ ] 핵심 사용자 별도 추가 혜택 안내

---

## 7. 트러블슈팅

### 사전등록 폼은 동작하는데 Klaviyo 리스트에 안 들어감

1. 브라우저 개발자도구 → Network 탭에서 `subscriptions` 요청 확인
2. Status 가 `202 Accepted` 면 정상 (실제 등록은 1~2초 후 반영)
3. `4xx` 에러 시 Console 에러 메시지 확인
4. CORS 에러 발생 시 → `revision` 헤더가 `2024-10-15` 로 되어 있는지 확인

### GA4 이벤트가 안 보임

1. GA4 → Realtime → Events 에서 30초 안에 표시되는지 확인
2. `ad blocker` (광고 차단기) 가 있으면 차단됨 → 일반 브라우저 / 시크릿 창에서 재테스트
3. Console 에 `[LUCIVE] GA4 not loaded` 가 보이면 `GA4_MEASUREMENT_ID` 가 비어 있음

### Klaviyo 환영 메일이 안 옴

1. Flow 가 **Live** 상태인지 확인 (Draft 아님)
2. Flow 의 Filter 에 `marketing_consent = true` 등이 걸려 있는지 확인
3. 발신 도메인 DKIM 검증 미완료 시 발송 실패 → 검증 마무리

### 마케팅 미동의자에게 환영 메일을 보내야 한다면?

- 환영 메일은 transactional 로 분류 (서비스 이용에 필수 안내)
- Klaviyo Flow Filter 를 비워두면 모든 가입자에게 발송
- 단, 이후 캠페인은 `marketing_consent = true` 필터 필수

---

## 8. 향후 확장

### Resend 추가 (transactional 분리 시점)

Klaviyo + Resend 병행이 필요해지면:

1. Resend 계정 + 도메인 검증
2. Zapier 추가 단계: `Pre-registered` 이벤트 → Resend `POST /emails`
3. Klaviyo Flow 의 환영 메일을 Resend 로 이관 (Klaviyo 는 마케팅 전용)

### 추천 리더보드 (Top 5 실시간)

옵션 A: Klaviyo Custom Property 로 카운트 (단순)
- 추천인 가입할 때마다 referrer의 `referral_count` += 1 업데이트
- Klaviyo Segment: `referral_count >= 1` 정렬

옵션 B: Sheet + Apps Script 자동 집계 (정밀)
- Zapier → Sheet 에 row 추가
- Apps Script 로 referrer 별 카운트 + rank 계산
- Top 5 페이지에 임베드 (iframe 또는 Sheet API)

---

## 9. 문의

- 통합 헬퍼 코드: `pre-register/_integrations.js`
- 페이지별 연동 상세: `pre-register/HANDOFF.md`
- 변경 요청: github.com/Chris-WS-Woo/lucive-promo Issues
