import flet as ft
from datetime import datetime, date


class DatePicker(ft.Container):
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def month_on_change(self, e):
        if self.monthDD.value == "2":
            if self.is_leap_year(int(self.yearDD.value)):
                self.dayDD.options = [ft.dropdown.Option(str(i)) for i in range(1, 30)]
                if int(self.dayDD.value) > 29:
                    self.dayDD.value = str(29)
            else:
                self.dayDD.options = [ft.dropdown.Option(str(i)) for i in range(1, 29)]
                if int(self.dayDD.value) > 28:
                    self.dayDD.value = str(28)
        elif self.monthDD.value in ["4", "6", "9", "11"]:
            self.dayDD.options = [ft.dropdown.Option(str(i)) for i in range(1, 31)]
            if int(self.dayDD.value) > 30:
                self.dayDD.value = str(datetime.now().day)
        else:
            self.dayDD.options = [ft.dropdown.Option(str(i)) for i in range(1, 32)]
        self.page.update()

    def year_on_change(self, e):
        self.isLeapYear = self.is_leap_year(int(self.yearDD.value))
        if int(self.monthDD.value) == 2:
            if self.isLeapYear:
                self.dayDD.options = [str(i) for i in range(1, 30)]
                if int(self.dayDD.value) > 29:
                    self.dayDD.value = str(29)
            else:
                self.dayDD.options = [str(i) for i in range(1, 29)]
                if int(self.dayDD.value) > 28:
                    self.dayDD.value = str(28)
        self.page.update()

    def __init__(self, day=datetime.now().day, month=datetime.now().month, year=datetime.now().year):
        self.dayDD = ft.Dropdown(
            label="Day",
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[ft.dropdown.Option(str(i)) for i in range(1, 32)],
            value=str(day),
            width=70,
        )

        self.monthDD = ft.Dropdown(
            label="Month",
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[ft.dropdown.Option(str(i)) for i in range(1, 13)],
            value=str(month),
            width=70,
            on_change=self.month_on_change,
        )

        self.yearDD = ft.Dropdown(
            label="Year",
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[ft.dropdown.Option(str(i)) for i in range(2020, 2031)],
            value=str(year),
            width=80,
            on_change=self.year_on_change,
        )

        self.isLeapYear = self.is_leap_year(int(self.yearDD.value))

        super().__init__(
            content=ft.Row(
                controls=[
                    self.dayDD,
                    self.monthDD,
                    self.yearDD,
                ],
                spacing=5,
                width=220,
                height=60,
                visible=True,
            ),
            visible=True,
        )

    def get_date(self):
        _date = date(
            year=int(self.yearDD.value),
            month=int(self.monthDD.value),
            day=int(self.dayDD.value)
        )

        return str(_date)
