
# fungsi untuk menhitung tunjangan sesuai golongan
def golonganJabatan(golongan: int, gaji_pokok: int) -> float:
    if golongan == 1:
        return gaji_pokok * (5/100)
    elif golongan == 2:
        return gaji_pokok * (10/100)
    elif golongan == 3:
        return gaji_pokok * (15/100)

# fungsi untuk menghitung golongan pendidikan
def golonganPendidikan(pendidikan: int, gaji_pokok: int) -> float:
    if pendidikan == 1:
        return gaji_pokok * (2.5/100)
    elif pendidikan == 2:
        return gaji_pokok * (5/100)
    elif pendidikan == 3:
        return gaji_pokok * (20/100)
    elif pendidikan == 4:
        return gaji_pokok * (30/100)
    
#funsi menghitung lembur
def lembur(jumlahJamKerja: int, normal_jam_kerja:int, gaji_lembur: int) -> int:
    jamLembur = jumlahJamKerja - normal_jam_kerja
    return jamLembur * gaji_lembur