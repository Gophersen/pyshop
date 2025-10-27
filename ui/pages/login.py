import reflex as rx

from layouts.auth import auth_layout


def login_page():
    content = rx.vstack(
        rx.hstack(
            rx.text("."),
            rx.image(
                "/images/logo-32-3.png",
                on_click=rx.redirect("/"),
                cursor="pointer",
            ),
            rx.icon(
                "arrow-right",
                color="black",
                cursor="pointer",
                on_click=rx.redirect("/"),
            ),
            justify="between",
            width="100%",
            padding_right="40px",
            padding_left="40px",
            display="flex",
            align_items="center",
        ),
        rx.hstack(
            rx.text(
                "ورود یا ثبت نام در ماریان آرچری",
                color="black",
                size="4",
                align="right",
            ),
            display="flex",
            justify_content="right",
            padding_top="20px",
            padding_right="30px",
            width="100%",
        ),
        rx.hstack(
            rx.text(
                "لطفا شماره موبایل خود را وارد کنید",
                color="grey",
                size="2",
                align="right",
            ),
            display="flex",
            justify_content="right",
            padding_right="30px",
            padding_bottom="15px",
            width="100%",
        ),
        rx.input(
            rx.input.slot(
                rx.icon(
                    "phone",
                    color="black",
                    size=20,
                ),
            ),
            color="black",
            radius="large",
            bg="white",
            border="1px solid grey",
            style={
                "input::placeholder": {"color": "grey"},
            },
            size="3",
            type="number",
            required=True,
            max_length=11,
            min_length=10,
        ),
        rx.button(
            "ورود یا ثبت نام",
            # color_scheme="tomato",
            bg="#ED0012",
            size="3",
            margin_top="10px",
            cursor="pointer",
        ),
        color="white",
        bg="white",
        width=rx.breakpoints(
            initial="95%",
            sm="70%",
            lg="25%",
        ),
        display="flex",
        align_items="center",
        border_radius="10px",
        padding_top="30px",
        padding_bottom="30px",
        border="1px solid #E0E0E2",
    )

    return auth_layout(content=content)
