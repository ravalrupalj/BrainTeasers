def countNegatives(grid):
    count=0
    for i in grid:
        for j in i:
            if j<0:
                count=count+1
    return count


print(countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))