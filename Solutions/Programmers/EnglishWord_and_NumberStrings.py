def solution(s):
    answer = ""

    NumberDict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                  'eight': '8', 'nine': '9'}

    i = 0
    while i < len(s):
        if s[i].isnumeric():
            answer += s[i]
            i += 1
            continue
        # Length = 3
        if i < len(s) - 2:
            if s[i:i + 3] in NumberDict:
                answer += NumberDict[s[i:i + 3]]
                i += 3
                continue
        if i < len(s) - 3:
            if s[i:i + 4] in NumberDict:
                answer += NumberDict[s[i:i + 4]]
                i += 4
                continue
        if i < len(s) - 4:
            if s[i:i + 5] in NumberDict:
                answer += NumberDict[s[i:i + 5]]
                i += 5
                continue
        i += 1

    return int(answer)