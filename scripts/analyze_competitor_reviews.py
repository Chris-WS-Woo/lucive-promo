"""
크랙/제타 1★·2★ 리뷰 분석:
 - 키워드 빈도 (한글 명사성 토큰 단순 추출)
 - 불만 카테고리 휴리스틱 (검열/버그/결제/AI품질/UI/기타)
 - 대표 인용문 샘플
 - 강점(역설적 언급) 포착
 - 비교 인사이트 → LUCIVE 포지셔닝 시사점

출력: output/reviews/analysis_report.md
"""
import json, re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
REVIEW_DIR = ROOT / "output" / "reviews"
OUT = REVIEW_DIR / "analysis_report.md"

APPS = {
    "crack": "크랙 (wrtn)",
    "zeta":  "제타 (Scatter Lab)",
}

STOPWORDS = set("""
이 그 저 것 수 등 들 및 의 를 을 은 는 이다 있다 없다 하다 되다 같다 그리고 그래서 하지만 너무 정말 진짜 좀 잘 안 못 더 또 또한 그냥 다 다른 근데 그런데 그런 어떤 이런 저런 요즘 지금 이제 계속 항상 자꾸 매번 매우 많이 조금 좀만 제발 처음 한번 두번 때문 때문에 그래도 그러면 그러니까 그래요 해요 했어요 합니다 있어요 없어요 같아요 싶어요 되네요 이랑 하고 까지 부터 에서 으로 에게 한테 라고 이라고 대해 대한 관련 관련된 이런거 저런거 이게 저게 그게 무슨 무엇 어떻게 어느 어디 누구 언제 왜 진짜로 정말로 아주 좀더 많음 있음 없음 사용 사용자 유저 리뷰 평점 별점 업뎃 업데이트 어플 앱 게임 서비스
""".split())

HEURISTICS = {
    "검열/규제": [r"검열", r"제재", r"차단", r"신고", r"ban", r"밴", r"경고", r"규제", r"규칙", r"위반", r"정책", r"세이프", r"필터", r"수위", r"19", r"성인"],
    "AI 품질/반복성": [r"반복", r"같은 말", r"똑같은", r"기억", r"맥락", r"이상해", r"엉뚱", r"이해", r"말귀", r"답변", r"대답", r"응답", r"ai", r"지능", r"바보", r"멍청", r"이상"],
    "결제/과금/가격": [r"과금", r"결제", r"환불", r"비싸", r"유료", r"요금", r"구독", r"가격", r"현질", r"돈", r"결제해야", r"뽑기", r"가챠", r"뽑"],
    "버그/크래시/로딩": [r"버그", r"오류", r"에러", r"튕", r"로딩", r"느림", r"느려", r"멈춤", r"멈춰", r"접속", r"서버", r"안 돼", r"안됨", r"안되", r"안 됨", r"렉", r"실행", r"종료", r"설치"],
    "UI/UX/편의성": [r"불편", r"ui", r"ux", r"화면", r"디자인", r"어렵", r"복잡", r"찾기", r"메뉴", r"글자", r"폰트", r"버튼", r"직관"],
    "캐릭터/콘텐츠 품질": [r"캐릭터", r"캐릭", r"페르소나", r"스토리", r"시나리오", r"설정", r"세계관", r"대사", r"말투", r"성격", r"붕괴"],
    "커뮤니티/유저": [r"유저", r"욕설", r"비매너", r"신고", r"도용", r"표절", r"불쾌", r"혐오"],
    "크리에이터/창작": [r"만들", r"제작", r"창작", r"크리에이터", r"작가", r"공개", r"비공개", r"봇"],
    "소통/운영": [r"운영", r"공지", r"답변 없", r"문의", r"고객센터", r"cs", r"피드백", r"개선"],
}

TOKEN_RE = re.compile(r"[가-힣a-zA-Z]{2,}")

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def tokenize(text: str):
    if not text: return []
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS and len(t) >= 2]

def classify(text: str):
    text_l = (text or "").lower()
    cats = []
    for cat, pats in HEURISTICS.items():
        if any(re.search(p, text_l) for p in pats):
            cats.append(cat)
    if not cats:
        cats.append("기타")
    return cats

def top_quotes(reviews_list, category, limit=4, min_len=20, max_len=180):
    quotes = []
    for r in reviews_list:
        c = r.get("content") or ""
        if len(c) < min_len: continue
        if category in classify(c):
            q = c.replace("\n", " ").strip()
            if len(q) > max_len:
                q = q[:max_len].rstrip() + "…"
            quotes.append((r.get("thumbsUp", 0) or 0, q))
    quotes.sort(key=lambda x: -x[0])
    return [q for _, q in quotes[:limit]]

def analyze_app(key):
    one = load(REVIEW_DIR / f"{key}_1star.json")
    two = load(REVIEW_DIR / f"{key}_2star.json")
    meta = load(REVIEW_DIR / f"{key}_meta.json")
    all_reviews = one + two
    # 카테고리 집계
    cat_counter = Counter()
    for r in all_reviews:
        for c in classify(r.get("content") or ""):
            cat_counter[c] += 1
    # 키워드 집계
    tok_counter = Counter()
    for r in all_reviews:
        tok_counter.update(tokenize(r.get("content") or ""))
    # 긍정 언급(역설) — "좋은데" "좋지만" "좋았는데" 포함 리뷰
    praise_contrast = [r for r in all_reviews if re.search(r"(좋[은았았는]|재밌|재미있|괜찮|최고)", r.get("content") or "")]
    return {
        "meta": meta,
        "n_1": len(one),
        "n_2": len(two),
        "cats": cat_counter,
        "tokens": tok_counter,
        "praise_contrast": praise_contrast,
        "all": all_reviews,
    }

def pct(n, total):
    return f"{(n/total*100):.1f}%" if total else "-"

def render(results):
    lines = []
    lines.append("# 경쟁사 Play Store 1★/2★ 리뷰 분석 — 크랙 vs 제타\n")
    lines.append("> 수집: 각 앱 1★/2★ 리뷰 최신순 ~300건씩. 분석 시점: 수집일 기준.\n")

    # 개요 표
    lines.append("## 1. 개요\n")
    lines.append("| 앱 | 전체 평점 | 누적 리뷰 | 히스토그램(1★→5★) | 수집 1★ | 수집 2★ |")
    lines.append("|----|:---:|:---:|---|:---:|:---:|")
    for key, name in APPS.items():
        r = results[key]
        m = r["meta"]
        hist = m.get("histogram") or []
        hist_str = " / ".join(str(x) for x in hist)
        lines.append(f"| {name} | {m.get('score'):.2f} | {m.get('reviews'):,} | {hist_str} | {r['n_1']} | {r['n_2']} |")
    lines.append("")

    # 히스토그램 비율 비교
    lines.append("## 2. 부정 리뷰 비중 (1★+2★ / 전체)\n")
    lines.append("| 앱 | 1★ 비중 | 2★ 비중 | 1★+2★ 합산 |")
    lines.append("|----|:---:|:---:|:---:|")
    for key, name in APPS.items():
        hist = results[key]["meta"].get("histogram") or [0]*5
        total = sum(hist) or 1
        lines.append(f"| {name} | {pct(hist[0], total)} | {pct(hist[1], total)} | {pct(hist[0]+hist[1], total)} |")
    lines.append("")

    # 카테고리별
    lines.append("## 3. 불만 카테고리 분포 (1★+2★ 리뷰 기준)\n")
    categories = list(HEURISTICS.keys()) + ["기타"]
    lines.append("| 카테고리 | 크랙 | 제타 |")
    lines.append("|---|:---:|:---:|")
    for c in categories:
        crack_c = results["crack"]["cats"].get(c, 0)
        zeta_c  = results["zeta"]["cats"].get(c, 0)
        crack_total = results["crack"]["n_1"] + results["crack"]["n_2"]
        zeta_total  = results["zeta"]["n_1"]  + results["zeta"]["n_2"]
        lines.append(f"| {c} | {crack_c} ({pct(crack_c, crack_total)}) | {zeta_c} ({pct(zeta_c, zeta_total)}) |")
    lines.append("\n*복수 카테고리 매칭 가능(한 리뷰가 여러 카테고리에 걸칠 수 있음).*\n")

    # 대표 인용문 — 상위 카테고리 Top 3씩
    for key, name in APPS.items():
        lines.append(f"## 4-{'A' if key=='crack' else 'B'}. {name} — 카테고리별 대표 인용문\n")
        top_cats = [c for c, _ in results[key]["cats"].most_common(6) if c != "기타"]
        for cat in top_cats:
            quotes = top_quotes(results[key]["all"], cat, limit=4)
            if not quotes: continue
            lines.append(f"### {cat}")
            for q in quotes:
                lines.append(f"- \"{q}\"")
            lines.append("")

    # 키워드 Top 30
    lines.append("## 5. 고빈도 키워드 (불용어 제거 후)\n")
    lines.append("| 순위 | 크랙 키워드(빈도) | 제타 키워드(빈도) |")
    lines.append("|:---:|---|---|")
    crack_top = results["crack"]["tokens"].most_common(30)
    zeta_top  = results["zeta"]["tokens"].most_common(30)
    for i in range(30):
        c = f"{crack_top[i][0]} ({crack_top[i][1]})" if i < len(crack_top) else ""
        z = f"{zeta_top[i][0]} ({zeta_top[i][1]})"   if i < len(zeta_top)  else ""
        lines.append(f"| {i+1} | {c} | {z} |")
    lines.append("")

    # 역설적 강점 — "좋은데/재밌는데" 패턴
    lines.append("## 6. 역설적 강점 시그널 (낮은 별점이지만 긍정 언급 포함 리뷰)\n")
    lines.append("부정 리뷰 속 '좋은데/재밌는데' 패턴은 **유저가 잃고 싶지 않은 핵심 가치**를 드러낸다.\n")
    for key, name in APPS.items():
        lines.append(f"### {name}")
        pcs = results[key]["praise_contrast"]
        lines.append(f"- 해당 리뷰 수: **{len(pcs)}건 / {results[key]['n_1']+results[key]['n_2']}건**")
        # 추천 많은 순 상위 5개
        pcs_sorted = sorted(pcs, key=lambda r: -(r.get("thumbsUp") or 0))[:5]
        for r in pcs_sorted:
            q = (r.get("content") or "").replace("\n"," ").strip()
            if len(q) > 180: q = q[:180] + "…"
            lines.append(f"  - ({r.get('score')}★, 👍{r.get('thumbsUp') or 0}) \"{q}\"")
        lines.append("")

    # 시사점
    lines.append("## 7. LUCIVE 포지셔닝 시사점 (드래프트)\n")
    lines.append("*아래는 분석 데이터 기반 가설이며, 최종 메시징 확정 전 검증 필요.*\n")
    lines.append("- **검열·규제 불만이 양사 공통 최상위이면 → LUCIVE의 \"합의된 연령 게이트\" + \"크리에이터 창작 자유(스토리 컨테이너)\" 프레임으로 차별화 가능**")
    lines.append("- **AI 반복/맥락 상실 불만 → LUCIVE DeepWriter의 '스토리 구조 기반 전개' (자유 채팅이 아닌 루시브 단위 서사)로 회피 논거**")
    lines.append("- **결제·뽑기·가챠 피로 → LUCIVE 3-Tier 모델 (Viewer 무료 + Player 일1회 무료 + Creator 구독) 단순성·투명성 강조**")
    lines.append("- **캐릭터 붕괴/설정 이탈 → LP 1명 고정(MVP) + 루시브 단위 세계관 고정으로 일관성 우위**")
    lines.append("- **'재밌는데 ~해서 별점 내림' 패턴 → 유저가 포기하지 못하는 핵심 경험(몰입/서사/관계)은 LUCIVE도 사수해야 할 카테고리 필수 요건**")
    lines.append("")

    return "\n".join(lines)

def main():
    results = {k: analyze_app(k) for k in APPS}
    OUT.write_text(render(results), encoding="utf-8")
    print(f"리포트 생성: {OUT}")
    print(f" - 크랙 1★+2★: {results['crack']['n_1']+results['crack']['n_2']}건")
    print(f" - 제타 1★+2★: {results['zeta']['n_1']+results['zeta']['n_2']}건")

if __name__ == "__main__":
    main()
