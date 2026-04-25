# 📧 Lucive 이메일 템플릿

Supabase Edge Function에서 발송할 트랜잭셔널 이메일 템플릿 모음.

## 파일

| 파일 | 트리거 | 수신자 |
|------|--------|--------|
| [00_kr_등록_확인.html](00_kr_등록_확인.html) | 등록 확인 + 추천 리더보드 안내 | 모든 사전 등록자 |
| [01_설문완료_로스터대기.html](01_설문완료_로스터대기.html) | 설문 완료 · 로스터 대기 | 설문 완료자 |
| [02_알파_선발.html](02_알파_선발.html) | 알파 선발 확정 | 선발된 알파 테스터 |
| [03_알파_대기자.html](03_알파_대기자.html) | 알파 미선발 · 대기 유지 | 미선발/대기자 |
| [04_알파_이용가이드_오픈전날.html](04_알파_이용가이드_오픈전날.html) | 오픈 전날 이용 가이드 | 선발된 알파 테스터 |
| [90_순위상승_알림.html](90_순위상승_알림.html) | 순위 상승 알림 | 이벤트성 발송 |

## 공통 설계 원칙

- **다크 테마 고정** (`color-scheme: dark` meta) — Gmail·네이버·다음·Outlook 다크모드 자동 반전 방지
- **테이블 기반 레이아웃** — 모든 이메일 클라이언트 호환 (flex/grid 미지원)
- **인라인 CSS** — 일부 클라이언트는 `<style>` 태그 제거
- **VML 폴백** — Outlook에서 pill 버튼이 사각형으로 깨지지 않도록
- **모바일 반응형** — `@media max-width: 640px` 중단점
- **Preheader** — 수신함 미리보기 텍스트 (display:none 트릭)
- **웹폰트 사용 안 함** — Apple SD Gothic Neo · Segoe UI · Noto Sans KR 폴백 체인
- **브랜드 토큰 일관성** — v4-final.html과 동일한 색상·그라디언트

## Supabase 연동

### Edge Function 구조 (권장)

```typescript
// supabase/functions/send-alpha-result-email/index.ts
import { serve } from "https://deno.land/std/http/server.ts";
import { Resend } from "npm:resend";

const resend = new Resend(Deno.env.get("RESEND_API_KEY"));

serve(async (req) => {
  const { user_id, result_type } = await req.json();

  // Load user data
  const { data: user } = await supabase
    .from('users')
    .select('*, screening:alpha_screening(*)')
    .eq('id', user_id)
    .single();

  const template = result_type === 'selected'
    ? await Deno.readTextFile('./templates/01_selected.html')
    : await Deno.readTextFile('./templates/02_waitlist.html');

  const html = template
    .replace(/{{user_name}}/g, user.name || user.email.split('@')[0])
    .replace(/{{user_rank}}/g, user.referral_rank)
    .replace(/{{referral_count}}/g, user.referral_count)
    .replace(/{{referral_share_url}}/g, `https://lucive.app/r/${user.referral_code}`)
    .replace(/{{dip_amount}}/g, '2000')
    .replace(/{{dip_consolation_amount}}/g, '300')
    .replace(/{{alpha_start_date}}/g, '2026-05-01')
    .replace(/{{alpha_end_date}}/g, '2026-05-14')
    .replace(/{{invite_link}}/g, `https://alpha.lucive.app/?token=${user.alpha_token}`)
    .replace(/{{discord_invite}}/g, 'https://discord.gg/lucive-alpha')
    .replace(/{{waitlist_position}}/g, user.waitlist_position)
    .replace(/{{next_wave_date}}/g, '2026-07-01')
    .replace(/{{unsubscribe_url}}/g, `https://lucive.app/unsubscribe?token=${user.unsub_token}`)
    .replace(/{{privacy_url}}/g, 'https://lucive.app/privacy');

  const subject = result_type === 'selected'
    ? '🎉 Lucive 알파 테스터로 선발되셨습니다'
    : 'Lucive 알파 대기자 명단 등록 안내';

  await resend.emails.send({
    from: 'Lucive <no-reply@lucive.app>',
    to: user.email,
    subject,
    html,
  });

  return new Response('OK');
});
```

### 호출 방식

```typescript
// 선발자에게
await supabase.functions.invoke('send-alpha-result-email', {
  body: { user_id: selectedUserId, result_type: 'selected' }
});

// 대기자에게
await supabase.functions.invoke('send-alpha-result-email', {
  body: { user_id: waitlistUserId, result_type: 'waitlist' }
});
```

## 변수 목록

### 공통
- `{{user_name}}` — 유저 이름 (없으면 이메일 local-part)
- `{{user_rank}}` — 현재 레퍼럴 순위
- `{{referral_count}}` — 초대한 친구 수
- `{{referral_share_url}}` — 내 초대 링크 (예: `https://lucive.app/r/ABC123`)
- `{{promo_code}}` — 프로모 코드 6자리 (prefix `LUCIVE-` 없이 `ABC123` 형태, 템플릿 내에서 prefix 별도 표시)
- `{{community_kakao}}` — 카카오톡 오픈채팅 URL (한국)
- `{{community_line}}` — LINE 공식계정 URL (일본)
- `{{community_discord}}` — Discord 서버 초대 URL (글로벌)
- `{{unsubscribe_url}}` — 수신 거부 링크
- `{{privacy_url}}` — 개인정보 처리방침 URL

### 등록 확인 이메일 (00)
- 공통 변수만 사용 — 마케터 가이던스(slide 29) 기준 "단일 CTA + 순위 동적 삽입 + 세계관 톤"

### 선발 이메일 (01)
- `{{dip_amount}}` — 지급 Dip (예: `2000`)
- `{{alpha_start_date}}` — 알파 시작일 (예: `2026-05-01`)
- `{{alpha_end_date}}` — 알파 종료일 (예: `2026-05-14`)
- `{{invite_link}}` — 알파 앱 접속 링크
- (커뮤니티는 공통 `{{community_kakao/line/discord}}` 사용)

### 대기자 이메일 (02)
- `{{dip_consolation_amount}}` — 위로 Dip (예: `300`)
- `{{waitlist_position}}` — 대기자 순번
- `{{next_wave_date}}` — 다음 웨이브 예정일

## 혜택 구조 (2026-04 업데이트)

- **전체 사전 등록자 공통**: 사전 체험(알파) 기간 기본 서비스를 **사전 등록 전용 특가**로 체험
  - LP 대화, 비주얼 노벨 다이브, L-Maker 창작 모두 포함
  - 순위·선발 여부와 무관
  - ⚠️ **무료가 아니라 특가** — 메시지 작성 시 혼동 주의
- **Top 5 추가 혜택** (런칭 혜택):
  - 🏆 1위 — 기본 플랜 평생 (런칭 후 지속)
  - 🥈 2-5위 — 초대한 친구 전원 3개월 무료
- **6-10위 별도 혜택 없음** (단, 사전 체험 공통 특가는 동일 적용)

## 발송 전 체크리스트

- [ ] 모든 `{{변수}}` 플레이스홀더가 실제 값으로 치환됨
- [ ] 내부 테스트 수신 (Gmail · 네이버 · 다음 · iPhone Mail · Outlook)
- [ ] 이미지 로드 차단 상태에서도 내용 이해 가능 (이미지 alt 확인)
- [ ] Preheader 텍스트가 받은편지함에 정상 표시
- [ ] CTA 버튼이 Outlook에서도 pill 모양 유지 (VML 폴백 동작)
- [ ] 모바일에서 가로 스크롤 없음
- [ ] 링크 UTM 파라미터 포함 (`?utm_source=email&utm_campaign=alpha_selected`)
- [ ] 발신 이메일 SPF·DKIM·DMARC 인증 완료
- [ ] Spam 테스트: https://www.mail-tester.com 10점 만점 9점+

## A/B 테스트 아이디어

추후 개선을 위한 변주안:

### 선발 이메일
- 제목: "🎉 선발되셨습니다" vs "알파 테스터 합격" vs "Lucive에 초대합니다"
- CTA 색상: aurora gradient vs primary gradient
- 혜택 리스트 vs 스토리형 구성

### 대기자 이메일
- 톤: 정중 vs 친근
- 레퍼럴 push 강도: 약 vs 중 vs 강
- 다음 웨이브 날짜 명시 vs "곧 안내"

## 추가 이메일 템플릿 후보 (향후 제작)

- `03_OTP_코드_발송.html` — 사전 등록 시 6자리 코드
- `04_등록_완료_공유링크.html` — 등록 직후 공유 링크 전달
- `05_스크리닝_리마인더.html` — 3일 후 미응답 대기자 알림
- `06_런칭_알림.html` — 정식 출시 1주일 전
- `07_레퍼럴_순위_알림.html` — Top 10 진입 시 축하
