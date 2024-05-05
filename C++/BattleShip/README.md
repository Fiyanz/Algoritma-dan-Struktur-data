## Menjalankan program

cara menjalankan programnya salin code atau cara clone repo ini

```bash
git clone https://github.com/Fiyanz/Algoritma-dan-Struktur-data
```

kemudian masuk ke dalam directory C++ dengan cara

```bash
cd C++/BattleShip
```

masih dalam terminal, untuk compile

Note: pastika sudah menginstall conpilernya

```bash
g++ ship.cpp -o ship
```

untuk run

```bash
./ship
```

## Cara Main

Sebelum mulai run programnya alangkah baiknya untuk memahami bagaimana cara bermain atau menebak dimana ship berada. angka 1 anggap saja sebagai ship :v.

Dalam sebuah array terutama di bahasa pemrograman C++ indeks atau mulainya program dimulai dari angka 0. dari array yang kita punya di bawah hanya memilili 4 baris, sehingga nilia yang kita gunakan hanya antara 0 dan 3.

pertanyaanya ini kan ada bari dan colom bagaimana cara menghitunya?
dari itu mari kita belajar indeks array terlebrlebih dahulu. array di bawah adalah jenis array 3d atau sering di sebuh array 3 x 3, sama halnya menyebutkan bilangan matriks. dalam matriks memiliki baris dan kolom, dalam array 3 x 3 dibawah juga memiliki baris dan kolom.

untuk membacanya baris diketahui melalui banyaknya deret bilangan angka dari samping kiri ke kanan, sedangkan kolom sendiri banyaknya baris angka dari atas ke bawah.

```bash

0   1   1   0   -> baris 1
0   0   0   0   -> baris 2
0   0   1   0   -> baris 3
0   0   1   0   -> baris 4

|   |   |   |
|---|---|---|----> kolom
1   2   3   4
```

namun perlu di perhatikan untuk membaca baris dan kolom dalam istilah matriks dan array berbeda. pembacaan matriks lebih cenderung agar udah dipahami bahasa manusia, berbeda dengan array yang cendering dipahami olah mesin atau komputer.

cara membaca matriks dimulai dari kiri ke kanan, jadi untuk membaca sebuah array berdimensi juga sama. nah sekarang bagaimana cara menyelesaikan game dibawah ini dengan winstreak pastinya!!!

untuk mencari kordinat angka 1 dalam baris pertama, tapi sebelum itu membaca sebuah array dimulai dari baris dan kolom, baris yang bersifat horisontal dan kolom yang vertikal.
pertama tentukan dimana angka satu dalam baris berada, kemudian tentukan angka satu dari kolom.

di bawah terdapat angka satu dalam indek 0, kenapa 0 bukan 1? ingat!! karena indeks dimulai dari 0, disini kita sedang mencari satu dari persektif baris atau nilai baris horisontal. kemudian mencari kolom atau nilai vertikal terdapat intek 1.

masukan nilai baris kemudian enter dan nanti diminta untuk memasukan nilai kolom.

```bash
0   1   2   3
|   |   |   |

0   1   1   0   -- 0
0   0   0   0   -- 1
0   0   1   0   -- 2
0   0   1   0   -- 3
Memilih koordinat
Pilih nomor baris antara 0 dan 3: 0
Pilih nomor kolom antara 0 dan 3: 1
Tertembak! 9 ship tersisa.
```

jika nilai yang dimasukan benar dan sesuai kordinat makan akan menampilkan sisa ship yang harus di tebak.

```bash
0   0   0   1
0   0   1   0
0   1   0   0
0   0   0   1
Memilih koordinat
Pilih nomor baris antara 0 dan 3:
```

dann program akan mengulang kembali serta mengacak kordiat ship. kordinat yang ditampilkan akan berbeda dengan yang kalian run, jadi selamat bermain!!!

### Jangan Lupa Tikik Komah (;)!!!
