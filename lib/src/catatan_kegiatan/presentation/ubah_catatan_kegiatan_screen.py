import flet as ft
from time import sleep

import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_screen as catatan_kegiatan_screen
import lib.src.catatan_kegiatan.controller.catatan_kegiatan_controller as catatan_kegiatan_controller
import lib.src.catatan_kegiatan.presentation.catatan_kegiatan_widget as catatan_kegiatan_widget
import lib.src.catatan_kegiatan.data.catatan_kegiatan_model as catatan_kegiatan_model
import lib.src.utilities.date_picker as date_picker
import lib.src.utilities.time_picker as time_picker
from lib.src.utilities.util import image_to_blob, blob_to_base64


# TODO : Ubah Cover
def main(page: ft.Page, id_catatan_kegiatan: int):
    _catatan_kegiatan_controller = catatan_kegiatan_controller.CatatanKegiatanController()
    catatan_kegiatan = _catatan_kegiatan_controller.getCatatanKegiatan(id_catatan_kegiatan)

    page.title = "Memoir - Ubah Catatan Kegiatan"

    page.snack_bar = ft.SnackBar(
        content=ft.Text(
            value="Catatan kegiatan berhasil diubah",
            size=20,
            font_family="Inter SemiBold",
        ),
        action_color=ft.colors.WHITE,
        action="Tutup",
    )

    def back_to_catatan_kegiatan_screen(e):
        page.dialog.open = False
        page.update()
        sleep(0.1)
        page.clean()
        catatan_kegiatan_screen.main(page)
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()

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
                on_click=back_to_catatan_kegiatan_screen,
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

    global result_img
    result_img = None

    def get_file_path(e):
        global result_img
        if e.files:
            result_img = e.files[0].path
            container_ref.current.image_src_base64 = blob_to_base64(image_to_blob(result_img))
            page.update()

    pick_image = ft.FilePicker(
        on_result=get_file_path,
    )

    page.overlay.append(pick_image)

    container_ref = ft.Ref[ft.Container]()

    desc_keg = ft.TextField(
            border_width=0,
            width=1300,
            multiline=False,
            min_lines=1,
            max_lines=1,
            height=95,
            text_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
            hint_text="Your title here...",
            hint_style=ft.TextStyle(
                color="#ffffff",
                size=40,
                font_family="Inter SemiBold",
            ),
            value=catatan_kegiatan[3],
            text_align=ft.TextAlign.JUSTIFY,
        )

    date = date_picker.DatePicker(
            day=int(catatan_kegiatan[1][8:10]),
            month=int(catatan_kegiatan[1][5:7]),
            year=int(catatan_kegiatan[1][0:4]),
        )
    time = time_picker.TimePicker(
            hour=int(catatan_kegiatan[2][0:2]),
            minute=int(catatan_kegiatan[2][3:5]),
    )
    feel = catatan_kegiatan_widget.Feel(
            feel=int(catatan_kegiatan[6]),
    )
    desc_syuk = ft.TextField(
        border_width=0,
        width=1300,
        height=500,
        multiline=True,
        text_style=ft.TextStyle(
            color="#ffffff",
            size=20,
            font_family="Inter Light",
        ),
        value=catatan_kegiatan[4],
        hint_text="Your description here...",
        hint_style=ft.TextStyle(
            color="#ffffff",
            size=20,
            font_family="Inter Light",
        ),
    )

    # TODO: Implementasi dan masukin ke database
    def ubah_foto(e):
        pick_image.pick_files(
            dialog_title="Pilih Gambar untuk Cover",
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
            allowed_extensions=["png", "jpg", "jpeg"],
        )
        # TODO: jangan lupa validasi ukuran bisa pake PIL kalo ga memenuhi tampilin dialog
        pass

    def batal_ubah_catatan_kegiatan(e):
        page.dialog = cancel_dialog
        page.dialog.open = True
        page.update()

    # TODO: Query ke database
    def ubah_catatan_kegiatan(e):
        try:
            if desc_keg.value == "" or desc_syuk.value == "":
                page.snack_bar.content.value = "Mohon isi semua kolom"
                page.snack_bar.open = True
                page.update()
                return

            if result_img is not None:
                imgBlob = image_to_blob(result_img)
            else:
                imgBlob = catatan_kegiatan[5]

            _catatan_kegiatan = catatan_kegiatan_model.CatatanKegiatan(
                id_kegiatan=catatan_kegiatan[0],
                tanggal=date.get_date(),
                jam=time.get_time(),
                desc_kegiatan=desc_keg.value,
                desc_syuk=desc_syuk.value,
                foto=imgBlob,
                jenis_perasaan=feel.get_feel(),
            )

            _catatan_kegiatan_controller.Memperbarui(_catatan_kegiatan)
            page.snack_bar.content.value = "Catatan Kegiatan berhasil diubah"
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            page.snack_bar.content.value = "Catatan Kegiatan gagal diubah"
            page.snack_bar.open = True
            page.update()
            print(e)

        page.clean()
        catatan_kegiatan_screen.main(page)
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value="Ubah Catatan Kegiatan",
                                color="#043edb",
                                size=45,
                                font_family="Inter SemiBold",
                                text_align=ft.TextAlign.START,
                            ),

                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                value="Ubah Cover",
                                                color="#6c6c6c",
                                                size=30,
                                                font_family="Inter SemiBold",
                                            ),
                                            on_click=ubah_foto,
                                        ),

                                        ft.Container(
                                            image_src="icons/cancel_button.png",
                                            width=50,
                                            height=50,
                                            on_click=batal_ubah_catatan_kegiatan,
                                        ),

                                        ft.Container(
                                            image_src="icons/confirm_button.png",
                                            width=50,
                                            height=50,
                                            on_click=ubah_catatan_kegiatan,
                                        )
                                    ],
                                    spacing=7
                                ),
                                alignment=ft.alignment.center_right
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        width=1300,
                        # height=70
                    ),

                    # Content yang diisi oleh user
                    ft.Container(
                        border_radius=15,
                        bgcolor="#043edb",
                        ref=container_ref,
                        image_src_base64=blob_to_base64(catatan_kegiatan[5]),
                        width=1300,
                        height=700,
                        image_fit=ft.ImageFit.COVER,
                        content=ft.Column(
                            [
                                ft.Container(
                                    border_radius=15,
                                    height=450,
                                    width=1300,
                                    bgcolor="#444980",
                                    content=ft.Column(
                                        controls=[
                                            # judul
                                            ft.Container(
                                                border_radius=15,
                                                height=150,
                                                width=1300,
                                                bgcolor="#444980",
                                                padding=ft.padding.only(left=10, right=10, top=15),
                                                content=ft.Column(
                                                    controls=[
                                                        desc_keg,

                                                        ft.Row(
                                                            controls=[
                                                                date,
                                                                time,
                                                                feel
                                                            ],
                                                            spacing=25,
                                                        )
                                                    ],
                                                    spacing=3,
                                                    alignment=ft.MainAxisAlignment.START,
                                                    horizontal_alignment=ft.CrossAxisAlignment.START
                                                )
                                            ),

                                            # deskripsi
                                            ft.Container(
                                                border_radius=15,
                                                height=250,
                                                width=1300,
                                                bgcolor="#06184E",
                                                padding=ft.padding.only(left=10, right=10, top=10),
                                                content=desc_syuk,
                                            ),
                                        ],
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        alignment=ft.alignment.bottom_center,
                    ),
                ],
                spacing=0
            ),
            width=page.window_width,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=80, top=35, right=52, bottom=35),
        ),
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../../../../assets")
