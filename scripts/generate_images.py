"""
Lucive 홍보 이미지 생성 스크립트
- Nanobanana (Gemini) API로 키비주얼 이미지 생성
"""

import os
import base64
import requests
import json
from pathlib import Path

# 환경변수 로드
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OUTPUT_DIR = Path(__file__).parent.parent / "assets" / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Gemini API 엔드포인트 (이미지 생성)
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/nano-banana-pro-preview:generateContent?key={GEMINI_API_KEY}"


def generate_image(prompt: str, filename: str):
    """Gemini API로 이미지 생성"""
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Generate an image: {prompt}"
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
        }
    }

    headers = {"Content-Type": "application/json"}

    print(f"\n[생성 중] {filename}...")
    print(f"  프롬프트: {prompt[:80]}...")

    try:
        resp = requests.post(GEMINI_URL, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()
        data = resp.json()

        # 응답에서 이미지 추출
        for candidate in data.get("candidates", []):
            for part in candidate.get("content", {}).get("parts", []):
                if "inlineData" in part:
                    img_data = base64.b64decode(part["inlineData"]["data"])
                    mime = part["inlineData"]["mimeType"]
                    ext = "png" if "png" in mime else "jpg"
                    filepath = OUTPUT_DIR / f"{filename}.{ext}"
                    filepath.write_bytes(img_data)
                    print(f"  [완료] {filepath}")
                    return str(filepath)

        # 이미지가 없으면 텍스트 응답 출력
        for candidate in data.get("candidates", []):
            for part in candidate.get("content", {}).get("parts", []):
                if "text" in part:
                    print(f"  [텍스트 응답] {part['text'][:200]}")

        print(f"  [실패] 이미지가 생성되지 않았습니다.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"  [에러] {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"  [응답] {e.response.text[:500]}")
        return None


# === 홍보 이미지 5종 프롬프트 ===

IMAGES = [
    {
        "filename": "01_teaser_dive",
        "prompt": (
            "Dark ocean abyss background with two diverging paths of glowing cyan light (#06B6D4), "
            "mysterious deep underwater atmosphere, cinematic lighting, mobile app promotional art style, "
            "the word 'DIVE' at the bottom center with soft ethereal glow effect, "
            "dark navy blue (#0a1628) background gradient, floating light particles, "
            "ethereal and immersive mood, ultra high quality, 16:9 aspect ratio"
        )
    },
    {
        "filename": "02_lp_companions",
        "prompt": (
            "Three anime-style AI android characters displayed as collectible cards side by side, "
            "first character: warm gentle female with soft golden accents, "
            "second character: cool strategic male with silver-blue tones, "
            "third character: creative expressive non-binary with purple-pink highlights, "
            "all have subtle cyan (#06B6D4) glowing circuit patterns on skin, "
            "dark ocean background (#0a1628), floating holographic card frames, "
            "mobile game character selection screen style, high quality digital illustration, "
            "mysterious yet inviting atmosphere, 4:5 portrait aspect ratio"
        )
    },
    {
        "filename": "03_lmaker_creation",
        "prompt": (
            "Futuristic holographic UI interface showing a story creation tool, "
            "floating genre selection buttons (Romance, Sci-Fi, Thriller, Fantasy) in glowing cyan (#06B6D4), "
            "a central AI brain icon generating story nodes connected by light lines, "
            "dark navy background (#0a1628), magical creation atmosphere, "
            "text 'L-Maker' in sleek futuristic font at top, "
            "sparkle and particle effects around the creation process, "
            "mobile app UI style, clean modern design, 1:1 square aspect ratio"
        )
    },
    {
        "filename": "04_dive_experience",
        "prompt": (
            "First-person POV entering a glowing portal into a story world, "
            "cyberpunk city visible through the portal with neon lights and rain, "
            "chat message bubbles floating in the foreground showing story choices, "
            "a translucent AI companion silhouette beside the viewer, "
            "cyan (#06B6D4) and deep navy (#0a1628) color palette, "
            "cinematic immersive atmosphere, sense of adventure and mystery, "
            "mobile game promotional art, 9:16 vertical aspect ratio"
        )
    },
    {
        "filename": "05_share_ranking",
        "prompt": (
            "Mobile app screenshot style showing a social ranking leaderboard, "
            "dark navy background (#0a1628), three ranking cards: "
            "#1 with gold badge and glow, #2 with silver badge, #3 with bronze badge, "
            "each card shows a small story thumbnail, username, view count and like count, "
            "cyan (#06B6D4) accent lines and highlights, "
            "header text 'Weekly Top Dives', clean modern mobile UI design, "
            "polished app store screenshot style, iPhone frame, 1:1 aspect ratio"
        )
    },
]


def main():
    print("=" * 60)
    print("Lucive 홍보 이미지 생성 시작")
    print(f"출력 폴더: {OUTPUT_DIR}")
    print("=" * 60)

    if not GEMINI_API_KEY:
        print("[에러] GEMINI_API_KEY가 설정되지 않았습니다.")
        return

    results = []
    for img in IMAGES:
        result = generate_image(img["prompt"], img["filename"])
        results.append((img["filename"], result))

    print("\n" + "=" * 60)
    print("생성 결과 요약")
    print("=" * 60)
    for name, path in results:
        status = "성공" if path else "실패"
        print(f"  [{status}] {name}")


if __name__ == "__main__":
    main()
