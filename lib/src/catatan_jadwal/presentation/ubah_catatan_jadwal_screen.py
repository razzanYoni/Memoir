import flet as ft
from time import sleep
from PIL import Image

import lib.src.catatan_jadwal.presentation.catatan_jadwal_screen as catatan_jadwal_screen
import lib.src.catatan_jadwal.controller.catatan_jadwal_controller as catatan_jadwal_controller
import lib.src.utilities.date_picker as date_picker
import lib.src.utilities.time_picker as time_picker
from lib.src.utilities.util import image_to_blob
import lib.src.catatan_jadwal.presentation.catatan_jadwal_widget as catatan_jadwal_widget
import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model

# TODO : Ubah Cover
def main(page: ft.Page):
    page.title = "Memoir - Ubah Catatan Jadwal"

    page.fonts = {
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
    }

    page.snack_bar = ft.SnackBar(
        content=ft.Text(
            value="Catatan jadwal berhasil diubah",
            size=20,
            font_family="Inter SemiBold",
        ),
        action_color=ft.colors.WHITE,
        action="Tutup",
    )
    def back_to_catatan_jadwal_screen(e):
        page.dialog.open = False
        page.update()
        sleep(0.1)
        page.clean()
        catatan_jadwal_screen.main(page)
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()
    page.theme = ft.Theme(font_family="Inter")

    cancel_dialog = ft.AlertDialog(
        modal=True,
        open=False,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        title=ft.Text(
            value="Apakah kamu yakin ingin membatalkan?",
            size=30,
            font_family="Inter SemiBold",
            text_align=ft.TextAlign.CENTER,),
        content=ft.Text(
            value="Semua perubahan yang belum disimpan akan hilang",
            size=20,
            font_family="Inter",
            text_align=ft.TextAlign.CENTER,
        ),
        actions=[
            ft.TextButton(
                content=ft.Text(
                    value="Ya",
                    size=25,
                    font_family="Inter SemiBold",
                    color=ft.colors.WHITE,
                ),
                width=150,
                height=60,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor="#e993bd",
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
                    }
                ),
                on_click=back_to_catatan_jadwal_screen,
            ),

            ft.TextButton(
                content=ft.Text(
                    value="Tidak",
                    size=25,
                    font_family="Inter SemiBold",
                    color=ft.colors.WHITE,
                ),
                width=150,
                height=60,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor="#c5cbe8",
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
                    },
                ),
                on_click=close_dialog,
            ),
        ],
    )

    nama_acara = ft.TextField(
        border_width=0,
        width=800,
        height=85,
        multiline=True,
        text_style=ft.TextStyle(
            color="#ffffff",
            size=19,
            font_family="Inter Light",
        ),
        hint_text="Your description here...",
        hint_style=ft.TextStyle(
            color="#ffffff",
            size=20,
            font_family="Inter Light",
        ),
    )

    desc_acara = ft.TextField(
            border_width=0,
            max_lines=1,
            multiline=False,
            width=800,
            height=85,
            text_align=ft.TextAlign.JUSTIFY,
            text_style=ft.TextStyle(
                color="#ffffff",
                size=19,
                font_family="Inter SemiBold",
            ),
    )

    def batal_ubah_catatan_kegiatan(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()

    def ubah_catatan_kegiatan(e):
        try:
            if desc_acara.value == "" or nama_acara.value == "" or nama_acara.value != "" or desc_acara.value != "":
                page.snack_bar.content.value = "Mohon isi semua kolom"
                page.snack_bar.open = True
                page.update()
                return

            page.snack_bar.content.value = "Catatan Kegiatan berhasil diubah"
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar.content.value = "Catatan Kegiatan gagal diubah"
            page.snack_bar.open = True
            page.update()
            print(e)

        page.clean()
        catatan_jadwal_screen.main(page)
        page.update()

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

    page.add(
        ft.Container(
            content=ft.Row(
            controls=[home_button, left_column, notification],
            visible=True,
            expand=True,
            spacing=0,
        ),
            expand=True,
            image_src="assets/images/home_page_bg.png",
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../../../assets")
