def smallest_diff(array1, array2):
    sorted_one = sorted(array1)
    sorted_two = sorted(array2)
    idx_one = idx_two = 0
    pair = []
    smallest = float("inf")

    while idx_one < len(sorted_one) and idx_two < len(sorted_two):
        diff = abs(sorted_one[idx_one] - sorted_two[idx_two])
        first_num = sorted_one[idx_one]
        second_num = sorted_two[idx_two]
        if first_num < second_num:
            idx_one += 1
        elif first_num > second_num:
            idx_two += 1
        else:
            return [first_num, second_num]
        if diff < smallest:
            smallest = diff
            pair = [first_num, second_num]
    return pair


array1 = [-1, 5, 10, 20, 28, 27]
array2 = [26, 134, 135, 15, 17]
result = smallest_diff(array1, array2)
print(result)
