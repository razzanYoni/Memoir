import pytest
import lib.src.artikel.controller.artikel_controller as artikel_controller
import lib.src.artikel.data.artikel_model as artikel_model
from lib.src.utilities.util import image_to_blob

class TestArtikelControllerUnit():
    def setup_method(self):
        self.controller = artikel_controller.ArtikelController()
        self.list = self.controller.getListArtikel()

    def test_tambahartikel(self):
        # Ambil length
        x = len(self.controller.getListArtikel())

        # Tambah Artikel
        image = image_to_blob("assets/images/artikel4.jpg")
        judul = "Dummy Judul Artikel"
        pengarang = "Dummy Pengarang Artikel"
        tanggal = "2022-08-01"
        isi = "Dummy Isi Artikel"
        self.controller.Tambah(judul, isi, pengarang, tanggal, image)

        # Testing
        idx = x+1
        assert self.controller.getArtikel(idx)[1] == "Dummy Judul Artikel"
        assert self.controller.getArtikel(idx)[2] == "Dummy Isi Artikel" 
        assert self.controller.getArtikel(idx)[3] == "Dummy Pengarang Artikel"
        assert self.controller.getArtikel(idx)[4] == "2022-08-01"
        assert self.controller.getArtikel(idx)[5] == image_to_blob("assets/images/artikel4.jpg")
        self.controller.Hapus(idx)

if __name__ == "__main__":
    pytest.main()