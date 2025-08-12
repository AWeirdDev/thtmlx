from typing import Union
from .core import AnyChild


def comment(*_: AnyChild, **__) -> None:
    """Creates a comment.

    Everything within `inner` is immediately ignored.

    This is useful for development, yet it's still recommended to use
    Python's built-in comments (`# like this`).
    """


def classes(*names: Union[str, bool, None]) -> str:
    """Creates the value used for the common `class` attribute.

    Args:
        *names: Class names. If false-like value is present, it's ignored.

    Example:

    ```python
    is_happy = False
    res = classes(
        "box",
        "colored",
        "happy" if is_happy else None
    )
    print(res)
    # "box colored"
    ```
    """
    res = " "

    for item in names:
        if item:
            res += f" {item}"

    return res.lstrip()


def styled():
    """Creates CSS styles."""
