import reflex as rx

config = rx.Config(
    app_name="az_documentvault_client",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)