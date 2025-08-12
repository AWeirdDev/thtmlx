# @ generated
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
    """Structured CSS.

    Functions have generated documentations for reference.
    """

    __slots__ = ("k", )
    k: Dict[str, Any]

    def __init__(self, df: Optional[Dict[str, Any]] = None):
        self.k = df or {}
    
    def accent_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the accent color for user-interface controls like checkboxes and radio buttons.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['accent-color'] = str(value)
        return self
    
    def align_content(self, value: Union[str, Literal["flex-start", "flex-end", "center", "space-between", "space-around", "space-evenly"]], /) -> "StructuredCss":
        """Aligns a flex container's lines within the flex container when there is extra space in the cross-axis.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['align-content'] = str(value)
        return self
    
    def align_items(self, value: Union[str, Literal["flex-start", "flex-end", "center", "baseline", "stretch"]], /) -> "StructuredCss":
        """Sets the default alignment in the cross axis for all of the flex container's items.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['align-items'] = str(value)
        return self
    
    def align_self(self, value: Union[str, Literal["auto", "flex-start", "flex-end", "center", "baseline", "stretch"]], /) -> "StructuredCss":
        """Overrides a flex item's align-items value.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['align-self'] = str(value)
        return self
    
    def all(self, value: Union[str, Literal["initial", "inherit", "unset", "revert"]], /) -> "StructuredCss":
        """Resets all properties (except unicode-bidi and direction) to their initial or inherited values.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['all'] = str(value)
        return self
    
    def animation(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all animation properties.
        
        Syntax: `<time> || <timing-function> || <time> || <integer> || <animation-direction> || <animation-fill-mode> || <animation-play-state> || [<string> | none]`

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['animation'] = str(value)
        return self
    
    def animation_delay(self, value: str, /) -> "StructuredCss":
        """Specifies a delay for the start of an animation.

        *@generated*

        Args:
            value: The value. Expected `time`.
        """
        self.k['animation-delay'] = str(value)
        return self
    
    def animation_direction(self, value: Union[str, Literal["normal", "reverse", "alternate", "alternate-reverse"]], /) -> "StructuredCss":
        """Specifies whether an animation should be played forwards, backwards or in alternate cycles.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['animation-direction'] = str(value)
        return self
    
    def animation_duration(self, value: str, /) -> "StructuredCss":
        """Specifies how long an animation should take to complete one cycle.

        *@generated*

        Args:
            value: The value. Expected `time`.
        """
        self.k['animation-duration'] = str(value)
        return self
    
    def animation_fill_mode(self, value: Union[str, Literal["none", "forwards", "backwards", "both"]], /) -> "StructuredCss":
        """Specifies a style for the element when the animation is not playing.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['animation-fill-mode'] = str(value)
        return self
    
    def animation_iteration_count(self, value: Union[int, float], /) -> "StructuredCss":
        """Specifies the number of times an animation should be played. Can be 'infinite'.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['animation-iteration-count'] = str(value)
        return self
    
    def animation_name(self, value: str, /) -> "StructuredCss":
        """Specifies the name of the @keyframes animation.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['animation-name'] = str(value)
        return self
    
    def animation_play_state(self, value: Union[str, Literal["paused", "running"]], /) -> "StructuredCss":
        """Specifies whether the animation is running or paused.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['animation-play-state'] = str(value)
        return self
    
    def animation_timing_function(self, value: Union[str, Literal["ease", "linear", "ease-in", "ease-out", "ease-in-out", "step-start", "step-end"]], /) -> "StructuredCss":
        """Specifies the speed curve of an animation.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['animation-timing-function'] = str(value)
        return self
    
    def aspect_ratio(self, value: str, /) -> "StructuredCss":
        """Specifies a preferred aspect ratio for the box.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['aspect-ratio'] = str(value)
        return self
    
    def backdrop_filter(self, value: str, /) -> "StructuredCss":
        """Applies graphical effects like blur or color shift to the area behind an element.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['backdrop-filter'] = str(value)
        return self
    
    def backface_visibility(self, value: Union[str, Literal["visible", "hidden"]], /) -> "StructuredCss":
        """Specifies whether or not the back face of an element is visible when turned towards the user.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['backface-visibility'] = str(value)
        return self
    
    def background(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all background properties.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['background'] = str(value)
        return self
    
    def background_attachment(self, value: Union[str, Literal["scroll", "fixed", "local"]], /) -> "StructuredCss":
        """Specifies whether the background image is fixed or scrolls with the page.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['background-attachment'] = str(value)
        return self
    
    def background_blend_mode(self, value: Union[str, Literal["normal", "multiply", "screen"]], /) -> "StructuredCss":
        """Specifies the blending mode of each background layer.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['background-blend-mode'] = str(value)
        return self
    
    def background_clip(self, value: Union[str, Literal["border-box", "padding-box", "content-box"]], /) -> "StructuredCss":
        """Specifies the painting area of the background.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['background-clip'] = str(value)
        return self
    
    def background_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Specifies the background color of an element.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['background-color'] = str(value)
        return self
    
    def background_image(self, value: str, /) -> "StructuredCss":
        """Specifies one or more background images for an element.

        *@generated*

        Args:
            value: The value. Expected `url`.
        """
        self.k['background-image'] = str(value)
        return self
    
    def background_origin(self, value: Union[str, Literal["padding-box", "border-box", "content-box"]], /) -> "StructuredCss":
        """Specifies where the background image is positioned.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['background-origin'] = str(value)
        return self
    
    def background_position(self, value: str, /) -> "StructuredCss":
        """Specifies the position of the background image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['background-position'] = str(value)
        return self
    
    def background_position_x(self, value: str, /) -> "StructuredCss":
        """Specifies the x-position of the background image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['background-position-x'] = str(value)
        return self
    
    def background_position_y(self, value: str, /) -> "StructuredCss":
        """Specifies the y-position of the background image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['background-position-y'] = str(value)
        return self
    
    def background_repeat(self, value: Union[str, Literal["repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round"]], /) -> "StructuredCss":
        """Specifies how the background image is repeated.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['background-repeat'] = str(value)
        return self
    
    def background_size(self, value: str, /) -> "StructuredCss":
        """Specifies the size of the background image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['background-size'] = str(value)
        return self
    
    def block_size(self, value: str, /) -> "StructuredCss":
        """Specifies the block size of an element, depending on writing mode.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['block-size'] = str(value)
        return self
    
    def border(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all border properties.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border'] = str(value)
        return self
    
    def border_block(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-block-width, border-block-style, border-block-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-block'] = str(value)
        return self
    
    def border_block_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the borders at the block start and end.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-block-color'] = str(value)
        return self
    
    def border_block_end(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-block-end-width, border-block-end-style, border-block-end-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-block-end'] = str(value)
        return self
    
    def border_block_end_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the border at the block end.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-block-end-color'] = str(value)
        return self
    
    def border_block_end_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the border at the block end.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-block-end-style'] = str(value)
        return self
    
    def border_block_end_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the border at the block end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-block-end-width'] = str(value)
        return self
    
    def border_block_start(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-block-start-width, border-block-start-style, border-block-start-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-block-start'] = str(value)
        return self
    
    def border_block_start_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the border at the block start.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-block-start-color'] = str(value)
        return self
    
    def border_block_start_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the border at the block start.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-block-start-style'] = str(value)
        return self
    
    def border_block_start_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the border at the block start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-block-start-width'] = str(value)
        return self
    
    def border_block_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the borders at the block start and end.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-block-style'] = str(value)
        return self
    
    def border_block_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the borders at the block start and end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-block-width'] = str(value)
        return self
    
    def border_bottom(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-bottom-width, border-bottom-style, border-bottom-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-bottom'] = str(value)
        return self
    
    def border_bottom_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the bottom border.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-bottom-color'] = str(value)
        return self
    
    def border_bottom_left_radius(self, value: str, /) -> "StructuredCss":
        """Sets the rounding of the bottom-left corner of the border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-bottom-left-radius'] = str(value)
        return self
    
    def border_bottom_right_radius(self, value: str, /) -> "StructuredCss":
        """Sets the rounding of the bottom-right corner of the border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-bottom-right-radius'] = str(value)
        return self
    
    def border_bottom_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the bottom border.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-bottom-style'] = str(value)
        return self
    
    def border_bottom_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the bottom border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-bottom-width'] = str(value)
        return self
    
    def border_collapse(self, value: Union[str, Literal["separate", "collapse"]], /) -> "StructuredCss":
        """Specifies whether table borders should be collapsed.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-collapse'] = str(value)
        return self
    
    def border_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the four borders.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-color'] = str(value)
        return self
    
    def border_end_end_radius(self, value: str, /) -> "StructuredCss":
        """Sets the rounding of the logical border radius at the end-end corner.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-end-end-radius'] = str(value)
        return self
    
    def border_end_start_radius(self, value: str, /) -> "StructuredCss":
        """Sets the rounding of the logical border radius at the end-start corner.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-end-start-radius'] = str(value)
        return self
    
    def border_image(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all border-image properties.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-image'] = str(value)
        return self
    
    def border_image_outset(self, value: Union[int, float], /) -> "StructuredCss":
        """Specifies the amount by which the border image area extends beyond the border box.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['border-image-outset'] = str(value)
        return self
    
    def border_image_repeat(self, value: Union[str, Literal["stretch", "repeat", "round", "space"]], /) -> "StructuredCss":
        """Specifies how the border image is repeated.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-image-repeat'] = str(value)
        return self
    
    def border_image_slice(self, value: Union[int, float], /) -> "StructuredCss":
        """Specifies how to slice the border image.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['border-image-slice'] = str(value)
        return self
    
    def border_image_source(self, value: str, /) -> "StructuredCss":
        """Specifies the source image for the border.

        *@generated*

        Args:
            value: The value. Expected `url`.
        """
        self.k['border-image-source'] = str(value)
        return self
    
    def border_image_width(self, value: str, /) -> "StructuredCss":
        """Specifies the width of the border image.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-image-width'] = str(value)
        return self
    
    def border_inline(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-inline-width, border-inline-style, border-inline-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-inline'] = str(value)
        return self
    
    def border_inline_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the borders at the inline start and end.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-inline-color'] = str(value)
        return self
    
    def border_inline_end(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-inline-end-width, border-inline-end-style, border-inline-end-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-inline-end'] = str(value)
        return self
    
    def border_inline_end_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the border at the inline end.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-inline-end-color'] = str(value)
        return self
    
    def border_inline_end_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the border at the inline end.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-inline-end-style'] = str(value)
        return self
    
    def border_inline_end_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the border at the inline end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-inline-end-width'] = str(value)
        return self
    
    def border_inline_start(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-inline-start-width, border-inline-start-style, border-inline-start-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-inline-start'] = str(value)
        return self
    
    def border_inline_start_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the border at the inline start.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-inline-start-color'] = str(value)
        return self
    
    def border_inline_start_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the border at the inline start.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-inline-start-style'] = str(value)
        return self
    
    def border_inline_start_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the border at the inline start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-inline-start-width'] = str(value)
        return self
    
    def border_inline_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the borders at the inline start and end.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-inline-style'] = str(value)
        return self
    
    def border_inline_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the borders at the inline start and end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-inline-width'] = str(value)
        return self
    
    def border_left(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-left-width, border-left-style, border-left-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-left'] = str(value)
        return self
    
    def border_left_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the left border.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-left-color'] = str(value)
        return self
    
    def border_left_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the left border.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-left-style'] = str(value)
        return self
    
    def border_left_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the left border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-left-width'] = str(value)
        return self
    
    def border_radius(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all border radius properties.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-radius'] = str(value)
        return self
    
    def border_right(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-right-width, border-right-style, border-right-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-right'] = str(value)
        return self
    
    def border_right_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the right border.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-right-color'] = str(value)
        return self
    
    def border_right_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the right border.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-right-style'] = str(value)
        return self
    
    def border_right_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the right border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-right-width'] = str(value)
        return self
    
    def border_spacing(self, value: str, /) -> "StructuredCss":
        """Sets the distance between the borders of adjacent table cells.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-spacing'] = str(value)
        return self
    
    def border_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the four borders.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-style'] = str(value)
        return self
    
    def border_top(self, value: str, /) -> "StructuredCss":
        """Shorthand for border-top-width, border-top-style, border-top-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['border-top'] = str(value)
        return self
    
    def border_top_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of the top border.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['border-top-color'] = str(value)
        return self
    
    def border_top_left_radius(self, value: str, /) -> "StructuredCss":
        """Sets the rounding of the top-left corner of the border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-top-left-radius'] = str(value)
        return self
    
    def border_top_right_radius(self, value: str, /) -> "StructuredCss":
        """Sets the rounding of the top-right corner of the border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-top-right-radius'] = str(value)
        return self
    
    def border_top_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of the top border.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['border-top-style'] = str(value)
        return self
    
    def border_top_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the top border.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-top-width'] = str(value)
        return self
    
    def border_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of the four borders.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['border-width'] = str(value)
        return self
    
    def bottom(self, value: str, /) -> "StructuredCss":
        """Specifies the offset of an absolutely positioned element from the bottom of the container.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['bottom'] = str(value)
        return self
    
    def box_decoration_break(self, value: Union[str, Literal["slice", "clone"]], /) -> "StructuredCss":
        """Specifies how an element's fragments should be rendered when broken across multiple lines.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['box-decoration-break'] = str(value)
        return self
    
    def box_shadow(self, value: str, /) -> "StructuredCss":
        """Attaches one or more shadows to an element.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['box-shadow'] = str(value)
        return self
    
    def box_sizing(self, value: Union[str, Literal["content-box", "border-box"]], /) -> "StructuredCss":
        """Specifies how the width and height of an element is calculated.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['box-sizing'] = str(value)
        return self
    
    def break_after(self, value: Union[str, Literal["auto", "avoid", "always"]], /) -> "StructuredCss":
        """Specifies whether a page, column, or region break should occur after the specified element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['break-after'] = str(value)
        return self
    
    def break_before(self, value: Union[str, Literal["auto", "avoid", "always"]], /) -> "StructuredCss":
        """Specifies whether a page, column, or region break should occur before the specified element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['break-before'] = str(value)
        return self
    
    def break_inside(self, value: Union[str, Literal["auto", "avoid"]], /) -> "StructuredCss":
        """Specifies whether a page, column, or region break should occur inside the specified element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['break-inside'] = str(value)
        return self
    
    def caption_side(self, value: Union[str, Literal["top", "bottom"]], /) -> "StructuredCss":
        """Specifies the position of a table caption.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['caption-side'] = str(value)
        return self
    
    def caret_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Specifies the color of the cursor (caret) in inputs, textareas, or editable content.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['caret-color'] = str(value)
        return self
    
    def clear(self, value: Union[str, Literal["none", "left", "right", "both"]], /) -> "StructuredCss":
        """Specifies on which sides of an element floating elements are not allowed to float.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['clear'] = str(value)
        return self
    
    def clip_path(self, value: str, /) -> "StructuredCss":
        """Creates a clipping region that determines what part of an element is visible.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['clip-path'] = str(value)
        return self
    
    def color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of text.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['color'] = str(value)
        return self
    
    def column_count(self, value: int, /) -> "StructuredCss":
        """Specifies the number of columns an element should be divided into.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['column-count'] = str(value)
        return self
    
    def column_fill(self, value: Union[str, Literal["balance", "auto"]], /) -> "StructuredCss":
        """Specifies how to fill columns.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['column-fill'] = str(value)
        return self
    
    def column_gap(self, value: str, /) -> "StructuredCss":
        """Specifies the gap between the columns.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['column-gap'] = str(value)
        return self
    
    def column_rule(self, value: str, /) -> "StructuredCss":
        """Shorthand for column-rule-width, column-rule-style, column-rule-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['column-rule'] = str(value)
        return self
    
    def column_rule_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Specifies the color of the rule between columns.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['column-rule-color'] = str(value)
        return self
    
    def column_rule_style(self, value: Union[str, Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Specifies the style of the rule between columns.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['column-rule-style'] = str(value)
        return self
    
    def column_rule_width(self, value: str, /) -> "StructuredCss":
        """Specifies the width of the rule between columns.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['column-rule-width'] = str(value)
        return self
    
    def column_span(self, value: Union[str, Literal["none", "all"]], /) -> "StructuredCss":
        """Specifies how many columns an element should span across.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['column-span'] = str(value)
        return self
    
    def column_width(self, value: str, /) -> "StructuredCss":
        """Specifies the optimal width of the columns.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['column-width'] = str(value)
        return self
    
    def columns(self, value: str, /) -> "StructuredCss":
        """Shorthand for column-width and column-count.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['columns'] = str(value)
        return self
    
    def contain(self, value: Union[str, Literal["none", "strict", "content", "size", "layout", "style", "paint"]], /) -> "StructuredCss":
        """Signals that an element and its contents are independent of the rest of the document tree.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['contain'] = str(value)
        return self
    
    def content(self, value: str, /) -> "StructuredCss":
        """Used with ::before and ::after pseudo-elements to insert content.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['content'] = str(value)
        return self
    
    def counter_increment(self, value: str, /) -> "StructuredCss":
        """Increments one or more counters.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['counter-increment'] = str(value)
        return self
    
    def counter_reset(self, value: str, /) -> "StructuredCss":
        """Creates or resets one or more counters.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['counter-reset'] = str(value)
        return self
    
    def counter_set(self, value: str, /) -> "StructuredCss":
        """Sets one or more counters to a specified value.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['counter-set'] = str(value)
        return self
    
    def cursor(self, value: Union[str, Literal["auto", "default", "pointer", "text"]], /) -> "StructuredCss":
        """Specifies the mouse cursor to be displayed when pointing over an element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['cursor'] = str(value)
        return self
    
    def direction(self, value: Union[str, Literal["ltr", "rtl"]], /) -> "StructuredCss":
        """Specifies the text direction/writing direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['direction'] = str(value)
        return self
    
    def display(self, value: Union[str, Literal["block", "inline", "inline-block", "flex", "grid", "none"]], /) -> "StructuredCss":
        """Specifies how an element is displayed.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['display'] = str(value)
        return self
    
    def empty_cells(self, value: Union[str, Literal["show", "hide"]], /) -> "StructuredCss":
        """Specifies whether or not to display borders and background on empty cells in a table.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['empty-cells'] = str(value)
        return self
    
    def filter(self, value: str, /) -> "StructuredCss":
        """Applies graphical effects like blur or color shift to an element.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['filter'] = str(value)
        return self
    
    def flex(self, value: str, /) -> "StructuredCss":
        """Shorthand for flex-grow, flex-shrink, flex-basis.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['flex'] = str(value)
        return self
    
    def flex_basis(self, value: str, /) -> "StructuredCss":
        """Specifies the initial length of a flex item.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['flex-basis'] = str(value)
        return self
    
    def flex_direction(self, value: Union[str, Literal["row", "row-reverse", "column", "column-reverse"]], /) -> "StructuredCss":
        """Specifies the direction of the flexible items.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['flex-direction'] = str(value)
        return self
    
    def flex_flow(self, value: str, /) -> "StructuredCss":
        """Shorthand for flex-direction and flex-wrap.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['flex-flow'] = str(value)
        return self
    
    def flex_grow(self, value: Union[int, float], /) -> "StructuredCss":
        """Specifies how much the item will grow relative to the rest.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['flex-grow'] = str(value)
        return self
    
    def flex_shrink(self, value: Union[int, float], /) -> "StructuredCss":
        """Specifies how much the item will shrink relative to the rest.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['flex-shrink'] = str(value)
        return self
    
    def flex_wrap(self, value: Union[str, Literal["nowrap", "wrap", "wrap-reverse"]], /) -> "StructuredCss":
        """Specifies whether the flexible items should wrap or not.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['flex-wrap'] = str(value)
        return self
    
    def float(self, value: Union[str, Literal["none", "left", "right"]], /) -> "StructuredCss":
        """Specifies whether an element should float to the left, right, or not at all.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['float'] = str(value)
        return self
    
    def font(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all font properties.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['font'] = str(value)
        return self
    
    def font_family(self, value: str, /) -> "StructuredCss":
        """Specifies the font family for text.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['font-family'] = str(value)
        return self
    
    def font_feature_settings(self, value: str, /) -> "StructuredCss":
        """Controls advanced typographic features in OpenType fonts.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['font-feature-settings'] = str(value)
        return self
    
    def font_kerning(self, value: Union[str, Literal["auto", "normal", "none"]], /) -> "StructuredCss":
        """Controls the usage of the kerning information.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-kerning'] = str(value)
        return self
    
    def font_language_override(self, value: str, /) -> "StructuredCss":
        """Controls the use of language-specific glyphs in a typeface.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['font-language-override'] = str(value)
        return self
    
    def font_optical_sizing(self, value: Union[str, Literal["auto", "none"]], /) -> "StructuredCss":
        """Enables automatic adjustments to font designs for different sizes.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-optical-sizing'] = str(value)
        return self
    
    def font_size(self, value: str, /) -> "StructuredCss":
        """Specifies the font size of text.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['font-size'] = str(value)
        return self
    
    def font_size_adjust(self, value: Union[int, float], /) -> "StructuredCss":
        """Preserves the readability of text when font fallback occurs.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['font-size-adjust'] = str(value)
        return self
    
    def font_stretch(self, value: Union[str, Literal["normal", "ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "semi-expanded", "expanded", "extra-expanded", "ultra-expanded"]], /) -> "StructuredCss":
        """Selects a normal, condensed, or expanded face from a font.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-stretch'] = str(value)
        return self
    
    def font_style(self, value: Union[str, Literal["normal", "italic", "oblique"]], /) -> "StructuredCss":
        """Specifies the font style for text.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-style'] = str(value)
        return self
    
    def font_synthesis(self, value: Union[str, Literal["none", "weight", "style"]], /) -> "StructuredCss":
        """Controls which missing typefaces can be synthesized by the browser.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-synthesis'] = str(value)
        return self
    
    def font_variant(self, value: Union[str, Literal["normal", "small-caps"]], /) -> "StructuredCss":
        """Specifies whether or not a text should be in small-caps.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-variant'] = str(value)
        return self
    
    def font_variant_alternates(self, value: str, /) -> "StructuredCss":
        """Controls the usage of alternate glyphs.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['font-variant-alternates'] = str(value)
        return self
    
    def font_variant_caps(self, value: Union[str, Literal["normal", "small-caps", "all-small-caps", "petite-caps", "all-petite-caps", "unicase", "titling-caps"]], /) -> "StructuredCss":
        """Controls the usage of alternate glyphs for capital letters.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-variant-caps'] = str(value)
        return self
    
    def font_variant_east_asian(self, value: Union[str, Literal["normal", "ruby"]], /) -> "StructuredCss":
        """Controls the usage of alternate glyphs for East Asian scripts.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-variant-east-asian'] = str(value)
        return self
    
    def font_variant_ligatures(self, value: Union[str, Literal["normal", "none", "common-ligatures"]], /) -> "StructuredCss":
        """Controls which ligatures and contextual forms are used in textual content.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-variant-ligatures'] = str(value)
        return self
    
    def font_variant_numeric(self, value: Union[str, Literal["normal", "ordinal", "slashed-zero"]], /) -> "StructuredCss":
        """Controls the usage of alternate glyphs for numbers, fractions, and ordinal markers.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-variant-numeric'] = str(value)
        return self
    
    def font_variant_position(self, value: Union[str, Literal["normal", "sub", "super"]], /) -> "StructuredCss":
        """Controls the usage of alternate, smaller glyphs that are positioned as superscript or subscript.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-variant-position'] = str(value)
        return self
    
    def font_variation_settings(self, value: str, /) -> "StructuredCss":
        """Allows low-level control over variable font characteristics.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['font-variation-settings'] = str(value)
        return self
    
    def font_weight(self, value: Union[str, Literal["normal", "bold", "bolder", "lighter", "100", "200"]], /) -> "StructuredCss":
        """Specifies the weight of the font.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['font-weight'] = str(value)
        return self
    
    def gap(self, value: str, /) -> "StructuredCss":
        """Shorthand for row-gap and column-gap.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['gap'] = str(value)
        return self
    
    def grid(self, value: str, /) -> "StructuredCss":
        """Shorthand for setting all grid properties.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid'] = str(value)
        return self
    
    def grid_area(self, value: str, /) -> "StructuredCss":
        """Specifies a grid item's size and location within the grid.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-area'] = str(value)
        return self
    
    def grid_auto_columns(self, value: str, /) -> "StructuredCss":
        """Specifies the size of an implicitly-created grid column track.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-auto-columns'] = str(value)
        return self
    
    def grid_auto_flow(self, value: Union[str, Literal["row", "column", "dense"]], /) -> "StructuredCss":
        """Controls how the auto-placement algorithm works.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['grid-auto-flow'] = str(value)
        return self
    
    def grid_auto_rows(self, value: str, /) -> "StructuredCss":
        """Specifies the size of an implicitly-created grid row track.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-auto-rows'] = str(value)
        return self
    
    def grid_column(self, value: str, /) -> "StructuredCss":
        """Shorthand for grid-column-start and grid-column-end.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-column'] = str(value)
        return self
    
    def grid_column_end(self, value: int, /) -> "StructuredCss":
        """Specifies where to end the grid item in the grid column.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['grid-column-end'] = str(value)
        return self
    
    def grid_column_gap(self, value: str, /) -> "StructuredCss":
        """Specifies the size of the gap between columns.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['grid-column-gap'] = str(value)
        return self
    
    def grid_column_start(self, value: int, /) -> "StructuredCss":
        """Specifies where to start the grid item in the grid column.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['grid-column-start'] = str(value)
        return self
    
    def grid_gap(self, value: str, /) -> "StructuredCss":
        """Shorthand for grid-row-gap and grid-column-gap.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['grid-gap'] = str(value)
        return self
    
    def grid_row(self, value: str, /) -> "StructuredCss":
        """Shorthand for grid-row-start and grid-row-end.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-row'] = str(value)
        return self
    
    def grid_row_end(self, value: int, /) -> "StructuredCss":
        """Specifies where to end the grid item in the grid row.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['grid-row-end'] = str(value)
        return self
    
    def grid_row_gap(self, value: str, /) -> "StructuredCss":
        """Specifies the size of the gap between rows.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['grid-row-gap'] = str(value)
        return self
    
    def grid_row_start(self, value: int, /) -> "StructuredCss":
        """Specifies where to start the grid item in the grid row.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['grid-row-start'] = str(value)
        return self
    
    def grid_template(self, value: str, /) -> "StructuredCss":
        """Shorthand for grid-template-rows, grid-template-columns, grid-template-areas.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-template'] = str(value)
        return self
    
    def grid_template_areas(self, value: str, /) -> "StructuredCss":
        """Specifies named grid areas.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['grid-template-areas'] = str(value)
        return self
    
    def grid_template_columns(self, value: str, /) -> "StructuredCss":
        """Specifies the size of the columns, and how many columns in a grid layout.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-template-columns'] = str(value)
        return self
    
    def grid_template_rows(self, value: str, /) -> "StructuredCss":
        """Specifies the size of the rows in a grid layout.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['grid-template-rows'] = str(value)
        return self
    
    def hanging_punctuation(self, value: Union[str, Literal["none", "first", "last", "allow-end", "force-end"]], /) -> "StructuredCss":
        """Specifies whether a punctuation mark may be placed outside the line box.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['hanging-punctuation'] = str(value)
        return self
    
    def height(self, value: str, /) -> "StructuredCss":
        """Specifies the height of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['height'] = str(value)
        return self
    
    def hyphens(self, value: Union[str, Literal["none", "manual", "auto"]], /) -> "StructuredCss":
        """Specifies how words should be hyphenated.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['hyphens'] = str(value)
        return self
    
    def hypen_ate_character(self, value: str, /) -> "StructuredCss":
        """Specifies a string that is used as the hyphenation character.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['hypen-ate-character'] = str(value)
        return self
    
    def image_orientation(self, value: Union[str, Literal["none", "from-image"]], /) -> "StructuredCss":
        """Specifies a rotation to be applied to an image before it is drawn.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['image-orientation'] = str(value)
        return self
    
    def image_rendering(self, value: Union[str, Literal["auto", "smooth", "high-quality", "crisp-edges", "pixelated"]], /) -> "StructuredCss":
        """Specifies the rendering quality of images.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['image-rendering'] = str(value)
        return self
    
    def inline_size(self, value: str, /) -> "StructuredCss":
        """Specifies the inline size of an element, depending on writing mode.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inline-size'] = str(value)
        return self
    
    def inset(self, value: str, /) -> "StructuredCss":
        """Shorthand for top, right, bottom, left for absolutely positioned elements.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset'] = str(value)
        return self
    
    def inset_block(self, value: str, /) -> "StructuredCss":
        """Specifies the position offset in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset-block'] = str(value)
        return self
    
    def inset_block_end(self, value: str, /) -> "StructuredCss":
        """Specifies the position offset from the block end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset-block-end'] = str(value)
        return self
    
    def inset_block_start(self, value: str, /) -> "StructuredCss":
        """Specifies the position offset from the block start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset-block-start'] = str(value)
        return self
    
    def inset_inline(self, value: str, /) -> "StructuredCss":
        """Specifies the position offset in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset-inline'] = str(value)
        return self
    
    def inset_inline_end(self, value: str, /) -> "StructuredCss":
        """Specifies the position offset from the inline end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset-inline-end'] = str(value)
        return self
    
    def inset_inline_start(self, value: str, /) -> "StructuredCss":
        """Specifies the position offset from the inline start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['inset-inline-start'] = str(value)
        return self
    
    def isolation(self, value: Union[str, Literal["auto", "isolate"]], /) -> "StructuredCss":
        """Defines whether an element must create a new stacking context.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['isolation'] = str(value)
        return self
    
    def justify_content(self, value: Union[str, Literal["flex-start", "flex-end", "center", "space-between", "space-around", "space-evenly"]], /) -> "StructuredCss":
        """Aligns the flexible container's items when the items do not use all available space on the main-axis.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['justify-content'] = str(value)
        return self
    
    def justify_items(self, value: Union[str, Literal["auto", "normal", "stretch"]], /) -> "StructuredCss":
        """Sets the default justify-self for all items of the box.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['justify-items'] = str(value)
        return self
    
    def justify_self(self, value: Union[str, Literal["auto", "normal", "stretch"]], /) -> "StructuredCss":
        """Sets the way a box is justified inside its alignment container along the appropriate axis.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['justify-self'] = str(value)
        return self
    
    def left(self, value: str, /) -> "StructuredCss":
        """Specifies the offset of an absolutely positioned element from the left of the container.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['left'] = str(value)
        return self
    
    def letter_spacing(self, value: str, /) -> "StructuredCss":
        """Increases or decreases the space between characters in a text.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['letter-spacing'] = str(value)
        return self
    
    def line_break(self, value: Union[str, Literal["auto", "loose", "normal", "strict", "anywhere"]], /) -> "StructuredCss":
        """Specifies how to break lines of Chinese, Japanese, or Korean text.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['line-break'] = str(value)
        return self
    
    def line_height(self, value: Union[int, float], /) -> "StructuredCss":
        """Sets the line height.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['line-height'] = str(value)
        return self
    
    def list_style(self, value: str, /) -> "StructuredCss":
        """Shorthand for list-style-type, list-style-position, list-style-image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['list-style'] = str(value)
        return self
    
    def list_style_image(self, value: str, /) -> "StructuredCss":
        """Specifies an image as the list-item marker.

        *@generated*

        Args:
            value: The value. Expected `url`.
        """
        self.k['list-style-image'] = str(value)
        return self
    
    def list_style_position(self, value: Union[str, Literal["inside", "outside"]], /) -> "StructuredCss":
        """Specifies the position of the list-item markers.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['list-style-position'] = str(value)
        return self
    
    def list_style_type(self, value: Union[str, Literal["disc", "circle", "square", "decimal", "none"]], /) -> "StructuredCss":
        """Specifies the type of list-item marker.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['list-style-type'] = str(value)
        return self
    
    def margin(self, value: str, /) -> "StructuredCss":
        """Shorthand for margin-top, margin-right, margin-bottom, margin-left.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin'] = str(value)
        return self
    
    def margin_block(self, value: str, /) -> "StructuredCss":
        """Specifies the margin in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-block'] = str(value)
        return self
    
    def margin_block_end(self, value: str, /) -> "StructuredCss":
        """Specifies the margin at the block end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-block-end'] = str(value)
        return self
    
    def margin_block_start(self, value: str, /) -> "StructuredCss":
        """Specifies the margin at the block start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-block-start'] = str(value)
        return self
    
    def margin_bottom(self, value: str, /) -> "StructuredCss":
        """Sets the bottom margin of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-bottom'] = str(value)
        return self
    
    def margin_inline(self, value: str, /) -> "StructuredCss":
        """Specifies the margin in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-inline'] = str(value)
        return self
    
    def margin_inline_end(self, value: str, /) -> "StructuredCss":
        """Specifies the margin at the inline end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-inline-end'] = str(value)
        return self
    
    def margin_inline_start(self, value: str, /) -> "StructuredCss":
        """Specifies the margin at the inline start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-inline-start'] = str(value)
        return self
    
    def margin_left(self, value: str, /) -> "StructuredCss":
        """Sets the left margin of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-left'] = str(value)
        return self
    
    def margin_right(self, value: str, /) -> "StructuredCss":
        """Sets the right margin of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-right'] = str(value)
        return self
    
    def margin_top(self, value: str, /) -> "StructuredCss":
        """Sets the top margin of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['margin-top'] = str(value)
        return self
    
    def mask(self, value: str, /) -> "StructuredCss":
        """Shorthand for mask-image, mask-mode, mask-position, mask-size, mask-repeat, mask-origin, mask-clip, mask-composite.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['mask'] = str(value)
        return self
    
    def mask_clip(self, value: Union[str, Literal["content-box", "padding-box", "border-box"]], /) -> "StructuredCss":
        """Specifies the mask painting area.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['mask-clip'] = str(value)
        return self
    
    def mask_composite(self, value: Union[str, Literal["add", "subtract", "intersect", "exclude"]], /) -> "StructuredCss":
        """Specifies how mask layers are composited.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['mask-composite'] = str(value)
        return self
    
    def mask_image(self, value: str, /) -> "StructuredCss":
        """Specifies the mask image.

        *@generated*

        Args:
            value: The value. Expected `url`.
        """
        self.k['mask-image'] = str(value)
        return self
    
    def mask_mode(self, value: Union[str, Literal["alpha", "luminance", "match-source"]], /) -> "StructuredCss":
        """Specifies whether the mask layer image is treated as a luminance or alpha mask.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['mask-mode'] = str(value)
        return self
    
    def mask_origin(self, value: Union[str, Literal["content-box", "padding-box", "border-box"]], /) -> "StructuredCss":
        """Specifies the origin position of a mask image.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['mask-origin'] = str(value)
        return self
    
    def mask_position(self, value: str, /) -> "StructuredCss":
        """Specifies the initial position of a mask image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['mask-position'] = str(value)
        return self
    
    def mask_repeat(self, value: Union[str, Literal["repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round"]], /) -> "StructuredCss":
        """Specifies how the mask image is repeated.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['mask-repeat'] = str(value)
        return self
    
    def mask_size(self, value: str, /) -> "StructuredCss":
        """Specifies the size of the mask image.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['mask-size'] = str(value)
        return self
    
    def max_block_size(self, value: str, /) -> "StructuredCss":
        """Sets the maximum size of an element in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['max-block-size'] = str(value)
        return self
    
    def max_height(self, value: str, /) -> "StructuredCss":
        """Sets the maximum height of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['max-height'] = str(value)
        return self
    
    def max_inline_size(self, value: str, /) -> "StructuredCss":
        """Sets the maximum size of an element in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['max-inline-size'] = str(value)
        return self
    
    def max_width(self, value: str, /) -> "StructuredCss":
        """Sets the maximum width of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['max-width'] = str(value)
        return self
    
    def min_block_size(self, value: str, /) -> "StructuredCss":
        """Sets the minimum size of an element in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['min-block-size'] = str(value)
        return self
    
    def min_height(self, value: str, /) -> "StructuredCss":
        """Sets the minimum height of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['min-height'] = str(value)
        return self
    
    def min_inline_size(self, value: str, /) -> "StructuredCss":
        """Sets the minimum size of an element in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['min-inline-size'] = str(value)
        return self
    
    def min_width(self, value: str, /) -> "StructuredCss":
        """Sets the minimum width of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['min-width'] = str(value)
        return self
    
    def mix_blend_mode(self, value: Union[str, Literal["normal", "multiply", "screen"]], /) -> "StructuredCss":
        """Specifies how an element's content should blend with the content of the element's parent and background.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['mix-blend-mode'] = str(value)
        return self
    
    def object_fit(self, value: Union[str, Literal["fill", "contain", "cover", "none", "scale-down"]], /) -> "StructuredCss":
        """Specifies how the contents of a replaced element should be fitted to the box established by its used height and width.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['object-fit'] = str(value)
        return self
    
    def object_position(self, value: str, /) -> "StructuredCss":
        """Specifies the alignment of the replaced element's contents within the element's box.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['object-position'] = str(value)
        return self
    
    def offset(self, value: str, /) -> "StructuredCss":
        """Shorthand for offset-path, offset-distance, offset-rotate, offset-anchor.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['offset'] = str(value)
        return self
    
    def offset_anchor(self, value: str, /) -> "StructuredCss":
        """Specifies a point on the positioned element that is the point that is moved along the offset-path.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['offset-anchor'] = str(value)
        return self
    
    def offset_distance(self, value: str, /) -> "StructuredCss":
        """Specifies the position along an offset-path.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['offset-distance'] = str(value)
        return self
    
    def offset_path(self, value: str, /) -> "StructuredCss":
        """Specifies the path an element follows for positioning along an offset.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['offset-path'] = str(value)
        return self
    
    def offset_rotate(self, value: str, /) -> "StructuredCss":
        """Specifies the orientation of the element along the offset-path.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['offset-rotate'] = str(value)
        return self
    
    def opacity(self, value: Union[int, float], /) -> "StructuredCss":
        """Specifies the transparency of an element.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['opacity'] = str(value)
        return self
    
    def order(self, value: int, /) -> "StructuredCss":
        """Specifies the order of a flexible item relative to the rest of the flexible items inside the same container.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['order'] = str(value)
        return self
    
    def orphans(self, value: int, /) -> "StructuredCss":
        """Specifies the minimum number of lines that must be left at the bottom of a page or column.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['orphans'] = str(value)
        return self
    
    def outline(self, value: str, /) -> "StructuredCss":
        """Shorthand for outline-width, outline-style, outline-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['outline'] = str(value)
        return self
    
    def outline_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Sets the color of an outline.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['outline-color'] = str(value)
        return self
    
    def outline_offset(self, value: str, /) -> "StructuredCss":
        """Sets the space between an outline and the edge or border of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['outline-offset'] = str(value)
        return self
    
    def outline_style(self, value: Union[str, Literal["none", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"]], /) -> "StructuredCss":
        """Sets the style of an outline.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['outline-style'] = str(value)
        return self
    
    def outline_width(self, value: str, /) -> "StructuredCss":
        """Sets the width of an outline.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['outline-width'] = str(value)
        return self
    
    def overflow(self, value: Union[str, Literal["visible", "hidden", "scroll", "auto"]], /) -> "StructuredCss":
        """Specifies what happens if content overflows an element's box.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow'] = str(value)
        return self
    
    def overflow_anchor(self, value: Union[str, Literal["auto", "none"]], /) -> "StructuredCss":
        """Opts out of scroll anchoring behavior.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow-anchor'] = str(value)
        return self
    
    def overflow_block(self, value: Union[str, Literal["visible", "hidden", "scroll", "auto"]], /) -> "StructuredCss":
        """Specifies what to do when content overflows the block direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow-block'] = str(value)
        return self
    
    def overflow_clip_margin(self, value: str, /) -> "StructuredCss":
        """Specifies how far the overflow clipping should extend from the element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['overflow-clip-margin'] = str(value)
        return self
    
    def overflow_inline(self, value: Union[str, Literal["visible", "hidden", "scroll", "auto"]], /) -> "StructuredCss":
        """Specifies what to do when content overflows the inline direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow-inline'] = str(value)
        return self
    
    def overflow_wrap(self, value: Union[str, Literal["normal", "anywhere", "break-word"]], /) -> "StructuredCss":
        """Specifies whether the browser may break lines within words to prevent overflow.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow-wrap'] = str(value)
        return self
    
    def overflow_x(self, value: Union[str, Literal["visible", "hidden", "scroll", "auto"]], /) -> "StructuredCss":
        """Specifies what to do with the left/right edges of the content if it overflows the element's content area.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow-x'] = str(value)
        return self
    
    def overflow_y(self, value: Union[str, Literal["visible", "hidden", "scroll", "auto"]], /) -> "StructuredCss":
        """Specifies what to do with the top/bottom edges of the content if it overflows the element's content area.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overflow-y'] = str(value)
        return self
    
    def overscroll_behavior(self, value: Union[str, Literal["auto", "contain", "none"]], /) -> "StructuredCss":
        """Specifies the browser behavior on overscroll.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overscroll-behavior'] = str(value)
        return self
    
    def overscroll_behavior_block(self, value: Union[str, Literal["auto", "contain", "none"]], /) -> "StructuredCss":
        """Specifies the browser behavior on overscroll in the block direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overscroll-behavior-block'] = str(value)
        return self
    
    def overscroll_behavior_inline(self, value: Union[str, Literal["auto", "contain", "none"]], /) -> "StructuredCss":
        """Specifies the browser behavior on overscroll in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overscroll-behavior-inline'] = str(value)
        return self
    
    def overscroll_behavior_x(self, value: Union[str, Literal["auto", "contain", "none"]], /) -> "StructuredCss":
        """Specifies the browser behavior on overscroll in the x direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overscroll-behavior-x'] = str(value)
        return self
    
    def overscroll_behavior_y(self, value: Union[str, Literal["auto", "contain", "none"]], /) -> "StructuredCss":
        """Specifies the browser behavior on overscroll in the y direction.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['overscroll-behavior-y'] = str(value)
        return self
    
    def padding(self, value: str, /) -> "StructuredCss":
        """Shorthand for padding-top, padding-right, padding-bottom, padding-left.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding'] = str(value)
        return self
    
    def padding_block(self, value: str, /) -> "StructuredCss":
        """Specifies the padding in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-block'] = str(value)
        return self
    
    def padding_block_end(self, value: str, /) -> "StructuredCss":
        """Specifies the padding at the block end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-block-end'] = str(value)
        return self
    
    def padding_block_start(self, value: str, /) -> "StructuredCss":
        """Specifies the padding at the block start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-block-start'] = str(value)
        return self
    
    def padding_bottom(self, value: str, /) -> "StructuredCss":
        """Sets the bottom padding of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-bottom'] = str(value)
        return self
    
    def padding_inline(self, value: str, /) -> "StructuredCss":
        """Specifies the padding in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-inline'] = str(value)
        return self
    
    def padding_inline_end(self, value: str, /) -> "StructuredCss":
        """Specifies the padding at the inline end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-inline-end'] = str(value)
        return self
    
    def padding_inline_start(self, value: str, /) -> "StructuredCss":
        """Specifies the padding at the inline start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-inline-start'] = str(value)
        return self
    
    def padding_left(self, value: str, /) -> "StructuredCss":
        """Sets the left padding of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-left'] = str(value)
        return self
    
    def padding_right(self, value: str, /) -> "StructuredCss":
        """Sets the right padding of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-right'] = str(value)
        return self
    
    def padding_top(self, value: str, /) -> "StructuredCss":
        """Sets the top padding of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['padding-top'] = str(value)
        return self
    
    def page_break_after(self, value: Union[str, Literal["auto", "always", "avoid", "left", "right"]], /) -> "StructuredCss":
        """Adjusts page breaks after the current element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['page-break-after'] = str(value)
        return self
    
    def page_break_before(self, value: Union[str, Literal["auto", "always", "avoid", "left", "right"]], /) -> "StructuredCss":
        """Adjusts page breaks before the current element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['page-break-before'] = str(value)
        return self
    
    def page_break_inside(self, value: Union[str, Literal["auto", "avoid"]], /) -> "StructuredCss":
        """Adjusts page breaks inside the current element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['page-break-inside'] = str(value)
        return self
    
    def paint_order(self, value: Union[str, Literal["normal", "fill", "stroke", "markers"]], /) -> "StructuredCss":
        """Controls the order in which paint operations are performed for text and shape elements.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['paint-order'] = str(value)
        return self
    
    def perspective(self, value: str, /) -> "StructuredCss":
        """Gives a 3D-positioned element some perspective.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['perspective'] = str(value)
        return self
    
    def perspective_origin(self, value: str, /) -> "StructuredCss":
        """Defines at which position the user is looking at the 3D-positioned element.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['perspective-origin'] = str(value)
        return self
    
    def place_content(self, value: str, /) -> "StructuredCss":
        """Shorthand for align-content and justify-content.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['place-content'] = str(value)
        return self
    
    def place_items(self, value: str, /) -> "StructuredCss":
        """Shorthand for align-items and justify-items.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['place-items'] = str(value)
        return self
    
    def place_self(self, value: str, /) -> "StructuredCss":
        """Shorthand for align-self and justify-self.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['place-self'] = str(value)
        return self
    
    def pointer_events(self, value: Union[str, Literal["auto", "none"]], /) -> "StructuredCss":
        """Specifies whether or not element reacts to pointer events.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['pointer-events'] = str(value)
        return self
    
    def position(self, value: Union[str, Literal["static", "relative", "absolute", "fixed", "sticky"]], /) -> "StructuredCss":
        """Specifies the positioning method used for an element (static, relative, absolute, fixed, or sticky).

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['position'] = str(value)
        return self
    
    def print_color_adjust(self, value: Union[str, Literal["economy", "exact"]], /) -> "StructuredCss":
        """Controls what, if any, adjustments the user agent may make to optimize the appearance for printing.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['print-color-adjust'] = str(value)
        return self
    
    def quotes(self, value: str, /) -> "StructuredCss":
        """Sets the type of quotation marks for embedded quotations.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['quotes'] = str(value)
        return self
    
    def resize(self, value: Union[str, Literal["none", "both", "horizontal", "vertical"]], /) -> "StructuredCss":
        """Specifies if (and on which sides) an element is resizable by the user.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['resize'] = str(value)
        return self
    
    def right(self, value: str, /) -> "StructuredCss":
        """Specifies the offset of an absolutely positioned element from the right of the container.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['right'] = str(value)
        return self
    
    def rotate(self, value: str, /) -> "StructuredCss":
        """Rotates an element around a fixed point on the page.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['rotate'] = str(value)
        return self
    
    def row_gap(self, value: str, /) -> "StructuredCss":
        """Specifies the gap between the grid rows.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['row-gap'] = str(value)
        return self
    
    def scale(self, value: Union[int, float], /) -> "StructuredCss":
        """Scales an element up or down on the 2D plane.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['scale'] = str(value)
        return self
    
    def scroll_behavior(self, value: Union[str, Literal["auto", "smooth"]], /) -> "StructuredCss":
        """Specifies whether to smoothly animate the scroll position in a scrollable box.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scroll-behavior'] = str(value)
        return self
    
    def scroll_margin(self, value: str, /) -> "StructuredCss":
        """Shorthand for scroll-margin-top, scroll-margin-right, scroll-margin-bottom, scroll-margin-left.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin'] = str(value)
        return self
    
    def scroll_margin_block(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margins in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-block'] = str(value)
        return self
    
    def scroll_margin_block_end(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the block end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-block-end'] = str(value)
        return self
    
    def scroll_margin_block_start(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the block start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-block-start'] = str(value)
        return self
    
    def scroll_margin_bottom(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the bottom.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-bottom'] = str(value)
        return self
    
    def scroll_margin_inline(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margins in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-inline'] = str(value)
        return self
    
    def scroll_margin_inline_end(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the inline end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-inline-end'] = str(value)
        return self
    
    def scroll_margin_inline_start(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the inline start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-inline-start'] = str(value)
        return self
    
    def scroll_margin_left(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the left.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-left'] = str(value)
        return self
    
    def scroll_margin_right(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the right.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-right'] = str(value)
        return self
    
    def scroll_margin_top(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll margin at the top.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-margin-top'] = str(value)
        return self
    
    def scroll_padding(self, value: str, /) -> "StructuredCss":
        """Shorthand for scroll-padding-top, scroll-padding-right, scroll-padding-bottom, scroll-padding-left.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding'] = str(value)
        return self
    
    def scroll_padding_block(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding in the block direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-block'] = str(value)
        return self
    
    def scroll_padding_block_end(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the block end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-block-end'] = str(value)
        return self
    
    def scroll_padding_block_start(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the block start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-block-start'] = str(value)
        return self
    
    def scroll_padding_bottom(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the bottom.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-bottom'] = str(value)
        return self
    
    def scroll_padding_inline(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding in the inline direction.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-inline'] = str(value)
        return self
    
    def scroll_padding_inline_end(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the inline end.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-inline-end'] = str(value)
        return self
    
    def scroll_padding_inline_start(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the inline start.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-inline-start'] = str(value)
        return self
    
    def scroll_padding_left(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the left.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-left'] = str(value)
        return self
    
    def scroll_padding_right(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the right.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-right'] = str(value)
        return self
    
    def scroll_padding_top(self, value: str, /) -> "StructuredCss":
        """Specifies the scroll padding at the top.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['scroll-padding-top'] = str(value)
        return self
    
    def scroll_snap_align(self, value: Union[str, Literal["none", "start", "end", "center"]], /) -> "StructuredCss":
        """Specifies the box's snap position as an alignment of its snap area within its snap container's snapport.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scroll-snap-align'] = str(value)
        return self
    
    def scroll_snap_stop(self, value: Union[str, Literal["normal", "always"]], /) -> "StructuredCss":
        """Defines whether the scroll container is allowed to snap to a snap position that is not the first in a sequence of snap positions.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scroll-snap-stop'] = str(value)
        return self
    
    def scroll_snap_type(self, value: Union[str, Literal["none", "x", "y", "block", "inline", "both", "proximity", "mandatory"]], /) -> "StructuredCss":
        """Defines the strictness of snap positions in a scroll container.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scroll-snap-type'] = str(value)
        return self
    
    def scroll_timeline(self, value: str, /) -> "StructuredCss":
        """Defines a named timeline for scrolling an element.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['scroll-timeline'] = str(value)
        return self
    
    def scroll_timeline_axis(self, value: Union[str, Literal["block", "inline", "x", "y"]], /) -> "StructuredCss":
        """Defines the axis of the scroll timeline.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scroll-timeline-axis'] = str(value)
        return self
    
    def scroll_timeline_name(self, value: str, /) -> "StructuredCss":
        """Defines the name of the scroll timeline.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['scroll-timeline-name'] = str(value)
        return self
    
    def scrollbar_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Specifies the color of the scrollbar track and thumb.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['scrollbar-color'] = str(value)
        return self
    
    def scrollbar_gutter(self, value: Union[str, Literal["auto", "stable", "always"]], /) -> "StructuredCss":
        """Reserves space for the scrollbar, preventing unwanted layout changes as the scrollbar appears and disappears.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scrollbar-gutter'] = str(value)
        return self
    
    def scrollbar_width(self, value: Union[str, Literal["auto", "thin", "none"]], /) -> "StructuredCss":
        """Specifies the width of the scrollbar.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['scrollbar-width'] = str(value)
        return self
    
    def shape_image_threshold(self, value: Union[int, float], /) -> "StructuredCss":
        """Defines the alpha channel threshold used to extract the shape using an image.

        *@generated*

        Args:
            value: The value. Expected `number`.
        """
        self.k['shape-image-threshold'] = str(value)
        return self
    
    def shape_margin(self, value: str, /) -> "StructuredCss":
        """Sets a margin on a shape created with shape-outside.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['shape-margin'] = str(value)
        return self
    
    def shape_outside(self, value: str, /) -> "StructuredCss":
        """Defines a shape around which inline content wraps.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['shape-outside'] = str(value)
        return self
    
    def tab_size(self, value: int, /) -> "StructuredCss":
        """Specifies the width of a tab character.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['tab-size'] = str(value)
        return self
    
    def table_layout(self, value: Union[str, Literal["auto", "fixed"]], /) -> "StructuredCss":
        """Specifies the algorithm used to lay out table cells, rows, and columns.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['table-layout'] = str(value)
        return self
    
    def text_align(self, value: Union[str, Literal["left", "right", "center", "justify"]], /) -> "StructuredCss":
        """Specifies the horizontal alignment of text.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-align'] = str(value)
        return self
    
    def text_align_last(self, value: Union[str, Literal["auto", "left", "right", "center", "justify"]], /) -> "StructuredCss":
        """Describes how the last line of a block or a line right before a forced line break is aligned when text-align is 'justify'.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-align-last'] = str(value)
        return self
    
    def text_combine_upright(self, value: Union[str, Literal["none", "all"]], /) -> "StructuredCss":
        """Specifies the combination of multiple characters into the space of a single character.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-combine-upright'] = str(value)
        return self
    
    def text_decoration(self, value: str, /) -> "StructuredCss":
        """Shorthand for text-decoration-line, text-decoration-color, text-decoration-style, text-decoration-thickness.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['text-decoration'] = str(value)
        return self
    
    def text_decoration_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Specifies the color of text decorations.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['text-decoration-color'] = str(value)
        return self
    
    def text_decoration_line(self, value: Union[str, Literal["none", "underline", "overline", "line-through", "blink"]], /) -> "StructuredCss":
        """Specifies the type of line in a text decoration.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-decoration-line'] = str(value)
        return self
    
    def text_decoration_skip(self, value: Union[str, Literal["none", "objects", "spaces", "ink", "edges", "box-decoration"]], /) -> "StructuredCss":
        """Specifies what parts of the content are skipped over when applying text decoration.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-decoration-skip'] = str(value)
        return self
    
    def text_decoration_skip_ink(self, value: Union[str, Literal["auto", "none", "all"]], /) -> "StructuredCss":
        """Specifies how overlines and underlines are drawn when they pass over glyphs.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-decoration-skip-ink'] = str(value)
        return self
    
    def text_decoration_style(self, value: Union[str, Literal["solid", "double", "dotted", "dashed", "wavy"]], /) -> "StructuredCss":
        """Specifies the style of the line in a text decoration.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-decoration-style'] = str(value)
        return self
    
    def text_decoration_thickness(self, value: str, /) -> "StructuredCss":
        """Specifies the thickness of the text decoration line.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['text-decoration-thickness'] = str(value)
        return self
    
    def text_emphasis(self, value: str, /) -> "StructuredCss":
        """Shorthand for text-emphasis-style and text-emphasis-color.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['text-emphasis'] = str(value)
        return self
    
    def text_emphasis_color(self, value: Union[str, StandardColor], /) -> "StructuredCss":
        """Specifies the color of emphasis marks.

        *@generated*

        Args:
            value: The value. Expected `color`.
        """
        self.k['text-emphasis-color'] = str(value)
        return self
    
    def text_emphasis_position(self, value: Union[str, Literal["over", "under", "right", "left"]], /) -> "StructuredCss":
        """Specifies the position of emphasis marks.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-emphasis-position'] = str(value)
        return self
    
    def text_emphasis_style(self, value: str, /) -> "StructuredCss":
        """Specifies the style of emphasis marks.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['text-emphasis-style'] = str(value)
        return self
    
    def text_indent(self, value: str, /) -> "StructuredCss":
        """Specifies the indentation of the first line in a text-block.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['text-indent'] = str(value)
        return self
    
    def text_justify(self, value: Union[str, Literal["auto", "inter-character", "inter-word", "none"]], /) -> "StructuredCss":
        """Specifies the justification method used when text-align is 'justify'.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-justify'] = str(value)
        return self
    
    def text_orientation(self, value: Union[str, Literal["mixed", "upright", "sideways"]], /) -> "StructuredCss":
        """Defines the orientation of the text in a line.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-orientation'] = str(value)
        return self
    
    def text_overflow(self, value: Union[str, Literal["clip", "ellipsis"]], /) -> "StructuredCss":
        """Specifies what should happen when text overflows the containing element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-overflow'] = str(value)
        return self
    
    def text_rendering(self, value: Union[str, Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"]], /) -> "StructuredCss":
        """Provides information to the browser about what to optimize for when rendering text.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-rendering'] = str(value)
        return self
    
    def text_shadow(self, value: str, /) -> "StructuredCss":
        """Adds shadow to text.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['text-shadow'] = str(value)
        return self
    
    def text_transform(self, value: Union[str, Literal["none", "capitalize", "uppercase", "lowercase", "full-width", "full-size-kana"]], /) -> "StructuredCss":
        """Controls the capitalization of text.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-transform'] = str(value)
        return self
    
    def text_underline_offset(self, value: str, /) -> "StructuredCss":
        """Specifies the offset of underlines from their original position.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['text-underline-offset'] = str(value)
        return self
    
    def text_underline_position(self, value: Union[str, Literal["auto", "under", "left", "right"]], /) -> "StructuredCss":
        """Specifies the position of the underline text decoration.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['text-underline-position'] = str(value)
        return self
    
    def top(self, value: str, /) -> "StructuredCss":
        """Specifies the offset of an absolutely positioned element from the top of the container.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['top'] = str(value)
        return self
    
    def touch_action(self, value: Union[str, Literal["auto", "none", "pan-x", "pan-y", "manipulation"]], /) -> "StructuredCss":
        """Determines whether touch input may trigger default behavior supplied by the user agent.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['touch-action'] = str(value)
        return self
    
    def transform(self, value: str, /) -> "StructuredCss":
        """Applies a 2D or 3D transformation to an element.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['transform'] = str(value)
        return self
    
    def transform_box(self, value: Union[str, Literal["content-box", "border-box", "fill-box", "stroke-box", "view-box"]], /) -> "StructuredCss":
        """Defines the layout box to which the transform and transform-origin properties relate.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['transform-box'] = str(value)
        return self
    
    def transform_origin(self, value: str, /) -> "StructuredCss":
        """Changes the position on transformed elements.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['transform-origin'] = str(value)
        return self
    
    def transform_style(self, value: Union[str, Literal["flat", "preserve-3d"]], /) -> "StructuredCss":
        """Specifies whether the children of an element are positioned in 3D space or flattened.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['transform-style'] = str(value)
        return self
    
    def transition(self, value: str, /) -> "StructuredCss":
        """Shorthand for transition-property, transition-duration, transition-timing-function, transition-delay.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['transition'] = str(value)
        return self
    
    def transition_delay(self, value: str, /) -> "StructuredCss":
        """Specifies when the transition effect will start.

        *@generated*

        Args:
            value: The value. Expected `time`.
        """
        self.k['transition-delay'] = str(value)
        return self
    
    def transition_duration(self, value: str, /) -> "StructuredCss":
        """Specifies how many seconds or milliseconds a transition effect takes to complete.

        *@generated*

        Args:
            value: The value. Expected `time`.
        """
        self.k['transition-duration'] = str(value)
        return self
    
    def transition_property(self, value: str, /) -> "StructuredCss":
        """Specifies the name of the CSS property the transition effect is for.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['transition-property'] = str(value)
        return self
    
    def transition_timing_function(self, value: Union[str, Literal["ease", "linear", "ease-in", "ease-out", "ease-in-out"]], /) -> "StructuredCss":
        """Specifies the speed curve of the transition effect.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['transition-timing-function'] = str(value)
        return self
    
    def translate(self, value: str, /) -> "StructuredCss":
        """Repositions an element in the horizontal and/or vertical directions.

        *@generated*

        Args:
            value: The value. Expected `complex`.
        """
        self.k['translate'] = str(value)
        return self
    
    def unicode_bidi(self, value: Union[str, Literal["normal", "embed", "bidi-override"]], /) -> "StructuredCss":
        """Used together with the direction property to set or return whether the text should be overridden to support multiple languages in the same document.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['unicode-bidi'] = str(value)
        return self
    
    def user_select(self, value: Union[str, Literal["auto", "text", "none", "contain", "all"]], /) -> "StructuredCss":
        """Specifies whether the text of an element can be selected.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['user-select'] = str(value)
        return self
    
    def vertical_align(self, value: Union[str, Literal["baseline", "sub", "super", "top", "text-top", "middle", "bottom", "text-bottom"]], /) -> "StructuredCss":
        """Sets the vertical alignment of an element.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['vertical-align'] = str(value)
        return self
    
    def visibility(self, value: Union[str, Literal["visible", "hidden", "collapse"]], /) -> "StructuredCss":
        """Specifies whether or not an element is visible.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['visibility'] = str(value)
        return self
    
    def white_space(self, value: Union[str, Literal["normal", "nowrap", "pre", "pre-line", "pre-wrap"]], /) -> "StructuredCss":
        """Specifies how white-space inside an element is handled.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['white-space'] = str(value)
        return self
    
    def widows(self, value: int, /) -> "StructuredCss":
        """Sets the minimum number of lines that must be left at the top of a page or column.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['widows'] = str(value)
        return self
    
    def width(self, value: str, /) -> "StructuredCss":
        """Specifies the width of an element.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['width'] = str(value)
        return self
    
    def will_change(self, value: str, /) -> "StructuredCss":
        """Provides a hint to the browser about what properties are expected to change.

        *@generated*

        Args:
            value: The value. Expected `string`.
        """
        self.k['will-change'] = str(value)
        return self
    
    def word_break(self, value: Union[str, Literal["normal", "break-all", "keep-all", "break-word"]], /) -> "StructuredCss":
        """Specifies how words should break when reaching the end of a line.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['word-break'] = str(value)
        return self
    
    def word_spacing(self, value: str, /) -> "StructuredCss":
        """Increases or decreases the space between words in a text.

        *@generated*

        Args:
            value: The value. Expected `length`.
        """
        self.k['word-spacing'] = str(value)
        return self
    
    def writing_mode(self, value: Union[str, Literal["horizontal-tb", "vertical-rl", "vertical-lr"]], /) -> "StructuredCss":
        """Specifies whether lines of text are laid out horizontally or vertically.

        *@generated*

        Args:
            value: The value. Expected `enum`.
        """
        self.k['writing-mode'] = str(value)
        return self
    
    def z_index(self, value: int, /) -> "StructuredCss":
        """Sets the stack order of a positioned element.

        *@generated*

        Args:
            value: The value. Expected `integer`.
        """
        self.k['z-index'] = str(value)
        return self
    

    def extras(self, k: Dict[str, Any]):
        """Add extra items to the CSS dictionary.
        
        Args:
            k (dict[str, Any]): The extra contents.
        """
        self.k |= k

    def _inline_style(self) -> str:
        """Create the inline style string."""
        res = ""
        for k, v in self.k.items():
            res += k + ": " + v + ";"

        return res

    def __str__(self) -> str:
        return self._inline_style()

    def __repr__(self) -> str:
        return self._inline_style()


def css(df: Optional[Dict[str, Any]] = None, /) -> StructuredCss:
    """Create a structured css instance.

    This enables typing intellisense, if available.

    Args:
        df (dict[str, Any], optional): Default CSS items, if any.
    """
    return StructuredCss(df)
