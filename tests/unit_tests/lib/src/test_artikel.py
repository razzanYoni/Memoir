import pytest
import lib.src.artikel.controller.artikel_controller as artikel_controller
import lib.src.artikel.data.artikel_model as artikel_model
from lib.src.utilities.util import image_to_blob

class TestArtikelUnit():
    def setup_method(self):
        self.controller = artikel_controller.ArtikelController()
        self.list = self.controller.getListArtikel()

    def test_tambahartikel(self):
        # Ambil length
        x = len(self.controller.getListArtikel())

        # Tambah Artikel
        image = image_to_blob("assets/images/foto_kelompok.png")
        judul = "Dummy Judul Artikel"
        pengarang = "Dummy Pengarang Artikel"
        tanggal = "2022-08-01"
        isi = "Dummy Isi Artikel"
        self.controller.Tambah(judul, isi, pengarang, tanggal, image)

        # Testing
        idx = 1
        for i in range(0,x):
            if idx < self.controller.getListArtikel()[i].getID():
                idx = self.controller.getListArtikel()[i].getID()

        assert self.controller.getArtikel(idx)[1] == "Dummy Judul Artikel"
        assert self.controller.getArtikel(idx)[2] == "Dummy Isi Artikel" 
        assert self.controller.getArtikel(idx)[3] == "Dummy Pengarang Artikel"
        assert self.controller.getArtikel(idx)[4] == "2022-08-01"
        assert self.controller.getArtikel(idx)[5] == image_to_blob("assets/images/foto_kelompok.png")    
    
    def test_hapusartikel(self):
        # Ambil length
        x = len(self.controller.getListArtikel())

        # Testing
        idx = x
        self.controller.Hapus(idx)
    
    def test_getListArtikel(self):
        # Ambil Length
        x = len(self.controller.getListArtikel())
        assert x > 0

if __name__ == "__main__":
    pytest.main()