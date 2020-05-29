#Longest Daily Streak
#Create a function that takes a list of booleans that represent whether or not a player has logged into a game that day. Output the longest streak of consecutive logged in days.
#Notes
#Return your output as an integer.
#If a given list is all False, return 0 (see example #2).
def daily_streak(lst):
    l=[]
    count=0
    for i in lst:
        if i==True:
            t=count=count+1
            l.append(t)
        else:
            count=0
    if len(l)==0:
        return 0
    else:
        return max(l)
print(daily_streak([True, True, False, True]) )
#➞ 2

print(daily_streak([False, False, False]) )
#➞ 0

print(daily_streak([True, True, True, False, True, True]))
#➞ 3
