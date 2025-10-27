import reflex as rx

from components.header import header_component


def main_layout(content):
    layout_content = rx.box(
        header_component(),
        rx.hstack(
            rx.hstack(
                content,
                width=rx.breakpoints(
                    initial="100%",
                    sm="70%",
                    lg="35%",
                ),
                justify="center",
                padding="10px",
                margin_top="70px",
            ),
            justify="center",
            width="100%",
        ),
        style={"body": {"overview": "hidden"}},
    )
    return layout_content
