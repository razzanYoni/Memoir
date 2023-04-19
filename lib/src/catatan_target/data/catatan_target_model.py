
class CatatanTarget:
    def __init__(self, id_target, tanggal, waktu, target, waktu_capai, status = "Belum"):
        self.__id_target = id_target
        self.__tanggal = tanggal
        self.__waktu = waktu
        self.__target = target
        self.__status = status
        self.__waktu_capai = waktu_capai

    def getID(self):
        return self.__id_target

    def getTanggal(self):
        return self.__tanggal

    def getWaktu(self):
        return self.__waktu

    def getTarget(self):
        return self.__target

    def getWaktuCapai(self):
        return self.__waktu_capai

    def getStatus(self):
        return self.__status

    def setTarget(self, target):
        self.__target = target

    def setWaktuCapai(self, waktu_capai):
        self.__waktu_capai = waktu_capai

    def setStatus(self, status):
        self.__status = status

    def __repr__(self):
        return f"""CatatanTarget(id_target={self.__id_target}, tanggal={self.__tanggal}, waktu={self.__waktu}, target={self.__target}, waktu_capai={self.__waktu_capai}, status={self.__status})"""

if __name__ == '__main__':
    catatan_target = CatatanTarget(1, '2020-01-01', '12:00:00', 'Umroh', '2023-01-01')
    print(catatan_target)
    catatan_target.setTarget('Hidup yang bener')
    print(catatan_target)
