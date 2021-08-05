def ArrayPartition(vals):
    #min(a,b) pair total sum's Largest.
    sorted_vals = sorted(vals)

    Total = 0

    for i in range(len(sorted_vals) - 1, -1, -2):
        Total += min(sorted_vals[i],sorted_vals[i-1])

    return Total

print(ArrayPartition([1,4,3,2]))