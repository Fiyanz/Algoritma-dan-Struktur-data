from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def bubble_sort(arr):
    n = len(arr)
    # Iterasi luar
    for i in range(n-1):
        swapped = False
        # Iterasi dalam
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Pengoptimalan: berhenti jika tidak ada pertukaran
        if not swapped:
            break
    return arr

''' uncommand code dibawah untuk run hanya bubble short '''

# Meminta input data
# jumlah_data = int(input("Masukkan jumlah data: "))
# data = []
# for i in range(jumlah_data):
#     nilai = int(input(f"Masukkan nilai data ke-{i+1}: "))
#     data.append(nilai)


# # Contoh penggunaan
# print("Data sebelum diurutkan:", data)
# data = bubble_sort(data)
# print("Data setelah diurutkan:", data)



# Bubbel short tapi menggunakan konkurensi
# def bubble_sort_portion(data, start, end):
#   swapped = True
#   while swapped:
#     swapped = False
#     for i in range(start, end - 1):
#       if data[i] > data[i + 1]:
#         data[i], data[i + 1] = data[i + 1], data[i]
#         swapped = True
# def concurrent_bubble_sort(data):
#   num_threads = 4  # Adjust based on your system
#   threads = []

#   # Divide data into chunks for each thread
#   chunk_size = len(data) // num_threads
#   for i in range(num_threads):
#     start = i * chunk_size
#     end = min((i + 1) * chunk_size, len(data))
#     thread = Thread(target=bubble_sort_portion, args=(data, start, end))
#     threads.append(thread)
#     thread.start()

#   # Wait for all threads to finish
#   for thread in threads:
#     thread.join()