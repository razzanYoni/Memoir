import sqlite3

import lib.src.artikel.data.artikel_model as artikel_model
from lib.src.utilities.util import image_to_blob

class ArtikelController:
    def __init__(self):
        self.__list_artikel = []
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS "artikel" (
            "id_artikel" INTEGER,
            "judul" string,
            "isi" string,
            "pengarang" string,
            "tanggal" date,
            "foto" BLOB,
            PRIMARY KEY("id_artikel" AUTOINCREMENT)
        )""")
        self.conn.commit()
        self.conn.close()

    def Tambah(self, judul: str, isi: str, pengarang: str, tanggal: str, foto: bytes):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO artikel (judul, isi, pengarang, tanggal, foto) VALUES (?, ?, ?, ?, ?)", (judul, isi, pengarang, tanggal, foto))
        self.conn.commit()
        self.conn.close()

    def Hapus(self, id_artikel: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM artikel WHERE id_artikel = ?", (id_artikel,))
        self.conn.commit()
        self.conn.close()
    
    def getArtikel(self, id_artikel: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM artikel WHERE id_artikel = ?", (id_artikel,))
        artikel = self.c.fetchone()
        self.conn.close()
        return artikel
    
    def getListArtikel(self):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM artikel ORDER BY tanggal DESC")
        list_artikel = self.c.fetchall()
        self.__list_artikel.clear()
        for i in list_artikel:
            self.__list_artikel.append(artikel_model.Artikel(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return self.__list_artikel
    
if __name__ == "__main__":
    controller = ArtikelController()
    print(controller.getListArtikel())