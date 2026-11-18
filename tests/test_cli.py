"""Tests for the command-line parser contract."""

import pytest

from mini_agent import build_parser, main


def test_parser_metadata() -> None:
    parser = build_parser()
    assert parser.prog == "mini-agent"
    assert parser.description == "A minimal Python agent skeleton."


def test_help_exits_zero_and_lists_version_flag(capsys) -> None:
    with pytest.raises(SystemExit) as excinfo:
        build_parser().parse_args(["--help"])

    assert excinfo.value.code == 0
    out = capsys.readouterr().out
    assert "usage: mini-agent" in out
    assert "--version" in out


def test_unknown_argument_exits_with_usage_error(capsys) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--does-not-exist"])

    assert excinfo.value.code == 2
    err = capsys.readouterr().err
    assert "unrecognized arguments" in err
