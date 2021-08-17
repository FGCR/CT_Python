def solution(answers):
    answer = []

    Solvers = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    Solvers_Corr = [0] * len(Solvers)

    for i in range(len(answers)):
        for j in range(len(Solvers)):
            if (Solvers[j][i % len(Solvers[j])] == answers[i]):
                Solvers_Corr[j] += 1

    Best = 0
    for i in range(len(Solvers_Corr)):
        if Best < Solvers_Corr[i]:
            answer = [i+1]
            Best = Solvers_Corr[i]
        elif Best == Solvers_Corr[i]:
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))