import flet as ft
from datetime import datetime
from time import sleep
import lib.src.artikel.presentation.artikel_screen as artikel_screen
import lib.src.catatan_jadwal.presentation.catatan_jadwal_screen as catatan_jadwal_screen
import lib.src.catatan_jadwal.presentation.ubah_catatan_jadwal_screen as ubah_catatan_jadwal_screen
import lib.src.catatan_target.presentation.catatan_target_screen as catatan_target_screen
import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_screen as catatan_kegiatan_screen
import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model
import lib.src.catatan_jadwal.data.catatan_jadwal_repo as catatan_jadwal_repo
import lib.src.catatan_jadwal.controller.catatan_jadwal_controller as catatan_jadwal_controller
import lib.home_page.main_screen as main_screen

class HomeButton(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="assets/icons/home_button_putih.png",
            on_click=self.home_button_on_click,
            width=64,
            height=64,
            padding=ft.padding.only(top=0, left=0, bottom=0, right=0),
            margin=ft.margin.only(bottom = 600, left=70, top=70),
        )
        self.page = page

    def home_button_on_click(self, e):
        self.page.controls.clear()
        main_screen.main(self.page)
        self.page.update()

        

class CalendarLeft(ft.Container):
    def __init__(self):
        self.calendar = Calendar()
        self.calendar_date = CalendarDate()
        super().__init__(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        self.calendar,
                        self.calendar_date
                    ],
                    opacity=1,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_right,
                    end=ft.alignment.bottom_left,
                    colors=[
                        "#A7AECD",
                        "#A7AECD"]
                ),
                border_radius=ft.border_radius.all(0),
                bgcolor="A7AECD",
                padding=ft.padding.only(top=50, left=32, bottom=30, right=72),
            ),
            width=825,
            height=625,
            padding=ft.padding.only(top=90, left=130, bottom=0, right=30),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.TRANSPARENT
)

class CalendarDate(ft.Container):
    def __init__(self):
        super().__init__(content=self.build(), bgcolor="#A7AECD")

    def build(self):
        # Define weekday names
        weekday_names = [" Mon  ", "  Tue  ", " Wed ", "  Thu  ", "   Fri  ", "   Sat  ", "   Sun  "]

        # Create weekday name labels
        weekday_labels = [
            ft.Text(
                width=59,
                value=name,
                size=23,
                color="#FFFFFF",
                font_family="Inter Medium",
                opacity=1,
                style="margin: 0 0px 0px 0px;"
            ) for name in weekday_names
        ]

        # Create calendar days
        calendar_days = []
        for i in range(35):
            day = i + 1
            if day > 31:
                calendar_days.append(
                    ft.Container(
                        bgcolor="#FFFFFF",
                        border_radius=ft.border_radius.all(10),
                        margin=ft.margin.all(7),
                        width=47,
                        height=47
                    )
                )
            else:
                calendar_days.append(
                    ft.Container(
                        content=ft.Text(
                            value=str(day),
                            size=16,
                            color="#06184E",
                            font_family="Inter Medium",
                            opacity=1,
                            style="margin: 0 auto;"
                        ),
                        bgcolor="#FFFFFF",
                        border_radius=ft.border_radius.all(10),
                        margin=ft.margin.all(7),
                        width=47,
                        height=47
                    )
                )
            
        # Group days into rows of 7
        rows = [weekday_labels] + [calendar_days[i:i+7] for i in range(0, len(calendar_days), 7)]

        # Create calendar grid
        calendar_grid = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=row,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ) for row in rows
                ],
                opacity=1,
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
                colors=[
                    "#A7AECD",
                    "#A7AECD"]
            ),
            border_radius=ft.border_radius.all(0),
            bgcolor="#A7AECD",
        )

        return calendar_grid




class Calendar(ft.Container):
    def __init__(self):
        super().__init__(
            content=self.build(),
            bgcolor="#A7AECD"
        )

    def build(self):
        return ft.Row(
            controls=[
                ft.Text(
                    value="KALENDER",
                    size=40,
                    color="#FFFFFF",
                    font_family="Inter Medium",
                    opacity=1,
                    style="margin-left: 50px; margin-top: 0px;"
                ),
                ft.Text(
                    value="April 2023",
                    size=30,
                    color="#ffffff",
                    font_family="Inter",
                    style="margin-left: 10px; margin-top: 10px;"
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,       
        )


class CalendarButton(ft.Container):
    def ubah_jadwal_button_on_click(self, e):
        self.page.controls.clear()
        id_catatan_jadwal = 0
        ubah_catatan_jadwal_screen.main(self.page, id_catatan_jadwal)

    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="assets/icons/jadwal_button1.png",
            on_click=self.ubah_jadwal_button_on_click,
            width=380,
            height=64,
            margin=17
        )
        self.page = page



class Agenda(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Text(
                value="Agenda",
                size=45,
                color="#FFFFFF",
                font_family="Inter Medium",
                opacity=1
            ),
            opacity=1,
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.TRANSPARENT,
            margin=ft.margin.only(left=250, bottom=22, top=52),
        )


class Reminders(ft.UserControl):
    def __init__(self, catatan_jadwal: catatan_jadwal_model.CatatanJadwal):
        super().__init__()
        self._catatan_jadwal = catatan_jadwal

    def ubah_jadwal_button_on_click(self, e):
        self.page.controls.clear()
        id_catatan_jadwal = 0
        ubah_catatan_jadwal_screen.main(self.page, id_catatan_jadwal)
        self.page.update()


    def build(self):
        _catatan_jadwal_controller = catatan_jadwal_controller.CatatanJadwalController()

        self.__nama_acara = self._catatan_jadwal.getNamaAcara()
        self.__desc_acara = self._catatan_jadwal.getDescAcara()
        # self.__desc_acara = self.getDescAcara() 
        retVal = self._catatan_jadwal.getNamaAcara() + "\n     " + self._catatan_jadwal.getDescAcara()
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value=retVal,
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    height="85",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                    on_click=self.ubah_jadwal_button_on_click,
                ),

                ft.Container(
                    content=ft.Text(
                        value=retVal,
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    height="85",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                    on_click=self.ubah_jadwal_button_on_click,
                ),
                ft.Container(
                    content=ft.Text(
                        value=retVal,
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    height="85",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                    on_click=self.ubah_jadwal_button_on_click,
                ),

                ft.Container(
                    content=ft.Text(
                        value=retVal,
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    height="85",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                    on_click=self.ubah_jadwal_button_on_click,
                ),

                ft.Container(
                    content=ft.Text(
                        value=retVal,
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    height="85",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                    on_click=self.ubah_jadwal_button_on_click,
                ),
            ],
            expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

class Notification(ft.Container):
    def __init__(self, catatan_jadwal: catatan_jadwal_model.CatatanJadwal):
        self.agenda = Agenda()
        self.reminders = Reminders(catatan_jadwal)
        super().__init__(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        self.agenda,
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
                border_radius=ft.border_radius.all(0),
                bgcolor=ft.colors.TRANSPARENT
            ),
            width=555,
            padding=ft.padding.only(top=0, left=155, bottom=0, right=0),
            margin=ft.margin.only(left = 10),
            alignment=ft.alignment.center,
        )

class CatatanJadwal(ft.UserControl):
    def __init__(self, catatan_jadwal: catatan_jadwal_model.CatatanJadwal):
        super().__init__()
        self._catatan_jadwal = catatan_jadwal

    def catatan_jadwal_on_click(self, e):
        self.page.controls.clear()
        ubah_catatan_jadwal_screen.main(self.page, self._catatan_jadwal.getID())

    def build(self):
        return ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                    value=self._catatan_jadwal.getNamaAcara(),
                                    size=19,
                                    color="#FFFFFF",
                                    text_align=ft.TextAlign.LEFT,
                                    overflow=ft.TextOverflow.VISIBLE,
                                    ),
                            
                            ft.Text(
                                    value=self._catatan_jadwal.getDescAcara(),
                                    size=19,
                                    color="#FFFFFF",
                                    text_align=ft.TextAlign.LEFT,
                                    overflow=ft.TextOverflow.VISIBLE,
                                    ),
                        ],
                        spacing=0
                    ),
                    width=800,
                    height=85,
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                    on_click=self.catatan_jadwal_on_click,
                )


class DaftarCatatanJadwal(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        _catatan_jadwal_controller = catatan_jadwal_controller.CatatanJadwalController()
        catatan_jadwal_list = _catatan_jadwal_controller.getListCatatanJadwal()
        if len(catatan_jadwal_list) == 0:
            return ft.Container(
                content=ft.Text(
                    value="Tidak ada catatan jadwal",
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
                height=300,
                width=555,
            )
        else :
            result = ft.Container(
                content=ft.Column(
                    controls=[
                        # TODO : AGENDA
                        # CatatanJadwal(i) for i in catatan_jadwal_list
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE,
                    spacing=15,
                ),
                width=555,
                padding=ft.padding.only(top=0, left=155, bottom=0, right=0),
                margin=ft.margin.only(left = 10,),
                bgcolor=ft.colors.TRANSPARENT,
                alignment=ft.alignment.center,
            )
            for i in catatan_jadwal_list:
                result.content.controls.append(CatatanJadwal(i))
            return result
