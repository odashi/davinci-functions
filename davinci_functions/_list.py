"""implementation of `list` function."""

import ast
import openai
import textwrap
from typing import Any


def list(prompt: str) -> list[Any]:
    """Obtains a list of something from GPT-3.

    Args:
        prompt: The prompt describing the values.
            Users basically don't need to write a complete prompt to describe the task
            that the GPT-3 solves.
    
    Returns:
        A list of something you described in the prompt.
        Since this is the result of an LLM, the value may not be correct in many cases.
    
    Raises:
        RuntimeError: Something went wrong.
    """

    base_prompt=textwrap.dedent(
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
        ["apple", "alphabet", "ancle", "ant", "art"]

        QUESTION:
        {}

        ANSWER:
        """
    )

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=base_prompt.format(prompt),
            max_tokens=1024,
            temperature=0,
        )

        answer = response["choices"][0]["text"]
        return ast.literal_eval(answer)
    except Exception as e:
        raise RuntimeError("Something went wrong.") from e
