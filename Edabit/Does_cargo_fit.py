#Does the Cargo Fit? (Part 2)
#A ship has to transport cargo from one place to another, while picking up cargo along the way. Given the total amount of cargo and the types of cargo holds in the ship as lists, create a function that returns True if each weight of cargo can fit in one hold, and False if it can't.
#"S" means 50 cargo space.
#"M" means 100 cargo space.
#"L" means 200 cargo space.
def will_fit(holds, cargo):
    d={'S':50,'M':100,'L':200}
    for i,j in zip(holds,cargo):
        if d[i]<j:
            return False
    return True

print(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) )
#➞ True

print(will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) )
#➞ False

print(will_fit(["L", "L", "M"], [56, 62, 84, 90]))
#➞ True
