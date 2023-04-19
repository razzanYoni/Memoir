import flet as ft

import lib.home_page.main_screen as main_screen
import lib.src.artikel.controller.artikel_controller as artikel_controller
import lib.src.artikel.presentation.lihat_artikel_screen as lihat_artikel_screen
import lib.src.artikel.data.artikel_model as artikel_model
from lib.src.utilities.util import image_to_blob, blob_to_base64
# import lib.src.artikel.presentation.lihat_artikel_screen as lihat_artikel_screen

class HomeButton(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/Home Button.png",
            on_click=self.home_button_on_click,
            width=64,
            height=64,
        )
        self.page = page

    def home_button_on_click(self, e):
        self.page.controls.clear()
        main_screen.main(self.page)
        self.page.update()

class SearchBar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            text="Hi",
        )
        self.page = page

    def search_bar_on_click(self,e):
        self.page.controls.clear()

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
        _artikel_controller = artikel_controller.ArtikelController()
        _artikel = _artikel_controller.getArtikel(self._artikel.getID())

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Container(
                            image_src_base64=str(blob_to_base64(_artikel[5])),
                            image_fit=ft.ImageFit.COVER,
                        ),
                        border_radius=20,
                        width=200,
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
                                ft.Divider(
                                    height=10,
                                    visible=True,
                                ),
                                ft.Text(
                                    value=self._artikel.getTanggal(),
                                    size=20,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter ExtraLight",
                                    color="#60648B",
                                ),

                                ft.Text(
                                    value=self._artikel.getJudul(),
                                    size=35,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter Medium",
                                    color="#60648B"
                                ),

                                ft.Text(
                                    value=self._artikel.getPengarang(),
                                    size=15,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter ExtraLight",
                                    color="#60648B"
                                ),
                                ft.Divider(
                                    
                                    height=10,
                                    visible=True,
                                ),
                            ],
                            spacing=6,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                        width=1000,
                        alignment=ft.alignment.center_left,
                    )
                ],
            ),
            
            width=1100,
            height=150,
            on_click=self.artikel_on_click,
            # bgcolor="#A7AECD",
            border_radius=15,
        )

class DaftarArtikel(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self._artikel_controller = artikel_controller.ArtikelController()
        self.artikel_list = self._artikel_controller.getListArtikel()
        self.colRef = ft.Ref[ft.Column]()
    
    def search_on_change(self, e):
        self.colRef.current.controls.clear()
        self.colRef.current.controls = [Artikel(i) for i in self._artikel_controller.getArtikelFromSearch(e.control.value)]
        if len(self.colRef.current.controls) == 0:
            self.colRef.current.controls = [
                ft.Divider(
                    height = 2,
                    color = "#60648B",
                ),
                ft.Container(
                    ft.Text(
                    value="Tidak ada artikel yang dicari",
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                    font_family="Inter Light",
                    color = "#60648B",
                
                    ),
                width = 1300,
            )]
        self.update()
        self.page.update()

    def build(self):
        # This content
        if len(self.artikel_list) == 0:
            self.this_content = ft.Container(
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
        else:
            self.this_content = ft.Container(
                content=ft.Column(
                    ref=self.colRef,
                    # controls=[
                    #     Artikel(i) for i in self.artikel_list
                    # ],
                    spacing=15,
                ),
                width=1164,
                bgcolor=ft.colors.TRANSPARENT,
                alignment=ft.alignment.center,
            )
        self.colRef.current.controls = [Artikel(i) for i in self.artikel_list]
    
        return ft.Container(
            alignment = ft.alignment.center,
            bgcolor = ft.colors.TRANSPARENT,
            content = ft.Column(
                controls = [
                    # Search Bar,
                    ft.Container(
                        # TODO styling Textfieldnya
                        content=ft.Row(
                            controls = [
                                ft.Container(
                                    image_src="icons/search_icon.png",
                                    width=25,
                                    height=25,
                                    margin = ft.margin.only(left=5, top=-16, right=0, bottom=0),
                                    # padding=ft.padding.only(left=0, top=-10, right=0, bottom=0),
                                    
                                ),
                                ft.TextField(
                                    hint_text="Cari judul artikel",
                                    on_change=self.search_on_change,
                                    hint_style=ft.TextStyle(
                                        color="#FFFFFF",
                                        size=20,
                                        font_family="Inter ExtraLight",
                                    ),
                                    text_style=ft.TextStyle(
                                        color="#FFFFFF",
                                        size=20,
                                        font_family="Inter ExtraLight",
                                    ),
                                    border_color="transparent"
                                ),
                            ],
                        ),
                        # border= "transparent",
                        border_radius=25,
                        bgcolor="#06184E",
                        height=50,
                        width=1200,
                        padding=ft.padding.only(left=20, top=15, right=0, bottom=0),
                        margin=15,
                    ),

                    # Decorator
                    ft.Container(
                        ft.Text(
                            value = "Jelajahi Harimu",
                            color = "#043EDB",
                            size=45,
                            font_family="Inter SemiBold",
                        ),
                        padding=ft.padding.only(left=20, top=20, right=0, bottom=0),
                    ),
                    
                    ft.Divider(
                        height=10
                    ),

                    # Featured Article
                    FeaturedArtikel(self.page),

                    # Artikel lainnya
                    ft.Container(
                        ft.Text(
                        value = "Cek artikel lainnya",
                        size=35,
                        font_family="Inter Light",
                        color = "#06184E",
                        ),
                        padding=ft.padding.only(left=57, top=0, right=0, bottom=0),
                    ),
                    

                    # Artikel List
                    self.this_content,
                ]
            )
        )
        
    
class ArtikelCard(ft.UserControl):
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
        self.page.clean()
        lihat_artikel_screen.main(self.page, self._artikel.getID())

    def build(self):
        _artikel_controller = artikel_controller.ArtikelController()
        _artikel = _artikel_controller.getArtikel(self._artikel.getID())
        return ft.Container(
            image_src_base64=str(blob_to_base64(_artikel[5])),
            image_fit=ft.ImageFit.COVER,
            image_opacity= 0.7,

            content = ft.Row(
                controls = [
                    ft.VerticalDivider(
                        width=50,
                        visible=False,
                    ),
                    ft.Container(
                        content = ft.Column(
                            controls = [
                                
                                ft.Text(
                                    value = self._artikel.getJudul(),
                                    color = "#FFFFFF",
                                    size = 40,
                                    font_family="Inter SemiBold",
                                    overflow=ft.TextOverflow.FADE,
                                
                                ),
                                ft.Text(
                                    value = self._artikel.getPengarang(),
                                    color = "#FFFFFF",
                                    size = 20,
                                    font_family="Inter Light",
                                )
                            ],
                        ),
                        width=630,
                        alignment=ft.alignment.center_left,
                        margin = 20,
                    ),
                ],
            ),
            margin= 20,
            width= 660,
            height=300,
            on_click=self.artikel_on_click,
            bgcolor="#000000",
            border_radius=15,
        )    

class FeaturedArtikel(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        _artikel_controller = artikel_controller.ArtikelController()
        artikel_list = _artikel_controller.getListArtikel()

        if len(artikel_list) < 0:
            return ft.Container(
                content=ft.Text(
                    value="Tidak ada artikel",
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
                height=300,
                width=1164,
            )
        return ft.Container(
            content=ft.Row(
                controls=[

                    ArtikelCard(i) for i in artikel_list
                ],
                spacing=15,
            ),
            width=1164,
            bgcolor=ft.colors.TRANSPARENT,
            alignment=ft.alignment.center,
        )