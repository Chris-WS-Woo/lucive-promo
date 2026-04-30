#!/usr/bin/env python3
"""
Klaviyo Templates API 업로더 (Python · Windows/Mac/Linux 모두 OK).

사용법:
    python upload-to-klaviyo.py "Welcome — Pre-register" 01-welcome.html

사전 조건:
    - 프로젝트 루트(/)에 .env 파일에 KLAVIYO_PRIVATE_KEY=pk_xxx 정의
    - Python 3.7+ (표준 라이브러리만 사용, 추가 설치 불필요)

출력:
    생성된 template id 콘솔 출력. Klaviyo → Content → Templates 에 즉시 표시.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


def load_private_key():
    """프로젝트 루트의 .env 에서 KLAVIYO_PRIVATE_KEY 읽기."""
    script_dir = Path(__file__).resolve().parent
    # _email_templates -> pre-register -> lucive-promo (root)
    env_file = script_dir.parent.parent / ".env"
    if not env_file.exists():
        sys.exit(f"Error: .env not found at {env_file}\n"
                 "Create .env with: KLAVIYO_PRIVATE_KEY=pk_xxxxx")

    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("KLAVIYO_PRIVATE_KEY="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if value:
                return value
    sys.exit("Error: KLAVIYO_PRIVATE_KEY not set in .env")


def upload_template(name: str, html_path: Path, private_key: str):
    html = html_path.read_text(encoding="utf-8")

    payload = {
        "data": {
            "type": "template",
            "attributes": {
                "name": name,
                "editor_type": "CODE",
                "html": html,
            }
        }
    }

    req = urllib.request.Request(
        "https://a.klaviyo.com/api/templates/",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "accept": "application/vnd.api+json",
            "revision": "2024-10-15",
            "content-type": "application/vnd.api+json",
            "Authorization": f"Klaviyo-API-Key {private_key}",
        },
        method="POST",
    )

    print(f"▸ Uploading '{name}' to Klaviyo...")

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            data = json.loads(body)
            template_id = data.get("data", {}).get("id", "")
            print(f"✓ Created (HTTP {resp.status})")
            print(f"  Template ID: {template_id}")
            print(f'  Klaviyo → Content → Templates 에서 "{name}" 확인')
            print()
            print("  Flow 에 연결: Flows → 해당 Flow → Email action → "
                  "Use existing template → 위 ID 선택")
    except urllib.error.HTTPError as e:
        print(f"✗ Failed (HTTP {e.code})")
        try:
            err_body = e.read().decode("utf-8")
            err_json = json.loads(err_body)
            print(json.dumps(err_json, ensure_ascii=False, indent=2))
        except Exception:
            print(err_body)
        sys.exit(1)
    except urllib.error.URLError as e:
        sys.exit(f"✗ Network error: {e.reason}")


def main():
    if len(sys.argv) != 3:
        print('Usage: python upload-to-klaviyo.py "Template Name" path/to/template.html')
        sys.exit(1)

    name = sys.argv[1]
    html_path = Path(sys.argv[2])

    if not html_path.exists():
        sys.exit(f"Error: HTML file not found: {html_path}")

    private_key = load_private_key()
    upload_template(name, html_path, private_key)


if __name__ == "__main__":
    main()
