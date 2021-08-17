def solution(nums):
    answer = 0

    # A + B + C = Prime Number
    # A + B + C Solution = 2Pointer
    # Prime Number => ?

    PrimeDict = dict()

    def isPrime(Number):
        if Number in PrimeDict:
            return PrimeDict[Number]
        for i in range(2, Number):
            if Number % i == 0:
                return False
        PrimeDict[Number] = True
        return True

    for i in range(len(nums) - 2):
        # There's no case to Remove Duplicated Case
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer