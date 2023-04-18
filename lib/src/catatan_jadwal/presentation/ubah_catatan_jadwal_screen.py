import flet as ft
from datetime import datetime
from time import sleep

import lib.src.catatan_jadwal.presentation.catatan_jadwal_screen as catatan_jadwal_screen
import lib.src.catatan_jadwal.controller.catatan_jadwal_controller as catatan_jadwal_controller
import lib.src.catatan_jadwal.presentation.catatan_jadwal_widget as catatan_jadwal_widget
import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model
import lib.src.utilities.date_picker as date_picker
import lib.src.utilities.time_picker as time_picker
from lib.src.utilities.util import image_to_blob, blob_to_base64


def main(page: ft.Page, id_catatan_jadwal: int):
    _catatan_jadwal_controller = catatan_jadwal_controller.CatatanJadwalController()
    catatan_jadwal = _catatan_jadwal_controller.getCatatanJadwal(id_catatan_jadwal)

    page.title = "Memoir - Ubah Catatan Jadwalr"

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


    desc_acara = ft.TextField(
            border_width=0,
            width=1300,
            multiline=False,
            min_lines=1,
            max_lines=1,
            height=95,
            text_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
            hint_text="Your title here...",
            hint_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
            value=catatan_jadwal[3],
            text_align=ft.TextAlign.JUSTIFY,
        )

    date = date_picker.DatePicker(
            day=int(catatan_jadwal[1][8:10]),
            month=int(catatan_jadwal[1][5:7]),
            year=int(catatan_jadwal[1][0:4]),
        )
    time = time_picker.TimePicker(
            hour=int(catatan_jadwal[2][0:2]),
            minute=int(catatan_jadwal[2][3:5]),
    )

    def batal_ubah_catatan_jadwal(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()


    def ubah_catatan_jadwal(e):
        try:
            if desc_acara.value == "":
                page.snack_bar.content.value = "Mohon isi semua kolom"
                page.snack_bar.open = True
                page.update()
                return

            _catatan_jadwal = catatan_jadwal_model.CatatanJadwal(
                id_jadwal=catatan_jadwal[0],
                tanggal=date.get_date(),
                jam=time.get_time(),
                desc_acara=desc_acara.value,
            )

            _catatan_jadwal_controller.Memperbarui(_catatan_jadwal)
            page.snack_bar.content.value = "Catatan Jadwal berhasil diubah"
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar.content.value = "Catatan Jadwal gagal diubah"
            page.snack_bar.open = True
            page.update()
            print(e)

        page.clean()
        catatan_jadwal_screen.main(page)
        page.update()

    calendar = ubah_catatan_jadwal_widget.CalendarLeft()
    notification = ubah_catatan_jadwal_widget.Notification()

    left_column = ft.Container(
        content=ft.Column(
            controls=[
                catatan_jadwal_widget.AddCatatanJadwalButton(page),
                calendar,
                ft.Container(
                    image_src="icons/cancel_button.png",
                    width=480,
                    height=94,
                    on_click=ubah_catatan_jadwal,
                ),
                
            ],
            visible=True,
            expand=True,
            spacing=0,
        ),
        expand=True,
        padding=ft.padding.only(top=30, left=0, bottom=0, right=0),
    )

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[left_column, notification],
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



if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../assets")
