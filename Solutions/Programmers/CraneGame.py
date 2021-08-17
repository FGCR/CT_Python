def solution(board, moves):
    answer = 0

    # Not Q, but Stack(Actually...)
    board_Qs = list(list())
    for i in range(len(board)):
        board_Qs.append(list())

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 0:
                board_Qs[col].append(board[row][col])

    basket_Q = list()

    for move in moves:
        # 1. Should Pop First
        if len(board_Qs[move - 1]) > 0:
            Popped = board_Qs[move - 1].pop(0)
            # Same as Popped
            if basket_Q and Popped == basket_Q[-1]:
                basket_Q.pop()
                answer += 2
            else:
                basket_Q.append(Popped)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))