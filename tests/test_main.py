from hello.main import say_hello

def test_say_hello_output(capsys):
    # 함수 실행
    say_hello()
    # 출력 캡처
    captured = capsys.readouterr()
    # 기대값 검증
    assert captured.out.strip() == "Hello from the hello package!"


