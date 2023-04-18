
class CatatanJadwal:
    def __init__(self, id_jadwal, tanggal, durasi, desc_acara, nama_acara, waktu):
        self.__id_jadwal = id_jadwal
        self.__tanggal = tanggal
        self.__waktu = waktu
        self.__nama_acara = nama_acara
        self.__desc_acara = desc_acara
        self.__durasi = durasi

    def getID(self):
        return self.__id_jadwal

    def getTanggal(self):
        return self.__tanggal

    def getWaktu(self):
        return self.__waktu

    def getDescAcara(self):
        return self.__desc_acara
    
    def getNamaAcara(self):
        return self.__nama_acara    

    def getDurasi(self):
        return self.__durasi

    def setDescAcara(self, desc_acara):
        self.__desc_acara = desc_acara

    def setTanggal(self, tanggal):
        self.__tanggal = tanggal

    def setWaktu(self, waktu):
        self.__waktu = waktu

    def setDurasi(self, durasi):
        self.__durasi = durasi

    def setNamaAcara(self, nama_acara):
        self.__nama_acara = nama_acara

    def __repr__(self):
        return f"""CatatanJadwal(id_jadwal={self.__id_jadwal}, tanggal={self.__tanggal}, durasi={self.__durasi},desc_acara={self.__desc_acara}, waktu={self.__waktu}, nama_acara={self.__nama_acara})"""


if __name__ == '__main__':
    catatan_jadwal = CatatanJadwal(1, '2020-01-01', '12:00:00', 'Makan', 'Makan', 'foto', 'Senang')
    print(catatan_jadwal)
    catatan_jadwal.setDescJadwal('sibuk')
    print(catatan_jadwal)