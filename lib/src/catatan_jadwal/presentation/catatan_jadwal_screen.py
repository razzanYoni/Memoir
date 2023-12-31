import flet as ft
from datetime import datetime
from time import sleep
import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model
import lib.src.catatan_jadwal.presentation.catatan_jadwal_widget as catatan_jadwal_widget
from lib.src.catatan_jadwal.presentation.catatan_jadwal_widget import CalendarButton


def main(page: ft.Page):
    page.title = "Memoir - Catatan Jadwal"

    page.window_width = 1440
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)
    page.bgcolor = ft.colors.TRANSPARENT

    page.fonts = {
        "Inter": "fonts/Inter-Regular.ttf",
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Light": "fonts/Inter-Light-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
    }

    page.theme = ft.Theme(font_family="Inter")

    calendar = catatan_jadwal_widget.CalendarLeft()
    calendar_button = catatan_jadwal_widget.CalendarButton(page)
    tes = catatan_jadwal_model.CatatanJadwal(1, 2, "aa", "ACARA XXX XXX XXX", "Agenda", "01:02:03")
    notification = catatan_jadwal_widget.Notification(tes)
    home_button = catatan_jadwal_widget.HomeButton(page)

    left_column = ft.Container(
        content=ft.Column(
            controls=[calendar, calendar_button],
            visible=True,
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
        ),
        expand=True,
        padding=ft.padding.only(top=30, left=0, bottom=0, right=0),
    )
    right_column = ft.Container(
        content=ft.Column(
            controls=[
            catatan_jadwal_widget.Agenda(),
            catatan_jadwal_widget.DaftarCatatanJadwal()],
            visible=True,
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )
    )
    page.add(
        ft.Container(
            content=ft.Row(
                controls=[home_button, left_column, right_column],
                visible=True,
                expand=True,
                spacing=0,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            expand=True,
            image_src="assets/images/ctt_jadwal_bg.png",
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
        )
    )



if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../assets")
