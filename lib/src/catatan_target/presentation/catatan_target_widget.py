import flet as ft

import lib.home_page.main_screen as main_screen
import lib.src.catatan_target.data.catatan_target_model as catatan_target_model
import lib.src.catatan_target.controller.catatan_target_controller as catatan_target_controller
import lib.src.catatan_target.presentation.tambah_catatan_target_screen as tambah_catatan_target_screen
import lib.src.catatan_target.presentation.lihat_catatan_target_screen as lihat_catatan_target_screen

class HomeButton(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="icons/home_button_dark.png",
            on_click=self.home_button_on_click,
            width=100,
            height=50,
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

@staticmethod
def buttonContent(text:str, selected: bool):
    if selected:
        return ft.Text(
                    text,
                    size=20,
                    font_family="Inter Light",
                    color="#A7AECD")
    else:
        return ft.Text(
                    text,
                    size=20,
                    font_family="Inter Light",
                    color="#D9D9D9")

@staticmethod
def buttonSide(selected: bool):
    if selected:
        return ft.BorderSide(3, "#A7AECD")
    else:
        return ft.BorderSide(3, "#D9D9D9")

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
        self.belumButton.content=buttonContent("Belum", True)
        self.berlangsungButton.content=buttonContent("Berlangsung", False)
        self.selesaiButton.content=buttonContent("Selesai", False)
        self.semuaButton.content=buttonContent("Semua", False)
        self.belumButton.style.side=buttonSide(True)
        self.berlangsungButton.style.side=buttonSide(False)
        self.selesaiButton.style.side=buttonSide(False)
        self.semuaButton.style.side=buttonSide(False)

        try:
            self.colRef.current.controls.clear()
            self.colRef.current.controls = [CatatanTarget(i) for i in self.belum_catatan_target_list]

            if len(self.colRef.current.controls) == 0:
                self.colRef.current.controls = [ft.Container(
                                                    ft.Text(
                                                        value="Tidak ada catatan target berstatus \"Belum\"",
                                                        size=30,
                                                        text_align=ft.TextAlign.CENTER,
                                                    ),

                                                    alignment=ft.alignment.center,
                                                    height=300,
                                                    width=1164
                                                    )
                                                ]
        except Exception as e:
            # print("-----")
            # print(e)
            # print("-----")
            pass

        self.update()
        self.page.update()

    def berlangsung_catatan_target_on_click(self, e):
        self.belumButton.content=buttonContent("Belum", False)
        self.berlangsungButton.content=buttonContent("Berlangsung", True)
        self.selesaiButton.content=buttonContent("Selesai", False)
        self.semuaButton.content=buttonContent("Semua", False)
        self.belumButton.style.side=buttonSide(False)
        self.berlangsungButton.style.side=buttonSide(True)
        self.selesaiButton.style.side=buttonSide(False)
        self.semuaButton.style.side=buttonSide(False)

        try:
            self.colRef.current.controls.clear()
            self.colRef.current.controls = [CatatanTarget(i) for i in self.berlangsung_catatan_target_list]

            if len(self.colRef.current.controls) == 0:
                self.colRef.current.controls = [ft.Container(
                                                    ft.Text(
                                                        value="Tidak ada catatan target berstatus \"Berlangsung\"",
                                                        size=30,
                                                        text_align=ft.TextAlign.CENTER,
                                                    ),

                                                    alignment=ft.alignment.center,
                                                    height=300,
                                                    width=1164
                                                    )
                                                ]
        except Exception as e:
            # print("-----")
            # print(e)
            # print("-----")
            pass

        self.update()
        self.page.update()

    def selesai_catatan_target_on_click(self, e):
        self.belumButton.content=buttonContent("Belum", False)
        self.berlangsungButton.content=buttonContent("Berlangsung", False)
        self.selesaiButton.content=buttonContent("Selesai", True)
        self.semuaButton.content=buttonContent("Semua", False)
        self.belumButton.style.side=buttonSide(False)
        self.berlangsungButton.style.side=buttonSide(False)
        self.selesaiButton.style.side=buttonSide(True)
        self.semuaButton.style.side=buttonSide(False)

        try:
            self.colRef.current.controls.clear()
            self.colRef.current.controls = [CatatanTarget(i) for i in self.selesai_catatan_target_list]

            if len(self.colRef.current.controls) == 0:
                self.colRef.current.controls = [ft.Container(
                                                    ft.Text(
                                                        value="Tidak ada catatan target berstatus \"Selesai\"",
                                                        size=30,
                                                        text_align=ft.TextAlign.CENTER,
                                                    ),

                                                    alignment=ft.alignment.center,
                                                    height=300,
                                                    width=1164
                                                    )
                                                ]
        except Exception as e:
            # print("-----")
            # print(e)
            # print("-----")
            pass

        self.update()
        self.page.update()

    def semua_catatan_target_on_click(self, e):
        self.belumButton.content=buttonContent("Belum", False)
        self.berlangsungButton.content=buttonContent("Berlangsung", False)
        self.selesaiButton.content=buttonContent("Selesai", False)
        self.semuaButton.content=buttonContent("Semua", True)
        self.belumButton.style.side=buttonSide(False)
        self.berlangsungButton.style.side=buttonSide(False)
        self.selesaiButton.style.side=buttonSide(False)
        self.semuaButton.style.side=buttonSide(True)

        try:
            self.colRef.current.controls.clear()
            self.colRef.current.controls = [CatatanTarget(i) for i in self.semua_catatan_target_list]

            if len(self.colRef.current.controls) == 0:
                self.colRef.current.controls = [ft.Container(
                                                    ft.Text(
                                                        value="Tidak ada catatan target",
                                                        size=30,
                                                        text_align=ft.TextAlign.CENTER,
                                                    ),

                                                    alignment=ft.alignment.center,
                                                    height=300,
                                                    width=1164
                                                    )
                                                ]
        except Exception as e:
            # print("-----")
            # print(e)
            # print("-----")
            pass

        self.update()
        self.page.update()

    def search_on_change(self, e):
        self.belumButton.content=buttonContent("Belum", False)
        self.berlangsungButton.content=buttonContent("Berlangsung", False)
        self.selesaiButton.content=buttonContent("Selesai", False)
        self.semuaButton.content=buttonContent("Semua", True)
        self.belumButton.style.side=buttonSide(False)
        self.berlangsungButton.style.side=buttonSide(False)
        self.selesaiButton.style.side=buttonSide(False)
        self.semuaButton.style.side=buttonSide(True)

        try:
            self.colRef.current.controls.clear()
            self.colRef.current.controls = [CatatanTarget(i) for i in self._catatan_target_controller.getCatatanTargetFromSearch(e.control.value)]

            if len(self.colRef.current.controls) == 0:
                self.this_content = ft.Container(
                content=ft.Text(
                    value="Tidak ada catatan target",
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.alignment.center,
                height=300,
                width=1164,
            )
                self.colRef.current.controls = [ft.Container(
                                                    ft.Text(
                                                        value="Tidak ada catatan target yang dicari",
                                                        size=30,
                                                        text_align=ft.TextAlign.CENTER,
                                                    ),

                                                    alignment=ft.alignment.center,
                                                    height=300,
                                                    width=1164
                                                    )
                                                ]
        except Exception as e:
            # print("-----")
            # print(e)
            # print("-----")
            pass

        self.update()
        self.page.update()

    def build(self):
        self.semuaButton = ft.TextButton(
                                    content=buttonContent("Semua", True),
                                    on_click=self.semua_catatan_target_on_click,
                                    style=ft.ButtonStyle(
                                        side=ft.BorderSide(3, "#A7AECD"),
                                        bgcolor=ft.colors.TRANSPARENT,
                                    ),
                                    width=150,
                                    height=50,
                                )
        self.belumButton = ft.TextButton(
                                content=buttonContent("Belum", False),
                                on_click=self.belum_catatan_target_on_click,
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(3, "#D9D9D9"),
                                    bgcolor=ft.colors.TRANSPARENT,
                                ),
                                width=150,
                                height=50,
                            )
        self.berlangsungButton = ft.TextButton(
                                    content=buttonContent("Berlangsung", False),
                                    on_click=self.berlangsung_catatan_target_on_click,
                                    style=ft.ButtonStyle(
                                        side=ft.BorderSide(3, "#D9D9D9"),
                                        bgcolor=ft.colors.TRANSPARENT,
                                    ),
                                    width=150,
                                    height=50,
                                )

        self.selesaiButton = ft.TextButton(
                                    content=buttonContent("Selesai", False),
                                    on_click=self.selesai_catatan_target_on_click,
                                    style=ft.ButtonStyle(
                                        side=ft.BorderSide(3, "#D9D9D9"),
                                        bgcolor=ft.colors.TRANSPARENT,
                                    ),
                                    width=150,
                                    height=50,
                                )
        if len(self.catatan_target_list) == 0:
            self.this_content = ft.Container(
                content=ft.Text(
                    value="Tidak ada catatan target",
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.alignment.center,
                height=300,
                width=1164,
            )
        else :
            self.this_content = ft.Container(
            content=ft.Column(
                controls = [CatatanTarget(i) for i in self.catatan_target_list],
                ref=self.colRef,
                spacing=15,
            ),
            bgcolor=ft.colors.TRANSPARENT,
            alignment=ft.alignment.center,
        )

        return ft.Container(
            alignment=ft.alignment.center,
            bgcolor=ft.colors.TRANSPARENT,
            content=ft.Column(
                controls=[
                    ft.Container(
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Image(
                                    src="/icons/search_icon.png",
                                    height=20,
                                    fit=ft.ImageFit.CONTAIN
                                ),

                                ft.TextField(
                                    border="none",
                                    expand=True,
                                    hint_text="Cari Sesuatu",
                                    on_change=self.search_on_change,
                                    hint_style=ft.TextStyle(
                                        color=ft.colors.WHITE,
                                        font_family="Inter Light",
                                        size=20
                                    ),
                                    text_style=ft.TextStyle(
                                        color=ft.colors.WHITE,
                                        font_family="Inter Light",
                                        size=20
                                    )
                                )
                            ]
                        ),
                        bgcolor="#06184E",
                        height=50,
                        width=1164,
                        border_radius=25,
                        padding=ft.padding.symmetric(horizontal=20)
                    ),

                    ft.Row(
                        spacing=20,
                        controls=[
                            ft.Divider(
                                height=10,
                                visible=False,
                            ),
                            self.semuaButton,
                            self.belumButton,
                            self.berlangsungButton,
                            self.selesaiButton
                        ],
                    ),
                    self.this_content,
                ]
            )
        )
