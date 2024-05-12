
total = 0

for i in range(1, 6):
    for j in range(1, i + 1):
        bilangan_genap = j * 2
        total += bilangan_genap
        print(bilangan_genap, end=" ")
        if j != i:
            print("+", end=" ")
    
    print("=", total)

