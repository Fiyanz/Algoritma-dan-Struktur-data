import statistics

list = [78, 89, 56, 72, 66, 43, 52, 32]
list.sort()

print(list)

# median 
rata = statistics.mean(list)
print(f"Rata Rata: {rata}")

# nilai tengah 
median = statistics.median(list)
print(f"Nilai Tengah: {median}")

# nilai yang seing muncul
modus = statistics.mode(list)
print(f"Nilai yang sering muncul: {modus}")