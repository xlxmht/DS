# Function takes sorted array and return sorted squared array
def sorted_squared(array):
    squared_sorted = []
    left = 0
    right = len(array) - 1
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            element_to_prepend = array[right]
            right -= 1
        else:
            element_to_prepend = array[left]
            left += 1
        squared_sorted = [element_to_prepend ** 2] + squared_sorted
    return squared_sorted


sample_array = [-6, -4, 1, 2, 3, 5]
result = sorted_squared(sample_array)
print(result)
