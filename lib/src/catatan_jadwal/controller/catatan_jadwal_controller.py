import sqlite3
import os

import lib.src.catatan_jadwal.data.catatan_jadwal_model as catatan_jadwal_model
import lib.src.utilities.util as util


class CatatanJadwalController:
    def __init__(self):
        self.__list_catatan_jadwal = []
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        if not os.path.exists('../Memoir.db'):
            f = open('../Memoir.db', 'w')
            f.close()
        self.conn = sqlite3.connect('../Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS "catatan_jadwal" (
            "id_jadwal" INTEGER,
            "tanggal" date,
            "waktu" time,
            "nama_acara" Text,
            "desc_acara" Text,
            "durasi" integer,
            PRIMARY KEY("id_jadwal" AUTOINCREMENT)
        )""")
        self.conn.commit()
        self.conn.close()

    def Tambah(self, tanggal: str, durasi: str, desc_acara: str, nama_acara: str):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('../Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO catatan_jadwal (tanggal, durasi, desc_acara, nama_acara) VALUES (?, ?, ?, ?)", (tanggal, durasi, desc_acara, nama_acara))
        self.conn.commit()
        self.conn.close()

    def Memperbarui(self, catatan_jadwal: catatan_jadwal_model.CatatanJadwal):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('../Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("UPDATE catatan_jadwal SET desc_acara = ?, WHERE id_jadwal = ?", (catatan_jadwal.getDesc(), catatan_jadwal.getID()))
        self.conn.commit()
        self.conn.close()

    def Hapus(self, id_jadwal: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('../Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM catatan_jadwal WHERE id_jadwal = ?", (id_jadwal,))
        self.conn.commit()
        self.conn.close()

    def getCatatanJadwal(self, id_jadwal: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('../Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_jadwal WHERE id_jadwal = ?", (id_jadwal,))
        catatan_jadwal = self.c.fetchone()
        self.conn.close()
        return catatan_jadwal

    def getListCatatanJadwal(self):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('../Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_jadwal ORDER BY tanggal DESC, durasi DESC")
        list_catatan_jadwal = self.c.fetchall()
        self.__list_catatan_jadwal.clear()
        for i in list_catatan_jadwal:
            self.__list_catatan_jadwal.append(catatan_jadwal_model.CatatanJadwal(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        self.conn.close()
        return self.__list_catatan_jadwal


if __name__ == "__main__":
    controller = CatatanJadwalController()
