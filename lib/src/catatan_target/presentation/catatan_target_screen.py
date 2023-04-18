import flet as ft

import lib.src.catatan_target.presentation.catatan_target_widget as catatan_target_widget

# alternatif button add catatan kegiatan di home screen pake floating action button

def main(page: ft.Page):
    page.title = "Memoir - Catatan Target"

    page.window_width = 1440
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window_focused = True
    page.theme_mode = ft.ThemeMode.LIGHT

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)

    page.fonts = {
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
        "Inter Light": "fonts/Inter-Light-BETA.otf",
    }

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    catatan_target_widget.HomeButton(page),
                    ft.VerticalDivider(
                        width=10,
                    ),
                    ft.Container(
                          content=ft.Column(
                              controls=[
                                  ft.Divider(
                                        height=10,
                                  ),

                                  ft.Row(
                                      controls=[
                                          ft.Text(
                                                value="Targetku",
                                                color="#043edb",
                                                size=30,
                                                font_family="Inter SemiBold",
                                          ),
                                          catatan_target_widget.AddCatatanTargetButton(page),
                                      ],
                                      # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                      width=1164,
                                  ),

                                  ft.Divider(
                                        height=10,
                                  ),

                                  catatan_target_widget.DaftarCatatanTarget(page),
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
