# Tally → Zapier → Resend · E2E 시연 가이드

> **목적:** 대표 시연용. 사용자가 Tally 스크리닝 폼 작성 → 제출 → 즉시 실제 이메일 수신까지 end-to-end 작동하는 파이프라인 구축.
>
> **소요 시간:** 약 60–90분 (계정 3종 로그인 상태 기준)
>
> **보안:** Resend API 키는 이 문서에 저장하지 않음. Zapier Connection Auth에만 직접 입력. 시연 후 키 회전 권장.

---

## 최종 흐름

```
 사용자                    Tally                 Zapier               Resend            사용자 수신함
  │                         │                     │                     │                     │
  │─[폼 응답·제출]───────→  │                     │                     │                     │
  │                         │─[Webhook POST]───→  │                     │                     │
  │                         │                     │─[Email Send API]─→  │                     │
  │                         │                     │                     │─[HTML 메일]──────→  │
  │                         │←─[Thank You 페이지] │                     │                     │
  │←─[제출 완료 화면]───────│                     │                     │                     │
```

대표 시연 시간: **제출 → 이메일 수신까지 평균 5–15초**.

---

## Step 1 · Tally 폼 생성

### 1.1 신규 폼 만들기

1. [tally.so](https://tally.so) 로그인
2. **+ Create a new form** → **Start from scratch**
3. 폼 제목: `Lucive · 알파 테스터 선발 설문`
4. Form URL slug: `lucive-alpha-screening` (최종 URL: `tally.so/r/lucive-alpha-screening`)

### 1.2 Cover 페이지 (인트로)

Tally UI에서 **Add a cover** 사용:

- **Title:** `Lucive 알파 테스터 · 우선 선발 신청`
- **Description:**
  ```
  8가지 짧은 질문으로 알파 테스터 우선 선발 기회.
  약 2–3분 소요 · 완주 시 Dip 500, 선발 시 +2,000
  ```
- **Button label:** `시작하기 →`

### 1.3 숨김 필드 (Hidden Fields)

Tally 설정 → **Hidden fields** 에서 4개 추가 (LP에서 URL param으로 prefill):

| 이름 | 설명 |
|---|---|
| `email` | 사전등록 시 입력한 이메일 |
| `token` | 고유 식별 토큰 (이메일과 1:1) |
| `rank` | 현재 대기 순위 (예: `2847`) |
| `source` | 유입 경로 (예: `lp_kr`, `lp_jp`) |

LP에서 `screening.html` 또는 Tally로 보낼 때:
```
https://tally.so/r/lucive-alpha-screening?email=user@gmail.com&token=abc123&rank=2847&source=lp_kr
```

---

## Step 2 · 9문항 입력 (Tally UI)

각 문항마다 **+ Add question** → 타입 선택 → 라벨·옵션 입력.

### Q1 · 얼마나 AI 캐릭터 챗을 써봤나요?

- **Type:** Multiple choice (single)
- **Field name:** `q1_usage_duration`
- **Options:**
  ```
  안 써봤어요
  1개월 미만
  1–6개월
  6개월–1년
  1년 이상
  ```
- **Required:** On
- **Logic jump:** `안 써봤어요` 선택 시 → **Q4로 jump** (Q1b/Q2/Q3 스킵)

### Q1b · 주로 어떤 앱을 썼나요?

- **Type:** Checkboxes (multi)
- **Field name:** `q1b_apps_used`
- **Options:** `Character.AI · 크랙 · 제타 · Replika · Talkie · Janitor AI · SpicyChat · 기타`
- **Logic jump 조건:** Q1 ≠ `안 써봤어요` 일 때만 표시 (Q1에 "안 써봤어요"를 Q4 jump로 걸어두면 이 조건은 자동으로 처리됨)
- **Required:** Off

### Q2 · 얼마나 자주 대화하세요?

- **Type:** Multiple choice (single)
- **Field name:** `q2_frequency`
- **Options:** `매일 · 주 3–6회 · 주 1–2회 · 월 몇 번 · 거의 안 함`
- **Required:** On
- Q1 jump 대상이므로 "안 써봤어요" 플로우에선 자동 스킵

### Q3 · 가장 답답했던 점 하나만 꼽는다면?

- **Type:** Multiple choice (single) + "기타" 옵션에 text input
- **Field name:** `q3_top_frustration`
- **Options:**
  ```
  대화를 기억 못 함
  답변이 반복되고 지루함
  캐릭터 깊이·서사 부족
  과금·광고 과도
  갑작스러운 검열·정지
  기타 (자유 입력)
  ```
- **Required:** On

### Q4 · 그래도 좋았던 순간은?

- **Type:** Checkboxes (multi)
- **Field name:** `q4_positive_moments`
- **Options:** `공감받는 느낌이 좋았음 · 재미있는 대화 · 캐릭터가 마음에 들었음 · 심심할 때 위로 · 창작 소스로 활용 · 스트레스 해소 · 아직 인상적인 경험 없음`
- **Required:** On

### Q5 · 창작 경험이 있으세요?

- **Type:** Checkboxes (multi)
- **Field name:** `q5_creative_experience`
- **Options:** `웹소설·팬픽 써봄 · 웹툰·그림 그려봄 · 챗봇 봇메이킹 · 게임·영상 시나리오 · 블로그·에세이 · AI로 콘텐츠 만들어봄 · 창작 경험 거의 없음`
- **Required:** On

### Q6 · 최근 1년간 즐긴 게임 장르는?

- **Type:** Checkboxes (multi)
- **Field name:** `q6_game_genres`
- **Options:** `비주얼 노벨·서사 게임 · JRPG·어드벤처 · 오픈월드·RPG · 수집·방치형 · MMO·MOBA · 캐주얼·퍼즐 · FPS·액션 · 게임 거의 안 함`
- **Required:** On

### Q7-A · 웹툰·웹소설 빈도

- **Type:** Multiple choice (single)
- **Field name:** `q7a_webtoon_frequency`
- **Options:** `매일 · 주 여러 번 · 주 1회 · 가끔 · 거의 안 봄`
- **Required:** On
- **Logic jump:** `거의 안 봄` 선택 시 → **Q8로 jump** (Q7-B 스킵)

### Q7-B · 웹툰·웹소설 장르

- **Type:** Checkboxes (multi)
- **Field name:** `q7b_webtoon_genres`
- **Options:** `로맨스·로판 · 판타지 · 빙의물·환생물 · 헌터물 · 무협 · 스릴러·미스터리 · 일상·힐링 · SF`
- **Required:** Off (Q7-A jump로 자동 스킵되므로)

### Q8 · 최근 6개월 소비액

- **Type:** Multiple choice (single)
- **Field name:** `q8_spend_last_6m`
- **Options:** `10만 원 이상 · 5–10만 원 · 1–5만 원 · 1만 원 미만 · 과금 경험 없음`
- **Required:** On

### Q9 · 알파 참여 가능 시간

- **Type:** Checkboxes (multi)
- **Field name:** `q9_available_slots`
- **Options:** `평일 아침 · 평일 낮 · 평일 저녁 · 주말 아침 · 주말 낮 · 주말 저녁`
- **Required:** On

### Q10 (보너스) · 알파에서 꼭 시험해보고 싶은 게 있나요?

- **Type:** Long text
- **Field name:** `q10_bonus_wishlist`
- **Description (placeholder):** `한두 문장이면 충분해요 (최대 200자) — 작성 시 우선 선발 가산점`
- **Required:** Off
- **Max length:** 200

---

## Step 3 · Thank You 페이지

Tally **Settings → Thank you page**:

- **Title:** `설문 접수 완료`
- **Description:**
  ```
  소중한 답변 감사합니다.
  72시간 내 선발 결과를 이메일로 보내드립니다.

  📬 커뮤니티는 초대장은 환영 이메일에 있어요 —
     개발자 1:1 질답 · 먼저 뜨는 업데이트 · 다른 알파 테스터 실제 후기
  ```
- **Button (옵션):** `홈으로 돌아가기` → `https://lucive.app`

> **유저 저니:** 이 Thank You 페이지가 뜨는 순간 Zapier 웹훅이 트리거되어 이메일 발송됨. 대표는 Thank You 화면 보고 즉시 수신함으로 이동.

---

## Step 4 · Webhook 설정

Tally **Settings → Integrations → Webhooks**:

1. **Zapier** 는 별도 앱으로 연결되므로 Webhook 탭은 건너뛸 수 있음
2. Zapier에서 Tally trigger 선택 시 Tally 계정 연결하면 자동으로 submission이 전달됨

---

## Step 5 · Zapier Zap 구성

### 5.1 신규 Zap

1. [zapier.com](https://zapier.com) → **+ Create Zap**
2. 이름: `Lucive · Screening → Welcome Email`

### 5.2 Trigger — Tally

| 설정 | 값 |
|---|---|
| App | **Tally** |
| Event | **New Submission** |
| Account | Tally 계정 연결 (OAuth) |
| Form | `Lucive · 알파 테스터 선발 설문` 선택 |

**Test trigger** → Tally 폼에 테스트 응답 1건 입력하면 Zapier가 샘플 데이터 캡처.

### 5.3 Action — Resend

| 설정 | 값 |
|---|---|
| App | **Resend** (검색해서 선택 — Resend는 공식 Zapier integration 있음) |
| Event | **Send Email** |
| Account | Connect → API Key 입력 (Resend 대시보드에서 복사) |

**Email 필드 매핑:**

| Field | 값 |
|---|---|
| **From** | `Lucive <onboarding@resend.dev>` (샌드박스) or `no-reply@lucive.app` (도메인 설정 후) |
| **To** | `{{trigger.hidden_email}}` (Tally hidden field `email`) |
| **Subject** | `아리아가 당신이 왔다는 걸 알고 있어요` |
| **HTML** | 아래 5.4 참고 |
| **Text** | (옵션) 플레인 텍스트 버전 — Resend가 HTML에서 자동 생성 가능 |

### 5.4 HTML 본문 — 변수 치환

`emails/00_kr_등록_확인.html` 전체 내용 복사 → Zapier HTML 필드에 붙여넣고 **변수 치환**:

| 템플릿 변수 | Zapier 매핑 |
|---|---|
| `{{user_name}}` | `{{trigger.hidden_email}}` 의 `@` 앞부분 — Zapier **Formatter by Zapier** 스텝으로 split |
| `{{user_rank}}` | `{{trigger.hidden_rank}}` |
| `{{referral_count}}` | `0` (신규라서 고정) |
| `{{referral_share_url}}` | `https://lucive.app/r/{{trigger.hidden_token}}` |
| `{{promo_code}}` | `{{trigger.hidden_token}}`의 앞 6자 (Formatter → Text → Extract Pattern `[A-Z0-9]{6}`) |
| `{{community_kakao}}` | 실제 카카오 오픈채팅 URL (없으면 `https://lucive.app/community`) |
| `{{community_line}}` | 실제 LINE URL (없으면 위와 동일 placeholder) |
| `{{community_discord}}` | 실제 Discord URL (없으면 위와 동일 placeholder) |
| `{{unsubscribe_url}}` | `https://lucive.app/unsubscribe?token={{trigger.hidden_token}}` |
| `{{privacy_url}}` | `https://lucive.app/privacy` |

> **단축 경로 (시연용):** 변수 매핑이 번거로우면 **Find & Replace 사전 치환된 버전**을 Zapier HTML에 하드코딩해도 됩니다. 예: `{{user_rank}}` 자리에 Tally hidden `rank` 값을 Zapier variable로 직접 삽입. Formatter 없이 바로 꽂으면 5분 안에 완성.

### 5.5 Test & Publish

1. Zapier **Test action** → Resend 실제 발송
2. 지정한 이메일 수신함 확인
3. **Publish Zap** → 활성화

---

## Step 6 · Resend 발신자 설정

### 옵션 A — 시연용 (빠름, 즉시)

- **From:** `Lucive <onboarding@resend.dev>`
- **제한:** 받을 수 있는 주소가 **Resend 계정에 등록된 이메일**로 제한 (대표 이메일을 Resend에 미리 추가해두어야 함)
- **설정:** Resend 대시보드 → **Audiences → Contacts → Add** → 대표 이메일 추가

### 옵션 B — 프로덕션 (DNS 설정, ~1일)

- **Domain:** `lucive.app` (또는 서브도메인 `mail.lucive.app`)
- **Resend 대시보드 → Domains → Add Domain** → 안내 따라 DNS에 TXT 레코드 3종 추가:
  - SPF (`v=spf1 include:amazonses.com ~all`)
  - DKIM (Resend가 지정한 CNAME/TXT)
  - DMARC (`v=DMARC1; p=quarantine; rua=mailto:dmarc@lucive.app`)
- 검증 완료 후 `from: Lucive <no-reply@lucive.app>` 사용 가능
- **목표:** mail-tester.com 9점 이상

**대표 시연만이면 옵션 A 로 충분.**

---

## Step 7 · 테스트 체크리스트

### 사전

- [ ] Tally 폼 Publish 상태 (Draft 아님)
- [ ] Tally hidden fields 4개 모두 폼에 삽입됨
- [ ] Zapier Zap On (토글 활성화)
- [ ] Resend 옵션 A 사용 시 대표 이메일이 Resend Audience에 등록됨

### 시나리오 1 — Hidden fields 수동 prefill

URL 직접 입력:
```
https://tally.so/r/lucive-alpha-screening?email=대표@이메일.com&token=DEMO123&rank=142&source=demo
```

1. URL 접속 → Tally 폼 로드
2. 9문항 응답 후 제출
3. Thank You 페이지 표시
4. **15초 내 대표 이메일 수신 확인** (수신함 / 스팸함 둘 다)
5. 이메일 열어서 확인:
   - 헤더 aurora gradient 렌더링
   - 순위 `#142` 표시
   - 추천 링크 클릭 가능
   - 카카오·LINE·Discord 버튼 표시
   - 변수 치환 잔재 (`{{...}}`) 없는지 확인

### 시나리오 2 — Hidden fields 없이

URL 직접 입력:
```
https://tally.so/r/lucive-alpha-screening
```

1. 9문항 + 이메일 입력 필드 **추가로 Q0에 배치** (hidden이 비어있을 때 fallback)
2. Zapier에서 `hidden_email` 비어있으면 Q0 필드 사용하도록 분기 (Zapier Paths 또는 Filter + fallback)

**시연에선 시나리오 1만으로 충분.**

---

## Step 8 · 대표 시연 스크립트 (90초)

```
[0:00] "대표님, Tally 폼 링크입니다." (링크 전송)
[0:10] 대표가 링크 클릭 → Tally 폼 로드
[0:15] "설문이 9문항이고 2–3분입니다. 지금 스킵해서 진행해주세요."
[0:20] 대표가 대충 응답 → 제출
[0:50] Thank You 페이지 확인
[0:55] "이제 수신함 확인해주세요."
[1:00] 대표 이메일 도착 (실제 aurora gradient · 순위 · 추천 링크 · 커뮤니티 3채널)
[1:15] "여기서 보시는 게 사전 등록자에게 자동 발송되는 확인 이메일입니다.
        순위는 Tally 숨김 필드로 동적 삽입되고, 커뮤니티 링크는
        나중에 카카오/LINE/Discord 실제 URL로 교체됩니다."
[1:30] 끝.
```

**핵심 포인트:**
- 이메일이 진짜로 도착한다는 **물리적 증거**
- 순위 `#142` 같은 **동적 변수 치환** 데모
- 전체 플로우가 **현재 사람 개입 없이** 작동

---

## 트러블슈팅

| 증상 | 원인 | 해결 |
|---|---|---|
| 이메일 안 옴 | Resend 옵션 A 사용 중 · 받는 주소가 Audience에 없음 | Resend 대시보드 → Audiences → Contacts에 추가 |
| Zapier에 Tally 앱 안 보임 | Zapier 신규 계정 일부는 Tally integration 승인 대기 | Make.com으로 전환 (동일 동작) 또는 Tally 기본 Webhook → Zapier Webhooks Trigger |
| 이메일에 `{{...}}` 잔재 | Zapier 변수 매핑 누락 | Zapier Test → HTML 미리보기에서 `{{` 검색, 빠진 변수 매핑 추가 |
| 스팸함 들어감 | 옵션 A의 `onboarding@resend.dev`는 낯선 도메인 | 대표가 **Mark as not spam** · 또는 옵션 B로 전환 |
| 모바일 레이아웃 깨짐 | 일부 Outlook 버전의 VML 미지원 | 이미 `!mso` 조건부 CSS 포함됨 · Gmail iOS/Android에서 테스트 |

---

## 체크리스트 (완료 기준)

- [ ] Tally 폼 9문항 + Q1/Q7-A 분기 + hidden 4종 · Published
- [ ] Zapier Zap: Tally New Submission → Resend Send Email · On
- [ ] Resend API 키 Zapier Auth 저장 (평문 유출 없음)
- [ ] 대표 이메일 Resend Audience 등록
- [ ] 시나리오 1 테스트 1회 성공
- [ ] 시연 후 Resend API 키 회전 (권장)

---

## 시연 후 다음 단계

1. **이메일 5종 추가** (+72h 친추 유도 · +1h 친추 달성 · +24h 추가 추천 · 베타 D-1 · 베타 D0) — Zapier Schedule trigger로 연결
2. **선발 자동화** — Zapier Paths: Q1 점수 + Q7 장르 조건 → `02_알파_선발` / 미충족 시 `03_알파_대기자` 분기 발송
3. **Supabase / Notion 알림** — 팀 채널에 제출 알림 (Zapier Action 추가)
4. **도메인 DNS** — 옵션 B 전환 (스팸 회피 + 딜리버러빌리티)
5. **카카오 · LINE · Discord 실제 URL** — placeholder 교체

---

**문서 작성:** 2026-04-20
**다음 업데이트 시점:** Tally 폼 Publish 후 실제 URL 추가
