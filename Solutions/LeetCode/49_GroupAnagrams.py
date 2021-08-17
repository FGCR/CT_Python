#애너그램 -> 같은 문자로 이루어져 있으나 순서가 다름
def GroupAnagrams(strs):
    AnaDict = dict()
    for string in strs:
        sorted_strarr = sorted(string)

        sorted_str = "".join(sorted_strarr)

        if sorted_str in AnaDict:
            AnaDict[sorted_str].append(string)
        else:
            AnaDict[sorted_str] = list()
            AnaDict[sorted_str].append(string)
    result = list()

    for key in AnaDict.keys():
        result.append(AnaDict[key])

    return result

print(GroupAnagrams(["eat","tea","tan","ate","nat","bat"]))