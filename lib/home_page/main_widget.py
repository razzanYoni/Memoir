import flet as ft
from datetime import datetime
from time import sleep

import lib.src.artikel.presentation.artikel_screen as artikel_screen
import lib.src.catatan_jadwal.presentation.catatan_jadwal_screen as catatan_jadwal_screen
import lib.src.catatan_target.presentation.catatan_target_screen as catatan_target_screen
import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_screen as catatan_kegiatan_screen

import lib.src.catatan_jadwal.controller.catatan_jadwal_controller as catatan_jadwal_controller


class FeatureButton(ft.Container):
    def feature_btn_on_click(self, e):
        self.page.controls.clear()
        self.feature_screen.main(self.page)
        
    def __init__(self, name, icon, feature_screen):
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Container(
                        image_src=icon,
                        width=73,
                        height=73,
                        tooltip=name,
                        on_click=self.feature_btn_on_click,
                        disabled=False,
                    ),
                    ft.Text(
                        value=name,
                        size=30,
                        color="#ffffff",
                        font_family="Inter"
                    )
                ],
            ),
            disabled=False,
        )
        self.feature_screen = feature_screen

class SideBar(ft.Container):
    def __init__(self, page:ft.Page, user: str):
        self.hamburger_btn = ft.Container(
            image_src="icons/hamburger_icon.png",
            padding=10,
            width=62,
            height=55,
            on_click=self.hamburger_btn_on_click,
        )
        self.times_of_day = "Pagi" if datetime.now().hour < 12 else (
            "Siang" if datetime.now().hour < 18 else "Malam")

        self.user = user

        self.view = ft.Ref[ft.Container]()
        self.default = ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="Selamat " + self.times_of_day + "!",
                                size=40,
                                color="#ffffff",
                                font_family="Inter SemiBold"
                            ),

                            ft.Text(
                                value=self.user,
                                size=40,
                                color="#ffffff",
                                font_family="Inter Light"
                            )
                        ],
                        spacing=19,
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    ),
                    expand=True,
                    margin=ft.margin.only(bottom=130),
                    alignment=ft.alignment.bottom_right,
                )
        
        self.featured = ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="MENU",
                                size=30,
                                color="#ffffff",
                                bgcolor=ft.colors.TRANSPARENT,
                                font_family="Inter",
                            ),

                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        FeatureButton(
                                            "Kegiatan",
                                            "icons/ctt_kegiatan_icon.png",
                                            catatan_kegiatan_screen
                                        ),

                                        FeatureButton(
                                            "Jadwalku",
                                            "icons/ctt_jadwal_icon.png",
                                            catatan_jadwal_screen
                                        ),

                                        FeatureButton(
                                            "Targetku",
                                            "icons/ctt_target_icon.png",
                                            catatan_target_screen
                                        ),

                                        FeatureButton(
                                            "Artikel Terkait",
                                            "icons/artikel_icon.png",
                                            artikel_screen
                                        ),
                                    ],
                                    spacing=25,
                                ),
                                margin=ft.margin.only(top=30, left=20),
                                alignment=ft.alignment.top_left,
                            )
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                        padding=ft.padding.only(top=70, left=30),
                    )
        super().__init__(
            ref=self.view,
            content=ft.Column(
            controls=[
                self.hamburger_btn,
                self.default,
                ]),
            bgcolor=ft.colors.TRANSPARENT,
            width=615,
            height=1024,
            padding=ft.padding.only(left=52, top=71),
            alignment=ft.alignment.top_left,
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(300),
        )
        self.is_default = True

        self.page = page
        # self.default_mode()

    def hamburger_btn_on_click(self, e):
        self.is_default = not self.is_default
        if self.is_default:
            self.view.current.offset = ft.transform.Offset(-2, 0)
            self.page.update()
            sleep(0.31)

            super.__setattr__(self, "bgcolor", ft.colors.TRANSPARENT)
            self.hamburger_btn.image_src = "icons/hamburger_icon.png"
            self.view.current.offset = ft.transform.Offset(0, 0)
            self.view.current.content.controls.pop()
            self.view.current.content.controls.append(self.default)
            self.view.current.offset = ft.transform.Offset(0, 0)
            self.update()
            self.page.update()
        else:
            self.view.current.offset = ft.transform.Offset(-2, 0)
            self.page.update()
            sleep(0.31)

            super.__setattr__(self, "bgcolor", "#07184f")
            self.hamburger_btn.image_src = "icons/hamburger_alt_icon.png"
            self.view.current.offset = ft.transform.Offset(0, 0)
            self.view.current.content.controls.pop()
            self.view.current.content.controls.append(self.featured)
            self.view.current.offset = ft.transform.Offset(0, 0)
            self.update()
            self.page.update()

class Time(ft.Container):
    def __init__(self):
        self.time = ft.Ref[ft.Text]()

        super().__init__(
            content=ft.Text(
                ref=self.time,
                size=170,
                color="#06184e",
                font_family="Inter Medium",
                opacity=1
            ),
            opacity=1,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.TRANSPARENT
        )
        self.time.current.value = (str(datetime.now().hour) if datetime.now().hour > 9 else ("0" + str(
            datetime.now().hour))) + "." + (str(datetime.now().minute) if datetime.now().minute > 9 else (
                "0" + str(datetime.now().minute)))


# TODO: Reminder Control, wait for the backend
class Reminders(ft.UserControl):
    def __init__(self):
        super().__init__(
            expand=True,
        )

    def build(self):
        # _catatan_jadwal_control = catatan_jadwal_controller.CatatanJadwalController()
        # _list_catatan_jadwal = _catatan_jadwal_control.get_list_catatan_jadwal()
        return ft.Column(
            controls=[],
            expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )


class Notification(ft.Container):
    def __init__(self):
        self.time = Time()
        self.reminders = Reminders()
        super().__init__(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        self.time,
                        ft.Divider(
                            height=1,
                            color=ft.colors.TRANSPARENT,
                            visible=False
                        ),
                        self.reminders
                    ],
                    opacity=1,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_right,
                    end=ft.alignment.bottom_left,
                    colors=[
                        "#e9ebf9",
                        "#f1f1f1"]
                ),
                border_radius=ft.border_radius.all(20),
                opacity=0.7,
            ),
            width=825,
            padding=ft.padding.only(top=51, left=135, bottom=60, right=65),
            alignment=ft.alignment.center,
        )
