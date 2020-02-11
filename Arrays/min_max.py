def min_max(arr):
    min = arr[0]
    max = arr[1]

    left = 2
    while left < len(arr):
        if arr[left] > max:
            max = arr[left]
        elif arr[left] < min:
            min = arr[left]
        left += 1
    return [min, max]

test_array = [-1000, 11, 445, -1, 330, 3000]
result = min_max(test_array)
print(result)
