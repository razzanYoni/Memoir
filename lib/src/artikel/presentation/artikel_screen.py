import flet as ft

import lib.home_page.main_screen as main_screen
import lib.src.artikel.presentation.artikel_widget as artikel_widget
import lib.src.artikel.controller.artikel_controller as artikel_controller

def main(page: ft.Page):
    page.title = "Memoir - Catatan Kegiatan"

    page.window_width = 1440
    page.window_height = 1024
    page.window_resizable = False
    page.window_maximizable = False

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)
    page.bgcolor = "#FFFFFF"

    page.fonts = {
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
        "Inter Light": "fonts/Inter-Light-BETA.otf",
    }

    page.scroll = ft.ScrollMode.ADAPTIVE

    page.add(
        ft.Container(
            content=ft.Column(
                controls = [
                    # Search Bar and Home
                    ft.Row(
                        controls = [
                            artikel_widget.HomeButton(page),

                            ft.VerticalDivider(
                                width=10,
                            ),
                            artikel_widget.DaftarArtikel(page),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),

                    
                ],
        ),
        margin = 10,
        alignment=ft.alignment.top_left,
        padding=ft.padding.only(left=52, top=60, right=62, bottom=0),
        ),
    )


if __name__ == '__main__':
    ft.app(target=main, assets_dir="../../../../assets")
