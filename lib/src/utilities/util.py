import flet as ft

# TODO: janlup kalo pindah pake page.clean()
# TODO: janlup di main screen matiin scroll

def default_page(page: ft.Page, title: str):
    page.title = title
    page.window_width = 1440
    page.window_height = 1024
    page.window_resizable = False
    page.window_maximizable = False

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)

    page.fonts = {
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
        "Inter Light": "fonts/Inter-Light-BETA.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter": "fonts/Inter-Regular.ttf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
    }
