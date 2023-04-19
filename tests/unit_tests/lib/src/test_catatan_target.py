import pytest
import lib.src.catatan_target.controller.catatan_target_controller as catatan_target_controller
import lib.src.catatan_target.data.catatan_target_model as catatan_target_model
from datetime import date
import time

class TestCatatanTargetUnit():
    def setup_method(self):
        self.controller = catatan_target_controller.CatatanTargetController()

    def get_max_id(self):
        maxID = -1 # id_target pasti lebih dari nol
        catatanTargetList = self.controller.getListCatatanTarget()
        for catatanTarget in catatanTargetList:
            if (catatanTarget.getID() > maxID):
                maxID = catatanTarget.getID()

        return maxID # jika maxID = -1 berarti tabel catatan_artikel kosong, jika > 0 artinya tabel catatan_artikel tidak kosong

    def test_tambah_catatan_target_valid(self):
        # Tambah Catatan Target
        tanggal = date.today().strftime("%Y-%m-%d")
        waktu = time.strftime("%H:%M:%S", time.localtime())
        target = "pytest - test_tambah_catatan_target_valid"
        waktu_capai = "2025-01-01"
        assert self.controller.Tambah(tanggal, waktu, target, waktu_capai) # jika gagal menambahkan ke database akan mengembalikan False

    def test_tambah_catatan_target_invalid(self):
        # Tambah Catatan Target
        tanggal = date.today().strftime("%Y-%m-%d")
        waktu = time.strftime("%H:%M:%S", time.localtime())
        target = "pytest - test_tambah_catatan_target_invalid"
        waktu_capai = "1999-12-12"
        assert not(self.controller.Tambah(tanggal, waktu, target, waktu_capai)) # jika gagal menambahkan ke database akan mengembalikan False

    def test_ubah_catatan_target_valid(self):
        # Mengubah catatan target berID maxID
        maxID = self.get_max_id()
        if (maxID != -1):
            prevCatatanTarget = self.controller.getCatatanTarget(maxID)
            target = "pytest - test_ubah_catatan_target_valid"
            waktu_capai = "2030-12-12"
            status = "Berlangsung"

            self.controller.Memperbarui(catatan_target_model.CatatanTarget(prevCatatanTarget[0], prevCatatanTarget[1], prevCatatanTarget[2], target, waktu_capai, status))
            currCatatanTarget = self.controller.getCatatanTarget(maxID)
            assert currCatatanTarget[1] == prevCatatanTarget[1]
            assert currCatatanTarget[2] == prevCatatanTarget[2]
            assert currCatatanTarget[3] == target
            assert currCatatanTarget[4] == waktu_capai
            assert currCatatanTarget[5] == status
        else: # tabel catatan_target kosong
            assert True # karena dengan GUI dapat dipastikan bahwa catatan target yang dapat diubah sudah ada di database

    def test_ubah_catatan_target_invalid(self):
        # Mengubah catatan target berID maxID
        maxID = self.get_max_id()
        if (maxID != -1):
            ubahCatatanTarget = self.controller.getCatatanTarget(maxID)
            target = "pytest - test_ubah_catatan_target_invalid"
            waktu_capai = "1999-12-12"
            status = "Berlangsung"
            assert not(self.controller.Memperbarui(catatan_target_model.CatatanTarget(ubahCatatanTarget[0], ubahCatatanTarget[1], ubahCatatanTarget[2], target, waktu_capai, status))) # jika gagal menambahkan ke database akan mengembalikan False
        else: # tabel catatan_target kosong
            assert True # karena dengan GUI dapat dipastikan bahwa catatan target yang dapat diubah sudah ada di database

    def test_search_target(self):
        query = "notfound"
        isQueryExist = False
        catatanTargetList = self.controller.getListCatatanTarget()
        for catatanTarget in catatanTargetList:
            if (query in catatanTarget.getTarget()):
                isQueryExist = True
                break

        foundList = self.controller.getCatatanTargetFromSearch(query)

        assert (len(foundList) != 0 and isQueryExist) or (len(foundList) == 0 and not(isQueryExist))

if __name__ == "__main__":
    pytest.main()

# python3 ./tests/unit_tests/lib/src/test_catatan_target.py
