# 📦 패키지 빌드를 위한 build 모듈 설치 (처음 한 번만)  
pip install build                           # 'python -m build' 명령을 사용하기 위한 모듈 설치

# 📚 프로젝트의 의존 패키지 설치
pip install -r requirements.txt             # requirements.txt 기반 의존성 설치

# 🛠 현재 프로젝트 디렉토리에서 빌드 실행
python -m build                             # pyproject.toml 설정을 기반으로 dist/*.whl, *.tar.gz 생성

# 📁 빌드 결과 확인 (dist 폴더 내 파일 목록 출력)
ls dist/                                    # 빌드 후 생성된 파일들 확인 (.whl, .tar.gz 등)
<!-- 
# 🧪 로컬 테스트용으로 설치 (wheel 파일 사용)
pip install dist/hello-0.1.0-py3-none-any.whl  # 로컬 패키지 설치

# 📍 설치된 hello 패키지 경로 확인
pip show hello                              # Location 필드에서 설치된 경로 확인 가능

# ✅ 설치 확인 및 코드 실행 테스트 (빌드된 패키지를 통해 main.py 직접 실행)
python -m hello.main > output.txt  # 패키지 설치 후 hello.main 모듈을 실행, 결과를 output.txt로 저장

# 📄 결과 확인
cat output.txt  # 출력: Hello from the hello package! -->



완벽하게 이해했어! 정확히 이렇게 정리할 수 있어:

⸻

✅ Java vs Python 실행 구조 비교

 Outer pipes  Cell padding 
No sorting
| 항목          | Java (JAR)                         | Python (wheel)                            |
| ----------- | ---------------------------------- | ----------------------------------------- |
| 🎯 실행 대상    | .jar 자체 실행 가능 (java -jar app.jar)  | .whl 자체는 실행 불가                            |
| 🔧 진입점 설정   | MANIFEST.MF의 Main-Class로 main() 지정 | 실행 불가 → 설치 후 python -m 또는 entry_points 필요 |
| 🧩 실행 조건    | Java Runtime만 있으면 됨                | Python 환경 + 설치 필요                         |
| 💡 설치 vs 실행 | 설치 없이도 실행 가능                       | 설치 후에만 실행 가능 (pip install)        