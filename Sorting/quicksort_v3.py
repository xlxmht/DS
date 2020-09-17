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
    # print(array)
    while left_idx <= right_idx:
        # Swap if left and right element is not in proper place with respect to pivot element
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        # Increment left index if correctly positioned wrt pivot element
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        # Increment right index if correctly positioned wrt pivot element
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    # Swap right element with pivot element after exiting loop
    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]
    isLeftSubArraySmaller = (right_idx - 1 - start) < (end - (right_idx + 1))
    # Recursively perform
    if isLeftSubArraySmaller:
        quicksort_helper(array, start, right_idx - 1)
        quicksort_helper(array, right_idx + 1, end)
    else:
        quicksort_helper(array, right_idx + 1, end)
        quicksort_helper(array, start, right_idx - 1)


# test_array = [8, 5, 2, 9, 5, 6, 3]
test_array = [50, 23, 9, 18, 61, 32]
sorted_array = quick_sort(test_array)
print(sorted_array)