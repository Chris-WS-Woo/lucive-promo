#!/bin/bash
# lucive-redesign 리포 업데이트 체크 스크립트
# 사용법: bash sync-check.sh

REPO_DIR="/c/Users/wonse/Downloads/lucive-redesign"

echo "=== Lucive Redesign 업데이트 체크 ==="
echo "시간: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

cd "$REPO_DIR" || { echo "리포 디렉토리를 찾을 수 없습니다"; exit 1; }

# 현재 커밋 저장
BEFORE=$(git rev-parse HEAD)

# 원격에서 fetch
git fetch origin 2>/dev/null

# 원격과 비교
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main 2>/dev/null || git rev-parse origin/master 2>/dev/null)

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "[UPDATE] 새로운 변경사항이 있습니다!"
    echo ""
    echo "--- 새 커밋 목록 ---"
    git log --oneline "$LOCAL".."$REMOTE"
    echo ""
    echo "--- 변경된 파일 ---"
    git diff --name-only "$LOCAL".."$REMOTE"
    echo ""
    echo "pull 하려면: cd $REPO_DIR && git pull"
else
    echo "[OK] 최신 상태입니다. (HEAD: ${LOCAL:0:8})"
fi
