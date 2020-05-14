#Applying Discounts
#Create a function that applies a discount d to every number in the list.
#The discount is the percentage of the original price (i.e the discount of "75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
#There won't be any awkward decimal numbers, only 0.5 to deal with.
def get_discounts(nums, d):
    l=[]
    for i in nums:
        t=int(d.strip('%'))

        r=((i*t)/100)
        l.append(r)
    return l
print(get_discounts([2, 4, 6, 11], "50%") )
#➞ [1, 2, 3, 5.5]
print(get_discounts([10, 20, 40, 80], "75%") )
#➞ [7.5, 15, 30, 60]
print(get_discounts([100], "45%") )
#➞ [45]
