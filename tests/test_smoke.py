from mini_agent import main


def test_main_prints_greeting(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from mini-agent!"
    assert captured.err == ""
