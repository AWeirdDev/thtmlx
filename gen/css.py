import json
import rjsonc

from typing import Dict, List, Literal, Optional, TypeVar, Union
from typing_extensions import TypedDict


class Specification(TypedDict):
    type: Literal[
        "enum",
        "complex",
        "color",
        "length",
        "number",
        "integer",
        "string",
        "url",
        "time",
    ]
    description: Union[str, List[str]]
    values: Optional[List[str]]


T = TypeVar("T")


def definite(o: Optional[T], /) -> T:
    return o  # type: ignore


def clean(s: str, /) -> str:
    return s.replace("-", "_")


def generate():
    print("generate css")

    with open("gen/specs-css.jsonc", "rb") as f:
        SPECS: Dict[str, Specification] = rjsonc.loads(f.read())

    PY = []
    for key, spec in SPECS.items():
        print("*", key, "-", spec["type"])

        if spec["type"] == "enum":
            typ = (
                "Union[str, Literal["
                + ", ".join(json.dumps(item) for item in definite(spec["values"]))
                + "]]"
            )
        elif spec["type"] in ("complex", "color", "length", "string", "url", "time"):
            typ = "str"
        elif spec["type"] == "integer":
            typ = "int"
        else:
            typ = "Union[int, float]"

        desc = spec["description"]
        if isinstance(desc, str):
            docs = desc
        else:
            docs = ("\n        " * 2).join(desc)

        PY.append(
            f"""\
    def {clean(key)}(self, value: {typ}, /) -> "StructuredCss":
        \"\"\"{docs}

        *@generated*

        Args:
            value: The value. Expected `{spec['type']}`.
        \"\"\"
        self.k[{key!r}] = str(value)
        return self
    """
        )

    with open("thtmlx/_css.py", "w") as f:
        f.write(
            f"""# @ generated
from typing import Any, Dict, Literal, Optional, Union

class StructuredCss:
    \"\"\"Structured CSS.

    Functions have generated documentations for reference.
    \"\"\"

    __slots__ = ("k", )
    k: Dict[str, Any]

    def __init__(self, df: Optional[Dict[str, Any]] = None):
        self.k = {'df or {}'}
    
{'\n'.join(PY)}

    def extras(self, k: Dict[str, Any]):
        \"\"\"Add extra items to the CSS dictionary.
        
        Args:
            k (dict[str, Any]): The extra contents.
        \"\"\"
        self.k |= k

    def _inline_style(self) -> str:
        \"\"\"Create the inline style string.\"\"\"
        res = ""
        for k, v in self.k.items():
            res += k + ": " + v + ";"

        return res

    def __str__(self) -> str:
        return self._inline_style()

    def __repr__(self) -> str:
        return self._inline_style()


def css(df: Optional[Dict[str, Any]] = None, /) -> StructuredCss:
    \"\"\"Create a structured css instance.

    This enables typing intellisense, if available.

    Args:
        df (dict[str, Any], optional): Default CSS items, if any.
    \"\"\"
    return StructuredCss(df)
"""
        )

    print("\nOK: typed css generated")
