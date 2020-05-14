#Matchstick Houses
#This challenge will help you interpret mathematical relationships both algebraically and geometrically.
#Matchstick Houses, Steps 1, 2 and 3
#Create a function that takes a number (step) as an argument and returns the amount of matchsticks in that step. See step 1, 2 and 3 in the image above.
#Step 0 returns 0 matchsticks.
#The input (step) will always be a non-negative integer.
def match_houses(step):
    l=[]
    if step==0:
        return 0
    for i in range(1,600,5):
        l.append(i)
    return l[step]

print(match_houses(1))
#➞ 6
print(match_houses(0))
#➞ 0
print(match_houses(4))
#➞ 21
print(match_houses(87))
#➞ 436
