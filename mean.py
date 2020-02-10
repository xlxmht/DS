def get_sum(array):
    total = 0
    for i in range(0, len(array)):
        total = total + array[i]
    return total / len(array)


def get_sum_while(array):
    counter = 0
    total = 0
    while counter < len(array):
        total += array[counter]
        counter += 1
    return total / len(array)


def get_mean(num1, num2):
    return num1 / num2


oddSum = get_sum_while([1, 3, 5, 9])
evenSum = get_sum_while([2, 4, 6, 8])

mean = get_mean(oddSum, evenSum)
print(mean)
