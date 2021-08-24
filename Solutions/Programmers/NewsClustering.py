import copy
def solution(str1, str2):
    answer = 0

    def make_cons(string):
        result = dict()
        for i in range(len(string) - 1):
            if string[i].isalpha() and string[i + 1].isalpha():
                kw = string[i:i + 2]
                if kw in result:
                    result[kw] += 1
                else:
                    result[kw] = 1
        return result

    #Make J
    J1 = make_cons(str1.lower())
    J2 = make_cons(str2.lower())

    JUnion = copy.deepcopy(J1)
    for key in list(J2.keys()):
        #J2Key Exist in J1
        if key in J1:
            #Bigger is
            JUnion[key] = max(JUnion[key],J2[key])
        else:
            #Success J2 Key
            JUnion[key] = J2[key]
    JIntersection = copy.deepcopy(J1)
    for key in list(JIntersection.keys()):
        if not (key in J2):
            JIntersection[key] = 0
        else:
            JIntersection[key] = min(JIntersection[key], J2[key])

    #Count JUnion
    Unionval = 0
    IntersectionVal = 0
    for key in JUnion:
        Unionval += JUnion[key]
    for key in JIntersection:
        IntersectionVal += JIntersection[key]

    if(Unionval == IntersectionVal and Unionval == 0):
        return 65536
    return int((IntersectionVal / Unionval)*65536)

print(solution("aabbb", "aaabb"))