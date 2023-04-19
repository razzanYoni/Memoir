import flet as ft

class StatusPicker(ft.Container):
    def __init__(self, status="Belum"):
        self.status = ft.Dropdown(
            label_style=ft.TextStyle(
                color="#ffffff"
            ),
            options=[ft.dropdown.Option("Belum"), ft.dropdown.Option("Berlangsung"), ft.dropdown.Option("Selesai")],
            value=status,
            width=150
        )

        super().__init__(
            content=ft.Row(
                controls=[
                    self.status
                ],
                spacing=5,
                height=60,
                width=100,
                visible=True,
            ),
            visible=True,
        )

    def get_status(self):
        return self.status.value
