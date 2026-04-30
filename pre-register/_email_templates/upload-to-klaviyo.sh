#!/usr/bin/env bash
# Klaviyo Templates API 업로더
# ────────────────────────────────────────────────────────────────
# 사용법:
#   ./upload-to-klaviyo.sh "Welcome — Pre-register" 01-welcome.html
#
# 사전 조건:
#   - 프로젝트 루트(/)에 .env 파일 존재 + KLAVIYO_PRIVATE_KEY=pk_xxx 정의
#   - jq 설치 (HTML 을 JSON 안전하게 escape 하기 위함)
#       Mac:    brew install jq
#       Ubuntu: sudo apt install jq
#       Windows (Git Bash): https://stedolan.github.io/jq/download/
#
# 출력:
#   생성된 template id 가 콘솔에 찍힘. Klaviyo → Content → Templates
#   에 동일 이름으로 즉시 표시됨.

set -euo pipefail

NAME="${1:-}"
HTML_FILE="${2:-}"

if [[ -z "$NAME" || -z "$HTML_FILE" ]]; then
  echo "Usage: $0 \"Template Name\" path/to/template.html"
  exit 1
fi

if [[ ! -f "$HTML_FILE" ]]; then
  echo "Error: HTML file not found: $HTML_FILE"
  exit 1
fi

# .env 로드 (스크립트 위치 기준 두 단계 위 = lucive-promo/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${SCRIPT_DIR}/../../.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Error: .env not found at $ENV_FILE"
  echo "Create .env with: KLAVIYO_PRIVATE_KEY=pk_xxxxx"
  exit 1
fi

# .env 의 KLAVIYO_PRIVATE_KEY 만 읽기 (다른 변수 무시)
KLAVIYO_PRIVATE_KEY=$(grep -E '^KLAVIYO_PRIVATE_KEY=' "$ENV_FILE" | cut -d '=' -f2- | tr -d '"' | tr -d "'" | tr -d '\r')

if [[ -z "$KLAVIYO_PRIVATE_KEY" ]]; then
  echo "Error: KLAVIYO_PRIVATE_KEY not set in .env"
  exit 1
fi

# HTML 을 JSON-safe 문자열로 변환
HTML_JSON=$(jq -Rs . < "$HTML_FILE")

# 임시 페이로드 파일 (큰 HTML 을 -d 인자로 직접 못 넘기는 환경 대비)
PAYLOAD_FILE=$(mktemp)
trap 'rm -f "$PAYLOAD_FILE"' EXIT

cat > "$PAYLOAD_FILE" <<EOF
{
  "data": {
    "type": "template",
    "attributes": {
      "name": "$NAME",
      "editor_type": "CODE",
      "html": $HTML_JSON
    }
  }
}
EOF

echo "▸ Uploading '$NAME' to Klaviyo..."

RESPONSE=$(curl -sS -w "\nHTTP_STATUS:%{http_code}" \
  -X POST "https://a.klaviyo.com/api/templates/" \
  -H "accept: application/vnd.api+json" \
  -H "revision: 2024-10-15" \
  -H "content-type: application/vnd.api+json" \
  -H "Authorization: Klaviyo-API-Key $KLAVIYO_PRIVATE_KEY" \
  --data-binary "@$PAYLOAD_FILE")

HTTP_STATUS=$(echo "$RESPONSE" | grep -oE 'HTTP_STATUS:[0-9]+' | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '$d')

if [[ "$HTTP_STATUS" =~ ^2 ]]; then
  TEMPLATE_ID=$(echo "$BODY" | jq -r '.data.id // empty')
  echo "✓ Created (HTTP $HTTP_STATUS)"
  echo "  Template ID: $TEMPLATE_ID"
  echo "  Klaviyo → Content → Templates 에서 \"$NAME\" 확인"
  echo ""
  echo "  Flow 에 연결: Flows → 해당 Flow → Email action → Use existing template → 위 ID 선택"
else
  echo "✗ Failed (HTTP $HTTP_STATUS)"
  echo "$BODY" | jq . 2>/dev/null || echo "$BODY"
  exit 1
fi
