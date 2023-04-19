import flet as ft
from datetime import datetime
from time import sleep
import os

import lib.home_page.main_widget as main_widget

def main(page: ft.Page):
    page.title = "Memoir"
    page.scroll = None

    page.window_width = 1440
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)

    page.fonts = {
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
        "Inter Light": "fonts/Inter-Light-BETA.otf",
    }

    page.theme = ft.Theme(font_family="Inter")
    
    user = "Hana Fathiyah"
    side_bar = main_widget.SideBar(page=page, user=user)
    notification = main_widget.Notification()
    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    side_bar,
                    notification
                ],
                visible=True,
                expand=True,
                spacing=0,
            ),
            image_src="images/home_page_bg.png",
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            height=page.window_height,
            width=page.window_width,
        )
    )

    page.update()

    
    while True:
        notification.time.time.current.value = (str(datetime.now().hour) if datetime.now().hour > 9 else (
                "0" + str(datetime.now().hour))) + "." + (str(datetime.now().minute) if datetime.now().minute > 9 else (
                    "0" + str(datetime.now().minute)))
        page.update()
        sleep(60 - datetime.now().second)

def app():
    ft.app(target=main, assets_dir="assets")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../assets")
