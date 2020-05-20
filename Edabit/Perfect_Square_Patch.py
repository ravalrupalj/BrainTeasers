#Perfect Square Patch
#Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.
#n >= 0.
#If n == 0, return an empty list.
def square_patch(n):
    i=0
    l=[]
    while i<n:
        list=[]

        i =i+1
        t = 0
        while t<n:
            list.append(n)
            t=t+1
        l.append(list)
    return l

print(square_patch(3) )
#➞ [ [3, 3, 3], [3, 3, 3], [3, 3, 3]]
print(square_patch(5))
#➞ [ [5, 5, 5, 5, 5],[5, 5, 5, 5, 5],[5, 5, 5, 5, 5], [5, 5, 5, 5, 5],[5, 5, 5, 5, 5]]
print(square_patch(1))
#➞ [ [1]]
print(square_patch(0))
#➞ []

