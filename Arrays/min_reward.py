# WIP
def min_reward(array):
    length = len(array)
    reward = [1] * length
    for index in range(1, length):
        if array[index] < array[index - 1]:
            continue
        else:
            reward[index] = reward[index - 1] + 1
    for index in reversed(range(0, length - 1)):
        if array[index] > array[index + 1]:
            continue
        else:
            pass


test_array = [8, 4, 2, 1, 3, 6, 7, 9, 5]
min_reward(test_array)
