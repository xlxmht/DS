def binary_search(array, target):
    return search_helper(array, target, 0, len(array) - 1)


def search_helper(array, target, left, right):
    mid_point = (left + right) // 2
    potential_match = array[mid_point]
    if left > right:
        return -1
    elif target == potential_match:
        return mid_point
    elif target < potential_match:
        return search_helper(array, target, left, mid_point - 1)
    else:
        return search_helper(array, target, mid_point + 1, right)


# sample_array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
sample_array = [13, 15, 16, 16, 18, 19, 19, 25, 27, 27, 30, 33, 33, 36, 36, 38, 40, 43, 45, 49, 50, 51, 53, 56, 57, 59,
                59, 61, 64, 65, 67, 68, 72, 73, 75, 76, 78, 79, 80, 81, 83, 84, 85, 91, 94, 97, 101, 106]
print('Enter number to search: ')
try:
    num_to_search = int(input())
except Exception:
    print('ERROR: Not a valid number')
else:
    result = binary_search(sample_array, num_to_search)
    print('OUTPUT: ', result)
