def rata(tugas1: int | float, tugas2: int | float, tugas3: int | float) -> int | float:
    '''
    fungsi untuk menghitung nilai rata rata 
    (tugas1 + tugas2 + tugas3) / 3

    tugas1: nilai tugas 1
    tugas2: nilai tugas 2
    tugas3: nilai tugas 3
    '''
    return (tugas1 + tugas2 + tugas3) / 3


#input
nim = int(input("NIM Siswa: "))
nama = input("Nama Siswa: ")
nilai_tugas1 = float(input("Tugas 1: "))
nilai_tugas2 = float(input("Tugas 2: "))
nilai_tugas3 = float(input("Tugas 3: "))
#proses menghitung rata rata
rata_rata = rata(nilai_tugas1, nilai_tugas2, nilai_tugas3)
#output
print("")
print(f"NIM {nim} Siswa yang bernama {nama}")
print(f"Memperoleh nilai rata rata {rata_rata}")