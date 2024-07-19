# Tugas ke 2 Algoritma Pemrograman dan Struktur Data

## Algoritma menghitung nilai rata rata mahasiswa (case 1)
**Narative Deskriptive**
1. Mulai/start
2. Memasukan NIM mahasiwa, program awal akan meminta user untuk memasukan NIM mahasiswa sebagai identitas.
3. Memasukan nama mahasiswa, kemudian user juga memasukana nama mahasiswa yang akan dihitung nilainya.
4. Memasukan nilai tugas 1, user akan memasukan nilai tugas 1.
5. Memasukan nilai tugas 2, user memasukan nilai tugas 2.
6. Memasukan nilai tugas 3, user memasukan nilai tugas 3
7. Menghitung rata rata dari nilai tugas 1 tambah tugas 2 tambah tugas 3, ditahap ini proses menghitung rata rata dengan menambahkan semua nilai yang di input user antara lain tugas 1, tugas 2, tugas 3, kemudian dibagi dengan banyak data antara lain 3 input. jadi semua nilai di jumlahkan kemudian dibagi banyak data.
8. Menampilkan nilai rata rata mahasiswa, setelah dihitung nilai rata ratanya kemudian akan ditampilakan hasil dari nilai/nilai akhir.
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
# Soal
## Tugas 2

Setelah mempelajari modul Praktikum C++:
1. Intro; 2. Syntax; 3. Output, 4. Comments;5. Variables;6. Input; 7 Data Types

### Kerjakan tugas berikut ini dengan menyusun Algoritmanya terlebih dahulu
1. Buat Notasi Algoritma Naratif Deskriptif.
2. Buat Notasi Algoritma Dengan Flowcart.
3. Buat Notasi Algoritma Pseudo Code.

# Case 1
Buatlah program untuk menghitung nilai rata-rata dari seorang siswa, dengan ketentuan sebagai berikut:
   - Nim Siswa, Nama Siswa, Nilai Tugas 1, Nilai Tugas II, Nilai Tugas III diinput.
   - Nilai Rata-rata merupakan hasil dari Nilai Tugas I, II, dan III dibagi dengan 3.
   - Tampilan yang diinginkan sebagai berikut:

   **Layar Masukkan**
   ```
   PROGRAM HITUNG NILAI RATA-RATA
   Nim Siswa :
   Nama Siswa :
   Nilai Tugas I :
   Nilai Tugas II :
   Nilai Tugas III :
   ```

   Kedua fungsi ini dapat digunakan untuk menahan tampilan hasil program yang di eksekusi agar tidak langsung kembali ke listing program tanpa menekan tombol ALT – F5. Karena fungsi getch() merupakan fungsi masukkan, jadi sebelum program keluar harus menginputkan satu buah karakter.

   **Layar Keluaran**
   ```
   Nim ........ Siswa yang bernama ……
   Memperoleh nilai rata-rata ….. dari hasil tugas yang diikutinya.
   ```


# Case 2
Buatlah program untuk menghitung nilai akhir seorang siswa dari kursus yang diikutinya. Dengan ketentuan sebagai berikut:
   - Nama Siswa, Nilai Keaktifan, Nilai Tugas, dan Nilai Ujian diinput.
   - Proses yang dilakukan untuk mendapatkan nilai murni dari masing-masing nilai, adalah:
     - Nilai Murni Keaktifan = Nilai Keaktifan dikalikan dengan 20%.
     - Nilai Murni Tugas = Nilai Tugas dikalikan dengan 50%.
     - Nilai Murni Ujian = Nilai Ujian dikalikan dengan 30%.
     - Nilai Akhir adalah Nilai Murni Keaktifan + Nilai Murni Tugas + Nilai Murni Ujian.
   - Tampilan yang diinginkan sebagai berikut:

   **Layar Masukkan**
   ```
   PROGRAM HITUNG NILAI AKHIR
   Nama Siswa :
   Nilai Keaktifan :
   Nilai Tugas :
   Nilai Ujian :
   ```

   **Layar Keluaran**
   ```
   Siswa yang bernama ……
   Dengan Nilai Persentasi Yang dihasilkan.
   Nilai Keaktifan * 20% : ……
   Nilai Tugas * 50% : ……
   Nilai Ujian * 30% : ……
   Jadi Siswa yang bernama …… memperoleh nilai akhir sebesar …..
   ```
