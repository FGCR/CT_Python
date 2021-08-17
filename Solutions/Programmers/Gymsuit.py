def solution(n, lost, reserve):
    answer = 0

    Total_Cloth = [1] * n
    for rsv in reserve:
        Total_Cloth[rsv - 1] += 1
    for lst in lost:
        Total_Cloth[lst - 1] -= 1

    for i in range(0, n):
        if Total_Cloth[i] == 0:
            # Check Back
            if i < n - 1 and Total_Cloth[i + 1] > 1:
                Total_Cloth[i + 1] -= 1
                Total_Cloth[i] += 1
            # Check Front
            elif i > 0 and Total_Cloth[i - 1] > 1:
                Total_Cloth[i - 1] -= 1
                Total_Cloth[i] += 1

    for i in range(n):
        if Total_Cloth[i] >= 1:
            answer += 1

    return answer

print(solution(5,[2,4],[1,3,5]))