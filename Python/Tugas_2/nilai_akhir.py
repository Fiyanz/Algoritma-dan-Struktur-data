def nilai(keaktifan: int | float, tugas: int | float, ujian: int | float) -> int | float:
    """
    nilai keaktifan * dengan 20%
    nilai tugas * dengan 50%
    nilai ujian * dengan 30%
    """
    nilai_keaktifan = keaktifan * 0.2
    nilai_tugas = tugas * 0.5
    nilai_ujian = ujian * 0.3

    return nilai_keaktifan, nilai_tugas, nilai_ujian



nama = input("Nama Mahasiswa: ")
keaktifan = float(input("Nilai Keaktifan: "))
tugas = float(input("Nilai Tugas: "))
ujian = float(input("Nilai Ujian: "))

#menghitung nilai
nilai_keaktifan, nilai_tugas, nilai_ujian = nilai(keaktifan=keaktifan, tugas=tugas, ujian=ujian)

#menghitung nilai akhir
nilai_akhir = nilai_keaktifan + nilai_tugas + nilai_ujian

#menampilkan nilai akhir
print("=============================================================================")
print(f"Mahasiswa yang bernama {nama}")
print(f"Dengan Nilai Persentasi Yang dihasilkan")
print(f"Nilai Keaktifan * 20% : {nilai_keaktifan}")
print(f"Nilai Tugas * 50% : {nilai_tugas}")
print(f"Nilai Ujian * 30% : {nilai_ujian}")
print(f"Jadi Siswa yang bernama {nama} memperoleh nilai akhir sebesar {nilai_akhir}")