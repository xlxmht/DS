def group_anagram(strs):
    map = {}
    result = []
    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str in map:
            map[sorted_str].append(str)
        else:
            map[sorted_str] = [str]
    for i in map:
        result.append(map[i])
    return result

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = group_anagram(input)
print(res)