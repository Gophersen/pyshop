import reflex as rx

from components.header import header_component


def main_layout(content):
    layout_content = rx.box(
        header_component(),
        content,
    )
    return layout_content
