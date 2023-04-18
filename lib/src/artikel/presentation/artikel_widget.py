import flet as ft

import lib.home_page.main_screen as main_screen
import lib.src.artikel.controller.artikel_controller as artikel_controller
import lib.src.artikel.data.artikel_model as artikel_model
# import lib.src.artikel.presentation.lihat_artikel_screen as lihat_artikel_screen

class HomeButton(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/home_button.png",
            on_click=self.home_button_on_click,
            width=64,
            height=64,
        )
        self.page = page

    def home_button_on_click(self, e):
        self.page.controls.clear()
        main_screen.main(self.page)
        self.page.update()

class Artikel(ft.UserControl):
    @staticmethod
    def convertTanggal(tanggal: str):
        tanggal = tanggal.split("-")
        bulan = {
            "01": "Januari",
            "02": "Februari",
            "03": "Maret",
            "04": "April",
            "05": "Mei",
            "06": "Juni",
            "07": "Juli",
            "08": "Agustus",
            "09": "September",
            "10": "Oktober",
            "11": "November",
            "12": "Desember",
        }

        return tanggal[2] + " " + bulan[tanggal[1]] + " " + tanggal[0]


    def __init__(self, artikel: artikel_model.Artikel):
        super().__init__()
        self._artikel = artikel

    def artikel_on_click(self, e):
        self.page.controls.clear()
        # self.page.clean()
        lihat_artikel_screen.main(self.page, self._artikel.getID())

    def build(self):

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            value="test",
                            size=50,
                            text_align=ft.TextAlign.CENTER,
                            color="#ffffff",
                        ),
                        width=150,
                        height=150,
                        padding=ft.padding.all(20)
                    ),

                    ft.VerticalDivider(
                        width=10,
                        visible=False,
                    ),

                    # judul tanggal artikel
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value="tanggal",
                                    size=20,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter ExtraLight",
                                    color="#ffffff",
                                ),

                                ft.Text(
                                    value="deskripsi",
                                    size=35,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter Medium",
                                    color="#ffffff"
                                ),

                                ft.Text(
                                    value="jam",
                                    size=15,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter ExtraLight",
                                    color="#ffffff"
                                ),
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                        width=1000,
                        alignment=ft.alignment.center_left,
                    )
                ],
            ),
            
            width=1164,
            height=120,
            on_click=self.artikel_on_click,
            bgcolor="#444980",
            border_radius=15,
        )

class DaftarArtikel(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        _artikel_controller = artikel_controller.artikelController()
        artikel_list = _artikel_controller.getListArtikel()  
        if len(artikel_list) == 0:
            return ft.Container(
                content=ft.Text(
                    value="Tidak ada Artikel",
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
                height=300,
                width=1164,
            )
        return ft.Container(
            content=ft.Column(
                controls=[
                    Artikel(i) for i in artikel_list
                ],
                spacing=15,
            ),
            width=1164,
            bgcolor=ft.colors.TRANSPARENT,
            alignment=ft.alignment.center,
        )