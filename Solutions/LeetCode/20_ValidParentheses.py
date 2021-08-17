import collections

def isValidParentheses(s):
    ParenthesesDict = {']':'[','}':'{',')':'('}

    Paren_Stack = collections.deque()

    for schar in s:
        if schar in ParenthesesDict:
            #1) if Paren Stack is empty, Not Valid Parentheses
            #2) if char and stack popped is not equal, Not Valid Parentheses
            if (not Paren_Stack) or Paren_Stack.pop() != ParenthesesDict[schar]:
                return False
        else:
            Paren_Stack.append(schar)

    #Stack is not empty = Not Valid
    if Paren_Stack:
        return False

    return True

print(isValidParentheses("((({})))"))