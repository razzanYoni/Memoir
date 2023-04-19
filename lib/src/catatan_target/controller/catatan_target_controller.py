import sqlite3
import os
from datetime import datetime

import lib.src.catatan_target.data.catatan_target_model as catatan_target_model

class CatatanTargetController:
    def __init__(self):
        self.__list_catatan_target = []
        if not os.path.exists('./db/Memoir.db'):
            f = open('./db/Memoir.db', 'w')
            f.close()
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS "catatan_target" (
            id_target INTEGER,
            tanggal DATE,
            waktu TIME,
            target TEXT,
            waktu_capai DATE,
            status VARCHAR(15),
            PRIMARY KEY("id_target" AUTOINCREMENT)
        )""")
        self.conn.commit()
        self.conn.close()

    def Tambah(self, tanggal: str, waktu: str, target: str, waktu_capai: str):
        found = True
        try :
            now = datetime.now()
            tanggal_converted = datetime(int(waktu_capai.split('-')[0]), int(waktu_capai.split('-')[1]), int(waktu_capai.split('-')[2])).date()
            # Tanggal tidak valid
            if tanggal_converted < now.date():
                found = False
                raise Exception('Tanggal kureng')
            self.conn = sqlite3.connect('./db/Memoir.db')
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO catatan_target (tanggal, waktu, target, status, waktu_capai) VALUES (?, ?, ?, ?, ?)", (tanggal, waktu, target, "Belum", waktu_capai))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(e)
            found = False
        return found

    def Memperbarui(self, catatan_target: catatan_target_model.CatatanTarget):
        found = True
        try :
            now = datetime.now()
            tanggal_converted = datetime(int(catatan_target.getWaktuCapai().split('-')[0]), int(catatan_target.getWaktuCapai().split('-')[1]), int(catatan_target.getWaktuCapai().split('-')[2])).date()
            # Tanggal tidak valid
            if tanggal_converted < now.date():
                found = False
                raise Exception('Tanggal kureng')
            self.conn = sqlite3.connect('./db/Memoir.db')
            self.c = self.conn.cursor()
            self.c.execute("UPDATE catatan_target SET target = ?, status = ?, waktu_capai = ? WHERE id_target = ?", (catatan_target.getTarget(), catatan_target.getStatus(), catatan_target.getWaktuCapai(), catatan_target.getID()))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(e)
            print("exception from controller")
            found = False
        return found

    def Hapus(self, id_target: int):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute(f"DELETE FROM catatan_target WHERE id_target = {id_target}")
        self.conn.commit()
        self.conn.close()

    def getCatatanTarget(self, id_target: int):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute(f"SELECT * FROM catatan_target WHERE id_target = {id_target}")
        catatan_target = self.c.fetchone()
        self.conn.close()
        return catatan_target

    def getListCatatanTarget(self):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_target WHERE waktu_capai >= date('now') ORDER BY waktu_capai")
        firstList = self.c.fetchall()
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_target WHERE waktu_capai < date('now') ORDER BY waktu_capai")
        secondList = self.c.fetchall()

        self.__list_catatan_target.clear()
        for i in firstList:
            self.__list_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        for i in secondList:
            self.__list_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return self.__list_catatan_target

    def getSemuaCatatanTarget(self):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_target ORDER BY waktu_capai")
        list_catatan_target = self.c.fetchall()
        semua_catatan_target = []
        for i in list_catatan_target:
            semua_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return semua_catatan_target

    def getBelumCatatanTarget(self):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_target WHERE status LIKE 'Belum' ORDER BY waktu_capai")
        list_catatan_target = self.c.fetchall()
        belum_catatan_target = []
        for i in list_catatan_target:
            belum_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return belum_catatan_target

    def getBerlangsungCatatanTarget(self):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_target WHERE status LIKE 'Berlangsung' ORDER BY waktu_capai")
        list_catatan_target = self.c.fetchall()
        berlangsung_catatan_target = []
        for i in list_catatan_target:
            berlangsung_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return berlangsung_catatan_target

    def getSelesaiCatatanTarget(self):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM catatan_target WHERE status LIKE 'Selesai' ORDER BY waktu_capai")
        list_catatan_target = self.c.fetchall()
        selesai_catatan_target = []
        for i in list_catatan_target:
            selesai_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return selesai_catatan_target

    def getCatatanTargetFromSearch(self, searchQuery: str):
        self.conn = sqlite3.connect('./db/Memoir.db')
        self.c = self.conn.cursor()
        self.c.execute(f"SELECT * FROM catatan_target WHERE target LIKE '{searchQuery}%' ORDER BY waktu_capai")
        list_catatan_target = self.c.fetchall()
        search_catatan_target = []
        for i in list_catatan_target:
            # self.__list_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
            search_catatan_target.append(catatan_target_model.CatatanTarget(i[0], i[1], i[2], i[3], i[4], i[5]))
        self.conn.close()
        return search_catatan_target

if __name__ == "__main__":
    controller = CatatanTargetController()
    controller.Tambah('2020-01-01', '03:03:03', "haaa", '2024-03-02')
