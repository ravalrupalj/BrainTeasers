#Does the Cargo Fit? (Part 1)
#A ship has to transport cargo from one place to another, while picking up cargo along the way. Given the total amount of cargo and the types of cargo holds in the ship as lists, create a function that returns True if all the cargo can fit on the ship, and False if it can't.

#"S" means 50 cargo space.
#"M" means 100 cargo space.
#"L" means 200 cargo space.
#Notes
#Calculate the cargo as a whole, and not for each seperate cargo hold (see example #2).
def will_fit(holds, cargo):
    keys=['M','S','L']
    values=[100,50,200]
    dictionary=dict(zip(keys,values))
    for i,j in zip(holds,cargo):
        if dictionary[i]<j:
            return False
    return True
print(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) )
#➞ True
print(will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) )
#➞ False
print(will_fit(["L", "L", "M"], [56, 62, 84, 90]) )
#➞ True
