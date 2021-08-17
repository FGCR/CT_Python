import collections

def DailyTemperatures(temps):
    days_to_upper = [0] * len(temps)

    temp_stack = collections.deque()

    for i, cur_temp in enumerate(temps):
        while temp_stack and (temps[temp_stack[-1]] < cur_temp):
            popped = temp_stack.pop()
            days_to_upper[popped] = i - popped
        temp_stack.append(i)

    return days_to_upper

print(DailyTemperatures([1,1,1,9,1,1,1,99]))