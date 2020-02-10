# Print all pairs of given sum
class InputModel:
    def __init__(self):
        # private members
        self._data = [1, 2, 4, 11, 5, 6, -1, 9, 27]
        self._target = 10

    @property
    def set_data(self, array):
        self._data = array

    def set_target(self, target=10):
        self._target = target

    def get_data(self):
        return self._data

    def get_target(self):
        return self._target


obj = InputModel()
# obj.set_target(20)
# obj.set_data([4, 6])
arr = obj.get_data()
target = obj.get_target()


# Complexity: O(n^2)
# def print_pairs(input_array, target):
#     length = len(input_array)
#     res = []
#     for i in range(0, length):
#         for k in range(1, length - 1):
#             if input_array[i] + input_array[k] == target:
#                 res.append([input_array[i], input_array[k]])
#     return res
#
#

# Complexity: O(n Log(n))
# def print_pairs(input_array, target):
#     input_array.sort()
#     res = []
#     left = 0
#     right = len(input_array) - 1
#     while left < right:
#         current_sum = input_array[left] + input_array[right]
#         if current_sum == target:
#             res.append([input_array[left], input_array[right]])
#             right -= 1
#             left += 1
#         elif current_sum > target:
#             right -= 1
#         elif current_sum < target:
#             left += 1
#     return res


# Complexity: O(n)
def print_pairs(input_array, target):
    hash_map = {}
    aggregated_result = []
    for num in input_array:
        target_sum = target - num
        if target_sum in hash_map:
            aggregated_result.append([target_sum, num])
        else:
            hash_map[num] = 'true'
    return aggregated_result


result = print_pairs(arr, target)
print(result)
