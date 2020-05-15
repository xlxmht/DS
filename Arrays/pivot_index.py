# Function to find index where sum of left side and right side of array is equal
# Time Complexity - O(n), Space Complexity - O(1)


def pivot_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    current_index = 0
    while current_index < len(arr):
        if left_sum == (total_sum - left_sum - arr[current_index]):
            return current_index
        left_sum += arr[current_index]
        current_index += 1


input_array = [1, 4, 3, 8, 2, 6]
result = pivot_index(input_array)
print(result)
