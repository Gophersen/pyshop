import reflex as rx


class CarouselState(rx.State):
    images = [
        "/images/top-1.jpg",
        "/images/top-2.jpg",
    ]
    current = 0

    @rx.event
    def next_image(self):
        self.current = 0 if self.current else 1


def carousel(margin_top: str = ""):
    return rx.hstack(
        rx.image(
            src=CarouselState.images[CarouselState.current],
            border_radius="10px",
            margin_top=margin_top,
        ),
        rx.moment(
            interval=5000,
            on_change=CarouselState.next_image,
            display="none",
        ),
        width="100%",
        cursor="pointer",
    )
