# Time Complexity: O(n)
def move_element_to_end(input_array, target):
    left = 0
    right = len(input_array) - 1
    while left < right:
        while left < right and input_array[left] == input_array[right]:
            right -= 1
        if input_array[left] == target:
            input_array[left], input_array[right] = input_array[right], input_array[left]
            left += 1
        else:
            left += 1

    return input_array


def move_element_to_end_revised(input_array, target):
    left = 0
    right = len(input_array) - 1
    while left < right:
        print(input_array)
        while left < right and input_array[right] == target:
            right -= 1
        if input_array[left] == target:
            input_array[left], input_array[right] = input_array[right], input_array[left]
        left += 1

    return input_array


def move_element_to_end_sequence(nums, target):
    left = right = 0
    while right < len(nums):
        if nums[left] == target and nums[right] != target:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] != target:
            left += 1
        right += 1
    return nums


arr = [2, 1, 2, 2, 3, 2, 4, 6, 2, 2]
# arr = [2, 1, 2, 3, 4, 2, 2, 5, 6, 7, 8, 1, 1, 4, 5, 6]
# arr = [3, 3, 3, 3, 3]
# arr = [0, 1, 0, 3, 12]
target = 2
result = move_element_to_end_sequence(arr, target)

print("============", result)
