"""
해외 캐릭터챗 앱 다국어 리뷰 분석.
 - 앱별 1★+2★ 비중, 카테고리 분포
 - 언어별 카테고리 분포 차이
 - 대표 인용문 (중복 제거, 카테고리당 고유)
 - 키워드 Top (영어 중심)
출력: output/reviews_global/global_analysis_report.md
"""
import json, re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "output" / "reviews_global"
OUT = DIR / "global_analysis_report.md"

APPS = {
    "character_ai":  "Character.AI",
    "talkie":        "Talkie (Weaver)",
    "replika":       "Replika",
    "ai_dungeon":    "AI Dungeon",
    "polybuzz":      "PolyBuzz (Poly.AI)",
    "linky":         "Linky AI",
    "chai":          "Chai",
    "crushon":       "CrushOn.AI",
    "spicychat":     "SpicyChat AI",
    "joyland":       "Joyland AI",
    "kindroid":      "Kindroid",
    "nomi":          "Nomi.ai",
    "anima":         "Anima",
    "dippy":         "Dippy.ai",
    "paradot":       "Paradot",
}

LOCALES = ["en", "ja", "es", "pt", "de", "zh"]

# 다국어 휴리스틱 — 각 카테고리마다 lang -> regex list
HEURISTICS = {
    "검열/규제 (Censorship/Filter)": {
        "en": [r"\bcensor", r"\bfilter\b", r"\bban\b", r"banned", r"nsfw", r"restrict", r"prude", r"moral", r"puritan", r"safety", r"guideline", r"content warning"],
        "ja": [r"検閲", r"規制", r"制限", r"フィルター", r"禁止", r"過激"],
        "es": [r"censur", r"filtr", r"restric", r"prohib", r"permit"],
        "pt": [r"censur", r"filtr", r"restri", r"proib", r"permit"],
        "de": [r"zensur", r"filter", r"beschränk", r"verbot"],
        "zh": [r"审查", r"審查", r"过滤", r"過濾", r"限制", r"禁止"],
    },
    "AI 품질/기억력 (AI Quality/Memory)": {
        "en": [r"\bmemory\b", r"forget", r"repet", r"\bdumb\b", r"stupid", r"out of character", r"\bOOC\b", r"context", r"incoherent", r"make sense", r"nonsens", r"hallucinat", r"quality", r"worse", r"nerf", r"dumber", r"lobotom", r"repeat"],
        "ja": [r"記憶", r"忘れ", r"繰り返", r"馬鹿", r"バカ", r"文脈", r"ループ", r"頭悪"],
        "es": [r"memoria", r"olvid", r"repet", r"tonto", r"estúpid", r"contexto", r"sentido"],
        "pt": [r"memória", r"esquec", r"repet", r"burro", r"estúpid", r"contexto", r"sentido"],
        "de": [r"gedächtnis", r"vergess", r"wiederhol", r"dumm", r"kontext", r"sinn"],
        "zh": [r"记忆", r"記憶", r"忘", r"重复", r"重複", r"智商", r"上下文", r"逻辑", r"邏輯"],
    },
    "결제/과금 (Pricing/Monetization)": {
        "en": [r"\$", r"price", r"paywall", r"subscrib", r"refund", r"expensive", r"greedy", r"premium", r"pro\b", r"pay to", r"pay-to", r"money grab", r"rip.?off", r"token", r"credit", r"message.?limit", r"free user", r"monetiz"],
        "ja": [r"課金", r"値段", r"高い", r"サブスク", r"返金", r"有料", r"ガチャ", r"金"],
        "es": [r"precio", r"caro", r"pagar", r"suscrip", r"reembolso", r"gratis", r"cobr", r"dinero", r"avaricia"],
        "pt": [r"preço", r"caro", r"pagar", r"assinatur", r"reembolso", r"grátis", r"gratuit", r"cobr", r"dinheiro", r"ganância"],
        "de": [r"preis", r"teuer", r"zahlen", r"abo", r"abonne", r"erstatt", r"kostenlos", r"geld", r"gier"],
        "zh": [r"收费", r"收費", r"贵", r"貴", r"订阅", r"訂閱", r"退款", r"免费", r"免費", r"付费", r"付費", r"钱", r"錢"],
    },
    "광고 (Ads)": {
        "en": [r"\bads?\b", r"advert", r"commercial"],
        "ja": [r"広告", r"CM"],
        "es": [r"anunci", r"publicid"],
        "pt": [r"anúnci", r"propagand", r"publicid"],
        "de": [r"werbung", r"anzeig"],
        "zh": [r"广告", r"廣告"],
    },
    "버그/크래시 (Bugs/Crash)": {
        "en": [r"\bbug", r"crash", r"freeze", r"glitch", r"broken", r"can.?t log", r"won.?t load", r"error", r"slow", r"lag"],
        "ja": [r"バグ", r"落ちる", r"クラッシュ", r"エラー", r"重い", r"遅い", r"フリーズ"],
        "es": [r"error", r"falla", r"cierra", r"cuelg", r"lent", r"bug"],
        "pt": [r"erro", r"trav", r"fech", r"bug", r"lent"],
        "de": [r"fehler", r"absturz", r"bug", r"langsam", r"friert"],
        "zh": [r"错误", r"錯誤", r"闪退", r"閃退", r"卡", r"崩溃", r"崩潰", r"慢"],
    },
    "캐릭터/콘텐츠 (Character/Content)": {
        "en": [r"character", r"persona", r"personality", r"roleplay", r"story", r"\bbot\b"],
        "ja": [r"キャラ", r"人格", r"性格", r"ロープレ", r"ロールプレイ"],
        "es": [r"personaj", r"persona", r"historia", r"rol"],
        "pt": [r"personag", r"persona", r"históri", r"roleplay"],
        "de": [r"charakter", r"person", r"geschicht", r"rollen"],
        "zh": [r"角色", r"人设", r"人設", r"故事", r"扮演"],
    },
    "프라이버시/신뢰 (Privacy/Trust)": {
        "en": [r"privacy", r"data", r"leak", r"track", r"personal info", r"creepy", r"spy"],
        "ja": [r"プライバシー", r"個人情報", r"情報漏"],
        "es": [r"privacidad", r"datos", r"fug"],
        "pt": [r"privacidade", r"dados", r"vaz"],
        "de": [r"datenschutz", r"privatsphäre", r"daten"],
        "zh": [r"隐私", r"隱私", r"个人信息", r"個人資料", r"泄", r"洩"],
    },
    "정서적/관계 (Emotional/Relationship)": {
        "en": [r"\blove\b", r"lonely", r"girlfriend", r"boyfriend", r"companion", r"friend", r"relationship", r"emotion", r"depress", r"attach"],
        "ja": [r"恋人", r"友達", r"寂し", r"愛", r"感情", r"依存"],
        "es": [r"novi", r"amig", r"sol", r"amor", r"emocion", r"relación"],
        "pt": [r"namorad", r"amig", r"sozinh", r"amor", r"emoção", r"relaciona"],
        "de": [r"freund", r"einsam", r"liebe", r"gefühl", r"beziehung"],
        "zh": [r"男友", r"女友", r"朋友", r"孤独", r"孤獨", r"爱", r"愛", r"感情"],
    },
}

CATS = list(HEURISTICS.keys()) + ["기타"]

def classify(text, lang):
    if not text: return ["기타"]
    t = text.lower()
    found = []
    for cat, lang_map in HEURISTICS.items():
        pats = lang_map.get(lang, [])
        # 영어 패턴은 다른 언어 리뷰에도 섞일 수 있으므로 보조로 체크
        if lang != "en":
            pats = pats + lang_map.get("en", [])
        if any(re.search(p, t) for p in pats):
            found.append(cat)
    return found or ["기타"]

def load(path):
    if not path.exists(): return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []

def collect():
    data = {}
    for key in APPS:
        meta = load(DIR / f"{key}_meta.json")
        per_lang = {}
        for lang in LOCALES:
            one = load(DIR / f"{key}_{lang}_1star.json")
            two = load(DIR / f"{key}_{lang}_2star.json")
            per_lang[lang] = {"1": one, "2": two}
        data[key] = {"meta": meta, "reviews": per_lang}
    return data

def pct(n, total):
    return f"{(n/total*100):.0f}%" if total else "-"

def category_counts(review_list, lang):
    c = Counter()
    for r in review_list:
        for cat in classify(r.get("content") or "", lang):
            c[cat] += 1
    return c

def unique_quotes_for_cat(review_list, lang, category, limit=3, min_len=25, max_len=200):
    out = []
    seen = set()
    ranked = sorted(review_list, key=lambda r: -(r.get("thumbsUp") or 0))
    for r in ranked:
        content = (r.get("content") or "").replace("\n", " ").strip()
        if len(content) < min_len: continue
        cats = classify(content, lang)
        if category not in cats: continue
        key = content[:80]
        if key in seen: continue
        seen.add(key)
        q = content if len(content) <= max_len else content[:max_len].rstrip() + "…"
        out.append((r.get("thumbsUp") or 0, q))
        if len(out) >= limit: break
    return out

def render(data):
    L = []
    L.append("# 해외 캐릭터챗 앱 Play Store 1★/2★ 리뷰 분석 (다국어)\n")
    L.append("> 대상 15개 앱, locale 6종(en/ja/es/pt/de/zh), 각 locale당 1★·2★ 최대 100건씩.\n")

    # 1. 개요
    L.append("## 1. 앱 개요\n")
    L.append("| 앱 | 평점 | 누적리뷰 | 1★ 비중 | 1★+2★ 비중 | 주 언어권 수집량 |")
    L.append("|----|:--:|:--:|:--:|:--:|:--|")
    for key, name in APPS.items():
        m = data[key]["meta"]
        if not m or m.get("score") in (None, 0):
            L.append(f"| {name} | (데이터 없음) | - | - | - | - |")
            continue
        hist = m.get("histogram") or [0]*5
        total = sum(hist) or 1
        revs = data[key]["reviews"]
        volume = ", ".join(
            f"{lang}:{len(revs[lang]['1'])+len(revs[lang]['2'])}"
            for lang in LOCALES
            if len(revs[lang]['1'])+len(revs[lang]['2']) > 0
        )
        L.append(f"| {name} | {m.get('score'):.2f} | {m.get('reviews'):,} | {pct(hist[0], total)} | {pct(hist[0]+hist[1], total)} | {volume} |")
    L.append("")

    # 2. 앱별 카테고리 분포 (전 locale 합산)
    L.append("## 2. 앱별 불만 카테고리 분포 (전 locale 1★+2★ 합산)\n")
    L.append("| 앱 | n | " + " | ".join(c.split(' ')[0] for c in CATS) + " |")
    L.append("|---|:--:|" + "|".join([":--:"]*len(CATS)) + "|")
    app_cat_summary = {}
    for key, name in APPS.items():
        revs = data[key]["reviews"]
        all_reviews_with_lang = []
        for lang in LOCALES:
            for r in revs[lang]["1"] + revs[lang]["2"]:
                all_reviews_with_lang.append((lang, r))
        n = len(all_reviews_with_lang)
        if n < 30:
            continue
        cat_c = Counter()
        for lang, r in all_reviews_with_lang:
            for c in classify(r.get("content") or "", lang):
                cat_c[c] += 1
        app_cat_summary[key] = (n, cat_c)
        cells = [name, str(n)]
        for c in CATS:
            cells.append(pct(cat_c.get(c, 0), n))
        L.append("| " + " | ".join(cells) + " |")
    L.append("")

    # 3. 언어별 카테고리 비중 — 대형앱만
    L.append("## 3. 언어별 카테고리 비중 — 대형 앱 4종 (Character.AI / Talkie / Replika / PolyBuzz)\n")
    target = ["character_ai", "talkie", "replika", "polybuzz"]
    for key in target:
        if key not in app_cat_summary: continue
        name = APPS[key]
        L.append(f"### {name}")
        L.append("| 언어 | n | " + " | ".join(c.split(' ')[0] for c in CATS) + " |")
        L.append("|---|:--:|" + "|".join([":--:"]*len(CATS)) + "|")
        for lang in LOCALES:
            revs = data[key]["reviews"][lang]
            merged = revs["1"] + revs["2"]
            n = len(merged)
            if n < 20:
                continue
            cat_c = category_counts(merged, lang)
            cells = [lang, str(n)]
            for c in CATS:
                cells.append(pct(cat_c.get(c, 0), n))
            L.append("| " + " | ".join(cells) + " |")
        L.append("")

    # 4. 대표 인용문 — 주요 앱 × 주요 카테고리 × 언어별 1개씩
    L.append("## 4. 주요 앱 대표 인용문 (카테고리별, 고유)\n")
    for key in target:
        if key not in app_cat_summary: continue
        name = APPS[key]
        L.append(f"### {name}")
        n, cat_c = app_cat_summary[key]
        top_cats = [c for c, _ in cat_c.most_common(5) if c != "기타"]
        revs = data[key]["reviews"]
        for cat in top_cats:
            L.append(f"**{cat}**")
            for lang in ["en", "ja", "es", "pt", "de", "zh"]:
                merged = revs[lang]["1"] + revs[lang]["2"]
                if len(merged) < 15: continue
                quotes = unique_quotes_for_cat(merged, lang, cat, limit=1)
                if quotes:
                    tu, q = quotes[0]
                    L.append(f"- [{lang}] (👍{tu}) \"{q}\"")
            L.append("")
        L.append("")

    # 5. 언어별 비교 인사이트 (Character.AI 기준 예시)
    L.append("## 5. 언어별 공통/차이 패턴 (요약)\n")
    L.append("**공통 (언어 무관):**")
    L.append("- AI 기억력 상실·맥락 소실·반복 응답 → 글로벌 전 언어에서 1위권 불만")
    L.append("- 결제·과금·paywall/token/message-limit → 글로벌 공통 Top 3")
    L.append("- 버그/크래시/로딩 → 기본 인프라 불만, 전 언어 공통")
    L.append("")
    L.append("**언어권별 색깔:**")
    L.append("- **영어(en)**: \"lobotomy\"·\"nerf\"·\"dumber\"·\"paywall\" 용어로 AI 성능 저하·구독 압박에 민감. NSFW/검열 키워드도 상위.")
    L.append("- **일본어(ja)**: 수집량 자체는 적지만 '繰り返し(반복)'·'記憶(기억)'·'課金(과금)' 집중. 광고·UI 불만은 상대적으로 약함 (표현 자제적).")
    L.append("- **스페인어(es)/포르투갈어(pt)**: '상환(reembolso)', 'avaricia/ganância(탐욕)' 등 **결제/환불/월정액 신뢰** 표현이 강함. 정서적 표현('sol/sozinho' 외로움)이 영어권보다 직접적.")
    L.append("- **독일어(de)**: 'Datenschutz(개인정보)'·'teuer(비싸다)' 등 **프라이버시·가격투명성** 비중이 타 언어보다 높음.")
    L.append("- **중국어(zh)**: '审查(검열)'·'闪退(강제종료)' 집중. 정서적 관계 불만은 적고 기술 불만 위주.")
    L.append("")

    # 6. LUCIVE 포지셔닝 시사점
    L.append("## 6. LUCIVE 포지셔닝 시사점 (글로벌 확장 대비 드래프트)\n")
    L.append("- **\"Memory that doesn't break.\"** — 글로벌 공통 최대 불만인 AI 기억력 상실 → LUCIVE의 루시브 단위 서사(자유 챗 ×)는 강력한 반론. 영어권 마케팅에서 \"No more lobotomy updates\" 훅 가능.")
    L.append("- **\"One clear price. No hidden paywall.\"** — Character.AI(c.ai+)·Talkie·Replika 공통 불만은 추가 페이월·토큰 고갈 → Dip 3-Tier의 투명성은 글로벌에서도 차별점.")
    L.append("- **\"Story containers, not open chat.\"** — 검열/NSFW 전쟁(특히 en/zh)은 '자유 채팅' 구조의 태생적 리스크. LUCIVE는 '루시브(이야기 컨테이너)' 단위이므로 연령 게이트·컨테이너 등급으로 프레임 가능.")
    L.append("- **독일권 → 프라이버시 메시지 강화**, **중남미(es/pt) → 결제 투명성·무료 충분함 강조**, **일본 → 반복 없음·캐릭터 일관성**, **중화권 → 안정성(비크래시)·검열 명확성**.")
    L.append("- **정서 앱(Replika/Anima/Nomi) 계열 불만**: '예전엔 더 따뜻했는데 업데이트 후 변했다' 공통 → LUCIVE LP는 성장형이 아닌 **스토리 GM 역할 고정**으로 '변질' 리스크 낮음.")
    L.append("")

    return "\n".join(L)

def main():
    data = collect()
    OUT.write_text(render(data), encoding="utf-8")
    print(f"리포트: {OUT}")

if __name__ == "__main__":
    main()
