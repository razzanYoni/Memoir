import flet as ft

import lib.src.catatan_target.presentation.catatan_target_screen as catatan_target_screen
import lib.src.catatan_target.presentation.ubah_catatan_target_screen as ubah_catatan_target_screen
import lib.src.catatan_target.presentation.catatan_target_widget as catatan_target_widget
import lib.src.catatan_target.controller.catatan_target_controller as catatan_target_controller

def main(page: ft.Page, id_target: int):
    _catatan_target_controller = catatan_target_controller.CatatanTargetController()
    _catatan_target = _catatan_target_controller.getCatatanTarget(id_target)

    page.title = "Memoir - Lihat Catatan Target"

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def back_to_catatan_target_screen(e):
        # hapus catatan target
        _catatan_target_controller.Hapus(id_target)
        page.dialog.open = False
        page.controls.clear()
        catatan_target_screen.main(page)
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
            value="Catatan target yang sudah dihapus tidak dapat dikembalikan.",
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

    def back_button(e):
        page.clean()
        catatan_target_screen.main(page)
        page.update()


    def hapus_catatan_target(e):
        page.dialog = delete_dialog
        delete_dialog.open = True
        page.update()

    def ubah_catatan_target(e):
        page.controls.clear()
        ubah_catatan_target_screen.main(page, id_target)
        page.update()

    waktu_capai = catatan_target_widget.convertTanggal(_catatan_target[4])

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
                                            value="Targetku",
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
                                                        on_click=hapus_catatan_target,
                                                    ),

                                                    ft.Container(
                                                        image_src="icons/edit_button.png",
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
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    height=70,
                                    width=1300,
                                ),

                                ft.Container(
                                    border_radius=15,
                                    bgcolor="#043edb",
                                    image_src="images/default_cover_ctt_target.png",
                                    width=1300,
                                    height=700,
                                    image_fit=ft.ImageFit.COVER,
                                    content=ft.Column(

                                        controls=[
                                            ft.Container(
                                                padding=ft.padding.all(30),
                                                border_radius=15,
                                                height=320,
                                                width=1300,
                                                bgcolor="#444980",
                                                content=ft.Column(
                                                    controls=[
                                                        # judul
                                                        ft.Container(
                                                            border_radius=15,
                                                            height=100,
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
                                                                            value=_catatan_target[3],
                                                                            text_align=ft.TextAlign.JUSTIFY,
                                                                        )],
                                                                        scroll=ft.ScrollMode.AUTO,
                                                                        ),

                                                                        ft.Divider(
                                                                            height=25,
                                                                            color="transparent"
                                                                        ),

                                                                        ft.Text(
                                                                            value="Waktu Capai",
                                                                            color="#ffffff",
                                                                            size=20,
                                                                            font_family="Inter Medium",
                                                                            text_align=ft.TextAlign.JUSTIFY,
                                                                        ),
                                                                        ft.Text(
                                                                            value=waktu_capai,
                                                                            color="#ffffff",
                                                                            size=20,
                                                                            font_family="Inter Light",
                                                                            text_align=ft.TextAlign.JUSTIFY,
                                                                        ),

                                                                        ft.Divider(
                                                                            height=15,
                                                                            color="transparent"
                                                                        ),

                                                                        ft.Text(
                                                                            value="Status",
                                                                            color="#ffffff",
                                                                            size=20,
                                                                            font_family="Inter Medium",
                                                                            text_align=ft.TextAlign.JUSTIFY,
                                                                        ),
                                                                        ft.Text(
                                                                            value=_catatan_target[5],
                                                                            color="#ffffff",
                                                                            size=20,
                                                                            font_family="Inter Light",
                                                                            text_align=ft.TextAlign.JUSTIFY,
                                                                        ),
                                                                ],
                                                                spacing=3,
                                                                alignment=ft.MainAxisAlignment.START,
                                                                horizontal_alignment=ft.CrossAxisAlignment.START
                                                            )
                                                        ),
                                                    ],
                                                    spacing=0,
                                                    alignment=ft.MainAxisAlignment.START,
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
