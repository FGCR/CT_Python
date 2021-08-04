def Two_Sum(vals, target):
    valdict = dict()

    for index, val in enumerate(vals):
        #if Duplicate, Overwrite
        #if answer contains 2 same vals (ex: 3 + 3 = 6), just filtered cause finding target starts at begin.
        valdict[val] = index

    for i in range(len(vals)):
        other_one = target - vals[i]
        if other_one in valdict:
            other_one_idx = valdict[other_one]
            if other_one_idx != i:
                return [i, valdict[other_one]]

    return None