import flet as ft
from time import sleep
from PIL import Image

import lib.src.catatan_jadwal.presentation.catatan_jadwal_screen as catatan_jadwal_screen
import lib.src.catatan_jadwal.controller.catatan_jadwal_controller as catatan_jadwal_controller
import lib.src.utilities.date_picker as date_picker
import lib.src.utilities.time_picker as time_picker
from lib.src.utilities.util import image_to_blob
import lib.src.catatan_jadwal.presentation.catatan_jadwal_widget as catatan_jadwal_widget
import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model
import lib.src.utilities.date_picker as date_picker
import lib.src.utilities.time_picker as time_picker

class CalendarButton2(ft.Container):

    def ubah_jadwal_button_on_click(self, e):
        self.page.controls.clear()
        id_catatan_jadwal = 0
        self.page.update()

    def __init__(self, page: ft.Page):
        super().__init__(
            image_src="assets/icons/jadwal_button2.png",
            on_click="",
            width=380,
            height=64,
            margin=17
        )
        self.page = page

class Agenda2(ft.Container):
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


class Reminders2(ft.UserControl):
    def __init__(self, catatan_jadwal: catatan_jadwal_model.CatatanJadwal):
        super().__init__()
        self._catatan_jadwal = catatan_jadwal

    def build(self):
        _catatan_jadwal_controller = catatan_jadwal_controller.CatatanJadwalController()

        self.__nama_acara = self._catatan_jadwal.getNamaAcara()
        self.__desc_acara = self._catatan_jadwal.getDescAcara()
        # self.__desc_acara = self.getDescAcara() 
        nama_acara = ft.TextField(
            border_width=0,
            width=800,
            height=88,
            multiline=True,
            text_style=ft.TextStyle(
                color="#ffffff",
                size=19,
                font_family="Inter Light",
            ),
            hint_text="Judul Acara: \n      ACARA XXX XXXX XXX",
            hint_style=ft.TextStyle(
                color="#ffffff",
                size=20,
                font_family="Inter Light",
            ),
        )
        desc_acara = ft.TextField(
                border_width=0,
                max_lines=1,
                multiline=False,
                width=800,
                height=85,
                text_align=ft.TextAlign.JUSTIFY,
                text_style=ft.TextStyle(
                    color="#ffffff",
                    size=19,
                    font_family="Inter SemiBold",
                ),
                hint_text="Deskripsi Acara: ",
                hint_style=ft.TextStyle(
                    color="#ffffff",
                    size=18,
                    font_family="Inter Light",
                ),        
        )        
        retVal = self._catatan_jadwal.getNamaAcara() + "\n     " + self._catatan_jadwal.getDescAcara()
        return ft.Column(
            controls=[
                ft.Container(
                    content=nama_acara,
                    width="800",
                    height="85",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),
                ft.Container(
                    content = desc_acara,
                    width="800",
                    height="185",
                    bgcolor="#444980",
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(top=15, left=25, bottom=0, right=0),
                    margin=ft.margin.only(bottom=22, right=70, left=0),
                ),

            ],
            expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )
        return __nama_acara, __desc_acara

class Notification2(ft.Container):
    def __init__(self, catatan_jadwal: catatan_jadwal_model.CatatanJadwal):
        self.agenda = Agenda2()
        self.reminders = Reminders2(catatan_jadwal)
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
        

# TODO : Ubah Cover
def main(page: ft.Page, id_catatan_jadwal: int):
    _catatan_jadwal_controller = catatan_jadwal_controller.CatatanJadwalController()
    catatan_jadwal = _catatan_jadwal_controller.getCatatanJadwal(id_catatan_jadwal)
    page.title = "Memoir - UbahCatatan Jadwal"

    page.window_width = 1440
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False

    page.padding = ft.padding.all(0)
    page.margin = ft.margin.all(0)
    page.bgcolor = ft.colors.TRANSPARENT

    page.fonts = {
        "Inter": "fonts/Inter-Regular.ttf",
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Light": "fonts/Inter-Light-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
    }

    page.theme = ft.Theme(font_family="Inter")

    page.title = "Memoir - Ubah Catatan Jadwal"

    page.fonts = {
        "Inter SemiBold": "fonts/Inter-SemiBold.otf",
        "Inter Bold": "fonts/Inter-Bold.otf",
        "Inter ExtraLight": "fonts/Inter-ExtraLight-BETA.otf",
        "Inter Medium": "fonts/Inter-Medium.otf",
        "Inter Thin": "fonts/Inter-Thin-BETA.otf",
    }

    page.snack_bar = ft.SnackBar(
        content=ft.Text(
            value="Catatan jadwal berhasil diubah",
            size=20,
            font_family="Inter SemiBold",
        ),
        action_color=ft.colors.WHITE,
        action="Tutup",
    )
    def back_to_catatan_jadwal_screen(e):
        page.dialog.open = False
        page.update()
        sleep(0.1)
        page.clean()
        catatan_jadwal_screen.main(page)
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()
    page.theme = ft.Theme(font_family="Inter")

    cancel_dialog = ft.AlertDialog(
        modal=True,
        open=False,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        title=ft.Text(
            value="Apakah kamu yakin ingin membatalkan?",
            size=30,
            font_family="Inter SemiBold",
            text_align=ft.TextAlign.CENTER,),
        content=ft.Text(
            value="Semua perubahan yang belum disimpan akan hilang",
            size=20,
            font_family="Inter",
            text_align=ft.TextAlign.CENTER,
        ),
        actions=[
            ft.TextButton(
                content=ft.Text(
                    value="Ya",
                    size=25,
                    font_family="Inter SemiBold",
                    color=ft.colors.WHITE,
                ),
                width=150,
                height=60,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor="#e993bd",
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
                    }
                ),
                on_click=back_to_catatan_jadwal_screen,
            ),

            ft.TextButton(
                content=ft.Text(
                    value="Tidak",
                    size=25,
                    font_family="Inter SemiBold",
                    color=ft.colors.WHITE,
                ),
                width=150,
                height=60,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor="#c5cbe8",
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
                    },
                ),
                on_click=close_dialog,
            ),
        ],
    )

    nama_acara = ft.TextField(
        border_width=0,
        width=800,
        height=85,
        multiline=True,
        text_style=ft.TextStyle(
            color="#ffffff",
            size=19,
            font_family="Inter Light",
        ),
        hint_text="Your description here...",
        hint_style=ft.TextStyle(
            color="#ffffff",
            size=20,
            font_family="Inter Light",
        ),
    )

    desc_acara = ft.TextField(
            border_width=0,
            max_lines=1,
            multiline=False,
            width=800,
            height=85,
            text_align=ft.TextAlign.JUSTIFY,
            text_style=ft.TextStyle(
                color="#ffffff",
                size=19,
                font_family="Inter SemiBold",
            ),
    )

    delete_dialog = ft.AlertDialog(
        modal=True,
        open=False,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        title=ft.Text(
            value="Apakah kamu yakin ingin menghapus?",
            size=30,
            font_family="Inter SemiBold",
            text_align=ft.TextAlign.CENTER, ),
        content=ft.Text(
            value="Catatan Jadwal yang sudah dihapus tidak dapat dikembalikan.",
            size=20,
            font_family="Inter",
            text_align=ft.TextAlign.CENTER,
        ),
        actions=[
            ft.TextButton(
                content=ft.Text(
                    value="Ya",
                    size=25,
                    font_family="Inter SemiBold",
                    color=ft.colors.WHITE,
                ),
                width=150,
                height=60,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor="#e993bd",
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
                    }
                ),
                on_click=back_to_catatan_jadwal_screen,
            ),

            ft.TextButton(
                content=ft.Text(
                    value="Tidak",
                    size=25,
                    font_family="Inter SemiBold",
                    color=ft.colors.WHITE,
                ),
                width=150,
                height=60,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor="#c5cbe8",
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
                    },
                ),
                on_click=close_dialog,
            ),
        ],
    )

    def hapus_catatan_jadwal(e):
        page.dialog = delete_dialog
        delete_dialog.open = True
        page.update()

    def batal_ubah_catatan_jadwal(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()

    def tambah_catatan_jadwal(e):
        page.snack_bar.content.value = "Catatan Kegiatan berhasil ditambahkan"
        page.snack_bar.open = True
        page.update()

        page.clean()
        catatan_jadwal_screen.main(page)
        page.update()

    def batal_tambah_catatan_jadwal(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()

    def ubah_catatan_jadwal(e):
        try:
            if desc_acara.value == "" or nama_acara.value == "" or nama_acara.value != "" or desc_acara.value != "":
                page.snack_bar.content.value = "Mohon isi semua kolom"
                page.snack_bar.open = True
                page.update()
                return

            page.snack_bar.content.value = "Catatan Jadwal berhasil diubah"
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar.content.value = "Catatan Jadwal gagal diubah"
            page.snack_bar.open = True
            page.update()
            print(e)

        page.clean()
        catatan_jadwal_screen.main(page)
        page.update()

    calendar = catatan_jadwal_widget.CalendarLeft()
    calendar_button = CalendarButton2(page)
    tes = catatan_jadwal_model.CatatanJadwal(1, 2, "aa", "ACARA XXX XXX XXX", "Agenda", "01:02:03")
    notification = Notification2(tes)
    home_button = catatan_jadwal_widget.HomeButton(page)

    left_column = ft.Container(
        content=ft.Column(
            controls=[
                calendar, 
                ft.Container(
                    image_src="assets/icons/jadwal_button2.png",
                    width=380,
                    height=64,
                    margin=17,
                    on_click=hapus_catatan_jadwal,
                ),    
                
            ],
            visible=True,
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
        ),
        expand=True,
        padding=ft.padding.only(top=30, left=0, bottom=0, right=0),
    )

    dlm_right = ft.Container(
        content= ft.Row(
            controls=[
                ft.Container(
                    image_src="assets/icons/cancel_button.png",
                    width=200,
                    height=300,
                    on_click=batal_tambah_catatan_jadwal,
                ),

                ft.Container(
                    image_src="assets/icons/confirm_button.png",
                    width=200,
                    height=300,
                    on_click=tambah_catatan_jadwal,
                ),
            ],     
        ),
        margin=ft.margin.only(left=110),
    )

    right_column = ft.Container(
        content=ft.Column(
        controls=[
            notification,
            dlm_right
        ]
        )
    )

    page.add(
        ft.Container(
            content=ft.Row(
            controls=[home_button, left_column, right_column],
            visible=True,
            expand=True,
            spacing=0,
        ),
            expand=True,
            image_src="assets/images/home_page_bg.png",
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../../../assets")
