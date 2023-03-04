"""implementation of `judge` function."""

from __future__ import annotations

import ast
import textwrap

import openai


def judge(prompt: str) -> bool:
    """Obtains a judgment of something from GPT.

    Args:
        prompt: The prompt describing the question.
            Users basically don't need to write a complete prompt to describe the task
            that the GPT solves.

    Returns:
        A Boolean representing the truth of the given prompt.
        Since this is the result of an LLM, the value may not be correct in many cases.

    Raises:
        RuntimeError: Something went wrong.

    Example:
        >>> davinci_functions.judge(
        ...     "San Francisco is the capital of the United States."
        ... )
        False
    """

    base_prompt = textwrap.dedent(
        """\
        Complete the following task.
        You must write a single answer to follow the last question.
        Do not output anything else, including programs, description, and remarks.
        The output must be a Boolean literal in Python: True or False.

        QUESTION:
        The sum of 2 and 3 is 5.

        ANSWER:
        True

        QUESTION:
        Antarctica is the largest continent in the world.

        ANSWER:
        False

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

    if not isinstance(answer, bool):
        raise TypeError(f"GPT didn't return a Python Boolean. {text=}")

    return answer
