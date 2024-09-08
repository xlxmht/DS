# Input: 99946
# Ouput: 9-9-946

def dash_insert(num):
  numArr = [x for x in str(num)]
  i = 1

  while i < len(numArr):
    idx = i
    curr_num = numArr[idx]
    last_num = numArr[idx - 1]

    if is_odd(curr_num) and is_odd(last_num):
      numArr[idx] = '-' + curr_num

    i += 1

  return ''.join(numArr)


def is_odd(num):
  return int(num) % 2 != 0


output = dash_insert(9994677889)
print(output)