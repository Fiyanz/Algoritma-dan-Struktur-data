#menghitung gaji kontak karyawan

import fungsi as fn

#============== deklarasi variable ==============
gaji_pokok = 300000

gaji_lembur = 3500
normal_jam_kerja = 8 #satuan jam

#============== input ===============
nama = input("Nama Karyawan: ")
# list golongan
print("""
      1. golongan 1
      2. Golongan 2
      3. Golongan 3
""")
golongan = int(input("Golongan Jabatan: "))
# menampilkan list pendidikan
print("""
      1. SMA
      2. D1
      3. D3
      4. S1
""")
pendidikan = int(input("Pendidikan: "))

#jam kerja
jumlahJamKerja = int(input("Jumlah Jam Kerja: "))

#=============== proses ==================
# gaji golongan jabatan
gajiGologanJabatan = fn.golonganJabatan(golongan=golongan, gaji_pokok=gaji_pokok)
# gaji golongan pendidikan
gajiGolonganPendidikan = fn.golonganPendidikan(pendidikan=pendidikan, gaji_pokok=gaji_pokok)
# gaji lembur
gajiLembur = fn.lembur(jumlahJamKerja=jumlahJamKerja, normal_jam_kerja=normal_jam_kerja, gaji_lembur=gaji_lembur)

#============== output ==================

output = f"""
      Siswa yang bernama {nama}
      Honor yang diterima: 
      Tunjangan Jabatan Rp{gajiGologanJabatan}
      Tunjangan Pendidikan Rp{gajiGolonganPendidikan}
      Honor Lembur Rp{gajiLembur}
"""
print(output)