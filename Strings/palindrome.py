def check_palindrome(string_name):
    flag = True
    left = 0
    right = len(string_name) - 1
    while left < right:
        if string_name[left] == string_name[right]:
            left += 1
            right -= 1
        else:
            flag = False
            break
    return flag


test_string = "abcdcba"
result = check_palindrome(test_string)
print(result)
