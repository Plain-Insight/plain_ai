# 🤖 Plain AI Project

> AI 기반 솔루션 개발을 위한 혁신적인 프로젝트

[![GitHub Issues](https://img.shields.io/github/issues/Plain-Insight/plain_ai)](https://github.com/Plain-Insight/plain_ai/issues)
[![GitHub Stars](https://img.shields.io/github/stars/Plain-Insight/plain_ai)](https://github.com/Plain-Insight/plain_ai/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 프로젝트 개요

Plain AI는 인공지능 기반의 다양한 솔루션을 개발하는 프로젝트입니다. 체계적인 Git 워크플로우와 자동화된 CI/CD 파이프라인을 통해 안정적이고 효율적인 개발 환경을 제공합니다.

### 🎯 주요 목표
- 🚀 **혁신적인 AI 솔루션 개발**
- 🔧 **체계적인 개발 워크플로우 구축**
- 🤝 **효율적인 팀 협업 환경 조성**
- 📚 **지속적인 학습과 개선**

## ⚡ 빠른 시작

### 📦 필수 요구사항
- **Python 3.9+**
- **Git**
- **GitHub CLI** (선택사항)

### 🚀 설치 방법

1. **저장소 클론**
```bash
git clone https://github.com/Plain-Insight/plain_ai.git
cd plain_ai
```

2. **가상환경 생성** (권장)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows
```

3. **의존성 설치**
```bash
pip install -r requirements.txt
```

4. **개발 도구 설치**
```bash
pip install black isort flake8 pytest
```

## 🔧 사용법

### 기본 실행
```bash
python main.py
```

### 개발 모드 실행
```bash
python main.py --dev
```

### 테스트 실행
```bash
pytest tests/
```

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

### 2. 브랜치 전략
- **main**: 프로덕션 브랜치 (안정적인 코드)
- **develop**: 개발 통합 브랜치 (기본 브랜치)
- **feat/숫자**: 새 기능 개발 브랜치
- **bug/숫자**: 버그 수정 브랜치
- **docs/숫자**: 문서 작업 브랜치

## 👨‍💻 새로운 개발자를 위한 완전 가이드

### 🚀 첫 기여를 위한 단계별 가이드

#### 1. 환경 준비 (최초 1회만)

```bash
# 1. 저장소 포크 (GitHub 웹에서)
# https://github.com/Plain-Insight/plain_ai 에서 "Fork" 버튼 클릭

# 2. 포크한 저장소 클론
git clone https://github.com/your-username/plain_ai.git
cd plain_ai

# 3. 원본 저장소를 upstream으로 추가
git remote add upstream https://github.com/Plain-Insight/plain_ai.git

# 4. GitHub CLI 설치 및 로그인 (선택사항이지만 권장)
# Windows: winget install --id GitHub.cli
# Mac: brew install gh
# Linux: apt install gh
gh auth login

# 5. 개발 도구 설치
pip install black isort flake8 pytest
```

#### 2. 이슈 기반 개발 워크플로우 실습

**🎯 예시: "사용자 로그인 기능" 개발하기**

```bash
# Step 1: 최신 코드 동기화
git checkout develop
git pull upstream develop

# Step 2: GitHub에서 이슈 생성
gh issue create \
  --title "[FEATURE] 사용자 로그인 기능 구현" \
  --body "# ✨ 개요
사용자 인증을 위한 로그인 시스템을 구현합니다.

## 💡 상세 기능 내용

### 📝 기능 설명
- [ ] JWT 토큰 기반 인증 시스템
- [ ] 로그인/로그아웃 API 엔드포인트
- [ ] 사용자 세션 관리

### 📝 사용자 시나리오
- [ ] 1. 사용자가 로그인 페이지 접속
- [ ] 2. 이메일/비밀번호 입력
- [ ] 3. 인증 성공 시 대시보드 이동" \
  --label "enhancement"

# 출력 예시: https://github.com/Plain-Insight/plain_ai/issues/5
# 이슈 번호를 확인하세요! (예: #5)
```

```bash
# Step 3: 이슈 번호에 맞는 브랜치 생성
git checkout -b feat/5  # 이슈 번호 사용

# Step 4: 개발 작업 수행
# 파일 생성, 코드 작성...
echo "# 로그인 모듈" > src/auth.py
mkdir -p tests
echo "# 로그인 테스트" > tests/test_auth.py

# Step 5: 변경사항 커밋
git add .
git commit -m "[FEATURE] #5 사용자 로그인 기능 구현

- JWT 토큰 기반 인증 시스템 구축
- 로그인/로그아웃 API 엔드포인트 개발
- 사용자 세션 관리 기능 추가

Closes #5"

# Step 6: 브랜치 푸시
git push origin feat/5

# Step 7: Pull Request 생성
gh pr create \
  --title "[FEATURE] 사용자 로그인 기능 구현" \
  --body "## 개요
사용자 인증을 위한 로그인 시스템을 구현했습니다.

## 작업 상세 내용

### 🚀 새로 추가된 기능
1. **JWT 토큰 기반 인증**
   - 보안 토큰 생성 및 검증
   - 토큰 만료 시간 관리

2. **API 엔드포인트**
   - POST /auth/login - 로그인
   - POST /auth/logout - 로그아웃
   - GET /auth/me - 사용자 정보 조회

3. **세션 관리**
   - 사용자 상태 추적
   - 자동 로그아웃 기능

## 🧪 테스트
- [x] 단위 테스트 작성
- [x] 로그인 성공/실패 케이스 테스트
- [x] 토큰 검증 테스트

Closes #5" \
  --base develop
```

#### 3. 코드 리뷰 및 머지 과정

```bash
# PR 생성 후 일어나는 일들:

# 1. 🤖 자동 체크 실행
#    - 코드 품질 검사 (Black, isort, Flake8)
#    - 테스트 실행
#    - PR 제목 및 브랜치명 검증

# 2. 🏷️ 자동 라벨 추가
#    - 파일 유형별 라벨 (python, javascript 등)
#    - 변경 크기별 라벨 (small-change, large-change 등)

# 3. 👥 코드 리뷰 요청
#    - 팀원들이 코드 리뷰 진행
#    - 피드백 반영 및 수정

# 4. ✅ 승인 후 머지
#    - 모든 체크 통과 시 develop 브랜치로 머지
#    - 이슈 #5 자동 닫힘
```

#### 4. 머지 후 정리 작업

```bash
# 1. 최신 develop 브랜치 받기
git checkout develop
git pull upstream develop

# 2. 완료된 브랜치 삭제
git branch -d feat/5           # 로컬 브랜치 삭제
git push origin --delete feat/5 # 원격 브랜치 삭제

# 3. 다음 작업 준비
git checkout -b feat/6  # 새로운 이슈를 위한 브랜치
```

### 📋 자주 사용하는 명령어 치트시트

```bash
# 🔍 상태 확인
git status                    # 현재 상태
git branch -a                 # 모든 브랜치 확인
gh issue list                 # 이슈 목록
gh pr list                    # PR 목록

# 🌿 브랜치 관리
git checkout develop          # develop 브랜치로 이동
git pull upstream develop     # 최신 코드 받기
git checkout -b feat/N        # 새 기능 브랜치 생성

# 📝 이슈 및 PR 관리
gh issue create --title "[TYPE] 제목" --body "내용" --label "라벨"
gh pr create --title "제목" --body "내용\n\nCloses #N" --base develop
gh issue view N               # 이슈 상세 보기
gh pr view N                  # PR 상세 보기

# 🧹 정리 작업
git branch --merged develop   # 머지된 브랜치 확인
git branch -d branch-name     # 로컬 브랜치 삭제
git remote prune origin       # 원격에서 삭제된 브랜치 정리
```

### 🎯 커밋 메시지 템플릿

```bash
# 기능 추가
[FEATURE] #이슈번호 간단한 설명

상세한 설명 (선택사항)
- 주요 변경사항 1
- 주요 변경사항 2

Closes #이슈번호

# 버그 수정
[BUG] #이슈번호 버그 설명

문제 상황 및 해결 방법 설명

Fixes #이슈번호

# 문서 작업
[DOCS] #이슈번호 문서 제목

추가/수정된 문서 내용 설명

Resolves #이슈번호
```

### ⚠️ 주의사항 및 팁

1. **브랜치 이름**: 반드시 `feat/이슈번호` 형태 사용
2. **커밋 메시지**: `[TYPE] #이슈번호` 형태로 시작
3. **이슈 연결**: PR 본문에 `Closes #이슈번호` 포함 필수
4. **코드 품질**: 커밋 전 `black .` 와 `flake8 .` 실행
5. **테스트**: 새 기능 추가 시 테스트 코드 작성 권장

### 🆘 문제 해결

```bash
# 실수로 잘못된 브랜치에서 작업한 경우
git stash                    # 현재 작업 임시 저장
git checkout correct-branch  # 올바른 브랜치로 이동
git stash pop               # 작업 내용 복원

# 커밋 메시지 수정하고 싶은 경우 (푸시 전)
git commit --amend -m "새로운 커밋 메시지"

# 원격 브랜치와 동기화 문제
git fetch upstream
git rebase upstream/develop

# 충돌 해결
git status                  # 충돌 파일 확인
# 충돌 파일 수정 후
git add .
git rebase --continue
```

## 🤝 기여하기

1. **이슈 생성**: 버그 리포트나 기능 요청
2. **포크**: 저장소를 자신의 계정으로 포크
3. **브랜치 생성**: `git checkout -b feat/amazing-feature`
4. **커밋**: `git commit -m '[FEATURE] Add amazing feature'`
5. **푸시**: `git push origin feat/amazing-feature`
6. **PR 생성**: Pull Request 생성 및 리뷰 요청

### 📝 커밋 규칙
- `[FEATURE] #이슈번호 새 기능 추가`
- `[BUG] #이슈번호 버그 수정`
- `[DOCS] #이슈번호 문서 업데이트`
- `[REFACTOR] #이슈번호 코드 리팩터링`

## 📁 프로젝트 구조

```
plain_ai/
├── .github/                    # GitHub 설정
│   ├── workflows/             # CI/CD 파이프라인
│   ├── ISSUE_TEMPLATE/        # 이슈 템플릿
│   └── pull_request_template.md
├── src/                       # 소스 코드 (예정)
├── tests/                     # 테스트 코드 (예정)
├── docs/                      # 문서
│   ├── git-workflow.md        # Git 워크플로우 가이드
│   └── planned-issues.md      # 이슈 계획
├── requirements.txt           # 의존성 (예정)
├── .gitignore                # Git 무시 파일
└── README.md                 # 프로젝트 설명
```

## 🛠️ 기술 스택

### 백엔드
- **Python 3.9+**
- **FastAPI/Flask** (예정)
- **SQLAlchemy** (예정)

### AI/ML
- **TensorFlow/PyTorch** (예정)
- **Hugging Face Transformers** (예정)
- **scikit-learn** (예정)

### 개발 도구
- **GitHub Actions** (CI/CD)
- **Black** (코드 포맷팅)
- **pytest** (테스트)
- **Docker** (예정)

## 📞 문의 및 지원

- **이슈**: [GitHub Issues](https://github.com/Plain-Insight/plain_ai/issues)
- **토론**: [GitHub Discussions](https://github.com/Plain-Insight/plain_ai/discussions)
- **이메일**: contact@plain-insight.com (예정)

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

⭐ **이 프로젝트가 도움이 되셨다면 별표를 눌러주세요!**

**Made with ❤️ by Plain-Insight Team**