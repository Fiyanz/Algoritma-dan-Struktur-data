from kelas import Mahasiswa
from prettytable import PrettyTable

jumlah = int(input("Masukan banyak data yang ingin dimasukan: "))

mahasiswa_lists = []

for x in range(jumlah):
    print(f"Memasukan Data ke-{x + 1}")
    nim = int(input("Masukan NIM: "))
    nama = input("Masukan Nama: ")
    uts = int(input("Masukan Nilai UTS: "))
    uas = int(input("Masukan NIlai UAS: "))
    print('\n')
    
    # membuat objek mahasiswa
    mahasiswa = Mahasiswa(nim=nim,
                          nama=nama,
                          uts=uts,
                          uas=uas)
    
    mahasiswa_lists.append(mahasiswa)
    # print(mahasiswa)


# head of tabel
tabelMahasiswa = PrettyTable(['Nim', 'Nama Mahasiswa', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir', 'Nilai Huruf'])


for mahasiswa in mahasiswa_lists:
    tabelMahasiswa.add_row([mahasiswa.getNim(), mahasiswa.getNama(), mahasiswa.getUTS(), mahasiswa.getUAS(), mahasiswa.getNilaiAkhir(), mahasiswa.getNilaiHuruf()])


print(tabelMahasiswa)
