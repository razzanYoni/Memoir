
class Artikel:
    def __init__(self, id_artikel, judul, isi, pengarang, tanggal, foto):
        self.__id_artikel = id_artikel
        self.__judul = judul
        self.__isi = isi
        self.__pengarang = pengarang 
        self.__tanggal = tanggal
        self.__foto = foto

    def getID(self):
        return self.__id_artikel
    
    def getJudul(self):
        return self.__judul
    
    def getIsi(self):
        return self.__isi
    
    def getPengarang(self):
        return self.__pengarang
    
    def getTanggal(self):
        return self.__tanggal
    
    def getFoto(self):
        return self.__foto
    
    def setJudul(self, judul):
        self.__judul = judul
    
    def setIsi(self, isi):
        self.__isi = isi
    
    def setPengarang(self, pengarang):
        self.__pengarang = pengarang
    
    def setTanggal(self, tanggal):
        self.__tanggal = tanggal
    
    def setFoto(self, foto):
        self.__foto = foto
    
    def __repr__(self):
        return f"""Artikel(id_artikel={self.__id_artikel}, judul={self.__judul}, isi={self.__isi}, pengarang={self.__pengarang}, tanggal={self.__tanggal}, foto={self.__foto})"""
    
if __name__ == '__main__':
    artikel = Artikel(1, 'Judulnya', 'Isinya', 'Pengarangnya', '2020-01-02', 'foto')
    print(artikel)
    artikel.setJudul('tidur')
    print(artikel)



