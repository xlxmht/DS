# O(N)
def largest_range(array):
    visited = {}
    longest_length = 0
    best_range = []
    for num in array:
        visited[num] = True
    for num in array:
        if not visited[num]:
            continue
        visited[num] = False
        current_length = 1
        left = num - 1
        right = num + 1
        while left in visited:
            current_length += 1
            left -= 1
        while right in visited:
            current_length += 1
            right += 1
        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]
    return best_range


test_array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# test_array = [4, 2, 1, 3, 6]
# test_array = [1]
result = largest_range(test_array)
print(result)


# Putting all elements in a hash map allows constant look up and to track if any element is visited or not.
