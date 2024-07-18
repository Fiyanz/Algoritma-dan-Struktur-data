'''
disini perbandingan kecepatan antara algotirma. 
data yang saya gunakan adalah data yang saya dapat dari kaggle.

data dibaca mengunakan liblary pandas


'''

import pandas as pd
import time
import BubelShort as bubbel
import MergeShort as merge
import QuickShort as quick

data = pd.read_csv("dataset/solar_data.csv")

# membaca data temperatur dan menjadikan list
temperatur = data['Temperature']
temp_list = temperatur.tolist()

def main():
    # Bubbel short
    # mulai = time.time()
    # data_shorted = bubbel.bubble_sort(temp_list) # clasik bubbel short
    
    # # data_shorted = bubbel.concurrent_bubble_sort(temp_list) # concurrency 214.47

    # selesai = time.time()
    # lama_waktu_merge = selesai - mulai

    # print(f"lama eksekusi merge sort: {lama_waktu_merge : .2f}s")

    # Merge Short
    mulai = time.time()
    merge.merge_sort(temp_list) #0.35s
    selesai = time.time()
    lama_waktu_merge = selesai - mulai

    print(f"lama eksekusi merge sort: {lama_waktu_merge : .2f}s")


    # Quick Short
    mulai = time.time()
    quick.quick_sort(temp_list, 0, len(temp_list) - 1) # 0.67 s
    selesai = time.time()
    lama_waktu_quick = selesai - mulai

    print(f"lama eksekusi quick short: {lama_waktu_quick: .2f}s")

    # print(data_shorted)


if __name__ == "__main__":
    main()