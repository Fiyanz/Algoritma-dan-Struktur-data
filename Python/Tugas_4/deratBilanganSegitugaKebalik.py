def calculate_triangle_sum(n):
    total_sum = 0
    current_num = n
    while current_num > 0:
        total_sum += current_num
        current_num -= 2
    return total_sum

def main():
    base_number = 10
    total = 0
    for i in range(base_number, 0, -2):
        total += calculate_triangle_sum(i)
        print(' + '.join(str(x) for x in range(base_number, i - 2, -2)), '=', calculate_triangle_sum(i))
    print('----------')
    print("Hasil total:", total)

if __name__ == "__main__":
    main()