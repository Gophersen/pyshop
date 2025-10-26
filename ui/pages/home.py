import reflex as rx

from layouts.main import main_layout
from components.product_card import products_column
from components.carousel import carousel


def simple_banner(src: str, margin_top: str = ""):
    content = (
        rx.image(
            src=src,
            border_radius="10px",
            margin_top=margin_top,
            cursor="pointer",
        ),
    )
    return content


def brand_box():
    content = (
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.avatar(fallback="MA"),
                    rx.text(
                        "اسم",
                        color="black",
                    ),
                    align="center",
                ),
                justify="center",
                width="100%",
            ),
            bg="white",
            width="25%",
            align_items="center",
            display="flex",
            justify_content="center",
            height="10vh",
            border_radius="10px",
            cursor="pointer",
        ),
    )

    return content


def brands_boxes(margin_top: str = ""):
    boxes = [brand_box() for i in range(4)]
    content = rx.hstack(
        *boxes,
        margin_top=margin_top,
        justify="between",
        width="100%",
    )
    return content


def products_heading(title: str):
    content = rx.hstack(
        rx.hstack(
            rx.icon(
                "arrow-left",
                color="black",
            ),
            rx.text(
                "مشاهده همه",
                color="black",
            ),
            spacing="1",
            justify="between",
            cursor="pointer",
        ),
        rx.text(
            title,
            width="50%",
            color="black",
            align="right",
        ),
        margin_top="8px",
        justify="between",
        width="100%",
    )
    return content


def home_page():
    content = rx.vstack(
        carousel(),
        products_heading("دسته بندی ها"),
        brands_boxes(margin_top="8px"),
        brands_boxes(),
        products_heading("محصولات پیشنهادی"),
        products_column(),
        products_column(),
        simple_banner(src="/images/banner-2.jpg", margin_top="8px"),
        products_heading("جدیدترین محصولات"),
        products_column(),
        simple_banner(src="/images/banner-3.jpg", margin_top="8px"),
        products_heading("برندها"),
        brands_boxes(),
        align="center",
        justify="between",
        width="100%",
    )

    return main_layout(content=content)
