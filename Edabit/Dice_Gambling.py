#Dice Gambling
#Create a function that takes a list consisting of dice rolls from 1-6. Return the sum of your rolls with the following conditions:

#If a 1 is rolled, that is bad luck. The next roll counts as 0.
#If a 6 is rolled, that is good luck. The next roll is multiplied by 2.
#The list length will always be 3 or higher.
#Notes
#Even if a 6 is rolled after a 1, 6 isn't summed but the 6's "effect" still takes place.
def rolls(lst):
    count = lst[0]
    for index in range(1, len(lst)):
        if lst[index-1] == 1:
            count = count + 0

        elif lst[index-1] == 6:
            count = count + (lst[index]*2)
        else:
            count=count+lst[index]
    return count
#OR
 #   total=lst[0]
 #   for index in range(1,len(lst)):
 #       if lst[index-1]==1:
 #           total=total+0
  #      elif lst[index-1]==6:
  #          total=total+(lst[index]*2)
  #      else:
  #          total=total+lst[index]
  #  return total



print(rolls([1, 2, 3]) )
#➞ 4
# The second roll, 2, counts as 0 as a result of rolling 1.
print(rolls([2, 6, 2, 5]) )
#➞ 17
# The 2 following the 6 was multiplied by 2.
print(rolls([6, 1, 1]) )
#➞ 8
# The first roll makes the second roll worth 2, but the
# second roll was still 1 so the third roll doesn't count.
