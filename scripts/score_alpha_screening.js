/**
 * Lucive 알파 스크리닝 점수화 + 선발 스크립트
 *
 * 사용법:
 *   node scripts/score_alpha_screening.js                 # 모의 데이터 600명 선발 시뮬
 *   node scripts/score_alpha_screening.js --target 150    # 선발 인원 지정
 *   node scripts/score_alpha_screening.js --input real.json  # 실제 응답 JSON 파일 로드
 *
 * Supabase 연동 예시는 파일 하단 참조.
 */

// =============================
// 점수화 로직
// =============================
function calculateScore(answers) {
  let score = 0;
  const persona = { A: 0, B: 0 };
  const reasons = []; // 점수 내역 (디버깅·투명성)

  // --- Q1: 챗봇 사용 기간 ---
  const durationScore = {
    never: 0,
    lt_1m: 10,
    '1_6m': 25,
    '6m_1y': 40,
    gt_1y: 50,
  };
  const q1Score = durationScore[answers.q1] || 0;
  score += q1Score;
  if (q1Score > 0) reasons.push(`Q1 사용기간 +${q1Score}`);
  if (answers.q1 && answers.q1 !== 'never') persona.A += 20;

  // --- Q1b: 사용 앱 수 ---
  const q1bLen = (answers.q1b || []).length;
  const q1bScore = Math.min(q1bLen * 5, 25);
  score += q1bScore;
  if (q1bScore > 0) reasons.push(`Q1b 앱개수(${q1bLen}) +${q1bScore}`);
  persona.A += Math.min(q1bLen * 3, 15);

  // --- Q2: 빈도 ---
  const freqScore = {
    daily: 30,
    weekly_high: 25,
    weekly_low: 15,
    monthly: 5,
    rare: 0,
  };
  const q2Score = freqScore[answers.q2] || 0;
  score += q2Score;
  if (q2Score > 0) reasons.push(`Q2 빈도 +${q2Score}`);

  // --- Q3: 불편 명확성 (복수 선택) ---
  // 이전 버전 호환: 문자열이면 배열로 승격
  const q3Answers = Array.isArray(answers.q3)
    ? answers.q3
    : answers.q3 ? [answers.q3] : [];
  const painSpecific = ['memory', 'repeat', 'shallow', 'censor'];
  let q3Score = 0;
  if (q3Answers.length > 0) {
    // 선택 개수 × 6점 (최대 24) — 구체적으로 여러 불만 짚을수록 가산
    q3Score += Math.min(q3Answers.length * 6, 24);
    // 고신호 pain point 1개당 +5 (LUCIVE가 해결하는 핵심 불만)
    const specificCount = q3Answers.filter(p => painSpecific.includes(p)).length;
    q3Score += specificCount * 5;
    // "기타" + 텍스트 10자+ 추가
    if (q3Answers.includes('other') && (answers.q3_other_text || '').length > 10) {
      q3Score += 8;
    }
    q3Score = Math.min(q3Score, 45);
  }
  score += q3Score;
  if (q3Score > 0) reasons.push(`Q3 불편(${q3Answers.length}개) +${q3Score}`);

  // --- Q3_alt: 챗봇 안 쓴 사람의 관심 이유 ---
  if (answers.q3_alt && answers.q3_alt.trim().length > 20) {
    score += 15;
    reasons.push(`Q3_alt 관심이유 +15`);
  }

  // --- Q4: 좋았던 순간 ---
  const q4Items = answers.q4 || [];
  const q4WithoutNone = q4Items.filter((i) => i !== 'none');
  const q4Score = Math.min(q4WithoutNone.length * 5, 20);
  score += q4Score;
  if (q4Score > 0) reasons.push(`Q4 좋은순간(${q4WithoutNone.length}) +${q4Score}`);

  // --- Q5: 창작 경험 (핵심 가산) ---
  const q5Items = answers.q5 || [];
  const q5WithoutNone = q5Items.filter((i) => i !== 'none');
  const q5Score = Math.min(q5WithoutNone.length * 10, 40);
  score += q5Score;
  if (q5Score > 0) reasons.push(`Q5 창작경험(${q5WithoutNone.length}) +${q5Score}`);
  if (q5Items.includes('webnovel') || q5Items.includes('botmaking')) {
    persona.B += 20;
  }

  // --- Q6: 게임 경험 (서사·VN 중시) ---
  const games = answers.q6 || [];
  let q6Score = 0;
  if (games.includes('vn')) {
    q6Score += 40;
    persona.B += 25;
  }
  if (games.includes('jrpg')) q6Score += 25;
  if (games.includes('openworld')) q6Score += 20;
  if (games.includes('gacha')) q6Score += 10;
  if (games.includes('mmo')) q6Score += 8;
  if (games.includes('casual')) q6Score += 5;
  if (games.includes('fps')) q6Score += 5;
  score += q6Score;
  if (q6Score > 0) reasons.push(`Q6 게임(${games.length}장르) +${q6Score}`);

  // --- Q7: 웹툰·웹소설 ---
  const webnovelFreq = {
    daily: 20,
    weekly: 15,
    weekly1: 10,
    rare: 5,
    never: 0,
  };
  const q7FreqScore = webnovelFreq[answers.q7_freq] || 0;
  score += q7FreqScore;
  if (q7FreqScore > 0) reasons.push(`Q7_freq 웹소설빈도 +${q7FreqScore}`);
  persona.B += q7FreqScore * 1.5;

  // 타겟 장르 매칭 (페르소나 B 핵심)
  const targetGenres = ['romance', 'binhwui', 'hunter'];
  const q7Genres = answers.q7_genres || [];
  const genreMatch = q7Genres.filter((g) => targetGenres.includes(g)).length;
  const q7GenreScore = genreMatch * 5;
  score += q7GenreScore;
  if (q7GenreScore > 0) reasons.push(`Q7_genres 타겟장르(${genreMatch}개) +${q7GenreScore}`);
  persona.B += genreMatch * 3;

  // --- Q8: 과금 경험 ---
  const payScore = {
    over_100k: 30,
    k_50_100: 25,
    k_10_50: 20,
    under_10k: 10,
    none: 5,
  };
  const q8Score = payScore[answers.q8] || 0;
  score += q8Score;
  if (q8Score > 0) reasons.push(`Q8 과금 +${q8Score}`);

  // --- Q10: 구체 의견 (선택, 최대 가산) ---
  const q10Text = (answers.q10 || '').trim();
  let q10Score = 0;
  if (q10Text.length >= 100) q10Score = 30;
  else if (q10Text.length >= 50) q10Score = 20;
  else if (q10Text.length >= 10) q10Score = 10;
  score += q10Score;
  if (q10Score > 0) reasons.push(`Q10 의견작성(${q10Text.length}자) +${q10Score}`);

  // --- 페르소나 분류 ---
  const personaType =
    persona.A > persona.B + 10
      ? 'A'
      : persona.B > persona.A + 10
      ? 'B'
      : 'AB'; // 양쪽 균형

  // --- 추천 등급 ---
  const recommendation = score >= 170 ? 'strong' : score >= 110 ? 'qualified' : 'waitlist';

  return {
    score,
    persona,
    personaType,
    recommendation,
    reasons,
  };
}

// =============================
// 선발 로직 (페르소나 균형)
// =============================
function selectAlphaTesters(scoredUsers, targetCount = 200) {
  const TARGET_A_RATIO = 0.6; // 페르소나 A 60% · B 40%는 잔여로 계산
  const targetA = Math.round(targetCount * TARGET_A_RATIO);
  const targetB = targetCount - targetA;

  // 점수 내림차순 정렬
  const sorted = [...scoredUsers].sort((a, b) => b.scoring.score - a.scoring.score);

  // 후보 풀: 최소 자격(waitlist 아님) 이상 + 여유 있게 3배수
  const qualified = sorted.filter((u) => u.scoring.recommendation !== 'waitlist');
  const poolSize = Math.min(qualified.length, targetCount * 3);
  const pool = qualified.slice(0, poolSize);

  // 페르소나별 분리
  const poolA = pool.filter((u) => u.scoring.personaType === 'A');
  const poolB = pool.filter((u) => u.scoring.personaType === 'B');
  const poolAB = pool.filter((u) => u.scoring.personaType === 'AB');

  const selected = [];

  // A 선발
  const aSelected = poolA.slice(0, Math.min(targetA, poolA.length));
  selected.push(...aSelected);

  // B 선발
  const bSelected = poolB.slice(0, Math.min(targetB, poolB.length));
  selected.push(...bSelected);

  // 부족분은 AB(양쪽) 풀에서 보충
  const need = targetCount - selected.length;
  if (need > 0 && poolAB.length > 0) {
    selected.push(...poolAB.slice(0, need));
  }

  // 최대한 채우기: 그래도 부족하면 남은 풀에서 점수순
  if (selected.length < targetCount) {
    const selectedIds = new Set(selected.map((u) => u.id));
    const remaining = pool.filter((u) => !selectedIds.has(u.id));
    const extra = remaining.slice(0, targetCount - selected.length);
    selected.push(...extra);
  }

  // 대기자 명단 (점수 내림차순)
  const selectedIds = new Set(selected.map((u) => u.id));
  const waitlist = sorted
    .filter((u) => !selectedIds.has(u.id))
    .map((u, i) => ({ ...u, waitlist_position: i + 1 }));

  return {
    selected,
    waitlist,
    stats: {
      totalCandidates: scoredUsers.length,
      qualified: qualified.length,
      selectedCount: selected.length,
      waitlistCount: waitlist.length,
      personaA: selected.filter((u) => u.scoring.personaType === 'A').length,
      personaB: selected.filter((u) => u.scoring.personaType === 'B').length,
      personaAB: selected.filter((u) => u.scoring.personaType === 'AB').length,
      avgScore: Math.round(
        selected.reduce((s, u) => s + u.scoring.score, 0) / (selected.length || 1)
      ),
      scoreRange: [
        Math.min(...selected.map((u) => u.scoring.score)),
        Math.max(...selected.map((u) => u.scoring.score)),
      ],
    },
  };
}

// =============================
// 모의 응답 생성기
// =============================
function generateMockResponse(index) {
  const rand = (arr) => arr[Math.floor(Math.random() * arr.length)];
  const randMulti = (arr, min, max) => {
    const n = min + Math.floor(Math.random() * (max - min + 1));
    const shuffled = [...arr].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, n);
  };

  const q1 = rand(['never', 'lt_1m', '1_6m', '6m_1y', 'gt_1y']);
  const neverUsed = q1 === 'never';

  return {
    id: `user_${index}`,
    email: `user${index}@example.com`,
    answers: {
      q1,
      q1b: neverUsed
        ? undefined
        : randMulti(
            ['character_ai', 'crack', 'zeta', 'replika', 'talkie', 'janitor', 'spicychat'],
            1,
            4
          ),
      q2: neverUsed ? undefined : rand(['daily', 'weekly_high', 'weekly_low', 'monthly', 'rare']),
      q3: neverUsed
        ? undefined
        : randMulti(
            ['memory', 'repeat', 'shallow', 'payment', 'censor', 'speed', 'ui', 'other'],
            1,
            4
          ),
      q3_other_text: Math.random() < 0.2 ? '광고가 너무 많아서 몰입이 깨짐' : '',
      q3_alt: neverUsed && Math.random() < 0.7 ? '웹소설 주인공이 되는 경험이 재밌을 것 같아서' : '',
      q4: neverUsed
        ? undefined
        : randMulti(['empathy', 'fun', 'character', 'comfort', 'creative', 'stress', 'none'], 1, 3),
      q5: randMulti(
        ['webnovel', 'webtoon', 'botmaking', 'scenario', 'blog', 'ai_content', 'none'],
        0,
        3
      ),
      q6: randMulti(
        ['vn', 'jrpg', 'openworld', 'gacha', 'mmo', 'casual', 'fps', 'none'],
        1,
        4
      ),
      q7_freq: rand(['daily', 'weekly', 'weekly1', 'rare', 'never']),
      q7_genres:
        Math.random() > 0.15
          ? randMulti(
              ['romance', 'fantasy', 'binhwui', 'hunter', 'martial', 'thriller', 'daily', 'scifi'],
              1,
              4
            )
          : [],
      q8: rand(['over_100k', 'k_50_100', 'k_10_50', 'under_10k', 'none']),
      q10:
        Math.random() < 0.35
          ? '17일 전 대화를 정확히 기억하는지, 그리고 백스토리 다이브 후 대화에 반영되는지 확인해보고 싶습니다'
          : Math.random() < 0.5
          ? '비주얼 노벨 모드 재밌을 것 같아요'
          : '',
    },
  };
}

// =============================
// 메인 실행
// =============================
function run() {
  const args = process.argv.slice(2);
  const targetIdx = args.indexOf('--target');
  const target = targetIdx !== -1 ? parseInt(args[targetIdx + 1], 10) : 200;
  const inputIdx = args.indexOf('--input');
  const inputFile = inputIdx !== -1 ? args[inputIdx + 1] : null;
  const mockCountIdx = args.indexOf('--mock');
  const mockCount = mockCountIdx !== -1 ? parseInt(args[mockCountIdx + 1], 10) : 600;

  let users = [];

  if (inputFile) {
    const fs = require('fs');
    try {
      users = JSON.parse(fs.readFileSync(inputFile, 'utf-8'));
      console.log(`✓ ${inputFile}에서 ${users.length}개 응답 로드\n`);
    } catch (e) {
      console.error(`❌ 입력 파일 로드 실패: ${e.message}`);
      process.exit(1);
    }
  } else {
    console.log(`🎲 모의 응답 ${mockCount}개 생성 중...\n`);
    users = Array.from({ length: mockCount }, (_, i) => generateMockResponse(i));
  }

  // 점수화
  console.log('📊 점수 계산 중...');
  const scored = users.map((u) => ({
    ...u,
    scoring: calculateScore(u.answers),
  }));

  // 선발
  console.log(`🎯 ${target}명 선발 시뮬레이션 중...\n`);
  const result = selectAlphaTesters(scored, target);

  // 결과 출력
  console.log('═══════════════════════════════════════════════════');
  console.log('                  선발 결과 요약                      ');
  console.log('═══════════════════════════════════════════════════');
  console.log(`전체 응답: ${result.stats.totalCandidates}`);
  console.log(`최소 자격: ${result.stats.qualified} (${Math.round((result.stats.qualified / result.stats.totalCandidates) * 100)}%)`);
  console.log(`선발 인원: ${result.stats.selectedCount}`);
  console.log(`대기자: ${result.stats.waitlistCount}`);
  console.log(`평균 점수: ${result.stats.avgScore}`);
  console.log(`점수 범위: ${result.stats.scoreRange[0]} - ${result.stats.scoreRange[1]}`);
  console.log('');
  console.log('페르소나 분포:');
  console.log(`  A (챗봇 지친):  ${result.stats.personaA} (${Math.round((result.stats.personaA / result.stats.selectedCount) * 100)}%)`);
  console.log(`  B (웹소설러):   ${result.stats.personaB} (${Math.round((result.stats.personaB / result.stats.selectedCount) * 100)}%)`);
  console.log(`  AB (균형):     ${result.stats.personaAB} (${Math.round((result.stats.personaAB / result.stats.selectedCount) * 100)}%)`);
  console.log('');
  console.log('');

  // 상위 5명 샘플
  console.log('🏆 상위 5명 샘플:');
  console.log('─────────────────────────────────────────────────');
  result.selected.slice(0, 5).forEach((u, i) => {
    console.log(`${i + 1}. ${u.id} (${u.email})`);
    console.log(`   점수: ${u.scoring.score} | 페르소나: ${u.scoring.personaType} | 등급: ${u.scoring.recommendation}`);
    console.log(`   내역: ${u.scoring.reasons.join(', ')}`);
    console.log('');
  });

  // 점수 분포 히스토그램
  console.log('📈 점수 분포 (선발자):');
  const buckets = {};
  result.selected.forEach((u) => {
    const bucket = Math.floor(u.scoring.score / 20) * 20;
    buckets[bucket] = (buckets[bucket] || 0) + 1;
  });
  Object.keys(buckets)
    .sort((a, b) => parseInt(a) - parseInt(b))
    .forEach((b) => {
      const bar = '█'.repeat(Math.ceil(buckets[b] / 3));
      console.log(`  ${b.toString().padStart(3)} - ${(parseInt(b) + 19).toString().padStart(3)}: ${bar} (${buckets[b]})`);
    });
  console.log('');

  // 결과 JSON 저장 옵션
  const outputIdx = args.indexOf('--output');
  if (outputIdx !== -1) {
    const outputPath = args[outputIdx + 1];
    const fs = require('fs');
    fs.writeFileSync(
      outputPath,
      JSON.stringify(
        {
          stats: result.stats,
          selected: result.selected.map((u) => ({
            id: u.id,
            email: u.email,
            score: u.scoring.score,
            persona: u.scoring.personaType,
            recommendation: u.scoring.recommendation,
          })),
          waitlist: result.waitlist.slice(0, 100).map((u) => ({
            id: u.id,
            email: u.email,
            score: u.scoring.score,
            waitlist_position: u.waitlist_position,
          })),
        },
        null,
        2
      )
    );
    console.log(`💾 결과 저장: ${outputPath}`);
  }

  console.log('✓ 완료\n');
}

// =============================
// Supabase 연동 예시 (주석)
// =============================
/*

// supabase/functions/select-alpha-testers/index.ts
import { createClient } from 'jsr:@supabase/supabase-js';
import { calculateScore, selectAlphaTesters } from './score.js';

const supabase = createClient(
  Deno.env.get('SUPABASE_URL'),
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
);

Deno.serve(async (req) => {
  // 1. 스크리닝 응답 전체 로드
  const { data: responses } = await supabase
    .from('alpha_screening')
    .select('*, user:users(id, email, referral_rank, referral_code)');

  // 2. 점수화 + 선발
  const scored = responses.map(r => ({
    id: r.user.id,
    email: r.user.email,
    answers: r.answers,
    scoring: calculateScore(r.answers)
  }));

  const result = selectAlphaTesters(scored, 200);

  // 3. DB에 결과 반영
  await supabase
    .from('users')
    .upsert(
      result.selected.map(u => ({
        id: u.id,
        alpha_status: 'selected',
        alpha_score: u.scoring.score,
        alpha_persona: u.scoring.personaType,
      }))
    );

  await supabase
    .from('users')
    .upsert(
      result.waitlist.map(u => ({
        id: u.id,
        alpha_status: 'waitlist',
        waitlist_position: u.waitlist_position,
        alpha_score: u.scoring.score,
      }))
    );

  // 4. 이메일 발송 트리거
  for (const u of result.selected) {
    await supabase.functions.invoke('send-alpha-result-email', {
      body: { user_id: u.id, result_type: 'selected' }
    });
  }
  for (const u of result.waitlist) {
    await supabase.functions.invoke('send-alpha-result-email', {
      body: { user_id: u.id, result_type: 'waitlist' }
    });
  }

  return new Response(JSON.stringify(result.stats));
});

*/

// =============================
// Export for reuse
// =============================
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    calculateScore,
    selectAlphaTesters,
    generateMockResponse,
  };
}

// Run if called directly
if (require.main === module) {
  run();
}
