total = 0

for i in range(1, 20, 2):
    bilangan_genap = i 
    total += bilangan_genap
    print(bilangan_genap, end=" ")
    if i != 10:
        print("+", end=" ")

print("=", total)
