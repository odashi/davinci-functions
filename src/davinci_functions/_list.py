"""implementation of `list` function."""

from __future__ import annotations

import ast
import builtins
import textwrap
from typing import Any

import openai


def list(prompt: str) -> builtins.list[Any]:
    """Obtains a list of something from GPT.

    Args:
        prompt: The prompt describing the values.
            Users basically don't need to write a complete prompt to describe the task
            that the GPT solves.

    Returns:
        A list of something you described in the prompt.
        Since this is the result of an LLM, the value may not be correct in many cases.

    Raises:
        SyntaxError: GPT didn't return a Python literal.
        TypeError: GPT didn't return a Python list.

    Example:
        >>> davinci_functions.list("5 random countries")
        ['Japan', 'Australia', 'Brazil', 'India', 'China']
    """

    base_prompt = textwrap.dedent(
        """\
        Complete the following task.
        You must write a single answer to follow the last question.
        Do not output anything else, including programs, description, and remarks.
        The output must be a Python list of literals.

        QUESTION:
        The first 5 positive integers.

        ANSWER:
        [1, 2, 3, 4, 5]

        QUESTION:
        List of 5 random English nouns starting with "a".

        ANSWER:
        ["apple", "alphabet", "ankle", "ant", "art"]

        QUESTION:
        {}

        ANSWER:
        """
    )

    response = openai.Completion.create(  # type: ignore[no-untyped-call]
        model="text-davinci-003",
        prompt=base_prompt.format(prompt),
        max_tokens=1024,
        temperature=0,
    )
    text = response["choices"][0]["text"]

    try:
        answer = ast.literal_eval(text)
    except SyntaxError:
        raise SyntaxError(f"GPT didn't return a Python literal. {text=}")

    if not isinstance(answer, builtins.list):
        raise TypeError(f"GPT didn't return a Python list. {text=}")

    return answer
