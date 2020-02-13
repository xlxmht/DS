def subarray_sort(array):
    min_val = float("inf")
    max_val = float("-inf")
    for index in range(len(array)):
        if not _is_out_of_order(index, array):
            min_max_array = _set_min_max(index, min_val, max_val, array)
            min_val = min_max_array[0]
            max_val = min_max_array[1]
    return _find_place(min_val, max_val, array)


def _find_place(min_val, max_val, array):
    if min_val == float("inf"):
        return [-1, -1]
    left_sub_array_idx = 0
    right_sub_array_idx = len(array) - 1
    while min_val >= array[left_sub_array_idx]:
        left_sub_array_idx += 1
    while max_val <= array[right_sub_array_idx]:
        right_sub_array_idx -= 1
    return [left_sub_array_idx, right_sub_array_idx]


def _set_min_max(index, min_val, max_val, array):
    if array[index] >= max_val:
        max_val = array[index]
    elif array[index] <= min_val:
        min_val = array[index]
    return [min_val, max_val]


def _is_out_of_order(index, array):
    if index == 0:
        return array[index] < array[index + 1]
    elif index == len(array) - 1:
        return array[index] > array[index - 1]
    else:
        return array[index - 1] < array[index] < array[index + 1]


test_array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]  # Expected Output: [3, 9]
# test_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Expected Output: [-1, -1]
result = subarray_sort(test_array)
print(result)

# scan whole array and find elements that are not in order
# select min and max while marking those elements as out of order
# Iterate array again and find place(index) for min and max to be put in
# Hence finding resulting sub-array
