def ProductOfArrayExceptSelf(vals):
    result = list()

    mul = 1

    for i in range(len(vals)):
        result.append(mul)
        mul *= vals[i]

    #Reset Multiplier
    mul = 1

    for i in range(len(vals) - 1, -1, -1):
        result[i] *= mul
        mul *= vals[i]

    return result


print(ProductOfArrayExceptSelf([1,2,3,4]))