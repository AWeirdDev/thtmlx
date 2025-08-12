import rjsonc

from itertools import chain

from typing import Dict, Literal, Union
from typing_extensions import TypedDict


class Specification(TypedDict):
    description: str
    attributes: Dict[str, "TypedDescription"]


class TypedDescription(TypedDict):
    type: Literal["string", "boolean", "integer"]
    description: str


Specifications = Dict[Union[Literal["$"], str], Specification]
TYPE_MAPPING = {
    "boolean": "Optional[bool] = None",
    "string": "Optional[str] = None",
    "integer": "Optional[int] = None",
    "number": "Optional[Union[int, float]] = None",
    "css": "Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None",
}
RESERVED_KEYWORDS = ("for", "del", "async", "class")
SKIP_KEYS = ("meta", "script", "style", "link")


def clean(s: str, /) -> str:
    if s in RESERVED_KEYWORDS:
        s = s + "_"
    return s.replace("-", "_")


def generate():
    print("generate html")

    with open("gen/specs.jsonc", "rb") as f:
        SPECS: Specifications = rjsonc.loads(f.read())

    COMMON: Specification = SPECS["$"]

    PY = []
    PYI = []
    KEYS = []

    for key, spec in SPECS.items():
        if key == "$":
            continue

        print(f"\nprocessing tag: {key}")

        rp_key = clean(key)
        desc = spec["description"]

        KEYS.append(rp_key)

        args = []
        doc = []
        attrs = spec["attributes"]
        name_map = []

        if key in SKIP_KEYS:
            it = []
        else:
            it = chain(attrs.items(), COMMON["attributes"].items())

        went_through = []
        for name, td in it:
            typ = TYPE_MAPPING[td["type"]]

            rp_name = clean(name)

            if rp_name in went_through:
                continue

            name_map.append(f"{name!r}: kwargs.pop({rp_name!r}, None)")

            went_through.append(rp_name)

            args.append(f"{rp_name}: {typ}")
            doc.append(f"{rp_name}: {td['description']}")

            print(" " * 16 + f"@ {rp_name}: {typ}")

        went_through.clear()

        upper = f"def {rp_key}(*inner: AnyChild{', ' if args else ''}{', '.join(args)}, **kwargs) -> Element:"

        if doc:
            PYI.append(
                f"""{upper}
    \"\"\"{desc}

    Args:
        {'\n        '.join(doc)}
    \"\"\"
"""
            )
        else:
            PYI.append(
                f"""{upper}
    \"\"\"{desc}\"\"\"
"""
            )

        PY.append(
            f"""def {rp_key}(*inner, **kwargs) -> Element:
    return Element({key!r}, inner, {'{'}{', '.join(name_map)}{',' if name_map else ''} **kwargs{'}'})
"""
        )

    with open("thtmlx/_elements.pyi", "w", encoding="utf-8") as f:
        f.write(
            f"""\
# @ generated
from typing import Any, Dict, Optional, Tuple, Union

from .core import AnyChild, Element
from ._css import StructuredCss

{'\n'.join(PYI)}"""
        )

    with open("thtmlx/_elements.py", "w", encoding="utf-8") as f:
        f.write(
            f"""\
# @generated
from .core import Element

{'\n'.join(PY)}
"""
        )

    with open("thtmlx/py.typed", "w", encoding="utf-8") as f:
        f.write("")

    with open("gen/imports", "w", encoding="utf-8") as f:
        f.write(f"from ._elements import (\n    {',\n    '.join(KEYS)}\n)")

    print("\nOK: typed html generated")
