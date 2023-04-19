import flet as ft
from datetime import date
from time import sleep
import time

import lib.src.catatan_target.presentation.catatan_target_screen as catatan_target_screen
import lib.src.catatan_target.controller.catatan_target_controller as catatan_target_controller
import lib.src.utilities.date_picker as date_picker

# TODO : Ubah Cover
def main(page: ft.Page):
    page.title = "Memoir - Tambah Catatan Target"

    page.fonts = {
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
    }

    page.snack_bar = ft.SnackBar(
        content=ft.Text(
            value="Catatan target berhasil ditambahkan",
            size=20,
            font_family="Inter SemiBold",
        ),
        action_color=ft.colors.WHITE,
        action="Tutup",
    )

    def back_to_catatan_target_screen(e):
        page.dialog.open = False
        page.update()
        sleep(0.1)
        page.clean()
        catatan_target_screen.main(page)
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
                on_click=back_to_catatan_target_screen,
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

    global result_img
    result_img = None

    container_ref = ft.Ref[ft.Container]()

    target = ft.TextField(
            border_width=0,
            max_lines=1,
            multiline=False,
            height=95,
            text_align=ft.TextAlign.JUSTIFY,
            text_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
            hint_text="Your target here...",
            hint_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
        )

    waktu_capai = date_picker.DatePicker()

    def batal_tambah_catatan_target(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()

    # TODO: Query ke database
    def tambah_catatan_target(e):
        try:
            if target.value == "":
                page.snack_bar.content.value = "Mohon isi semua kolom"
                page.snack_bar.open = True
                page.update()
                return

            _catatan_target_controller = catatan_target_controller.CatatanTargetController()
            tambah_valid = _catatan_target_controller.Tambah(
                date.today().strftime("%Y-%m-%d"),
                time.strftime("%H:%M:%S", time.localtime()),
                target.value,
                waktu_capai.get_date()
            )
            if tambah_valid :
                page.snack_bar.content.value = "Catatan target berhasil ditambahkan"
            else:
                page.snack_bar.content.value = "Catatan target gagal ditambahkan"
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar.content.value = "Catatan target gagal ditambahkan"
            page.snack_bar.open = True
            page.update()
            # print(e)

        page.clean()
        catatan_target_screen.main(page)
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value="Tambah Catatan Target",
                                color="#043edb",
                                size=45,
                                font_family="Inter SemiBold",
                                text_align=ft.TextAlign.START,
                            ),

                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            image_src="icons/cancel_button.png",
                                            width=50,
                                            height=50,
                                            on_click=batal_tambah_catatan_target,
                                        ),

                                        ft.Container(
                                            image_src="icons/confirm_button.png",
                                            width=50,
                                            height=50,
                                            on_click=tambah_catatan_target,
                                        )
                                    ],
                                    spacing=7
                                ),
                                alignment=ft.alignment.center_right
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        width=1300,
                        # height=70
                    ),

                    # Content yang diisi oleh user
                    ft.Container(
                        ref=container_ref,
                        image_src="images/default_cover_ctt_target.jpg",
                        border_radius=15,
                        bgcolor="#043edb",
                        width=1300,
                        height=700,
                        image_fit=ft.ImageFit.COVER,
                        content=ft.Column(
                            [
                                ft.Container(
                                    border_radius=15,
                                    height=250,
                                    width=1300,
                                    padding=ft.padding.all(20),
                                    alignment=ft.alignment.top_left,
                                    bgcolor="#444980",
                                    content=ft.Column(
                                        controls=[
                                            # judul
                                            ft.Container(
                                                border_radius=15,
                                                height=150,
                                                width=1300,
                                                bgcolor="#444980",
                                                padding=ft.padding.only(left=10, right=10, top=15),
                                                content=ft.Column(
                                                    controls=[
                                                        target,

                                                        ft.Row(
                                                            controls=[
                                                                waktu_capai
                                                            ],
                                                            spacing=25,
                                                        )
                                                    ],
                                                    spacing=3,
                                                    alignment=ft.MainAxisAlignment.START,
                                                    horizontal_alignment=ft.CrossAxisAlignment.START
                                                )
                                            ),
                                        ],
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        alignment=ft.alignment.bottom_center,
                    ),
                ],
                spacing=0
            ),
            width=page.window_width,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=80, top=35, right=52, bottom=35),
        ),
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../../../assets")
