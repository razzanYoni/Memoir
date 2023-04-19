import flet as ft
from time import sleep
from datetime import date
import time

import lib.src.catatan_target.presentation.catatan_target_screen as catatan_target_screen
import lib.src.catatan_target.controller.catatan_target_controller as catatan_target_controller
import lib.src.catatan_target.data.catatan_target_model as catatan_target_model
import lib.src.utilities.date_picker as date_picker
import lib.src.utilities.status_picker as status_picker

def main(page: ft.Page, id_catatan_target: int):
    _catatan_target_controller = catatan_target_controller.CatatanTargetController()
    catatan_target = _catatan_target_controller.getCatatanTarget(id_catatan_target)

    page.title = "Memoir - Ubah Catatan Target"

    page.snack_bar = ft.SnackBar(
        content=ft.Text(
            value="Catatan target berhasil diubah",
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
            value="Semua perubahan yang belum disimpan akan hilang.",
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

    container_ref = ft.Ref[ft.Container]()

    target = ft.TextField(
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
            hint_text="Your target here...",
            hint_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
            # ?
            value=catatan_target[3],
            text_align=ft.TextAlign.JUSTIFY,
        )

    waktu_capai = date_picker.DatePicker(
            day=int(catatan_target[4][8:10]),
            month=int(catatan_target[4][5:7]),
            year=int(catatan_target[4][0:4]),
        )

    statusPick = status_picker.StatusPicker(status=catatan_target[5])

    def batal_ubah_catatan_target(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()

    # TODO: Query ke database
    def ubah_catatan_target(e):
        try:
            if target.value == "":
                page.snack_bar.content.value = "Mohon isi semua kolom"
                page.snack_bar.open = True
                page.update()
                return

            _catatan_target = catatan_target_model.CatatanTarget(
                id_target=catatan_target[0],
                tanggal=date.today().strftime("%Y-%m-%d"),
                waktu=time.strftime("%H:%M:%S", time.localtime()),
                target=target.value,
                waktu_capai=waktu_capai.get_date(),
                status=statusPick.get_status(),
            )

            ubah = _catatan_target_controller.Memperbarui(_catatan_target)
            if ubah == False:
                page.snack_bar.content.value = "Catatan target gagal diubah"
            else:
                page.snack_bar.content.value = "Catatan target berhasil diubah"
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar.content.value = "Catatan target gagal diubah"
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
                                value="Ubah Catatan Kegiatan",
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
                                            on_click=batal_ubah_catatan_target,
                                        ),

                                        ft.Container(
                                            image_src="icons/confirm_button.png",
                                            width=50,
                                            height=50,
                                            on_click=ubah_catatan_target,
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
                        border_radius=15,
                        bgcolor="#043edb",
                        ref=container_ref,
                        image_src="images/default_cover_ctt_target.jpg",
                        width=1300,
                        height=700,
                        image_fit=ft.ImageFit.COVER,
                        content=ft.Column(
                            [
                                ft.Container(
                                    border_radius=15,
                                    height=400,
                                    width=1300,
                                    bgcolor="#444980",
                                    padding=ft.padding.all(20),
                                    content=ft.Column(

                                        controls=[
                                            # judul
                                            ft.Container(
                                                border_radius=15,
                                                padding=ft.padding.all(20),
                                                content=ft.Column(
                                                    controls=[
                                                        target,

                                                        ft.Text(
                                                            value="Waktu Capai",
                                                            color="#ffffff",
                                                            size=20,
                                                            font_family="Inter Medium",
                                                            text_align=ft.TextAlign.JUSTIFY,
                                                        ),

                                                        waktu_capai,

                                                        ft.Divider(
                                                            height=5,
                                                            color="transparent"
                                                        ),

                                                        ft.Text(
                                                            value="Status",
                                                            color="#ffffff",
                                                            size=20,
                                                            font_family="Inter Medium",
                                                            text_align=ft.TextAlign.JUSTIFY,
                                                        ),

                                                        statusPick
                                                    ],
                                                    spacing=10,
                                                    alignment=ft.MainAxisAlignment.START,
                                                    horizontal_alignment=ft.CrossAxisAlignment.START
                                                )
                                            )
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
