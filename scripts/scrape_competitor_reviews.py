"""
경쟁사(크랙, 제타) Play Store 리뷰 수집 — 1★/2★ 위주.

출력:
  output/reviews/<app>_1star.json
  output/reviews/<app>_2star.json
  output/reviews/<app>_meta.json
"""
import json
from pathlib import Path
from google_play_scraper import reviews, Sort, app as app_info

APPS = {
    "crack": {"id": "com.wrtn.character", "name": "크랙 (wrtn)"},
    "zeta":  {"id": "com.scatterlab.messenger", "name": "제타 (Scatter Lab)"},
}

OUT = Path(__file__).resolve().parent.parent / "output" / "reviews"
OUT.mkdir(parents=True, exist_ok=True)

TARGET_PER_RATING = 300  # 1★, 2★ 각각

def fetch(app_id: str, score: int, count: int):
    result, _ = reviews(
        app_id,
        lang="ko",
        country="kr",
        sort=Sort.NEWEST,
        count=count,
        filter_score_with=score,
    )
    return result

def simplify(r):
    return {
        "userName": r.get("userName"),
        "score": r.get("score"),
        "at": r.get("at").isoformat() if r.get("at") else None,
        "thumbsUp": r.get("thumbsUpCount"),
        "reviewCreatedVersion": r.get("reviewCreatedVersion"),
        "content": r.get("content"),
        "replyContent": r.get("replyContent"),
    }

for key, meta in APPS.items():
    print(f"\n=== {meta['name']} ({meta['id']}) ===")
    try:
        info = app_info(meta["id"], lang="ko", country="kr")
        meta_out = {
            "id": meta["id"],
            "title": info.get("title"),
            "score": info.get("score"),
            "ratings": info.get("ratings"),
            "reviews": info.get("reviews"),
            "installs": info.get("installs"),
            "updated": info.get("updated"),
            "histogram": info.get("histogram"),
        }
        print(f"  평점: {meta_out['score']:.2f} / 누적리뷰: {meta_out['reviews']:,} / 히스토그램: {meta_out['histogram']}")
        (OUT / f"{key}_meta.json").write_text(json.dumps(meta_out, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    except Exception as e:
        print(f"  meta 조회 실패: {e}")

    for score in (1, 2):
        try:
            rs = fetch(meta["id"], score, TARGET_PER_RATING)
            simplified = [simplify(r) for r in rs]
            out_path = OUT / f"{key}_{score}star.json"
            out_path.write_text(json.dumps(simplified, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  {score}★ 수집: {len(simplified)}건 → {out_path.name}")
        except Exception as e:
            print(f"  {score}★ 실패: {e}")

print("\n완료.")
