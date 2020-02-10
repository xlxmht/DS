# Encrypt string by shifting by given key
# Time - O(N)


def encrypt(string_name, key):
    new_str = ''
    key %= 26
    i = 0
    length = len(string_name)
    while i < length:
        code = ord(string_name[i])
        nlc = code + key
        if nlc <= 122:
            new_str += chr(nlc)
        else:
            new_str += chr((96 + nlc) % 122)

        i += 1
    return new_str


test_string = 'xyza'
print(encrypt(test_string, 54))
