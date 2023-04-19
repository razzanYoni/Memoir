import pytest
import lib.src.catatan_kegiatan.controller.catatan_kegiatan_controller as catatan_kegiatan_controller
import lib.src.catatan_kegiatan.data.catatan_kegiatan_model as catatan_kegiatan_model
from lib.src.utilities.util import image_to_blob

class TestCatatankegiatanUnit():
    def setup_method(self):
        self.controller = catatan_kegiatan_controller.CatatanKegiatanController()
        self.list = self.controller.getListCatatanKegiatan()

    def test_tambahcatatankegiatan(self):
        # Ambil length
        x = len(self.controller.getListCatatanKegiatan())

        # Tambah catatan_kegiatan
        tanggal = "2022-08-01"
        jam = "10:05:00"
        desc_kegiatan = "Dummy Deskripsi Kegiatan"
        desc_syuk = "Dummy Hal yang Disyukuri"
        # assets/images/default_cover_ctt_kegiatan.png
        foto = image_to_blob("assets/images/default_cover_ctt_kegiatan.png")
        jenis_perasaan = 1
        self.controller.Tambah(tanggal, jam, desc_kegiatan, desc_syuk, foto, jenis_perasaan)

        # Testing
        idx = 1
        for i in range(0,x):
            if idx < self.controller.getListCatatanKegiatan()[i].getID():
                idx = self.controller.getListCatatanKegiatan()[i].getID()

        assert self.controller.getCatatanKegiatan(idx)[1] == "2022-08-01"
        assert self.controller.getCatatanKegiatan(idx)[2] == "10:05:00"
        assert self.controller.getCatatanKegiatan(idx)[3] == "Dummy Deskripsi Kegiatan"
        assert self.controller.getCatatanKegiatan(idx)[4] == "Dummy Hal yang Disyukuri"
        assert self.controller.getCatatanKegiatan(idx)[5] == image_to_blob("assets/images/default_cover_ctt_kegiatan.png")
        assert self.controller.getCatatanKegiatan(idx)[6] == 1 
    
    def test_memperbaruiCatatanKegiatan(self):
        x = len(self.controller.getListCatatanKegiatan())
        # Old file
        tanggal = "2022-08-01"
        jam = "10:05:00"
        desc_kegiatan = "Dummy Deskripsi Kegiatan"
        desc_syuk = "Dummy Hal yang Disyukuri"
        foto = image_to_blob("assets/images/default_cover_ctt_kegiatan.png")
        jenis_perasaan = 1
        # Tambah catatan_kegiatan
        self.controller.Tambah(tanggal, jam, desc_kegiatan, desc_syuk, foto, jenis_perasaan)

        # Memperbarui
        idx = 1
        for i in range(0,x):
            if idx < self.controller.getListCatatanKegiatan()[i].getID():
                idx = self.controller.getListCatatanKegiatan()[i].getID()

        catatan_kegiatan_baru = catatan_kegiatan_model.CatatanKegiatan(
                id_kegiatan=idx,
                tanggal= "2022-08-01",
                jam= "10:05:00",
                desc_kegiatan="Dummy Deskripsi Kegiatan Baru",
                desc_syuk="Dummy Hal yang Disyukuri Baru",
                foto=image_to_blob("assets/images/foto_kelompok.png"),
                jenis_perasaan=2,
        )

        self.controller.Memperbarui(catatan_kegiatan_baru)

        assert self.controller.getCatatanKegiatan(idx)[1] == "2022-08-01"
        assert self.controller.getCatatanKegiatan(idx)[2] == "10:05:00"
        assert self.controller.getCatatanKegiatan(idx)[3] == "Dummy Deskripsi Kegiatan Baru"
        assert self.controller.getCatatanKegiatan(idx)[4] == "Dummy Hal yang Disyukuri Baru"
        assert self.controller.getCatatanKegiatan(idx)[5] == image_to_blob("assets/images/foto_kelompok.png")  
        assert self.controller.getCatatanKegiatan(idx)[6] == 2
        self.controller.Hapus(idx)

    def test_getListcatatan_kegiatan(self):
        # Ambil Length
        x = len(self.controller.getListCatatanKegiatan())
        assert x > 0
    
    def test_hapuscatatan_kegiatan(self):
        # Ambil length
        x = len(self.controller.getListCatatanKegiatan())
        # Testing
        idx = 1
        for i in range(0,x):
            if idx < self.controller.getListCatatanKegiatan()[i].getID():
                idx = self.controller.getListCatatanKegiatan()[i].getID()

        self.controller.Hapus(idx)
        assert self.controller.getCatatanKegiatan(idx) is None
        
if __name__ == "__main__":
    pytest.main()