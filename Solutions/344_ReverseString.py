def ReverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()

def ReverseString_Swapping(s):
    """
    Do not return anything, modify s in-place instead.
    """
    for index in range(len(s) // 2):
        s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]