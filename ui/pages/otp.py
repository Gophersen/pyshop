import reflex as rx

from layouts.auth import auth_layout


def otp_page():
    content = rx.vstack(
        rx.hstack(
            rx.text("."),
            rx.image(
                "/images/logo-32-3.png",
                cursor="pointer",
            ),
            rx.icon(
                "arrow-right",
                color="black",
                cursor="pointer",
                on_click=rx.redirect("/login"),
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
            justify_content="center",
            padding_top="20px",
            width="100%",
        ),
        rx.hstack(
            rx.text(
                "لطفا کد تایید ارسال شده را وارد کنید",
                color="grey",
                size="2",
                align="right",
            ),
            display="flex",
            justify_content="center",
            padding_bottom="15px",
            width="100%",
        ),
        rx.hstack(
            rx.input(
                type="number",
                max_length=5,
                border="1px solid grey",
                color="black",
                radius="large",
                text_align="center",
                bg="white",
                size="3",
                style={
                    "input::placeholder": {"color": "grey"},
                },
                placeholder="کد تایید",
            ),
            justify="between",
            width=rx.breakpoints(
                initial="40%",
                sm="70%",
                lg="35%",
            ),
        ),
        rx.button(
            "تایید و ورود",
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
