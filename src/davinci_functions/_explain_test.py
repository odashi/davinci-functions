"""Tests for davinci_functions._explain."""

from __future__ import annotations

import pytest_mock

from davinci_functions._explain import explain


def test_explain(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "This is a test."}]},
    )

    def dummy() -> int:
        return 42

    assert explain(dummy) == "This is a test."
