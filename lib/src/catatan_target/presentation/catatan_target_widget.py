import flet as ft

import lib.home_page.main_screen as main_screen
import lib.src.catatan_target.data.catatan_target_model as catatan_target_model
import lib.src.catatan_target.controller.catatan_target_controller as catatan_target_controller
import lib.src.catatan_target.presentation.tambah_catatan_target_screen as tambah_catatan_target_screen
import lib.src.catatan_target.presentation.lihat_catatan_target_screen as lihat_catatan_target_screen

class HomeButton(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/home_button.png",
            on_click=self.home_button_on_click,
            width=100,
            height=68,
        )
        self.page = page

    def home_button_on_click(self, e):
        self.page.controls.clear()
        main_screen.main(self.page)
        self.page.update()

class AddCatatanTargetButton(ft.Container):
    def add_catatan_target_button_on_click(self, e):
        self.page.controls.clear()
        tambah_catatan_target_screen.main(self.page)

    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/tes.png",
            on_click=self.add_catatan_target_button_on_click,
            width=60,
            height=60,
        )
        self.page = page

@staticmethod
def getStatusColor(status: str):
    if status == "Belum":
        statusColor = "#FF97E2"
    elif status == "Berlangsung":
        statusColor = "#F1EAA5"
    else:
        statusColor = "#7FE5D3"
    return statusColor

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


class CatatanTarget(ft.UserControl):
    def __init__(self, catatan_target: catatan_target_model.CatatanTarget):
        super().__init__()
        self._catatan_target = catatan_target

    def catatan_target_on_click(self, e):
        self.page.controls.clear()
        lihat_catatan_target_screen.main(self.page, self._catatan_target.getID())

    def build(self):
        return ft.Container(
            content=ft.Row(
                spacing=20,
                controls=[
                    ft.Container(
                        width=50,
                        height=50,
                        padding=ft.padding.all(20),
                        border_radius=25,
                        bgcolor=getStatusColor(self._catatan_target.getStatus())
                    ),

                    ft.VerticalDivider(
                        width=10,
                        visible=False,
                    ),

                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value=self._catatan_target.getTarget(),
                                    size=35,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter Medium",
                                    color="#ffffff"
                                ),

                                ft.Text(
                                    value=convertTanggal(self._catatan_target.getWaktuCapai()),
                                    size=20,
                                    text_align=ft.TextAlign.LEFT,
                                    font_family="Inter ExtraLight",
                                    color="#ffffff",
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
            on_click=self.catatan_target_on_click,
            bgcolor="#444980",
            border_radius=15,
            padding=ft.padding.symmetric(horizontal=25),
        )


class DaftarCatatanTarget(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        _catatan_target_controller = catatan_target_controller.CatatanTargetController()
        catatan_target_list = _catatan_target_controller.getListCatatanTarget()

        if len(catatan_target_list) == 0:
            return ft.Container(
                content=ft.Text(
                    value="Tidak ada catatan target",
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
                    CatatanTarget(i) for i in catatan_target_list
                ],
                spacing=15,
            ),
            width=1164,
            bgcolor=ft.colors.TRANSPARENT,
            alignment=ft.alignment.center,
        )
