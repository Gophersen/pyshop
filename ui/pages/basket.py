import reflex as rx

from layouts.main import main_layout


def basket_page():
    content = rx.vstack(
        rx.text(
            "سبد خرید من",
            color="black",
            size="6",
        ),
        rx.hstack(
            rx.text(
                "۲ عدد",
                color="black",
                width="50px",
                height="30px",
                border_radius="10px",
                bg="#C2D4F8",
                display="flex",
                align_items="center",
                justify_content="center",
                direction="rtl",
            ),
            rx.vstack(
                rx.text(
                    "نام محصول",
                    color="black",
                    size="5",
                    cursor="pointer",
                ),
                rx.text(
                    "۲ x ۳۵,۰۰۰,۰۰۰",
                    color="grey",
                    size="2",
                ),
                rx.text(
                    "مجموع: ۷۰,۰۰۰,۰۰۰",
                    color="grey",
                    size="2",
                ),
                align="center",
            ),
            rx.avatar(
                fallback="MA",
                size="5",
                cursor="pointer",
            ),
            rx.icon(
                "x",
                color="white",
                width="25px",
                height="25px",
                bg="red",
                border_radius="20px",
                cursor="pointer",
            ),
            justify="between",
            width="100%",
            bg="white",
            border_radius="10px",
            align="center",
            padding="25px",
        ),
        rx.separator(
            bg="grey",
        ),
        rx.hstack(
            rx.button(
                "پرداخت",
                color_scheme="amber",
                cursor="pointer",
            ),
            rx.text(
                "پرداخت: ۷۰,۰۰۰,۰۰۰ تومان",
                color="black",
                direction="rtl",
            ),
            justify="between",
            width="100%",
            bg="white",
            padding="25px",
        ),
        align="center",
        justify="between",
        width="100%",
    )
    return main_layout(content=content)
