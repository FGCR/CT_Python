def Two_Sum(vals, target):
    valdict = dict()

    for index, val in enumerate(vals):
        #if Duplicate,
        valdict[val] = index

