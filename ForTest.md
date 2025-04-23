## ✅ 테스트 실행을 위한 VS Code 설정 (상세 설명 포함)

### 🔧 1. `tasks.json`을 이용한 테스트 명령 정의

먼저 `.vscode/tasks.json` 파일을 생성하거나 수정하여, 현재 열려 있는 테스트 파일을 `pytest`로 실행하는 명령을 등록합니다.  
이렇게 하면 VS Code 내부에서 원하는 테스트 실행 명령을 태스크(Task)로 정의할 수 있습니다.

```json
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run tests in module",  // 태스크 이름 (키 바인딩에서도 이 이름으로 호출함)
      "type": "shell",
      "command": "pytest \"${file}\"",  // 현재 열려 있는 파일 경로를 인자로 전달
      "group": {
        "kind": "test",  // 테스트 작업 그룹으로 분류
        "isDefault": true  // 디폴트 테스트 작업으로 지정
      },
      "problemMatcher": []  // 오류 형식 분석 도구는 비워둠 (단순 실행용)
    }
  ]
}
```

### ⌨️ 2. 단축키를 이용한 테스트 실행

위에서 정의한 태스크를 빠르게 실행할 수 있도록 단축키를 등록합니다.  
이 설정은 사용자 단축키 파일(`keybindings.json`)에 작성됩니다.

#### 단축키 설정 방법:

1. `⌘(Command) + K`, 그 다음 `⌘ + S`를 눌러 키 바인딩 설정 화면을 엽니다.
2. 오른쪽 상단의 `{}` 아이콘을 눌러 `keybindings.json` 파일을 엽니다.
3. 아래 내용을 추가합니다:

```json
{
  "key": "shift+alt+cmd+t",
  "command": "workbench.action.tasks.runTask",
  "args": "Run tests in module"  // 위에서 정의한 태스크 이름과 일치해야 함
}
```

### ✅ 최종 결과

이제 VS Code에서 `Shift + ⌥ + ⌘ + T` 단축키를 누르면,
현재 열려 있는 테스트 파일이 자동으로 `pytest`를 통해 실행됩니다.

이 방식은 프로젝트 내에서 반복적으로 테스트를 실행할 때 매우 효율적이며,
테스트 파일을 열고 단축키만 누르면 결과를 바로 확인할 수 있어 개발 생산성이 높아집니다.
