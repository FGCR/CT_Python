def Three_Sum(vals):

    sorted_vals = sorted(vals)

    result = list()

    if(len(sorted_vals) < 3):
        return result

    for i in range(len(sorted_vals)):

        #Pass Duplicated Pivot
        if i > 0 and sorted_vals[i] == sorted_vals[i-1]:
            continue

        left = i + 1
        right = len(sorted_vals) - 1

        while left < right:
            sum = sorted_vals[i] + sorted_vals[left] + sorted_vals[right]

            if sum < 0:
                left += 1
                # Pass Duplicated Leftval
                while left < right and sorted_vals[left] == sorted_vals[left - 1]:
                    left += 1
            elif sum > 0:
                right -= 1
                # Pass Duplicated Rightval
                while left < right and sorted_vals[right] == sorted_vals[right + 1]:
                    right -= 1
            else:
                result.append([sorted_vals[i], sorted_vals[left], sorted_vals[right]])
                left += 1
                right -= 1
                while left < right and sorted_vals[left] == sorted_vals[left - 1]:
                    left += 1
                while left < right and sorted_vals[right] == sorted_vals[right + 1]:
                    right -= 1

    return result

print(Three_Sum([-1,0,1,2,-1,4]))