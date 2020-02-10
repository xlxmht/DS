class InputModel:
    def __init__(self):
        # private members
        self._data = [12, 3, 1, 2, -6, 5, -8, 6]
        self._target = 10

    @property
    def set_data(self, array):
        self._data = array

    def set_target(self, target):
        self._target = target

    def get_data(self):
        return self._data

    def get_target(self):
        return self._target


def print_triplets(input_array, target):
    input_array.sort()
    pair = []
    for current in range(len(input_array) - 2):
        left = current + 1
        right = len(input_array) - 1
        while left < right:
            s = input_array[current] + input_array[left] + input_array[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                pair.append([input_array[current], input_array[left], input_array[right]])
                left += 1
                right -= 1

    return pair


obj = InputModel()
arr = obj.get_data()
obj.set_target(0)
target = obj.get_target()

result = print_triplets(arr, target)
print(result)
