"""implementation of `function` function."""

from __future__ import annotations

import textwrap
from collections.abc import Callable
from typing import Any

import openai


def function(prompt: str) -> Callable[..., Any]:
    """Synthesizes a function by asking GPT to write it.

    This function is not secure as it calls `exec` internally.
    Please don't use this function in the real product.

    Args:
        prompt: The prompt describing the behavior of the function.
            Users basically don't need to write a complete prompt to describe the task
            that the GPT solves.

    Returns:
        A callable object that may represent the behavior of the prompt.

    Raises:
        SyntaxError: GPT didn't return a meaningful Python program.
        TypeError: GPT didn't return a Python callable.

    Example:
        >>> f = davinci_functions.list("Multiply the argument x by 2.")
        >>> f(3)
        6
    """

    base_prompt = textwrap.dedent(
        """\
        Write a single Python function that processes the following task.
        You must output only a single function definition in Python.
        You must not output examples, description, remarks,
        or anything else that are not related to the function itself.
        The name of the function must be "func".
        The function must have positional arguments if it is specified in the question.
        The function may return some values if necessary.

        QUESTION:
        The sum of two integer arguments x and y.

        ANSWER:
        def func(x, y):
            return x + y

        QUESTION:
        {}

        ANSWER:
        """
    )

    response = openai.Completion.create(  # type: ignore[no-untyped-call]
        model="text-davinci-003",
        prompt=base_prompt.format(prompt),
        max_tokens=2048,
        temperature=0,
    )
    src = response["choices"][0]["text"]

    try:
        locals: dict[str, Any] = {}
        exec(src, globals(), locals)
        func = locals["func"]
    except SyntaxError:
        raise SyntaxError(f"GPT didn't return a meaningful Python program. {src=}")

    if not callable(func):
        raise TypeError(f"GPT didn't return a Python Callable. {src=}")

    return func  # type: ignore[no-any-return]
