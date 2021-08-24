import copy

answer = 0

def solution(numbers, target):

    def internal(idx,curval):
        global answer
        if idx == len(numbers):
            if curval == target:
                answer += 1
            return

        internal(idx+1,curval + numbers[idx])
        internal(idx+1,curval - numbers[idx])

    internal(0,0)

    return answer

print(solution([1,2,3,4,5],15))