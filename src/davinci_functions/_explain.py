"""implementation of `explain` function."""

from __future__ import annotations

import textwrap
from collections.abc import Callable
from typing import Any

import dill  # type: ignore[import]
import openai


def explain(fn: Callable[..., Any]) -> str:
    """Describes the behavior of the given function.

    Args:
        fn: A callable. The corresponding source code must be associated to this object.
            i.e., inspect.getsource(fn) should work.

    Returns:
        The description of `fn` written by GPT.

    Example:
        >>> def my_function(x):
        ...     if x == 0:
        ...         return 1.0
        ...     else:
        ...         return math.sin(x) / x
        ...
        >>> f = davinci_functions.explain(my_function)
        'This function takes a single argument x and returns a float value. If x is ...
         0, it returns 1.0, otherwise it returns the result of the sine of x divided ...
         by x. This is known as the sinc function.'
    """
    src = dill.source.getsource(fn)
    base_prompt = textwrap.dedent(
        """\
        Describe the detailed behavior of the following Python function.
        The question may have multiple lines.
        It is written between "BEGIN_QUESTION" and "END_QUESTION".
        The answer is written after "ANSWER".
        The result may have multiple lines.
        It is recommended to write as detailed explanation as possible.
        If the algorithm written in the function has some contexts, describe it as well.
        For example, if the algorithm has a name, it should be written in the answer.

        BEGIN_QUESTION
        def sum(a, b):
            return a + b
        END_QUESTION

        ANSWER
        This function adds two variables a and b and returns its result.

        BEGIN_QUESTION
        {}
        END_QUESTION

        ANSWER
        """
    )

    return openai.Completion.create(  # type: ignore[no-any-return, no-untyped-call]
        model="text-davinci-003",
        prompt=base_prompt.format(src),
        max_tokens=2048,
        temperature=0,
    )["choices"][0]["text"]
