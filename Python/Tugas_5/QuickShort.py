def partition(data, low, high):
    """Mempartisi data menjadi dua subarray berdasarkan pivot."""
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
          i += 1
          data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def quick_sort(data, low, high):
    """Mengurutkan data menggunakan Quick Sort."""
    if low < high:
        pivot_index = partition(data, low, high)
        quick_sort(data, low, pivot_index - 1)
        quick_sort(data, pivot_index + 1, high)
        return data
  

