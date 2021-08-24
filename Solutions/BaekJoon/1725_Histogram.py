#This problem is as same as LeetCode #84
def largestRectangleArea(heights) -> int:
    h_stk = list()
    max_size = 0;

    for i in range(len(heights)):
        success_ptr = i;
        i_val = heights[i]

        while h_stk and h_stk[-1][1] > i_val:
            popped = h_stk.pop()

            w = i - popped[0]
            h = popped[1]

            max_size = max(max_size, w*h)
            success_ptr = popped[0]
        h_stk.append([success_ptr,i_val])

    while h_stk:
        popped = h_stk.pop()
        max_size = max(max_size, (len(heights) - popped[0]) * popped[1])

    return max_size
print(largestRectangleArea([3,3,2,3,3]))