import flet as ft
from lib.src.utilities.util import blob_to_base64

import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_screen as catatan_kegiatan_screen
import lib.src.catatan_kegiatan.presentation.ubah_catatan_kegiatan_screen as ubah_catatan_kegiatan_screen
import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_widget as catatan_kegiatan_widget
import lib.src.catatan_kegiatan.controller.catatan_kegiatan_controller as catatan_kegiatan_controller


# TODO : jangan lupa kalau misal ada foto yang diganti terus gaada di lokal, pasang foto default lagi
# ? : kenapa ga pake blob ajah buat foto nya?


def main(page: ft.Page, id_kegiatan: int):
    _catatan_kegiatan_controller = catatan_kegiatan_controller.CatatanKegiatanController()
    _catatan_kegiatan = _catatan_kegiatan_controller.getCatatanKegiatan(id_kegiatan)

    page.title = "Memoir - Lihat Catatan Kegiatan"

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def back_to_catatan_kegiatan_screen(e):
        # hapus catatan kegiatan
        _catatan_kegiatan_controller.Hapus(id_kegiatan)
        page.dialog.open = False
        page.controls.clear()
        catatan_kegiatan_screen.main(page)
        page.update()

    delete_dialog = ft.AlertDialog(
        modal=True,
        open=False,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        title=ft.Text(
            value="Apakah kamu yakin ingin menghapus?",
            size=30,
            font_family="Inter SemiBold",
            text_align=ft.TextAlign.CENTER, ),
        content=ft.Text(
            value="Catatan Kegiatan yang sudah dihapus tidak dapat dikembalikan.",
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
                on_click=back_to_catatan_kegiatan_screen,
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

    def back_button(e):
        page.clean()
        catatan_kegiatan_screen.main(page)
        page.update()


    def hapus_catatan_kegiatan(e):
        page.dialog = delete_dialog
        delete_dialog.open = True
        page.update()

    def ubah_catatan_kegiatan(e):
        page.controls.clear()
        ubah_catatan_kegiatan_screen.main(page, id_kegiatan)
        page.update()

    date = catatan_kegiatan_widget.convertTanggal(_catatan_kegiatan[1])
    time = _catatan_kegiatan[2][:5]
    emotion = catatan_kegiatan_widget.getJenisPerasaanEmoji(_catatan_kegiatan[6])

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        image_src="icons/back_button.png",
                        width=35,
                        height=35,
                        on_click=back_button,
                        margin=ft.margin.only(top=20, left=-10),
                    ),

                    ft.VerticalDivider(
                        width=10,
                        visible=False,
                    ),

                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            value="Hariku",
                                            color="#043edb",
                                            size=45,
                                            font_family="Inter SemiBold",
                                            text_align=ft.TextAlign.CENTER,
                                        ),

                                        ft.Container(
                                            content=ft.Row(
                                                controls=[

                                                    ft.Container(
                                                        image_src="icons/delete_button.png",
                                                        width=50,
                                                        height=50,
                                                        on_click=hapus_catatan_kegiatan,
                                                    ),

                                                    ft.Container(
                                                        image_src="icons/edit_button.png",
                                                        width=50,
                                                        height=50,
                                                        on_click=ubah_catatan_kegiatan,
                                                    )
                                                ],
                                                spacing=7
                                            ),
                                            alignment=ft.alignment.center_right
                                         ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    height=70,
                                    width=1300,
                                ),

                                ft.Container(
                                    border_radius=15,
                                    bgcolor="#043edb",
                                    image_src_base64=str(blob_to_base64(_catatan_kegiatan[5])),
                                    width=1300,
                                    height=700,
                                    image_fit=ft.ImageFit.COVER,
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                border_radius=15,
                                                height=450,
                                                width=1300,
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
                                                                    ft.Row(
                                                                    controls=[
                                                                        ft.Text(
                                                                            overflow=ft.TextOverflow.VISIBLE,
                                                                            width=1300,
                                                                            height=50,
                                                                            color="#ffffff",
                                                                            size=40,
                                                                            font_family="Inter SemiBold",
                                                                            value=_catatan_kegiatan[3],
                                                                            text_align=ft.TextAlign.JUSTIFY,
                                                                        )],
                                                                        scroll=ft.ScrollMode.AUTO,
                                                                        ),

                                                                        ft.Divider(
                                                                            height=25,
                                                                            color="transparent"
                                                                        ),

                                                                        ft.Row(
                                                                            controls=[
                                                                                ft.Text(
                                                                                    value=date,
                                                                                    color="#ffffff",
                                                                                    size=20,
                                                                                    font_family="Inter Light",
                                                                                    text_align=ft.TextAlign.JUSTIFY,
                                                                                ),
                                                                                ft.Text(
                                                                                    value=time,
                                                                                    color="#ffffff",
                                                                                    size=20,
                                                                                    font_family="Inter Light",
                                                                                    text_align=ft.TextAlign.JUSTIFY,
                                                                                ),
                                                                                ft.Text(
                                                                                    value=emotion,
                                                                                    size=20,
                                                                                    text_align=ft.TextAlign.START,
                                                                                )
                                                                            ],
                                                                            spacing=10,
                                                                        )
                                                                ],
                                                                spacing=3,
                                                                alignment=ft.MainAxisAlignment.START,
                                                                horizontal_alignment=ft.CrossAxisAlignment.START
                                                            )
                                                        ),

                                                        # deskripsi
                                                        ft.Container(
                                                            border_radius=15,
                                                            height=300,
                                                            width=1300,
                                                            bgcolor="#06184E",
                                                            padding=ft.padding.only(left=10, right=10, top=10),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text(
                                                                        width=1300,
                                                                        overflow=ft.TextOverflow.VISIBLE,
                                                                        color="#ffffff",
                                                                        size=20,
                                                                        font_family="Inter Light",
                                                                        value=_catatan_kegiatan[4][:len(_catatan_kegiatan[4])],
                                                                    )
                                                                ],
                                                                scroll=ft.ScrollMode.ADAPTIVE,
                                                                expand=True,
                                                            ),
                                                        ),
                                                    ],
                                                    spacing=0,
                                                    alignment=ft.MainAxisAlignment.END,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                )
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.END,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    alignment=ft.alignment.bottom_center,
                                ),
                            ],
                            spacing=0,
                            # width=1163,
                            # height=1024,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            width=page.window_width,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=45, top=35, right=52, bottom=35),
        ),
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../../../assets")
