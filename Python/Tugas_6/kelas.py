

# class bahasiswa
class Mahasiswa():
    def __init__(self,
                 nim: int,
                 nama: str,
                 uts: int,
                 uas: int) -> None:
        
        self.nim = nim
        self.nama = nama
        self.uts = uts
        self.uas = uas

    # fungsi untuk akses nim mahasiswa
    def getNim(self) -> int:
        return self.nim
    # fungsi untuk akses nama mahasiswa
    def getNama(self) -> str:
        return self.nama
    # fungsi untuk akses nilai uts
    def getUTS(self) -> int:
        return self.uts
    # fungsi untuk akses nilai uas
    def getUAS(self) -> int:
        return self.uas
    # fungsi untuk mengambil nilai akhir mahasiswa
    def getNilaiAkhir(self) -> float:
        return ((self.uas * (40/100)) + (self.uts * (60/100)))
    
    def getNilaiHuruf(self) -> str:
        nilai = ((self.uas * (40/100)) + (self.uts * (60/100)))
        if nilai >= 80:
            return 'A'
        elif nilai >= 70:
            return 'B'
        elif nilai >= 56:
            return 'C'
        elif nilai >= 47:
            return 'D'
        else:
            return 'E'
    

# class untuk karyawan
class Karyawan:
    
    def __init__(self, nama: str, jamKerja: int) -> None:
        self.nama = nama
        self.jamKerja = jamKerja

    def getNama(self):
        return self.nama
    
    def getJamKerja(self):
        return self.jamKerja
    
    def getLembur(self, lembur):
        return lembur - self.jamKerja
    
    def honorLembur(self):
        
        
    def getHonor(self):
        return 15000