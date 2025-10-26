import reflex as rx

from pages.home import home_page


app = rx.App(
    style={
        "background_color": "#E9EEFF",
        "font_family": "Vazirmatn",
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap",
    ],
)

app.add_page(
    home_page,
    route="/",
)
