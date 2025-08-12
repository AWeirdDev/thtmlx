# create a shortcut
import thtmlx as x

# create a div
ele = x.div(
    x.p("Welcome to typed html!"),
    x.a("hot pics", href="https://discord.com/jobs", target="_blank"),
    x.p("click on it lil bro"),
    # apply *typed* css styles
    style=(
        x.css()
        .display("flex")
        .flex_direction("row")
        .align_items("center")
        .justify_content("space-between")
        .color("white")
        .background_color("red")
    ),
)

print(ele)