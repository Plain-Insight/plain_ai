## 🌿 개발 워크플로우

### 1. 새 기능 개발
```bash
# 최신 develop 브랜치 받기
git checkout develop
git pull origin develop

# 새 이슈 생성 (GitHub CLI)
gh issue create --title "[FEATURE] 기능명" --body "설명" --label "enhancement"

# 기능 브랜치 생성 (이슈 번호 사용)
git checkout -b feat/이슈번호

# 개발 작업...
git add .
git commit -m "[FEATURE] #이슈번호 기능 구현"

# 브랜치 푸시 및 PR 생성
git push origin feat/이슈번호
gh pr create --title "[FEATURE] 기능명" --body "설명\n\nCloses #이슈번호" --base develop
```