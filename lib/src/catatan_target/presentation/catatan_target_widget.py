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
    # def __init__(self, page: ft.Page):
    def __init__(self):
        super().__init__()
        # self.page = page
        self._catatan_target_controller = catatan_target_controller.CatatanTargetController()
        self.catatan_target_list = self._catatan_target_controller.getListCatatanTarget()
        self.belum_catatan_target_list = self._catatan_target_controller.getBelumCatatanTarget()
        self.berlangsung_catatan_target_list = self._catatan_target_controller.getBerlangsungCatatanTarget()
        self.selesai_catatan_target_list = self._catatan_target_controller.getSelesaiCatatanTarget()
        self.semua_catatan_target_list = self._catatan_target_controller.getSemuaCatatanTarget()
        self.colRef = ft.Ref[ft.Column]()
    
    def belum_catatan_target_on_click(self, e):
        self.colRef.current.controls.clear()
        self.colRef.current.controls = [CatatanTarget(i) for i in self.belum_catatan_target_list]
        self.update()
        self.page.update()

    def berlangsung_catatan_target_on_click(self, e):
        self.colRef.current.controls.clear()
        self.colRef.current.controls = [CatatanTarget(i) for i in self.berlangsung_catatan_target_list]
        self.update()
        self.page.update()

    def selesai_catatan_target_on_click(self, e):
        self.colRef.current.controls.clear()
        self.colRef.current.controls = [CatatanTarget(i) for i in self.selesai_catatan_target_list]
        self.update()
        self.page.update()

    def semua_catatan_target_on_click(self, e):
        self.colRef.current.controls.clear()
        self.colRef.current.controls = [CatatanTarget(i) for i in self.semua_catatan_target_list]
        self.update()
        self.page.update()
    
    def search_on_change(self, e):
        self.colRef.current.controls.clear()
        self.colRef.current.controls = [CatatanTarget(i) for i in self._catatan_target_controller.getCatatanTargetFromSearch(e.control.value)]
        if len(self.colRef.current.controls) == 0:
            self.colRef.current.controls = [ft.Text(
                value="Tidak ada catatan target yang dicari",
                size=30,
                text_align=ft.TextAlign.CENTER,
            )]
        self.update()
        self.page.update()

    def build(self):
        if len(self.catatan_target_list) == 0:
            # TODO : styling
            self.this_content = ft.Container(
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
        else :
            self.this_content = ft.Container(
            content=ft.Column(
                ref=self.colRef,
                # controls=[
                #     # Tambah Catatan Target
                #     CatatanTarget(i) for i in self.catatan_target_list
                # ],
                spacing=15,
            ),
            bgcolor=ft.colors.TRANSPARENT,
            alignment=ft.alignment.center,
        )
        self.colRef.current.controls = [CatatanTarget(i) for i in self.catatan_target_list]

        return ft.Container(
            alignment=ft.alignment.center,
            bgcolor=ft.colors.TRANSPARENT,
            content=ft.Column(
                controls=[
                    ft.Container(
                        # TODO styling Textfieldnya
                        content=ft.TextField(
                            hint_text="Cari catatan target",
                            on_change=self.search_on_change,
                            # hint_style=ft.TextStyle(
                            # )
                            # text_style=ft.TextStyle(
                            # )
                            # border=
                        ),
                        bgcolor=ft.colors.YELLOW,
                        height=50,
                        width=1164,
                    ),
                    ft.Row(
                        controls=[
                            ft.Divider(
                                height=10,
                                visible=False,
                            ),
                            # TODO : Styling button nya
                            ft.TextButton(
                                text="SEMUA",
                                on_click=self.semua_catatan_target_on_click,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.RED,
                                    color=ft.colors.BLUE,
                                ),
                                width=250,
                                height=50,
                            ),
                            ft.TextButton(
                                text="BELUM",
                                on_click=self.belum_catatan_target_on_click,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.RED,
                                    color=ft.colors.BLUE,
                                ),
                                width=250,
                                height=50,
                            ),
                            ft.TextButton(
                                text="BERLANGSUNG",
                                on_click=self.berlangsung_catatan_target_on_click,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.RED,
                                    color=ft.colors.BLUE,
                                ),
                                width=250,
                                height=50,
                            ),
                            ft.TextButton(
                                text="SELESAI",
                                on_click=self.selesai_catatan_target_on_click,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.RED,
                                    color=ft.colors.BLUE,
                                ),
                                width=250,
                                height=50,
                            )
                        ],
                        spacing=52,
                        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.this_content,
                ]
            )
        )
