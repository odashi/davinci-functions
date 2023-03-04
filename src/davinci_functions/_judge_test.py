"""Tests for davinci_functions._judge."""

from __future__ import annotations

import pytest
import pytest_mock

from davinci_functions._judge import judge


def test_judge_true(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "True"}]},
    )

    assert judge("This is a test.") is True


def test_judge_false(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "False"}]},
    )

    assert judge("This is a test.") is False


def test_judge_non_python(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "Error."}]},
    )

    with pytest.raises(SyntaxError, match=r"^GPT didn't return a Python literal"):
        judge("This is a test.")


def test_judge_non_bool(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "[1, 2, 3]"}]},
    )

    with pytest.raises(TypeError, match=r"^GPT didn't return a Python Boolean"):
        judge("This is a test.")
