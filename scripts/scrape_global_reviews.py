"""
해외 캐릭터챗/AI 롤플레이 앱 Play Store 리뷰 수집 (다국어).
각 앱 × 각 locale × (1★, 2★) × 최대 N건.
"""
import json, time
from pathlib import Path
from google_play_scraper import reviews, Sort, app as app_info

APPS = {
    # Tier A — 직접 경쟁
    "character_ai":  {"id": "ai.character.app",                    "name": "Character.AI"},
    "talkie":        {"id": "com.weaver.app.prod",                 "name": "Talkie (Weaver)"},
    "replika":       {"id": "ai.replika.app",                      "name": "Replika"},
    "ai_dungeon":    {"id": "com.aidungeon",                       "name": "AI Dungeon"},
    # Tier B — 가설 검증
    "polybuzz":      {"id": "ai.socialapps.speakmaster",           "name": "PolyBuzz (Poly.AI)"},
    "linky":         {"id": "com.aigc.ushow.ichat",                "name": "Linky AI"},
    "chai":          {"id": "com.Beauchamp.Messenger.external",    "name": "Chai"},
    "crushon":       {"id": "com.aiperfectbuddy.chat",             "name": "CrushOn.AI"},
    "spicychat":     {"id": "com.passiohk.ai.spicychat",           "name": "SpicyChat AI"},
    "joyland":       {"id": "com.grefert.joy",                     "name": "Joyland AI"},
    # Tier C — 참고
    "kindroid":      {"id": "com.kindroid.app",                    "name": "Kindroid"},
    "nomi":          {"id": "ai.nomi.twa",                         "name": "Nomi.ai"},
    "anima":         {"id": "anima.virtual.ai.robot.friend",       "name": "Anima"},
    "dippy":         {"id": "com.tryimpel.dippy",                  "name": "Dippy.ai"},
    "paradot":       {"id": "com.withfeeling.ai.test",             "name": "Paradot"},
}

LOCALES = [
    # (lang, country, label)
    ("en", "us", "en"),
    ("ja", "jp", "ja"),
    ("es", "es", "es"),
    ("pt", "br", "pt"),
    ("de", "de", "de"),
    ("zh", "tw", "zh"),
]

COUNT_PER_STAR = 100

OUT = Path(__file__).resolve().parent.parent / "output" / "reviews_global"
OUT.mkdir(parents=True, exist_ok=True)

def simplify(r):
    return {
        "score": r.get("score"),
        "at": r.get("at").isoformat() if r.get("at") else None,
        "thumbsUp": r.get("thumbsUpCount"),
        "content": r.get("content"),
    }

summary = []

for key, meta in APPS.items():
    print(f"\n=== {meta['name']} ({meta['id']}) ===")
    # 메타 (en 기준)
    try:
        info = app_info(meta["id"], lang="en", country="us")
        meta_out = {
            "id": meta["id"],
            "title": info.get("title"),
            "score": info.get("score"),
            "ratings": info.get("ratings"),
            "reviews": info.get("reviews"),
            "installs": info.get("installs"),
            "histogram": info.get("histogram"),
        }
        (OUT / f"{key}_meta.json").write_text(json.dumps(meta_out, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(f"  ★{meta_out.get('score')} / reviews: {meta_out.get('reviews')} / hist: {meta_out.get('histogram')}")
    except Exception as e:
        print(f"  meta fail: {e}")
        continue

    per_app = {"app": key, "name": meta["name"], "locales": {}}
    for lang, country, label in LOCALES:
        per_locale = {}
        for score in (1, 2):
            try:
                rs, _ = reviews(
                    meta["id"], lang=lang, country=country,
                    sort=Sort.NEWEST, count=COUNT_PER_STAR,
                    filter_score_with=score,
                )
                simplified = [simplify(r) for r in rs]
                out_path = OUT / f"{key}_{label}_{score}star.json"
                out_path.write_text(json.dumps(simplified, ensure_ascii=False, indent=2), encoding="utf-8")
                per_locale[f"{score}star"] = len(simplified)
                print(f"  [{label}] {score}★: {len(simplified)}")
            except Exception as e:
                per_locale[f"{score}star"] = f"err:{e}"
                print(f"  [{label}] {score}★ err: {e}")
            time.sleep(0.3)
        per_app["locales"][label] = per_locale
    summary.append(per_app)

(OUT / "_collection_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print("\n수집 완료.")
