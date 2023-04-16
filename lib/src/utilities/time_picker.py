import flet as ft
from datetime import datetime, time


class TimePicker(ft.Container):

    def __init__(self, hour=datetime.now().hour, minute=datetime.now().minute):
        self.hourDD = ft.Dropdown(
            label="Hour",
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[ft.dropdown.Option(str(i)) for i in range(0, 24)],
            value=str(hour),
            width=70,
        )

        self.minuteDD = ft.Dropdown(
            label="Minute",
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[ft.dropdown.Option(str(i)) for i in range(0, 60)],
            value=str(minute),
            width=70,
        )

        print(self.get_time())

        super().__init__(
            content=ft.Row(
                controls=[
                    self.hourDD,
                    self.minuteDD,
                ],
                spacing=5,
                width=140,
                height=60,
            )
        )

    def get_time(self):
        _time = time(int(self.hourDD.value), int(self.minuteDD.value))
        return str(_time)
