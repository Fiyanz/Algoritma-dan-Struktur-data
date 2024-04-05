# Tugas ke 2 Algoritma Pemrograman dan Basis Data

## Algoritma menghitung nilai rata rata mahasiswa (case 1)
**Narative Deskriptive**
1. Mulai/start
2. Memasukan NIM mahasiwa
3. Memasukan nama mahasiswa
4. Memasukan nilai tugas 1
5. Memasukan nilai tugas 2
6. Memasukan nilai tugas 3
7. Menghitung rata rata dari nilai tugas 1 tambah tugas 2 tambah tugas 3 kemudia dibagi 3
8. Menampilkan nilai rata rata mahasiswa
9. Program selesai

### Flowchart menghitung nilai rata rata
**Img Flowchart**

![](https://github.com/Fiyanz/Algoritma-dan-Basis-data/blob/main/img/Flowchat_rata-rata.png)


### Pseudo Code menghitung rata rata
```
Algoritma Menghitung Rata-Rata

Start/Mulai
    deklarasi variabel:
        nama string
        nim int
        nilaiTugas1, nilaiTugas2, nilaiTugas3: int | float
        nilaiRataRata float

    Input:
        nama
        nim
        nilaiTugas1
        nilaiTugas2
        nilaiTugas3

    Proses:
        nilaiRataRata = (nilaiTugas1 + nilaiTugas2 + nilaiTugas3) / 3

    Output:
        nama
        nim
        nilaiRataRata
End/Selesai
```


## Algoritma menghitung nilai akhir
**Narative Deskriptive**
1. Mulai
2. Memasukan nama mahasiswa
3. Memasukan nilai murni keaktifan
4. Memasukan nilai murni tugas
5. Memasukan nilai murni ujian
6. Proses menghitung nilai dengan menambahkan nilai keaktifan, tugas, ujian
7. Proses menghitung nilai akhir
8. menampilkan nilai akhir
9. Selesai

### Flowchart menghitung nilai akhir
**Img Flowchart**

![](https://github.com/Fiyanz/Algoritma-dan-Basis-data/blob/main/img/flowchart_nilai_akhir.png)


### Pseudo Code
```
Algoritma Menghitung Nilai Akhir Siswa

Mulai
    Deklarasi variabel:
        nama: string
        nilaiKeaktifan, nilaiTugas, nilaiUjian: int
        nilaiAkhir: float

    Input:
        nama
        nilaiKeaktifan
        nilaiTugas
        nilaiUjian

    Proses:
        nilaiKeaktifan = nilaiKeaktifan * 0.2
        nilaiTugas = nilaiTugas * 0.5
        nilaiUjian = nilaiUjian * 0.3
        nilaiAkhir = nilaiKeaktifan + nilaiTugas + nilaiUjian

    Output:
        nama
        nilaiAkhir
Selesai
```
