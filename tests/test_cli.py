from __future__ import annotations

import pytest

from clubtool.config import load_settings


def test_load_settings_requires_message(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CLUBTOOL_MESSAGE", raising=False)
    with pytest.raises(RuntimeError) as excinfo:
        load_settings()
    assert "CLUBTOOL_MESSAGE" in str(excinfo.value)


def test_load_settings_reads_message(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CLUBTOOL_MESSAGE", "hello")
    monkeypatch.setenv("CLUBTOOL_LOG_LEVEL", "INFO")
    settings = load_settings()
    assert settings.message == "hello"
    assert settings.log_level == "INFO"
    