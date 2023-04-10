import flet as ft
from time import sleep

import lib.home_page.main_screen as main_screen
import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_widget as catatan_kegiatan_widget

import lib.src.catatan_kegiatan.controller.catatan_kegiatan_controller as catatan_kegiatan_controller

# alternatif button add catatan kegiatan di home screen pake floating action button

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
    }

    page.scroll = ft.ScrollMode.ADAPTIVE

    grafik_perasaan = catatan_kegiatan_widget.GrafikPerasaan(page)
    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    catatan_kegiatan_widget.HomeButton(page),
                    ft.VerticalDivider(
                        width=10,
                    ),
                    ft.Container(
                          content=ft.Column(
                              controls=[
                                  ft.Text(
                                        value="Perasaanku",
                                        color="#043edb",
                                        size=45,
                                        font_family="Inter SemiBold",
                                  ),

                                  ft.Divider(
                                        height=10,
                                  ),

                                  grafik_perasaan,

                                  ft.Divider(
                                        height=10,
                                  ),

                                  ft.Row(
                                      controls=[
                                          ft.Text(
                                                value="HARIKU",
                                                color="#043edb",
                                                size=30,
                                                font_family="Inter SemiBold",
                                          ),
                                          catatan_kegiatan_widget.AddCatatanKegiatanButton(page),
                                      ],
                                      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                      width=1164,
                                  ),

                                  ft.Divider(
                                        height=10,
                                  ),

                                  catatan_kegiatan_widget.DaftarCatatanKegiatan(page),
                              ],
                              spacing=0,
                              alignment=ft.MainAxisAlignment.CENTER,
                              horizontal_alignment=ft.CrossAxisAlignment.START,
                          ),
                      )
                    ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=52, top=60, right=62, bottom=0),
        ),
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir="../../../../assets")
