import lib.src.artikel.controller.artikel_controller as artikel_controller
import lib.src.artikel.data.artikel_model as artikel_model
from lib.src.utilities.util import image_to_blob

class TestArtikelControllerUnit():
    def __init__(self):
        self.controller = artikel_controller.ArtikelController()
        self.list = self.controller.getListArtikel()

    def test_tambahartikel(self):
        # Ambil length
        x = len(self.controller.getListArtikel())

        # Testing
        idx = 1
        print(len(self.list))
        print(self.controller.getArtikel(1)[1])

if __name__ == "__main__":
    ttes = TestArtikelControllerUnit()
    ttes.test_tambahartikel()