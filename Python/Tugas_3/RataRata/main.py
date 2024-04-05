# #fungsi untuk menghitung rata rata
# def rataRata(nilai_pertama: int | float, nilai_kedua: int | float, nilai_ketiga: int | float) -> float:
#     """
#     fungsi untuk menghitung nilai rata rata dari:
#     (pertandingan 1 + pertandingan 2 + pertandingan3) / 3

#     nilai_pertama: di isi dengan nilai integer atau float
#     nilai_kedua: isi dengan nilai integer atau float
#     nilai_ketiga: isi dengan nilai ingeger atau float
#     """

#     rata_rata = (nilai_pertama + nilai_kedua + nilai_ketiga) / 3
#     return rata_rata


#input nama 
#input nilai pertandingan
nama = input("Nama Siswa: ")
nilaiPertama = float(input("Nilai Pertandingan I: "))
nilaiKedua = float(input("Nilai Pertandingan II: "))
nilaiKetiga = float(input("Nilai Pertandingan III: "))

#proses perhitungan nilai rata rata
# nilaiRataRata = rataRata(nilaiPertama, nilaiKedua, nilaiKetiga)
nilaiRataRata = (nilaiPertama + nilaiKedua + nilaiKetiga) / 3

#logic
#jika nilai pertandingan 80
if nilaiRataRata >= 80:
    print(f"Siswa yang bernama {nama}")
    print(f"Memperoleh nilai rata-rata {nilaiRataRata} dan menjadi juara ke-1 dari hasil perlombaan yang diikutinya.")
#jika nilai pertandingan 75
elif nilaiRataRata >= 75:
    print(f"Siswa yang bernama {nama}")
    print(f"Memperoleh nilai rata-rata {nilaiRataRata} dan menjadi juara ke-2 dari hasil perlombaan yang diikutinya.")
#jika nilai pertandingan 65
elif nilaiRataRata >= 65:
    print(f"Siswa yang bernama {nama}")
    print(f"Memperoleh nilai rata-rata {nilaiRataRata} dan menjadi juara ke-3 dari hasil perlombaan yang diikutinya.")
else:
    print("Tidak ada yang mendapatkan juara.")