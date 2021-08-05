def TrappingRainWater(heights):
    if len(heights) <= 2:
        return 0

    leftptr = 0
    rightptr = len(heights) - 1

    max_leftheight = heights[leftptr]
    max_rightheight = heights[rightptr]

    water_amount = 0

    while leftptr < rightptr:
        max_leftheight = max(heights[leftptr], max_leftheight)
        max_rightheight = max(heights[rightptr], max_rightheight)

        if max_leftheight > max_rightheight:
            water_amount += max_rightheight - heights[rightptr]
            rightptr -= 1
        else :
            water_amount += max_leftheight - heights[leftptr]
            leftptr += 1

    return water_amount

print(TrappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))