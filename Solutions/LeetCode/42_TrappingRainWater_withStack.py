from typing import List

def trap(heights: List[int]) -> int:
    h_stk = list()
    vol = 0

    for i in range(len(heights)):
        #현재 index의 높이가 stack최상단보다 크면
        #즉, heights[i]가 더 작거나, 같아질 때 까지 stack에서 뺀다
        while h_stk and heights[i] > heights[h_stk[-1]]:
            #Stack최상단을 pop하고 기록
            top = h_stk.pop()

            #Stack이 비어있으면 그만한다.
            #현재 stk의 최상단이 제일 긴 녀석이 된다.
            if not h_stk:
                break

            #거리는 현재 index에서 다음 stack최상단과 1을 뺀 값
            distance = i - h_stk[-1] - 1
            waters = min(heights[i], heights[h_stk[-1]]) - heights[top]

            vol += distance * waters

        h_stk.append(i)
    return vol
print(trap([2,1,0,0,0,2,1]))
