"""Tests for davinci_functions._list."""

from __future__ import annotations

import pytest
import pytest_mock

from davinci_functions._list import list


def test_list_integers(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "[1, 2, 3]"}]},
    )

    assert list("This is a test.") == [1, 2, 3]


def test_list_strings(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "['foo', 'bar', 'baz']"}]},
    )

    assert list("This is a test.") == ["foo", "bar", "baz"]


def test_list_mixture(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "['foo', 123, True]"}]},
    )

    assert list("This is a test.") == ["foo", 123, True]


def test_list_non_python(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "Error."}]},
    )

    with pytest.raises(SyntaxError, match=r"^GPT didn't return a Python literal"):
        list("This is a test.")


def test_list_non_list(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch(
        "openai.Completion.create",
        return_value={"choices": [{"text": "True"}]},
    )

    with pytest.raises(TypeError, match=r"^GPT didn't return a Python list"):
        list("This is a test.")
