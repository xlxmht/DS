# Last array element is taken as Pivot Element
def quick_sort(array, start_idx, end_idx):
    if start_idx < end_idx:
        start = start_idx
        end = end_idx
        print(array)
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)


# Function returns index of pivot element after placing it to its correct position
def partition(array, start, end):
    pivot = array[end]
    temp = start - 1
    left = start
    while left <= end - 1:
        if array[left] < pivot:
            temp += 1
            _swap(temp, left, array)
        left += 1
    # print(array)
    _swap(temp + 1, end, array)
    return temp + 1


def _swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
    # return arr


# test_array = [10, 80, 30, 90, 40, 50, 70]
test_array = [8, 5, 2, 9, 5, 6, 3]
# test_array = [50, 23, 9, 18, 61, 32]
# test_array = [1, 2, 3, 4, 5, 6, 7]
start_index = 0
end_index = len(test_array) - 1
quick_sort(test_array, start_index, end_index)
print(test_array)
