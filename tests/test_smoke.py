from importlib.metadata import version

import pytest

from mini_agent import main


def test_main_prints_greeting(capsys) -> None:
    main([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from mini-agent!"
    assert captured.err == ""


def test_version_flag_prints_package_version(capsys) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])

    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == f"mini-agent {version('mini-agent')}"
