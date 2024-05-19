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
    mulai = time.time()
    # Bubbel short
    # data_shorted = bubbel.bubble_sort(temp_list) # clasik bubbel short
    # data_shorted = bubbel.concurrent_bubble_sort(temp_list) # concurrency 214.47

    # Merge Short
    data_shorted = merge.merge_sort(temp_list) #0.35s

    # Quick Short
    # data_shorted = quick.quick_sort(temp_list, 0, len(temp_list) - 1) # 0.67 s
    selesai = time.time()


    lama_waktu = selesai - mulai

    print(data_shorted)

    print(f"lama eksekusi: {lama_waktu: .2f}s")



if __name__ == "__main__":
    main()