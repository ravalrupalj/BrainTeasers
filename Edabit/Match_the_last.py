#Match the Last Item
#Create a function that takes a list of items and checks if the last item matches the rest of the list.
def match_last_item(lst):
    s=''
    for i in lst[:-1]:
        s=s+str(i)
    return  s==lst[-1]
print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]) )
#➞ True
# The last item is the rest joined.
print(match_last_item([1, 1, 1, "11"]) )
#➞ False
# The last item should be "111".
print(match_last_item([8, "thunder", True, "8thunderTrue"]) )
#➞ True
#Notes
#The list is always filled with items.