def subarray_sort(array):
    min = float("inf")
    max = float("-inf")
    for index in range(len(array)):
        if not _is_out_of_order(index, array):
            result = _set_min_max(index, min, max, array)
            min = result[0]
            max = result[1]
    return _find_place(min, max, array)


def _find_place(min, max, array):
    if min == float("inf"):
        return [-1, -1]
    left_sub_array_idx = 0
    right_sub_array_idx = len(array) - 1
    while min >= array[left_sub_array_idx]:
        left_sub_array_idx += 1
    while max <= array[right_sub_array_idx]:
        right_sub_array_idx -= 1
    return [left_sub_array_idx, right_sub_array_idx]


def _set_min_max(index, mn, mx, array):
    if array[index] >= mx:
        mx = array[index]
    elif array[index] <= mn:
        mn = array[index]
    return [mn, mx]


def _is_out_of_order(index, array):
    if index == 0:
        return array[index] < array[index + 1]
    elif index == len(array) - 1:
        return array[index] > array[index - 1]
    else:
        return array[index] > array[index - 1] and array[index] < array[index + 1]


# test_array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
test_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = subarray_sort(test_array)
print(result)
