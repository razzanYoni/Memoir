import flet as ft
from datetime import datetime
from time import sleep
import PyQt5.QtWidgets as QtWidgets
import lib.src.artikel.presentation.artikel_screen as artikel_screen
import lib.src.catatan_jadwal.presentation.catatan_jadwal_screen as catatan_jadwal_screen
import lib.src.catatan_target.presentation.catatan_target_screen as catatan_target_screen
import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_screen as catatan_kegiatan_screen

import lib.src.catatan_jadwal.data.catatan_jadwal_repo as catatan_jadwal_repo

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
                padding=ft.padding.only(top=50, left=72, bottom=30, right=72),
            ),
            width=825,
            height=625,
            padding=ft.padding.only(top=90, left=130, bottom=0, right=30),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.TRANSPARENT
)

class CalendarButton(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Container(
                content=ft.Text(
                    value="Calendar",
                    size=24,
                    color="#FFFFFF",
                    font_family="Inter Medium",
                    opacity=1,
                    style="margin: 0 auto;"
                ),
                width=120,
                height=40,
                border=ft.Border(
                    width=2,
                    style=ft.BorderStyle.SOLID,
                    color="#6E7198"
                ),
                bgcolor="#06184E",
                on_click=self.toggle_color
            )
        )

    def toggle_color(self, event):
        if self.content.bgcolor == "#06184E":
            self.content.bgcolor = "#F99494"
        else:
            self.content.bgcolor = "#06184E"


class CalendarDate(ft.Container):
    def __init__(self):
        super().__init__(content=self.build(), bgcolor="#A7AECD")

    def build(self):
        # Define weekday names
        weekday_names = ["Mon  ", " Tue  ", "Wed  ", " Thu  ", "  Fri  ", "  Sat  ", "  Sun  "]

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
    def __init__(self):
        super().__init__(
        )

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
            margin=ft.margin.only(left=81, bottom=22, top=52),
        )
    



# TODO: Reminder Control, wait for the backend
class Reminders(ft.UserControl):
    def __init__(self):
        super().__init__(
            expand=True,
        )

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value="  Agenda\n  ACARA XXX XXX XXX\n   ",
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=0, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),

                ft.Container(
                    content=ft.Text(
                        value="  Agenda\n  ACARA XXX XXX XXX\n   ",
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=0, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),
                ft.Container(
                    content=ft.Text(
                        value="  Agenda\n  ACARA XXX XXX XXX\n   ",
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=0, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),

                ft.Container(
                    content=ft.Text(
                        value="  Agenda\n  ACARA XXX XXX XXX\n   ",
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=0, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),

                ft.Container(
                    content=ft.Text(
                        value="  Agenda\n  ACARA XXX XXX XXX\n   ",
                        size=19,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    width="800",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=0, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),
            ],
            expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )



class Notification(ft.Container):
    def __init__(self):
        self.agenda = Agenda()
        self.reminders = Reminders()
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
