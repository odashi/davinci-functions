"""Tests for davinci_functions._function."""

from __future__ import annotations

import pytest
import pytest_mock

from davinci_functions._function import function


def test_function(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "def func(x):\n    return x * 2"}]},
    )

    f = function("This is a test.")
    assert callable(f)
    assert f(3) == 6


def test_function_non_python(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "Error."}]},
    )

    with pytest.raises(SyntaxError, match=r"^GPT didn't return a meaningful Python"):
        function("This is a test.")


def test_function_non_function(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "func = 42"}]},
    )

    with pytest.raises(TypeError, match=r"^GPT didn't return a Python Callable"):
        function("This is a test.")
