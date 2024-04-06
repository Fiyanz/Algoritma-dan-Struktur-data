"""
create by Fiyanz
"""
nama = input("Nama Siswa: ")
nilaiKeaktifan = float(input("Nilai Keaktifan: "))
nilaiTugas = float(input("Nilai Tugas: "))
nilaiUjian = float(input("Nilai Ujian: "))

#menghitung nilai murni
nilaiKeaktifan = nilaiKeaktifan * 0.2
nilaiTugas = nilaiTugas * 0.3
nilaiUjian = nilaiUjian * 0.5

#nilai akhir
nilaiAkhir = nilaiKeaktifan + nilaiTugas + nilaiUjian

#seleksi nilai
def seleksiNilai(nilaiAkhir) -> str:
    if nilaiAkhir > 80:
        return 'A'
    elif nilaiAkhir > 70:
        return 'B'
    elif nilaiAkhir > 56:
        return 'C'
    elif nilaiAkhir > 46:
        return 'D'
    else:
        return 'E'
    
grade = seleksiNilai(nilaiAkhir=nilaiAkhir)

#menampilkan nilai
print(f"Siswa yang bernama {nama}")
print(f"Dengan Nilai Persentasi Yang dihasilkan.")
print(f"Nilai Keaktifan * 20% : {nilaiKeaktifan}")
print(f"Nilai Tugas * 30% : {nilaiTugas}")
print(f"Nilai Ujian * 50% : {nilaiUjian}")
print(f"Jadi Siswa yang bernama {nama} memperoleh nilai akhir sebesar {nilaiAkhir} dengan grade {grade}")