
class CatatanKegiatan:
    def __init__(self, id_kegiatan, tanggal, jam, desc_kegiatan, desc_syuk, foto, jenis_perasaan):
        self.__id_kegiatan = id_kegiatan
        self.__tanggal = tanggal
        self.__jam = jam
        self.__desc_kegiatan = desc_kegiatan
        self.__desc_syuk = desc_syuk
        self.__foto = foto
        self.__jenis_perasaan = jenis_perasaan

    def getID(self):
        return self.__id_kegiatan

    def getTanggal(self):
        return self.__tanggal

    def getJam(self):
        return self.__jam

    def getDescKegiatan(self):
        return self.__desc_kegiatan

    def getDescSyuk(self):
        return self.__desc_syuk

    def getFoto(self):
        return self.__foto

    def getJenisPerasaan(self):
        return self.__jenis_perasaan

    def setDescKegiatan(self, desc_kegiatan):
        self.__desc_kegiatan = desc_kegiatan

    def setDescSyuk(self, desc_syuk):
        self.__desc_syuk = desc_syuk

    def setFoto(self, foto):
        self.__foto = foto

    def setJenisPerasaan(self, jenis_perasaan):
        self.__jenis_perasaan = jenis_perasaan

    def __repr__(self):
        return f"""CatatanKegiatan(id_kegiatan={self.__id_kegiatan}, tanggal={self.__tanggal}, jam={self.__jam},desc_kegiatan={self.__desc_kegiatan}, desc_syuk={self.__desc_syuk}, foto={self.__foto}, jenis_perasaan={self.__jenis_perasaan})"""


if __name__ == '__main__':
    catatan_kegiatan = CatatanKegiatan(1, '2020-01-01', '12:00:00', 'Makan', 'Makan', 'foto', 'Senang')
    print(catatan_kegiatan)
    catatan_kegiatan.setDescKegiatan('tidur')
    print(catatan_kegiatan)