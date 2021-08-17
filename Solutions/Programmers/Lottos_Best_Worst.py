def solution(lottos, win_nums):
    answer = []

    # Remove ALL Zeros
    ZeroCount = 0
    while 0 in lottos:
        lottos.remove(0)
        ZeroCount += 1

    win_num_dict = dict()
    for win_num in win_nums:
        win_num_dict[win_num] = True

    ATARI_Count = 0
    for lotto_num in lottos:
        if lotto_num in win_num_dict:
            ATARI_Count += 1

    # ATARI_Count, ATARI_Count + ZeroCount
    # ATARI_Count <= 1 -> 6
    # ATARI_Count == 2 -> 5
    # ATARI_Count == 3 -> 4
    # ATARI_Count == 4 -> 3
    # ATARI_Count == 5 -> 2
    # ATARI_Count == 6 -> 1
    Min = 7 - ATARI_Count
    if Min == 7:
        Min = 6
    Max = 7 - ATARI_Count - ZeroCount
    if Max == 7:
        Max = 6
    return [Max, Min]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))