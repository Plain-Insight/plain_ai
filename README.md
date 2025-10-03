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

## 👨‍💻 이슈 기반 개발 워크플로우

### � 실제 사용 방법

```bash
# 1. GitHub CLI 로그인 (최초 1회)
gh auth login

# 2. 이슈 생성
gh issue create --title "[FEATURE] 기능명" --body "설명" --label "enhancement"
# 출력: https://github.com/Plain-Insight/plain_ai/issues/3

# 3. 브랜치 생성 (이슈 번호 사용)
git checkout develop
git pull origin develop
git checkout -b feat/3

# 4. 작업 후 커밋
git add .
git commit -m "[FEATURE] #3 기능 구현

상세 설명

Closes #3"

# 5. 푸시 및 PR 생성
git push origin feat/3
gh pr create --title "[FEATURE] 기능명" --body "설명\n\nCloses #3" --base develop
```

### 📝 커밋 메시지 규칙
- `[FEATURE] #이슈번호 기능명` - 새 기능
- `[BUG] #이슈번호 버그명` - 버그 수정  
- `[DOCS] #이슈번호 문서명` - 문서 작업

### 🔗 자동 연동
- 커밋에 `#이슈번호` 포함 → 이슈와 연결
- PR에 `Closes #이슈번호` 포함 → 머지 시 이슈 자동 닫힘

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