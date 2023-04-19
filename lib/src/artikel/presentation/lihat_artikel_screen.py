import flet as ft
from lib.src.utilities.util import blob_to_base64

import lib.src.artikel.presentation.artikel_screen as artikel_screen
import lib.src.artikel.presentation.artikel_widget as artikel_widget
import lib.src.artikel.controller.artikel_controller as artikel_controller

def main(page: ft.Page, id_artikel: int):
    _artikel_controller = artikel_controller.ArtikelController()
    _artikel = _artikel_controller.getArtikel(id_artikel)

    page.title = "Jelajahi Harimu"

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def back_to_catatan_kegiatan_screen(e):
        # hapus catatan kegiatan
        page.controls.clear()
        artikel_screen.main(page)
        page.update()


    def back_button(e):
        page.clean()
        artikel_screen.main(page)
        page.update()

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
                                ft.Container(
                                        ft.Text(
                                            value="Jelajahi Harimu",
                                            color="#043edb",
                                            size=35,
                                            font_family="Inter SemiBold",
                                            text_align=ft.TextAlign.LEFT,
                                        ),
                                
                                    # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    height=70,
                
                                    padding=ft.padding.only(left=20, top=12, right=0, bottom=0),

    
                                ),

                                ft.Container(
                                    content = ft.Row(
                                        controls = [
                                            ft.Container(
                                                image_src="icons/ellipse.png",
                                                width=50,
                                                height=50,
                                                margin = 10,
                                            ),

                                            ft.Column(
                                                controls = [
                                                    ft.Text(
                                                        value = _artikel[3],
                                                        color = '#FFFFFF',
                                                        size=25,
                                                        font_family="Inter SemiBold",
                                                    ),
                                                    ft.Text(
                                                        value = _artikel[4],
                                                        color = '#FFFFFF',
                                                        size=15,
                                                        font_family="Inter Light",
                                                    ),
                                                ],
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                    ),
                                    padding = ft.padding.only(80, 350, 20, 20),
                                    border_radius=15,
                                    bgcolor="#043edb",
                                    image_src_base64=str(blob_to_base64(_artikel[5])),
                                    width=1100-20,
                                    height=500,
                                    image_fit=ft.ImageFit.COVER,
                                    alignment=ft.alignment.center,
                                    margin = 20,
                                ),

                                ft.Text(
                                    # overflow=ft.TextOverflow.ELLIPSIS,
                                    width=1100,
                                    color="#60648B",
                                    size=40,
                                    font_family="Inter SemiBold",
                                    value=_artikel[1],
                                    text_align=ft.TextAlign.CENTER,
                                ),

                                ft.Text(
                                    overflow=ft.TextOverflow.VISIBLE,
                                    color="#60648B",
                                    width=1100,
                                    size=20,
                                    font_family="Inter Light",
                                    value=_artikel[2][:len(_artikel[2])],
                                    text_align=ft.TextAlign.JUSTIFY,
                                )
                            ],
                            spacing=5,
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
            padding=ft.padding.only(left=180, top=35, right=52, bottom=35),
        ),
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../../../assets")

