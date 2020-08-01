# Select first element as Pivot
def quick_sort(array):
    quicksort_helper(array, 0, len(array) - 1)
    return array


def quicksort_helper(array, start, end):
    if start >= end:
        return
    pivot_idx = start
    left_idx = start + 1
    right_idx = end
    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] > array[right_idx]:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]
    isLeftSubArraySmaller = right_idx - 1 - start < end - (right_idx + 1)
    if isLeftSubArraySmaller:
        quicksort_helper(array, start, right_idx - 1)
        quicksort_helper(array, right_idx + 1, end)
    else:
        quicksort_helper(array, right_idx + 1, end)
        quicksort_helper(array, start, right_idx - 1)


test_array = [8, 5, 2, 9, 5, 6, 3]
sorted_array = quick_sort(test_array)
print(sorted_array)