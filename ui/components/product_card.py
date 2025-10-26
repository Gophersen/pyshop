import reflex as rx


def product_card():
    content = rx.hstack(
        rx.box(
            rx.vstack(
                rx.avatar(
                    fallback="MA",
                    margin_top="6px",
                    size="8",
                    width="95%",
                ),
                rx.hstack(
                    rx.text(
                        "نام محصول",
                        color="grey",
                        width="100%",
                        align="right",
                        margin_right="10px",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.hstack(
                    rx.text(
                        "۳۵,۰۰۰,۰۰۰ تومان",
                        color="black",
                        margin_left="10px",
                        width="100%",
                    ),
                    justify="between",
                    width="100%",
                ),
                align_items="center",
                width="100%",
            ),
            justify_content="center",
            display="flex",
            bg="white",
            border_radius="10px",
            width="100%",
            # height="15vh",
        ),
        justify="center",
        width="100%",
    )
    return content


def products_column():
    boxes = [product_card() for i in range(3)]
    content = rx.hstack(
        *boxes,
        justify="between",
        width="100%",
    )
    return content
