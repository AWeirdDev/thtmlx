import json
from typing import Any, Dict, List, Optional, Tuple, Union

import thtml_escape as escaper

from ._css import StructuredCss

AnyChild = Union[Any, "Element", "Fragment", "NoEscapeElement"]


def cinner(items: Tuple[Any, ...]) -> List[str]:
    """Convert inner children to plain text (HTML)."""
    res = []
    for item in items:
        if item is None:
            continue

        if isinstance(item, Element):
            res.append(item.html())
        else:
            res.append(escaper.encode(str(item)))

    return res


class Element:
    """Represents an HTML element."""

    __slots__ = ("tag", "inner", "attributes")

    tag: str
    inner: Tuple[Any, ...]
    attributes: Dict[str, Any]

    def __init__(self, tag: str, /, inner: Tuple[Any, ...], kwargs: Dict[str, Any]):
        self.tag = tag
        self.inner = inner
        self.attributes = kwargs

    def __attrs_str(self) -> str:
        if self.attributes:
            attrs = ""
            for k, v in self.attributes.items():
                if v is not None:
                    if k == "style":
                        if isinstance(v, StructuredCss):
                            s = str(v)
                        elif isinstance(v, tuple):
                            s = ""
                        elif isinstance(v, str):
                            s = v
                        elif isinstance(v, dict):
                            s = str(StructuredCss(v))
                        else:
                            # unknown!
                            # i know this is the same as the first case,
                            # but i'd like to clarify
                            s = str(v)
                    else:
                        if isinstance(v, bool):
                            s = str(v).lower()
                        else:
                            s = str(v)
                    attrs += f" {k}={json.dumps(escaper.encode(s))}"
            return attrs
        else:
            return ""

    def extras(self, kw: Dict[str, Any], /) -> "Element":
        """Add extra classes.

        This is useful when the attributes are dynamic, or the name
        matches a Python keyword.


        Example:
        ```python
        import thtmlx as x

        ele = x.div("Yeah!").extras({"i-have-dashes": True})
        print(ele)
        ```
        """
        self.attributes |= kw
        return self

    def html(self) -> str:
        """Converts this element to its HTML form."""
        res = cinner(self.inner)

        return f"<{self.tag}{self.__attrs_str()}>{'\n'.join(res)}</{self.tag}>"

    def __str__(self):
        return self.html()

    def __repr__(self):
        return self.html()


class Fragment(Element):
    __slots__ = ("inner",)
    inner: Tuple[Any, ...]

    def __init__(self, inner: Tuple[Any, ...]):
        self.inner = inner

    def html(self) -> str:
        return "\n".join(cinner(self.inner))


class NoEscapeElement(Element):
    __slots__ = ("content",)

    content: str

    def __init__(self, html: str):
        self.content = html

    def html(self) -> str:
        return self.content


def frag(*inner: AnyChild) -> Fragment:
    """Create a document fragment.

    Args:
        *inner: Children.
    """
    return Fragment(inner)


def noescape(html: str, /) -> NoEscapeElement:
    """**DO NOT USE** unless you're aware of the consequences.

    Directly insert HTML code without escaping.

    Args:
        html (str): The inner html to ***dangerously*** set.
    """
    return NoEscapeElement(html)


def tag(
    name: str,
    /,
    *inner: AnyChild,
    accesskey: Optional[str] = None,
    class_: Optional[str] = None,
    contenteditable: Optional[bool] = None,
    dir: Optional[str] = None,
    draggable: Optional[bool] = None,
    hidden: Optional[bool] = None,
    id: Optional[str] = None,
    lang: Optional[str] = None,
    spellcheck: Optional[bool] = None,
    tabindex: Optional[int] = None,
    title: Optional[str] = None,
) -> Element:
    """Create a custom element.

    Args:
        name (str): Name of the element. Must be a safe name.
    """
    return Element(
        name,
        inner,
        {
            "accesskey": accesskey,
            "class": class_,
            "contenteditable": contenteditable,
            "dir": dir,
            "draggable": draggable,
            "hidden": hidden,
            "id": id,
            "lang": lang,
            "spellcheck": spellcheck,
            "tabindex": tabindex,
            "title": title,
        },
    )
