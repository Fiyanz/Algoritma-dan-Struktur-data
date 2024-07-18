
import os
import string
import random
from prettytable import PrettyTable


# head dari table
tabelHead = ['Nim', 'Nama Mahasiswa', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir', 'Nilai Huruf']

# template dict mahasiswa
mahasiswa_template = {
	'nama':'nama',
	'nim':'00000000',
	'nilai_uts': 0,
	'nilai_uas': 0,
	'nilai_akhir': 0,
	'nilai_huruf': None
}

data_mahasiswa = {}

# fungsi menghitung nilai nilai
def nilai(nilai_uts: int | float, nilai_uas: int | float) -> float:
	return ((nilai_uas * (40/100)) + (nilai_uts * (60/100)))

# fungsi untuk mengambalikan nilai karakter
def nilaiH(nilaiAkhir) -> str:
	if nilaiAkhir >= 80:
		return 'A'
	elif nilaiAkhir >= 70:
		return 'B'
	elif nilaiAkhir >= 56:
		return 'C'
	elif nilaiAkhir >= 47:
		return 'D'
	else:
		return 'D'

while True:
	# os.system("cls") # untuk windows
	os.system("clear")

	mahasiswa = dict.fromkeys(mahasiswa_template.keys())
	mahasiswa['nama'] = input("Nama Mahasiswa: ")
	mahasiswa['nim'] = input("NIM Mahasiswa: ")
	mahasiswa['nilai_uts'] = int(input("Nilai UTS: "))
	mahasiswa['nilai_uas'] = int(input("Nilai UAS: "))
	nilaiAkhir = nilai(mahasiswa['nilai_uts'], mahasiswa['nilai_uas'])
	mahasiswa['nilai_akhir'] = nilaiAkhir
	nilaiHuruf = nilaiH(nilaiAkhir=nilaiAkhir)
	mahasiswa['nilai_huruf'] = nilaiHuruf



	KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
	data_mahasiswa.update({KEY:mahasiswa})

	# Membuat Tabel
	tabelMahasiswa = PrettyTable(tabelHead)

	for mahasiswa in data_mahasiswa:
		KEY = mahasiswa
		
		NAMA = data_mahasiswa[KEY]['nama']
		NIM = data_mahasiswa[KEY]['nim']
		UTS = data_mahasiswa[KEY]['nilai_uts']
		UAS = data_mahasiswa[KEY]['nilai_uas']
		NAKHIR = data_mahasiswa[KEY]['nilai_akhir']
		NHURUF = data_mahasiswa[KEY]['nilai_huruf']

		tabelMahasiswa.add_row([NIM, NAMA, UTS, UAS, NAKHIR, NHURUF])	

	print(tabelMahasiswa)
	
	print("\n")
	is_done = input("Mau tambah lagi (y/n)? ")
	if is_done == "n":
		break
