import reflex as rx

from pages.home import home_page
from pages.basket import basket_page
from pages.login import login_page


app = rx.App(
    style={
        "background_color": "#E9EEFF",
        "font_family": "Vazirmatn",
        "body": {"overview": "hidden"},
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap",
    ],
)

app.add_page(
    home_page,
    route="/",
)
app.add_page(
    basket_page,
    route="/basket",
)
app.add_page(
    login_page,
    route="/login",
)
