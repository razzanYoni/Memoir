import pytest
import lib.src.artikel.controller.artikel_controller as artikel_controller

controller = artikel_controller.ArtikelController()

def test1():
    x = len(controller.getListArtikel())
    assert x > 0

if __name__ == "__main__":
    pytest.main()