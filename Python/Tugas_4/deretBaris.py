total = 0

for i in range(1, 11):
    bilangan_genap = i * 2
    total += bilangan_genap
    print(bilangan_genap, end=" ")
    if i != 10:
        print("+", end=" ")

print("=", total)
