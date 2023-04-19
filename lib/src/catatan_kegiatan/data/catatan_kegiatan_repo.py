import sqlite3

import lib.src.catatan_kegiatan.data.catatan_kegiatan_model as catatan_kegiatan_model

class CatatanKegiatanRepo:
    def __init__(self, db):
        self.db = db

    def getCatatanKegiatan(self, id_kegiatan):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM catatan_kegiatan WHERE id_kegiatan = %s", (id_kegiatan,))
        result = cursor.fetchone()
        cursor.close()
        return result