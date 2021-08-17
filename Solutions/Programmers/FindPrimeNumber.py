import copy
def solution(numbers):
    answer = 0

    # 1. Pick
    # 2. ChangeLoc
    ExistDict = {}

    def MakeNumber(Construction, LeftPicked: str):
        if Construction and isPrime(int(Construction)) and not (int(Construction) in ExistDict):
            ExistDict[int(Construction)] = True
        for i in range(len(LeftPicked)):
            Cloned_LeftPicked = copy.deepcopy(LeftPicked)
            Cloned_LeftPicked = Cloned_LeftPicked[:i] + Cloned_LeftPicked[i + 1:]
            MakeNumber(Construction + LeftPicked[i], Cloned_LeftPicked)

    PrimeDict = {0: False, 1: False}

    def isPrime(Number):
        if Number in PrimeDict:
            return PrimeDict[Number]
        for i in range(2, Number):
            if Number % i == 0:
                PrimeDict[Number] = False
                return False
        PrimeDict[Number] = True
        return True



    MakeNumber("",numbers)

    return len(ExistDict)

print(solution("011"))

