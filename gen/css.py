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
        elif spec["type"] in ("complex", "length", "string", "url", "time"):
            typ = "str"
        elif spec["type"] == "color":
            typ = "Union[str, StandardColor]"
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

StandardColor = Literal[
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "black",
    "blanchedalmond",
    "blue",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkgrey",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkslategrey",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "green",
    "greenyellow",
    "grey",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgray",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightslategrey",
    "lightsteelblue",
    "lightyellow",
    "lime",
    "limegreen",
    "linen",
    "magenta",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "purple",
    "red",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "silver",
    "skyblue",
    "slateblue",
    "slategray",
    "slategrey",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "white",
    "whitesmoke",
    "yellow",
    "yellowgreen",
    "rebeccapurple"  # In honor of Rebecca Meyer.
]

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
