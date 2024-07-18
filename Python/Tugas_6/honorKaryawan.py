import os
import string
import random
from prettytable import PrettyTable

# Head dari table
header = ['NIK', 'Nama Karyawan', 'Jam Kerja', 'Honor Harian', 'Honor Lembur', 'Total Honor']

# Template dict karyawan
karyawan_template = {
    'nama': 'nama',
    'nik': '00000000',
    'jam_kerja': 0,
    'honor_harian': 0,
    'honor_lembur': 0,
    'total_honor': 0
}

data_karyawan = {}

# Fungsi menghitung honor lembur
def hitung_honor_lembur(jam_kerja: int, honor_harian: int) -> int:
    jam_normal = 8
    tarif_lembur = 5000
    if jam_kerja > jam_normal:
        lembur = (jam_kerja - jam_normal) * tarif_lembur
        return lembur + honor_harian
    else:
        return honor_harian

while True:
    # os.system("cls") # untuk Windows
    os.system("clear") # untuk Linux/Unix

    karyawan = dict.fromkeys(karyawan_template.keys())
    karyawan['nama'] = input("Nama Karyawan: ")
    karyawan['nik'] = input("NIK Karyawan: ")
    karyawan['jam_kerja'] = int(input("Jam Kerja: "))
    karyawan['honor_harian'] = int(input("Honor Harian: "))
    honor_lembur = hitung_honor_lembur(karyawan['jam_kerja'], karyawan['honor_harian'])
    karyawan['honor_lembur'] = honor_lembur - karyawan['honor_harian']  # hanya honor lembur
    karyawan['total_honor'] = honor_lembur  # total honor termasuk honor lembur

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_karyawan.update({KEY: karyawan})

    # Membuat tabel baru setiap kali looping
    tabelKaryawan = PrettyTable(header)

    for key in data_karyawan:
        karyawan = data_karyawan[key]
        tabelKaryawan.add_row([karyawan['nik'], karyawan['nama'], karyawan['jam_kerja'], karyawan['honor_harian'], karyawan['honor_lembur'], karyawan['total_honor']])

    print(tabelKaryawan)

    print("\n")
    is_done = input("Mau tambah lagi (y/n)? ")
    if is_done.lower() == "n":
        break
