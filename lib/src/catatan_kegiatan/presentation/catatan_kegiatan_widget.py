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
        catatan_kegiatan_list.reverse()
        catatan_kegiatan_list = catatan_kegiatan_list[:30]
        jenis_perasaan_list = [(i.getJenisPerasaan()) for i in catatan_kegiatan_list]
        if len(jenis_perasaan_list) == 1:
            jenis_perasaan_list.append(jenis_perasaan_list[0])
        df = pd.DataFrame(jenis_perasaan_list, columns=['jenis_perasaan'])

        fig, ax = plt.subplots()
        ax.set_facecolor('#07184f')
        ax.axes.get_yaxis().set_visible(False)
        ax.axes.get_xaxis().set_visible(False)
        ax.set_ylabel('Jenis Perasaan', color='#f5f5f5')
        ax.set_ylim(0, 5.5)
        xmax = len(jenis_perasaan_list) - 1 if len(jenis_perasaan_list) > 1 and len(jenis_perasaan_list) < 30 else 30
        ax.set_xlim(0, xmax)
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
        # self.page.update()

    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/add_ctt_kegiatan_button.png",
            on_click=self.add_catatan_kegiatan_button_on_click,
            width=100,
            height=68,
        )
        self.page = page

@staticmethod
def getJenisPerasaanEmoji(jenis_perasaan: int):
    if jenis_perasaan == 1:
        return "😢"
    elif jenis_perasaan == 2:
        return "😕"
    elif jenis_perasaan == 3:
        return "😐"
    elif jenis_perasaan == 4:
        return "😊"
    else:   # self._catatan_kegiatan.getJenisPerasaan() == 5:
        return "😁"

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


class CatatanKegiatan(ft.UserControl):


    def __init__(self, catatan_kegiatan: catatan_kegiatan_model.CatatanKegiatan):
        super().__init__()
        self._catatan_kegiatan = catatan_kegiatan

    def catatan_kegiatan_on_click(self, e):
        self.page.controls.clear()
        # self.page.clean()
        lihat_catatan_kegiatan_screen.main(self.page, self._catatan_kegiatan.getID())

    def build(self):
        self.emoji = getJenisPerasaanEmoji(self._catatan_kegiatan.getJenisPerasaan())

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
                                    value=convertTanggal(self._catatan_kegiatan.getTanggal()),
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
                                    value=self._catatan_kegiatan.getJam()[0:5],
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


class Feel(ft.Container):
    def __init__(self, feel: int = 5):
        self.feelDD = ft.Dropdown(
            label="Feel",
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[
                ft.dropdown.Option(key="1", text="😢"),
                ft.dropdown.Option(key="2", text="😕"),
                ft.dropdown.Option(key="3", text="😐"),
                ft.dropdown.Option(key="4", text="😊"),
                ft.dropdown.Option(key="5", text="😁"),
            ],
            value=str(feel),
            width=70,
        )

        super().__init__(
            content=ft.Row(
                controls=[
                    self.feelDD
                ],
                spacing=5,
                width=220,
                height=60,
                visible=True,
            ),
            visible=True,
        )

        print(self.get_feel())

    def get_feel(self):
        return int(self.feelDD.value)
