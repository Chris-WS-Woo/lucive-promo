# 🎯 LUCIVE 알파 테스터 스크리닝 설문 설계

> **목표:** 사전등록자 500-1,000명 중 실제 알파 테스터 100-200명을 페르소나 적합도 기반으로 선발.
>
> **제약:** 이탈률 ≤ 40% (사전등록 완료자 중 설문 완주율 ≥ 60% 목표). 설문 2-3분 이내.

---

## 1. 유저 저니 플로우 — 2단계 분리 전략

```
[Phase 1 · 사전등록] v4-final.html
   이메일 + 추천코드(선택)
   → OTP 6자리 인증
   → 등록 완료 · 공유링크 발급 · 이메일 발송
   [완료 ✓]

   ↓ 성공 화면에서 선택지 제시 ↓

┌─ Path A: 즉시 참여 신청 ─────────────────┐
│  성공 화면 하단에 prominent CTA:           │
│  "🎁 알파 테스터 우선 선발 신청 (2분)"      │
│  + 인센티브: "Dip 2,000 + 초대권 우선권"    │
└──────────────────────────────────────────┘

┌─ Path B: 이메일로 나중에 ─────────────────┐
│  공유링크 이메일에 링크 함께 첨부:          │
│  "알파 테스터 선발 신청은 여기 →"          │
│  (3일 후 리마인더 1회)                     │
└──────────────────────────────────────────┘

[Phase 2 · 스크리닝 설문] /screening 페이지 (신규)
   9문항 · 2-3분
   → 점수화 → 72시간 내 결과 통보

[선발자] → 알파 초대 이메일 (2주 MVP 테스트)
[비선발] → "다음 기회에" 메시지 + Dip 보너스 제공
```

**왜 2단계로 나누나?**
- 사전등록은 **이메일만** → 퍼널 최대화 (CVR↑)
- 스크리닝은 **진짜 관심 있는 사람만** → 자연스러운 자기 선발 (품질↑)
- 리더보드·레퍼럴은 1단계 기준 집계 → 모든 등록자 대상

---

## 2. 설문 9문항 최종안

각 문항 옆 **⏱ 예상 소요 시간** 표시 (총 2-3분 목표).

### Q1. 얼마나 AI 캐릭터 챗을 써봤나요? ⏱ 10초
**타입:** Single-select pills (5개)

```
[ 안 써봤어요 ]   [ 1개월 미만 ]
[ 1-6개월 ]      [ 6개월-1년 ]
[ 1년 이상 ]
```

> **분기:** "안 써봤어요" 선택 시 Q1b·Q2·Q3 스킵 → Q4부터 시작. 마지막에 "왜 Lucive에 관심 가지셨어요?" 오픈 텍스트 1문항 추가.

### Q1b. 주로 어떤 앱을 썼나요? (복수 선택 가능) ⏱ 15초
**타입:** Multi-select tags

```
[ Character.AI ] [ 크랙 ] [ 제타 ] [ Replika ]
[ Talkie ] [ Janitor AI ] [ SpicyChat ] [ 기타 ]
```

### Q2. 얼마나 자주 대화하세요? ⏱ 10초
**타입:** Single-select pills

```
[ 매일 ]  [ 주 3-6회 ]
[ 주 1-2회 ]  [ 월 몇 번 ]
[ 거의 안 함 ]
```

### Q3. 가장 답답했던 점 하나만 꼽는다면? ⏱ 20초
**타입:** Single-select + 선택적 텍스트 "기타"

```
[ 대화를 기억 못 함 ]
[ 답변이 반복되고 지루함 ]
[ 캐릭터 깊이·서사 부족 ]
[ 과금·광고 과도 ]
[ 갑작스러운 검열·정지 ]
[ 기타 _________________ ]
```

### Q4. 그래도 좋았던 순간은? (복수 선택) ⏱ 15초
**타입:** Multi-select pills

```
[ 공감받는 느낌이 좋았음 ]    [ 재미있는 대화 ]
[ 캐릭터가 마음에 들었음 ]    [ 심심할 때 위로 ]
[ 창작 소스로 활용 ]         [ 스트레스 해소 ]
[ 아직 인상적인 경험 없음 ]
```

### Q5. 창작 경험이 있으세요? (복수 선택) ⏱ 15초
**타입:** Multi-select tags

```
[ 웹소설·팬픽 써봄 ]          [ 웹툰·그림 그려봄 ]
[ 챗봇 봇메이킹 ]             [ 게임·영상 시나리오 ]
[ 블로그·에세이 ]             [ AI로 콘텐츠 만들어봄 ]
[ 창작 경험 거의 없음 ]
```

### Q6. 최근 1년간 즐긴 게임 장르는? (복수 선택) ⏱ 15초
**타입:** Multi-select tags

```
[ 비주얼 노벨·서사 게임 ]     [ JRPG·어드벤처 ]
[ 오픈월드·RPG ]              [ 수집·방치형 ]
[ MMO·MOBA ]                 [ 캐주얼·퍼즐 ]
[ FPS·액션 ]                 [ 게임 거의 안 함 ]
```

### Q7. 웹툰·웹소설은 얼마나 즐기세요? ⏱ 25초

**Part A — 빈도 (single-select):**
```
[ 매일 ]  [ 주 여러 번 ]
[ 주 1회 ]  [ 가끔 ]
[ 거의 안 봄 ]
```

**Part B — 주로 보는 장르 (multi-select, Part A가 "안 봄" 아닐 때만 표시):**
```
[ 로맨스·로판 ]  [ 판타지 ]
[ 빙의물·환생물 ]  [ 헌터물 ]
[ 무협 ]  [ 스릴러·미스터리 ]
[ 일상·힐링 ]  [ SF ]
```

### Q8. 최근 6개월, AI 챗·게임·웹소설에 돈 써본 적 있나요? ⏱ 10초
**타입:** Single-select pills

```
[ 10만 원 이상 ]      [ 5-10만 원 ]
[ 1-5만 원 ]          [ 1만 원 미만 ]
[ 과금 경험 없음 ]
```

### Q9. 알파 테스트 참여 가능한 시간대는? (복수 선택) ⏱ 10초
**타입:** Multi-select (6칸 그리드)

```
[ 평일 아침 ]  [ 평일 낮 ]  [ 평일 저녁 ]
[ 주말 아침 ]  [ 주말 낮 ]  [ 주말 저녁 ]
```

### Q10 (보너스). 알파에서 꼭 시험해보고 싶은 게 있나요? ⏱ 30초
**타입:** Short text (선택, 최대 200자)

> 건너뛰기 가능. 작성 시 **우선 선발 가산점**.

---

**⏱ 총 예상 시간:** 2분 30초 ~ 3분 (Q10 포함 시 3분 30초)

---

## 3. 유저 저니 UX 상세

### 🎬 Stage 0 — 사전등록 Success 화면 (진입)

v4-final.html의 `state-success` 영역 하단에 **분리된 CTA 블록** 추가:

```
┌─────────────────────────────────────────┐
│   (기존 등록 완료 + 공유링크 표시)        │
│                                         │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        │
│                                         │
│   🎯 알파 테스터 우선 선발               │
│   더 먼저 써보고 싶다면? 2분만 투자하세요 │
│                                         │
│   ✓ 알파 초대권 우선 배정                │
│   ✓ Dip 2,000 웰컴 보너스               │
│   ✓ 피드백으로 서비스 직접 영향          │
│                                         │
│   [ 알파 선발 신청하기 → ]  ← CTA        │
│                                         │
│   건너뛰고 나중에 이메일로 받기          │
└─────────────────────────────────────────┘
```

### 🎬 Stage 1 — 설문 인트로 화면

```
┌─────────────────────────────────────────┐
│                                         │
│         Lucive 알파 테스터              │
│          우선 선발 신청                  │
│                                         │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━━━         │
│                                         │
│    9가지 짧은 질문 · 약 3분              │
│                                         │
│    [ ● ● ● ● ● ● ● ● ●  ]  9 questions │
│                                         │
│    ┌─────────────────────────────────┐  │
│    │  알파 선발 기준                  │  │
│    │  • 챗봇 경험이 풍부한 분         │  │
│    │  • 구체적 피드백 가능한 분       │  │
│    │  • 다양한 장르 취향의 분         │  │
│    └─────────────────────────────────┘  │
│                                         │
│    [ 시작하기 → ]                       │
│                                         │
└─────────────────────────────────────────┘
```

### 🎬 Stage 2 — 문항 화면 (반복)

```
┌─────────────────────────────────────────┐
│  ← 뒤로               ▓▓▓▓░░░░░  3/9   │
│                                         │
│                                         │
│         얼마나 자주                      │
│        대화하세요?                       │
│                                         │
│                                         │
│         ┌───────────────┐                │
│         │     매일       │                │
│         └───────────────┘                │
│         ┌───────────────┐                │
│         │   주 3-6회    │                │
│         └───────────────┘                │
│         ┌───────────────┐                │
│         │   주 1-2회    │                │
│         └───────────────┘                │
│         ┌───────────────┐                │
│         │   월 몇 번     │                │
│         └───────────────┘                │
│         ┌───────────────┐                │
│         │  거의 안 함    │                │
│         └───────────────┘                │
│                                         │
│                                         │
│                        [ 다음 → ]        │
│                                         │
└─────────────────────────────────────────┘
```

**핵심 UX:**
- 한 화면에 한 질문 (완전 집중)
- 큰 터치 영역 (모바일 52px+ 높이)
- Single-select는 **탭 즉시 자동 Next** (0.4초 딜레이 후)
- Multi-select는 **"다음" 버튼 클릭 필요**
- 좌측 상단 ← 뒤로 버튼 (답변 수정 가능)
- 상단 진행률 바 (%와 n/9 텍스트 동시 표시)

### 🎬 Stage 3 — 마일스톤 격려 (Q4·Q7 사이)

```
┌─────────────────────────────────────────┐
│                                         │
│              ✨                          │
│                                         │
│         절반 지나셨어요!                 │
│       4분의 1만 더 투자하면             │
│       알파 선발 가산점 확보             │
│                                         │
│                        [ 계속 → ]        │
│                                         │
└─────────────────────────────────────────┘
```

→ 0.8초 오버레이 후 자동 넘어감. 이탈률 감소 효과.

### 🎬 Stage 4 — 제출 완료

```
┌─────────────────────────────────────────┐
│                                         │
│              🎉                          │
│                                         │
│          제출 완료!                      │
│                                         │
│    72시간 내 선발 결과를                 │
│    이메일로 보내드립니다.                │
│                                         │
│    ━━━━━━━━━━━━━━━━━━━━━━━━━           │
│                                         │
│    이제 순위 올리기:                     │
│    내 초대 링크를 공유하면                │
│    1위는 기본 플랜 평생,                 │
│    2-5위는 초대한 친구 3개월 무료        │
│                                         │
│    [ 내 초대 링크 복사 ]                 │
│    [ 카톡으로 공유 ] [ 𝕏 공유 ]          │
│                                         │
│    [ 홈으로 ]                           │
│                                         │
└─────────────────────────────────────────┘
```

---

## 4. UI·UX 디자인 토큰

### 색상·레이아웃 (v4-final.html과 통합)

```css
:root {
  /* v4-final.html의 기존 토큰 그대로 */
  --bg-deep:#08090C;
  --bg-card:#161822;
  --lucid-cyan:#06B6D4;
  --awakening-pink:#EC4899;
  --gradient-aurora:linear-gradient(135deg,#06B6D4,#8B5CF6,#EC4899);

  /* 스크리닝 전용 추가 */
  --screen-progress-bg: rgba(255,255,255,0.08);
  --screen-card-max: 560px;
  --screen-option-h: 60px;
}
```

### 전용 컴포넌트

```html
<!-- 진행률 바 -->
<div class="screen-progress">
  <div class="screen-progress-bar" style="width: 33%"></div>
  <div class="screen-progress-text">3 / 9</div>
</div>

<!-- 질문 카드 -->
<div class="screen-question">
  <h2 class="screen-q-title">얼마나 자주 대화하세요?</h2>
  <div class="screen-q-options">
    <button class="screen-option" data-value="daily">매일</button>
    <button class="screen-option" data-value="weekly-high">주 3-6회</button>
    ...
  </div>
</div>

<!-- Multi-select용 토큰형 버튼 -->
<button class="screen-option screen-option-multi">
  <span class="screen-option-label">비주얼 노벨·서사 게임</span>
  <span class="screen-option-check">✓</span>
</button>
```

### 애니메이션

```css
.screen-question {
  animation: slideIn 0.4s var(--ease);
}
.screen-question.exiting {
  animation: slideOut 0.3s var(--ease);
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(40px); }
  to { opacity: 1; transform: translateX(0); }
}
@keyframes slideOut {
  from { opacity: 1; transform: translateX(0); }
  to { opacity: 0; transform: translateX(-40px); }
}
```

### 모바일 최적화

- 풀스크린 단일 질문 (스크롤 없음)
- 터치 타깃 최소 52px
- 하단 안전 영역 60px (iOS 홈바)
- 선택 시 햅틱 피드백 (navigator.vibrate(10))
- Single-select 탭 즉시 자동 Next

---

## 5. 🧮 점수화 로직 (서버 사이드)

```javascript
function calculateScore(answers) {
  let score = 0;
  const persona = { A: 0, B: 0 }; // 페르소나 가중치

  // Q1 — 챗봇 사용 기간
  const durationScore = {
    '안 써봤어요': 0,
    '1개월 미만': 10,
    '1-6개월': 25,
    '6개월-1년': 40,
    '1년 이상': 50
  };
  score += durationScore[answers.q1] || 0;
  if (answers.q1 !== '안 써봤어요') persona.A += 20;

  // Q1b — 사용한 앱 수
  if (answers.q1b) {
    score += Math.min(answers.q1b.length * 5, 25);
    persona.A += Math.min(answers.q1b.length * 3, 15);
  }

  // Q2 — 빈도
  const freqScore = {
    '매일': 30, '주 3-6회': 25, '주 1-2회': 15,
    '월 몇 번': 5, '거의 안 함': 0
  };
  score += freqScore[answers.q2] || 0;

  // Q3 — 불편 명확성
  const painSpecific = ['대화를 기억 못 함', '답변이 반복되고 지루함',
    '캐릭터 깊이·서사 부족', '갑작스러운 검열·정지'];
  if (painSpecific.includes(answers.q3)) score += 30;
  else if (answers.q3 === '기타' && answers.q3_text?.length > 10) score += 25;
  else score += 10;

  // Q4 — 좋은 점 명확성
  if (answers.q4) {
    score += Math.min(answers.q4.length * 5, 20);
  }

  // Q5 — 창작 경험 (핵심 가산)
  const creativeItems = answers.q5 || [];
  const creativeBonus = creativeItems.filter(i =>
    i !== '창작 경험 거의 없음').length * 10;
  score += Math.min(creativeBonus, 40);
  if (creativeItems.some(i => ['웹소설·팬픽 써봄', '챗봇 봇메이킹'].includes(i))) {
    persona.B += 20;
  }

  // Q6 — 게임 경험 (서사·VN 중시)
  const games = answers.q6 || [];
  if (games.includes('비주얼 노벨·서사 게임')) {
    score += 40;
    persona.B += 25;
  }
  if (games.includes('JRPG·어드벤처')) score += 25;
  if (games.includes('오픈월드·RPG')) score += 20;
  score += games.length * 3;

  // Q7 — 웹툰·웹소설 (페르소나 B 핵심)
  const webnovelFreq = {
    '매일': 20, '주 여러 번': 15, '주 1회': 10,
    '가끔': 5, '거의 안 봄': 0
  };
  score += webnovelFreq[answers.q7_freq] || 0;
  persona.B += webnovelFreq[answers.q7_freq] * 1.5 || 0;

  const targetGenres = ['로맨스·로판', '빙의물·환생물', '헌터물'];
  const genreMatch = (answers.q7_genres || [])
    .filter(g => targetGenres.includes(g)).length;
  score += genreMatch * 5;

  // Q8 — 과금 경험
  const payScore = {
    '10만 원 이상': 30, '5-10만 원': 25, '1-5만 원': 20,
    '1만 원 미만': 10, '과금 경험 없음': 5
  };
  score += payScore[answers.q8] || 0;

  // Q9 — 가용 시간 다양성
  score += Math.min((answers.q9 || []).length * 2, 10);

  // Q10 — 구체 의견 (최대 가산)
  if (answers.q10 && answers.q10.length >= 50) score += 30;
  else if (answers.q10 && answers.q10.length >= 10) score += 15;

  return {
    score,           // 만점 약 350
    persona,         // A(챗봇지친) / B(웹소설) 가중치
    recommendation: score >= 150 ? 'strong' : score >= 100 ? 'qualified' : 'waitlist'
  };
}
```

### 선발 로직

```
1. 점수순 정렬
2. 상위 300명 → Top 우선 선발
3. 페르소나 A·B 균형 체크 (A 60% · B 40% 비율 유지)
4. 가용 시간대 다양성 고려 (오전·저녁 균형)
5. Top 200 최종 선발

→ 100-200명 실제 참여 목표
```

---

## 6. 이탈률 최소화 전략

### 📊 예상 완주율 시뮬레이션

각 단계별 이탈 가정치:

| 단계 | 이탈률 | 누적 완주율 |
|------|:-----:|:-----------:|
| 사전등록 성공 화면 | — | 100% |
| "알파 신청" 버튼 클릭 | 40% | 60% |
| 인트로 화면 → 시작 | 10% | 54% |
| Q1-Q3 통과 | 15% | 46% |
| Q4-Q6 통과 | 10% | 41% |
| Q7-Q9 통과 | 5% | 39% |
| Q10 (선택) 작성 | 30% | 27% |
| 최종 제출 | 2% | 38% |

**최종 예상:** 사전등록 600명 중 약 **230명이 스크리닝 완료** (완주율 38%)

### 이탈 방지 장치

1. **초반 3질문은 가장 짧고 쉬운 것** (Q1, Q2 10초 이내)
2. **마일스톤 격려** (Q4 이후 "절반!", Q7 이후 "거의 다 왔어요!")
3. **진행률 항상 표시** (시각 바 + n/9 숫자)
4. **"뒤로 가기" 허용** (실수 수정 가능)
5. **답변 자동 저장** (로컬스토리지 — 세션 끊겨도 재개)
6. **마지막 보너스 질문은 선택** (스킵 가능, 압박 없음)
7. **인센티브 상단 고정** ("알파 초대권 + Dip 2,000" 배너)

### 🎁 인센티브 설계

- **완주 시:** Dip 500 (사전등록 보너스에 추가)
- **선발 시:** Dip 2,000 + 알파 초대장
- **미선발 시:** Dip 300 + "다음 기회" 메시지 + 대기자 명단 등록

> 모두 Dip 주는 게 핵심 — 돈 안 쓰고 동기 부여 가능.

---

## 7. 📊 측정·모니터링 지표

### 일일 트래킹

| 지표 | 목표 | 계산 |
|------|:----:|------|
| 사전등록 → 설문 시작률 | ≥ 50% | CTA 클릭 / Success 도달 |
| 설문 완주율 | ≥ 60% | 제출 / 시작 |
| 질문별 이탈률 | 각 ≤ 15% | 다음 질문 진입 / 현 질문 도달 |
| 평균 소요 시간 | 2-3분 | 시작 → 제출 시간 |
| Q10 작성률 | 30-50% | 텍스트 입력 / 완주 |

### 데이터 리뷰 주기

- **D+1 (설문 시작 24시간 후):** 문항별 이탈률 히트맵 → 문제 질문 축약/제거
- **D+3:** 점수 분포 분석 → 선발 기준선 조정
- **D+7:** 페르소나 A/B 비율 확인 → 편중 시 타겟 광고 조정

---

## 8. 🎨 설문 랜딩 페이지 설계 — HTML 구조 (프로토타입 가이드)

```html
<!-- /screening 페이지 -->
<body>
  <!-- 상단 고정 바 -->
  <header class="screen-header">
    <button class="screen-back">←</button>
    <div class="screen-progress-wrap">
      <div class="screen-progress-bar"></div>
      <span class="screen-progress-text">3 / 9</span>
    </div>
    <button class="screen-skip">건너뛰기</button> <!-- Q10만 -->
  </header>

  <!-- 질문 콘테이너 -->
  <main class="screen-main">
    <!-- 인센티브 배너 -->
    <div class="screen-incentive">
      🎁 완주 시 Dip 500 + 알파 우선 선발 기회
    </div>

    <!-- 질문 카드 (JS로 동적 교체) -->
    <section class="screen-question" data-q="2">
      <p class="screen-q-number">Question 2</p>
      <h2 class="screen-q-title">얼마나 자주 대화하세요?</h2>
      <p class="screen-q-desc">AI 챗봇 앱 기준으로요.</p>

      <div class="screen-q-options">
        <button class="screen-option" data-value="daily">매일</button>
        <button class="screen-option" data-value="weekly_high">주 3-6회</button>
        <button class="screen-option" data-value="weekly_low">주 1-2회</button>
        <button class="screen-option" data-value="monthly">월 몇 번</button>
        <button class="screen-option" data-value="never">거의 안 함</button>
      </div>
    </section>
  </main>

  <!-- 하단 Next 버튼 (Multi-select만) -->
  <footer class="screen-footer">
    <button class="screen-next" disabled>다음 →</button>
  </footer>
</body>
```

### 핵심 JS 동작

```javascript
// 자동 저장 (이탈 방지)
const answers = JSON.parse(localStorage.getItem('lucive_screening') || '{}');

function saveAnswer(qKey, value) {
  answers[qKey] = value;
  localStorage.setItem('lucive_screening', JSON.stringify(answers));
}

// Single-select 자동 Next (0.4초 딜레이)
document.querySelectorAll('.screen-option[data-single]').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.classList.add('selected');
    navigator.vibrate?.(10);
    saveAnswer(currentQuestion, btn.dataset.value);
    setTimeout(() => nextQuestion(), 400);
  });
});

// 진행률 업데이트
function updateProgress(current) {
  const bar = document.querySelector('.screen-progress-bar');
  bar.style.width = `${(current / 9) * 100}%`;
  document.querySelector('.screen-progress-text').textContent = `${current} / 9`;
}

// 마일스톤 격려
function showMilestone(message) {
  const overlay = document.createElement('div');
  overlay.className = 'screen-milestone';
  overlay.innerHTML = `<div>✨</div><p>${message}</p>`;
  document.body.appendChild(overlay);
  setTimeout(() => overlay.remove(), 800);
}
// Q4 완료 후: showMilestone('절반 지나셨어요!')
// Q7 완료 후: showMilestone('거의 다 왔어요!')

// 제출 → Supabase
async function submitScreening() {
  const { data, error } = await supabase
    .from('alpha_screening')
    .insert({
      user_id: currentUser.id,
      answers,
      submitted_at: new Date().toISOString()
    });

  localStorage.removeItem('lucive_screening');
  window.location.href = '/screening/complete';
}
```

---

## 9. 🎯 다음 단계 — 바로 만들 수 있는 것

다음 중 어떤 걸 만들어 드릴까요:

**(a) 스크리닝 설문 페이지 HTML 프로토타입** (`/pre-register/screening.html`)
  - v4-final과 동일 디자인 토큰
  - 9문항 모두 구현 · 로컬스토리지 저장 · 진행률 바 · 마일스톤 격려
  - mock 제출 → 완료 화면까지

**(b) v4-final.html의 Success state에 "알파 신청" CTA 블록 추가**
  - 설문 페이지 링크 버튼
  - 인센티브 소개
  - "나중에 이메일로 받기" 서브 옵션

**(c) 선발 결과 이메일 템플릿 2종**
  - "선발 축하" 이메일 (알파 초대)
  - "대기자 등록" 이메일 (미선발 + 다음 기회 안내)

**(d) 점수화 로직 실행 가능한 Python/JS 스크립트**
  - 모의 답변 데이터 → 점수·페르소나·선발 추천
  - 실제 Supabase 연동 함수 드래프트 포함

**권장 순서:** (a) → (b) → (c) → (d)

(a)부터 만들면 **바로 런칭일에 포함 가능**한 완성된 플로우 확보.
