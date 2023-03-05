"""Package definition."""

from __future__ import annotations

try:
    from davinci_functions import _version

    __version__ = _version.__version__
except Exception:
    __version__ = ""

from davinci_functions._function import function
from davinci_functions._judge import judge
from davinci_functions._list import list

__all__ = [
    "function",
    "judge",
    "list",
]
