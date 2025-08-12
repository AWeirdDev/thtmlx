# @ generated
from typing import Any, Dict, Optional, Tuple, Union

from .core import AnyChild, Element
from ._css import StructuredCss

def html(*inner: AnyChild, manifest: Optional[str] = None, xmlns: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the root (top-level element) of an HTML document. All other elements must be descendants of this element.

    Args:
        manifest: Specifies the URL of the document's cache manifest (for offline applications).
        xmlns: Specifies the XML namespace (typically 'http://www.w3.org/1999/xhtml' for XHTML).
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def head(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Contains machine-readable information (metadata) about the document, like its title, scripts, and style sheets.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def title(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines the document's title that is shown in a browser's title bar or a page's tab.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def base(*inner: AnyChild, href: Optional[str] = None, target: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

    Args:
        href: The base URL to use for all relative URLs in the document.
        target: The default target for all hyperlinks and forms in the document.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def link(*inner: AnyChild, **kwargs) -> Element:
    """Specifies relationships between the current document and an external resource. Commonly used to link to CSS or icons."""

def meta(*inner: AnyChild, **kwargs) -> Element:
    """Represents metadata that cannot be represented by other HTML meta-related elements."""

def body(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the content of an HTML document. There can be only one such element in a document.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def article(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a self-contained composition in a document, which is intended to be independently distributable or reusable.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def section(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def nav(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a section of a page whose purpose is to provide navigation links.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def aside(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a portion of a document whose content is only indirectly related to the document's main content.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def h1(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the highest level section heading.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def h2(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the second level section heading.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def h3(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the third level section heading.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def h4(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the fourth level section heading.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def h5(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the fifth level section heading.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def h6(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the lowest level section heading.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def header(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents introductory content, typically a group of introductory or navigational aids.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def footer(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a footer for its nearest sectioning content or sectioning root element.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def address(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Indicates that the enclosed HTML provides contact information for a person, people, or organization.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def p(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a paragraph.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def hr(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a thematic break between paragraph-level elements.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def pre(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents preformatted text which is to be presented exactly as written in the HTML file.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def blockquote(*inner: AnyChild, cite: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Indicates that the enclosed text is an extended quotation.

    Args:
        cite: A URL that designates a source document or message for the quoted content.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def ol(*inner: AnyChild, reversed: Optional[bool] = None, start: Optional[int] = None, type: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents an ordered list of items.

    Args:
        reversed: Specifies that the list order should be reversed.
        start: Specifies the starting value of an ordered list.
        type: Specifies the kind of marker to use in the list (1, a, A, i, I).
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def ul(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents an unordered list of items.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def menu(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents an unordered list of items, typically rendered as a bulleted list (similar to ul, but semantic for menus).

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def li(*inner: AnyChild, value: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents an item in a list.

    Args:
        value: Specifies the value of a list item in ordered lists.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def dl(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a description list.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def dt(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies a term in a description or definition list.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def dd(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Provides the description, definition, or value for the preceding term (dt) in a description list (dl).

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def figure(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents self-contained content, potentially with an optional caption (figcaption).

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def figcaption(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a caption or legend describing the rest of the contents of its parent figure element.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def main(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the dominant content of the body of a document.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def div(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """The generic container for flow content. It has no effect on the content or layout until styled.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def a(*inner: AnyChild, href: Optional[str] = None, target: Optional[str] = None, download: Optional[str] = None, rel: Optional[str] = None, hreflang: Optional[str] = None, type: Optional[str] = None, referrerpolicy: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Creates a hyperlink to web pages, files, email addresses, locations in the same page, or anything else a URL can address.

    Args:
        href: The URL that the hyperlink points to.
        target: Where to display the linked URL (_self, _blank, _parent, _top).
        download: Indicates that the hyperlink is to be used for downloading a resource.
        rel: Specifies the relationship between the current document and the linked document.
        hreflang: Specifies the language of the linked resource.
        type: Specifies the MIME type of the linked resource.
        referrerpolicy: Specifies which referrer is sent when fetching the resource.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def em(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Marks text that has stress emphasis.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def strong(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents strong importance, seriousness, or urgency for its contents.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def small(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents side-comments and small print, like copyright and legal text.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def s(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents contents that are no longer accurate or no longer relevant.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def cite(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a reference to a creative work.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def q(*inner: AnyChild, cite: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Indicates that the enclosed text is a short inline quotation.

    Args:
        cite: A URL that designates a source document or message for the quoted content.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def dfn(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to indicate the term being defined within the context of a definition phrase or sentence.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def abbr(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents an abbreviation or acronym.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def ruby(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def rt(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies the ruby text component of a ruby annotation.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def rp(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to provide fall-back parentheses for browsers that do not support display of ruby annotations.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def data(*inner: AnyChild, value: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Links a given piece of content with a machine-readable translation.

    Args:
        value: A machine-readable translation of the content.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def time(*inner: AnyChild, datetime: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a specific period in time.

    Args:
        datetime: A machine-readable form of the date/time.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def code(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def var(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the name of a variable in a mathematical expression or a programming context.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def samp(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to enclose inline text which represents sample (or quoted) output from a computer program.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def kbd(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def sub(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies inline text which should be displayed as subscript for solely typographical reasons.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def sup(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies inline text which is to be displayed as superscript for solely typographical reasons.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def i(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a range of text that is set off from the normal text for a different reason, such as idiomatic text or technical terms.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def b(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a span of text stylistically different from normal text, without conveying any special importance.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def u(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def mark(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents text which is marked or highlighted for reference or notation purposes.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def bdi(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def bdo(*inner: AnyChild, dir: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Overrides the current directionality of text, so that the text within is rendered in a different direction.

    Args:
        dir: Overrides the text direction (ltr or rtl).
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def span(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """A generic inline container for phrasing content, which does not inherently represent anything.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def br(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Produces a line break in text (carriage-return).

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def wbr(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a word break opportunity—a position within text where the browser may optionally break a line.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def ins(*inner: AnyChild, cite: Optional[str] = None, datetime: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a range of text that has been added to a document.

    Args:
        cite: A URI for a resource that explains the change.
        datetime: The date and time when the text was inserted/changed.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def del_(*inner: AnyChild, cite: Optional[str] = None, datetime: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a range of text that has been deleted from a document.

    Args:
        cite: A URI for a resource that explains the change.
        datetime: The date and time when the text was deleted.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def picture(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Contains zero or more source elements and one img element to offer alternative versions of an image for different display/device scenarios.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def source(*inner: AnyChild, src: Optional[str] = None, srcset: Optional[str] = None, sizes: Optional[str] = None, media: Optional[str] = None, type: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies multiple media resources for the picture, audio, or video element.

    Args:
        src: The URL of the embeddable content (for audio/video).
        srcset: Images to use in different situations (e.g., high-resolution displays, small monitors).
        sizes: Image sizes for different page layouts.
        media: Media query of the resource's intended media.
        type: The MIME type of the resource.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def img(*inner: AnyChild, alt: Optional[str] = None, src: Optional[str] = None, srcset: Optional[str] = None, sizes: Optional[str] = None, crossorigin: Optional[str] = None, usemap: Optional[str] = None, ismap: Optional[bool] = None, width: Optional[int] = None, height: Optional[int] = None, referrerpolicy: Optional[str] = None, decoding: Optional[str] = None, loading: Optional[str] = None, fetchpriority: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Embeds an image into the document.

    Args:
        alt: Alternative text for the image.
        src: The URL of the embeddable image.
        srcset: One or more responsive image candidates.
        sizes: Image sizes for different page layouts.
        crossorigin: How the element handles cross-origin requests.
        usemap: The partial URL (starting with #) of an image map associated with the element.
        ismap: Indicates that the image is part of a server-side image map.
        width: The width of the image, in pixels.
        height: The height of the image, in pixels.
        referrerpolicy: Referrer policy for fetches initiated by the element.
        decoding: Provides a hint to the browser as to how it should decode the image.
        loading: Indicates how the browser should load the image (eager or lazy).
        fetchpriority: Provides a hint of the relative priority to use when fetching the image.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def iframe(*inner: AnyChild, src: Optional[str] = None, srcdoc: Optional[str] = None, name: Optional[str] = None, sandbox: Optional[str] = None, allow: Optional[str] = None, allowfullscreen: Optional[bool] = None, width: Optional[int] = None, height: Optional[int] = None, referrerpolicy: Optional[str] = None, loading: Optional[str] = None, credentialless: Optional[bool] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a nested browsing context, embedding another HTML page into the current one.

    Args:
        src: The URL of the page to embed.
        srcdoc: Inline HTML to embed as the content of the frame.
        name: A name for the embedded browsing context.
        sandbox: Enables a set of extra restrictions for the content in the iframe.
        allow: Specifies a feature policy for the iframe.
        allowfullscreen: Indicates whether the iframe can activate fullscreen mode.
        width: The width of the frame, in pixels.
        height: The height of the frame, in pixels.
        referrerpolicy: Referrer policy for fetches initiated by the element.
        loading: Indicates how the browser should load the iframe (eager or lazy).
        credentialless: Indicates whether to load the iframe in a credentialless mode.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def embed(*inner: AnyChild, src: Optional[str] = None, type: Optional[str] = None, width: Optional[int] = None, height: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Embeds external content at the specified point in the document.

    Args:
        src: The URL of the resource to embed.
        type: The MIME type to use to select the plug-in to instantiate.
        width: The displayed width of the resource, in pixels.
        height: The displayed height of the resource, in pixels.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def object(*inner: AnyChild, data: Optional[str] = None, type: Optional[str] = None, name: Optional[str] = None, form: Optional[str] = None, width: Optional[int] = None, height: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

    Args:
        data: The address of the resource.
        type: The MIME type of the resource specified by data.
        name: Name of the object (for form submission).
        form: Associates the element with a form element.
        width: The width of the resource, in pixels.
        height: The height of the resource, in pixels.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def video(*inner: AnyChild, src: Optional[str] = None, crossorigin: Optional[str] = None, poster: Optional[str] = None, preload: Optional[str] = None, autoplay: Optional[bool] = None, playsinline: Optional[bool] = None, loop: Optional[bool] = None, muted: Optional[bool] = None, controls: Optional[bool] = None, width: Optional[int] = None, height: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Embeds a media player which supports video playback into the document.

    Args:
        src: The URL of the video to embed.
        crossorigin: How the element handles cross-origin requests.
        poster: A URL for an image to be shown while the video is downloading.
        preload: Hints how much buffering the media resource will likely need.
        autoplay: Hint that the media resource can be started automatically when the page is loaded.
        playsinline: Hints that the media should play inline instead of requiring fullscreen.
        loop: Whether to loop the media resource.
        muted: Whether to mute the media resource by default.
        controls: Shows the default video controls (play/pause etc.).
        width: The width of the video, in pixels.
        height: The height of the video, in pixels.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def audio(*inner: AnyChild, src: Optional[str] = None, crossorigin: Optional[str] = None, preload: Optional[str] = None, autoplay: Optional[bool] = None, loop: Optional[bool] = None, muted: Optional[bool] = None, controls: Optional[bool] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to embed sound content in documents.

    Args:
        src: The URL of the audio to embed.
        crossorigin: How the element handles cross-origin requests.
        preload: Hints how much buffering the media resource will likely need.
        autoplay: Hint that the media resource can be started automatically when the page is loaded.
        loop: Whether to loop the media resource.
        muted: Whether to mute the media resource by default.
        controls: Shows the default audio controls.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def track(*inner: AnyChild, default: Optional[bool] = None, kind: Optional[str] = None, label: Optional[str] = None, src: Optional[str] = None, srclang: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles.

    Args:
        default: Indicates that the track should be enabled unless the user's preferences indicate something different.
        kind: How the text track is meant to be used (subtitles, captions, descriptions, chapters, metadata).
        label: A user-readable title of the text track.
        src: Address of the track (.vtt file).
        srclang: Language of the track text data.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def canvas(*inner: AnyChild, width: Optional[int] = None, height: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Container element to use with either the canvas scripting API or the WebGL API to draw graphics and animations.

    Args:
        width: The width of the coordinate space, in pixels.
        height: The height of the coordinate space, in pixels.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def table(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def caption(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies the caption (or title) of a table.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def colgroup(*inner: AnyChild, span: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a group of columns within a table.

    Args:
        span: Number of columns the group spans.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def col(*inner: AnyChild, span: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a column within a table and is used for defining common semantics on all common cells.

    Args:
        span: Number of columns the column definition spans.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def tbody(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Encapsulates a set of table rows (tr elements), indicating that they comprise the body of the table.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def thead(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a set of rows defining the head of the columns of the table.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def tfoot(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a set of rows summarizing the columns of the table.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def tr(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a row of cells in a table.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def td(*inner: AnyChild, colspan: Optional[int] = None, rowspan: Optional[int] = None, headers: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a cell of a table that contains data.

    Args:
        colspan: Number of columns the cell extends.
        rowspan: Number of rows the cell extends.
        headers: List of space-separated IDs of th elements that the cell is related to.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def th(*inner: AnyChild, colspan: Optional[int] = None, rowspan: Optional[int] = None, headers: Optional[str] = None, scope: Optional[str] = None, abbr: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a cell as a header of a group of table cells.

    Args:
        colspan: Number of columns the header cell extends.
        rowspan: Number of rows the header cell extends.
        headers: List of space-separated IDs of other th elements that the header is related to.
        scope: Defines the cells that the header relates to (row, col, rowgroup, colgroup).
        abbr: Alternative label to use for the header cell when referencing it.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def form(*inner: AnyChild, accept_charset: Optional[str] = None, action: Optional[str] = None, autocomplete: Optional[str] = None, enctype: Optional[str] = None, method: Optional[str] = None, name: Optional[str] = None, novalidate: Optional[bool] = None, target: Optional[str] = None, rel: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a document section containing interactive controls for submitting information.

    Args:
        accept_charset: Space-separated character encodings the server accepts.
        action: URL that processes the form submission.
        autocomplete: Indicates whether controls in this form can have their values automatically completed (on or off).
        enctype: Encoding type when method is post (application/x-www-form-urlencoded, multipart/form-data, text/plain).
        method: HTTP method to use for form submission (get, post).
        name: Name of the form.
        novalidate: Indicates that the form shouldn't be validated when submitted.
        target: Where to display the response after submitting the form.
        rel: Relationship between the form and the action URL.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def label(*inner: AnyChild, for_: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a caption for an item in a user interface.

    Args:
        for_: The id of a labelable form-related element.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def input(*inner: AnyChild, accept: Optional[str] = None, alt: Optional[str] = None, autocomplete: Optional[str] = None, capture: Optional[str] = None, checked: Optional[bool] = None, dirname: Optional[str] = None, disabled: Optional[bool] = None, form: Optional[str] = None, formaction: Optional[str] = None, formenctype: Optional[str] = None, formmethod: Optional[str] = None, formnovalidate: Optional[bool] = None, formtarget: Optional[str] = None, height: Optional[int] = None, list: Optional[str] = None, max: Optional[str] = None, maxlength: Optional[int] = None, min: Optional[str] = None, minlength: Optional[int] = None, multiple: Optional[bool] = None, name: Optional[str] = None, pattern: Optional[str] = None, placeholder: Optional[str] = None, popovertarget: Optional[str] = None, popovertargetaction: Optional[str] = None, readonly: Optional[bool] = None, required: Optional[bool] = None, size: Optional[int] = None, src: Optional[str] = None, step: Optional[str] = None, type: Optional[str] = None, value: Optional[str] = None, width: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to create interactive controls for web-based forms in order to accept data from the user.

    Args:
        accept: Hint for expected file type in file upload controls.
        alt: Alt text for an image input type.
        autocomplete: Hint for form autofill feature.
        capture: Media capture input method in file upload controls.
        checked: Whether the control is checked.
        dirname: Name of form field to use for sending the element's directionality in form submission.
        disabled: Whether the form control is disabled.
        form: Associates the control with a form element.
        formaction: URL to use for form submission.
        formenctype: Form data set encoding type to use for form submission.
        formmethod: HTTP method to use for form submission.
        formnovalidate: Bypass form control validation for form submission.
        formtarget: Browsing context for form submission.
        height: Height of the image for type=image.
        list: The id of a datalist element that provides predefined options.
        max: Maximum value.
        maxlength: Maximum length of value.
        min: Minimum value.
        minlength: Minimum length of value.
        multiple: Whether to allow multiple values.
        name: Name of the form control.
        pattern: Pattern the value must match to be valid.
        placeholder: Text that appears in the form control when empty.
        popovertarget: The id of the popover element this input targets.
        popovertargetaction: The action to perform on the popover (show, hide, toggle).
        readonly: Whether to allow the value to be edited by the user.
        required: Whether the control is required for form submission.
        size: Size of the control.
        src: Image URL for type=image.
        step: Incremental values that are valid.
        type: Type of form control (text, password, checkbox, radio, file, etc.).
        value: Value of the form control.
        width: Width of the image for type=image.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def button(*inner: AnyChild, disabled: Optional[bool] = None, form: Optional[str] = None, formaction: Optional[str] = None, formenctype: Optional[str] = None, formmethod: Optional[str] = None, formnovalidate: Optional[bool] = None, formtarget: Optional[str] = None, name: Optional[str] = None, popovertarget: Optional[str] = None, popovertargetaction: Optional[str] = None, type: Optional[str] = None, value: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology.

    Args:
        disabled: Whether the form control is disabled.
        form: Associates the element with a form element.
        formaction: URL to use for form submission.
        formenctype: Form data set encoding type to use for form submission.
        formmethod: HTTP method to use for form submission.
        formnovalidate: Bypass form control validation for form submission.
        formtarget: Browsing context for form submission.
        name: Name of the element to use for form submission.
        popovertarget: The id of the popover element this button targets.
        popovertargetaction: The action to perform on the popover (show, hide, toggle).
        type: Type of button (button, reset, submit).
        value: Value to be sent with form submission.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def select(*inner: AnyChild, autocomplete: Optional[str] = None, disabled: Optional[bool] = None, form: Optional[str] = None, multiple: Optional[bool] = None, name: Optional[str] = None, required: Optional[bool] = None, size: Optional[int] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a control that provides a menu of options.

    Args:
        autocomplete: Hint for form autofill feature.
        disabled: Whether the form control is disabled.
        form: Associates the element with a form element.
        multiple: Whether to allow multiple options to be selected.
        name: Name of the element to use for form submission.
        required: Whether the control is required for form submission.
        size: Number of options to show to the user.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def datalist(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Contains a set of option elements that represent the permissible or recommended options available to choose from within other controls.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def optgroup(*inner: AnyChild, disabled: Optional[bool] = None, label: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Creates a grouping of options within a select element.

    Args:
        disabled: If present, all options in this group are disabled.
        label: The name of the group of options.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def option(*inner: AnyChild, disabled: Optional[bool] = None, label: Optional[str] = None, selected: Optional[bool] = None, value: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to define an item contained in a select, an optgroup, or a datalist element.

    Args:
        disabled: Whether the option is disabled.
        label: Text to be displayed for the option.
        selected: Whether the option is initially selected.
        value: Value to be submitted if the option is selected.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def textarea(*inner: AnyChild, autocomplete: Optional[str] = None, cols: Optional[int] = None, dirname: Optional[str] = None, disabled: Optional[bool] = None, form: Optional[str] = None, maxlength: Optional[int] = None, minlength: Optional[int] = None, name: Optional[str] = None, placeholder: Optional[str] = None, readonly: Optional[bool] = None, required: Optional[bool] = None, rows: Optional[int] = None, wrap: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text.

    Args:
        autocomplete: Hint for form autofill feature.
        cols: The visible width of the text control, in average character widths.
        dirname: Name of form field to use for sending the element's directionality.
        disabled: Whether the form control is disabled.
        form: Associates the control with a form element.
        maxlength: Maximum length of value.
        minlength: Minimum length of value.
        name: Name of the control.
        placeholder: Text that appears in the control when empty.
        readonly: Whether the value can be edited.
        required: Whether the control is required.
        rows: The number of visible text lines.
        wrap: How the control wraps text (soft, hard).
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def output(*inner: AnyChild, for_: Optional[str] = None, form: Optional[str] = None, name: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents the result of a calculation or user action.

    Args:
        for_: Space-separated IDs of other elements associated with the calculation.
        form: Associates the element with a form element.
        name: Name of the element.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def progress(*inner: AnyChild, max: Optional[Union[int, float]] = None, value: Optional[Union[int, float]] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Displays an indicator showing the completion progress of a task.

    Args:
        max: The upper bound of the range (default 1).
        value: The current progress value.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def meter(*inner: AnyChild, value: Optional[Union[int, float]] = None, min: Optional[Union[int, float]] = None, max: Optional[Union[int, float]] = None, low: Optional[Union[int, float]] = None, high: Optional[Union[int, float]] = None, optimum: Optional[Union[int, float]] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents either a scalar value within a known range or a fractional value.

    Args:
        value: The current numeric value.
        min: The lower bound of the range (default 0).
        max: The upper bound of the range (default 1).
        low: The upper bound of the low range.
        high: The lower bound of the high range.
        optimum: The optimal numeric value.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def fieldset(*inner: AnyChild, disabled: Optional[bool] = None, form: Optional[str] = None, name: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Used to group several controls as well as labels within a web form.

    Args:
        disabled: Disables all form controls within the fieldset.
        form: The id of a form this fieldset belongs to.
        name: Name of the fieldset.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def legend(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a caption for the content of its parent fieldset.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def details(*inner: AnyChild, open: Optional[bool] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a disclosure widget from which the user can obtain additional information or controls.

    Args:
        open: Indicates whether the details are visible.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def summary(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Specifies a summary, caption, or legend for a details element's disclosure box.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def dialog(*inner: AnyChild, open: Optional[bool] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

    Args:
        open: Indicates that the dialog is active and can be interacted with.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def script(*inner: AnyChild, **kwargs) -> Element:
    """Used to embed executable code or data; this is typically used to embed or refer to JavaScript code."""

def noscript(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def template(*inner: AnyChild, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

    Args:
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """

def slot(*inner: AnyChild, name: Optional[str] = None, accesskey: Optional[str] = None, class_: Optional[str] = None, style: Optional[Union[StructuredCss, str, Dict[str, Any], Tuple[()]]] = None, contenteditable: Optional[bool] = None, dir: Optional[str] = None, draggable: Optional[bool] = None, hidden: Optional[bool] = None, id: Optional[str] = None, lang: Optional[str] = None, spellcheck: Optional[bool] = None, tabindex: Optional[int] = None, title: Optional[str] = None, **kwargs) -> Element:
    """A placeholder inside a web component that you can fill with your own markup.

    Args:
        name: The name of the slot.
        accesskey: Specifies a shortcut key to activate or focus an element.
        class_: Class names, separated with spaces.
        style: Inline CSS styles.
        contenteditable: Indicates whether the element's content is editable.
        dir: Specifies the text direction for the content (values: ltr, rtl, auto).
        draggable: Specifies whether an element is draggable.
        hidden: Indicates that the element is not yet, or is no longer, relevant and should not be rendered.
        id: A unique identifier that only appears once throughout the whole document.
        lang: Specifies the language of the element's content.
        spellcheck: Specifies whether the element should have its spelling and grammar checked.
        tabindex: Specifies the tab order of an element.
        title: Specifies extra information about an element (displayed as a tooltip).
    """
