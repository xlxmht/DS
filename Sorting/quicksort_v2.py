# 1. Select first element as Pivot
# 2. Partition in such a way that elements smaller than Pivot comes to left and largest
#       comes to right and return Pivot Index


def quick_sort(array, start, end):
    if start < end:
        pivot_idx = partition(array, start, end)
        quick_sort(array, start, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, end)


def partition(array, start_idx, end_idx):
    # pivot = array[start_idx]
    pivot_idx = start_idx
    left = right = start_idx + 1
    while right <= end_idx:
        if array[right] < array[pivot_idx]:
            swap(array, left, right)
            left += 1
        right += 1
    swap(array, pivot_idx, left - 1)
    return left - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# test_array = [1, 2, 3, 4, 5, 6, 7]
# test_array = [50, 23, 9, 18, 61, 32]
test_array = [8, 5, 2, 9, 5, 6, 3]
quick_sort(test_array, 0, len(test_array) - 1)
print(test_array)