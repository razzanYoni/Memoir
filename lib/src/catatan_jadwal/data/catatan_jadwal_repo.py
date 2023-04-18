import sqlite3

import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model

class CatatanJadwalRepo:
    def __init__(self, db):
        self.db = db

    def getCatatanJadwal(self, id_jadwal):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM catatan_jadwal WHERE id_jadwal = %s", (id_jadwal,))
        result = cursor.fetchone()
        cursor.close()
        return result