import sqlite3

import lib.src.artikel.data.artikel_model as catatan_kegiatan_model

class ArtikelRepo:
    def __init__(self, db):
        self.db = db

    def getArtikel(self, id_artikel):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM artikel WHERE id_artikel = %s", (id_artikel,))
        result = cursor.fetchone()
        cursor.close()
        return result
