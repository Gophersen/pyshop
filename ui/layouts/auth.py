import reflex as rx


def auth_layout(content: rx.Component) -> rx.Component:
    content = rx.box(
        content,
        # bg="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        bg="white",
        height="100vh",
        width="100vw",
        display="flex",
        align_items="center",
        justify_content="center",
    )
    return content
