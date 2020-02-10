def bubble_sort(arr):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1, arr)
                is_swapped = True
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


input_array = [8, 5, 2, 9, 5, 6, 3]
# input_array = [8, 5, 2]
sorted_array = bubble_sort(input_array)
print(sorted_array)
