import flet as ft
import PIL.Image as Image
import base64

# TODO: janlup kalo pindah pake page.clean()
# TODO: janlup di main screen matiin scroll


def blob_to_base64(blob: str):
    return base64.b64encode(blob).decode("utf-8")

def image_to_blob(imagefile: str):
    with open(imagefile, "rb") as f:
        blob = f.read()
    return blob

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
