import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

import lib.home_page.main_screen as main_screen

import lib.src.catatan_kegiatan.data.catatan_kegiatan_model as catatan_kegiatan_model
import lib.src.catatan_kegiatan.controller.catatan_kegiatan_controller as catatan_kegiatan_controller
import lib.src.catatan_kegiatan.presentation.tambah_catatan_kegiatan_screen as tambah_catatan_kegiatan_screen
import lib.src.catatan_kegiatan.presentation.lihat_catatan_kegiatan_screen as lihat_catatan_kegiatan_screen

matplotlib.use("svg")


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

# !: bisa pake ft.LineChart
#  TODO
# ?

class GrafikPerasaan(ft.Container):
    @staticmethod
    def getFrame():
        _catatan_kegiatan_controller = catatan_kegiatan_controller.CatatanKegiatanController()
        catatan_kegiatan_list = _catatan_kegiatan_controller.getListCatatanKegiatan()
        jenis_perasaan_and_tanggal_list = [(i.getJenisPerasaan()) for i in catatan_kegiatan_list]
        df = pd.DataFrame(jenis_perasaan_and_tanggal_list, columns=['jenis_perasaan'])

        fig, ax = plt.subplots()
        ax.set_facecolor('#07184f')
        ax.axes.get_yaxis().set_visible(False)
        ax.axes.get_xaxis().set_visible(False)
        ax.set_ylabel('Jenis Perasaan', color='#f5f5f5')
        ax.set_ylim(0, 5)
        ax.set_xlim(0, len(catatan_kegiatan_list)-1 if len(catatan_kegiatan_list) < 30 else 30)
        ax.plot(df['jenis_perasaan'], color='#f5f5f5')
        for line in ax.get_lines():
            line.set_linewidth(1)
            line.set_color('#f5f5f5')

        ax.axhline(y=0.5, color='#f5f5f5', linewidth=1)
        for spine in ax.spines.values():
            spine.set_visible(False)

        fig.set_figheight(2.1979166667)
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

        return MatplotlibChart(
            fig,
            expand=True,
            isolated=True,
            transparent=True,
        )

    def update(self):
        super.__setattr__(self, "content", self.getFrame())
        self.page.update()

    def __init__(self, page: ft.Page):
        super().__init__(
            content=self.getFrame(),
            height=300,
            width=1164,
            bgcolor="#07184f",
            border_radius=10,
            alignment=ft.alignment.center,
        )
        self.page = page


# TODO : Create add view catatan kegiatan
class AddCatatanKegiatanButton(ft.Container):
    def add_catatan_kegiatan_button_on_click(self, e):
        self.page.controls.clear()
        tambah_catatan_kegiatan_screen.main(self.page)
        self.page.update()

    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/add_ctt_kegiatan_button.png",
            on_click=self.add_catatan_kegiatan_button_on_click,
            width=100,
            height=68,
        )
        self.page = page


class CatatanKegiatan(ft.UserControl):
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


    def __init__(self, catatan_kegiatan: catatan_kegiatan_model.CatatanKegiatan):
        super().__init__()
        self._catatan_kegiatan = catatan_kegiatan

    def catatan_kegiatan_on_click(self, e):
        self.page.controls.clear()
        # self.page.clean()
        lihat_catatan_kegiatan_screen.main(self.page, self._catatan_kegiatan.getID())

    def build(self):
        if self._catatan_kegiatan.getJenisPerasaan() == 1:
            self.emoji = "😢"
        elif self._catatan_kegiatan.getJenisPerasaan() == 2:
            self.emoji = "😕"
        elif self._catatan_kegiatan.getJenisPerasaan() == 3:
            self.emoji = "😐"
        elif self._catatan_kegiatan.getJenisPerasaan() == 4:
            self.emoji = "😊"
        else:   # self._catatan_kegiatan.getJenisPerasaan() == 5:
            self.emoji = "😁"

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            value=self.emoji,
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

                    # judul tanggal catatan kegiatan
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value=self.convertTanggal(self._catatan_kegiatan.getTanggal()),
                                    size=20,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter ExtraLight",
                                    color="#ffffff",
                                ),

                                ft.Text(
                                    value=self._catatan_kegiatan.getDescKegiatan(),
                                    size=35,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter Medium",
                                    color="#ffffff"
                                ),

                                ft.Text(
                                    value=self._catatan_kegiatan.getJam(),
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
            on_click=self.catatan_kegiatan_on_click,
            bgcolor="#444980",
            border_radius=15,
        )


class DaftarCatatanKegiatan(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        _catatan_kegiatan_controller = catatan_kegiatan_controller.CatatanKegiatanController()
        catatan_kegiatan_list = _catatan_kegiatan_controller.getListCatatanKegiatan()

        if len(catatan_kegiatan_list) == 0:
            return ft.Container(
                content=ft.Text(
                    value="Tidak ada catatan kegiatan",
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
                    CatatanKegiatan(i) for i in catatan_kegiatan_list
                ],
                spacing=15,
            ),
            width=1164,
            bgcolor=ft.colors.TRANSPARENT,
            alignment=ft.alignment.center,
        )