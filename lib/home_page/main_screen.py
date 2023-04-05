import flet as ft
from datetime import datetime
from time import sleep

import lib.home_page.main_widget as main_widget


def main(page: ft.Page):
    page.title = "Memoir"

    page.window_width = 1440
    page.window_height = 1024
    page.window_resizable = False
    page.window_maximizable = False

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)
    page.bgcolor = ft.colors.TRANSPARENT

    page.fonts = {"Inter": "fonts/Inter-Regular.ttf",
                  "Inter SemiBold": "fonts/Inter-SemiBold.otf",
                  "Inter Light": "fonts/Inter-Light-BETA.otf",
                  "Inter Medium": "fonts/Inter-Medium.otf",}

    page.theme = ft.Theme(font_family="Inter")

    user = "User"

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
            expand=True,
            image_src="images/home_page_bg.png",
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
        )
    )

    while True:
        notification.time.time.current.value = (str(datetime.now().hour) if datetime.now().hour > 9 else (
                "0" + str(datetime.now().hour))) + "." + (str(datetime.now().minute) if datetime.now().minute > 9 else (
                    "0" + str(datetime.now().minute)))
        page.update()
        sleep(60 - datetime.now().second)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../assets")
