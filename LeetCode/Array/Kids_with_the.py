def kidsWithCandies(candies, extraCandies):
    l=[]
    new_list=[]
    for i in range(0,extraCandies+1):
        l.append(str(i))
    maximum=max(candies)
    for each in candies:
        remaining=maximum-each
        if str(remaining) in l:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list



print(kidsWithCandies([2,3,5,1,3],3))
#[true,true,true,false,true]