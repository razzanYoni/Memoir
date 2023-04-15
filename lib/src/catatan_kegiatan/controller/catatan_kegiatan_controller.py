import sqlite3

import lib.src.catatan_kegiatan.data.catatan_kegiatan_model as catatan_kegiatan_model


class CatatanKegiatanController:
    def __init__(self):
        self.__list_catatan_kegiatan = []
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS "catatan_kegiatan" (
            "id_kegiatan" INTEGER,
            "tanggal" date,
            "jam" time,
            "desc_kegiatan" string,
            desc_syuk string,
            foto string,
            jenis_perasaan integer,
            PRIMARY KEY("id_kegiatan" AUTOINCREMENT)
        )""")
        self.conn.commit()
        self.conn.close()

    def Tambah(self, tanggal: str, jam: str, desc_kegiatan: str, desc_syuk: str, foto: str, jenis_perasaan: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO catatan_kegiatan (tanggal, jam, desc_kegiatan, desc_syuk, foto, jenis_perasaan) VALUES (?, ?, ?, ?, ?, ?)", (tanggal, jam, desc_kegiatan, desc_syuk, foto, jenis_perasaan))
        self.conn.commit()
        self.conn.close()

    def Memperbarui(self, catatan_kegiatan: catatan_kegiatan_model.CatatanKegiatan):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("UPDATE catatan_kegiatan SET desc_kegiatan = ?, desc_syuk = ?, foto = ?, jenis_perasaan = ? WHERE id_kegiatan = ?", (catatan_kegiatan.getDescKegiatan(), catatan_kegiatan.getDescSyuk(), catatan_kegiatan.getFoto(), catatan_kegiatan.getJenisPerasaan(), catatan_kegiatan.getID()))
        self.conn.commit()
        self.conn.close()

    def Hapus(self, id_kegiatan: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM catatan_kegiatan WHERE id_kegiatan = ?", (id_kegiatan,))
        self.conn.commit()
        self.conn.close()

    def getCatatanKegiatan(self, id_kegiatan: int):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_kegiatan WHERE id_kegiatan = ?", (id_kegiatan,))
        catatan_kegiatan = self.c.fetchone()
        self.conn.close()
        return catatan_kegiatan

    def getListCatatanKegiatan(self):
        # self.conn = sqlite3.connect('../../../../db/Memoir.db')
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_kegiatan ORDER BY tanggal DESC, jam DESC")
        list_catatan_kegiatan = self.c.fetchall()
        self.__list_catatan_kegiatan.clear()
        for i in list_catatan_kegiatan:
            self.__list_catatan_kegiatan.append(catatan_kegiatan_model.CatatanKegiatan(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        self.conn.close()
        return self.__list_catatan_kegiatan


if __name__ == "__main__":
    controller = CatatanKegiatanController()
    controller.Tambah("2021-05-01", "12:00:00", "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM", "Makan", "Makan", 1)
    controller.Memperbarui(catatan_kegiatan_model.CatatanKegiatan(1, "2021-05-01", "12:00:00", "Makan", "Makan", "Makan", 1))
    controller.Tambah("2021-05-03", "13:00:00", "Makan", "Makan", "Makan", 1)
    print(controller.getListCatatanKegiatan())
