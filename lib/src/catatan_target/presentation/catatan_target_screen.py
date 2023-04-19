import flet as ft

import lib.src.catatan_target.presentation.catatan_target_widget as catatan_target_widget

# alternatif button add catatan kegiatan di home screen pake floating action button

def main(page: ft.Page):
    page.title = "Memoir - Catatan Target"

    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window_focused = True
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    catatan_target_widget.HomeButton(page),
                    ft.VerticalDivider(
                        width=10,
                        visible=False,
                    ),
                    ft.Container(
                          content=ft.Column(
                              controls=[
                                  ft.Divider(
                                        height=10,
                                        visible=False,
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
                                        visible=False,
                                  ),

                                #   catatan_target_widget.DaftarCatatanTarget(page),
                                  catatan_target_widget.DaftarCatatanTarget(),
                              ],
                              spacing=0,
                              alignment=ft.MainAxisAlignment.START,
                              horizontal_alignment=ft.CrossAxisAlignment.START,
                              expand=True,
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
