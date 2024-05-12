

# def multiply_odd_series(n):
#     result = 1
#     series = []
#     for i in range(1, n + 1):
#         result *= 2 * i - 1
#         series.append(result)
#     return series

# def print_odd_triangle(series):
#     for i in range(len(series)):
#         print(" * ".join(str(x) for x in series[:i+1]))

# n = 5  # Jumlah baris segitiga
# odd_series = multiply_odd_series(n)
# print_odd_triangle(odd_series)


def hitung_perkalian_dan_cetak(baris):
    hasil = 1
    deret = ""
    for i in range(baris):
        for j in range(i + 1):
            bilangan_ganjil = 2 * j + 1
            hasil *= bilangan_ganjil
            deret += str(bilangan_ganjil)
            if j < i:
                deret += " * "
        deret += " = " + str(hasil)
        print(deret)
        deret = ""
        hasil = 1

def main():
    jumlah_baris = 5  # Jumlah baris segitiga
    hitung_perkalian_dan_cetak(jumlah_baris)

if __name__ == "__main__":
    main()
