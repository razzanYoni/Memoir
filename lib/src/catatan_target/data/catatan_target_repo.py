class CatatanTargetRepo:
    def __init__(self, db):
        self.db = db

    def getCatatanTarget(self, id_target):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM catatan_kegiatan WHERE id_kegiatan = %s", (id_target))
        result = cursor.fetchone()
        cursor.close()
        return result
