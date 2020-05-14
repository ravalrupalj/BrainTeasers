#Multiply by Length
#Create a function to multiply all of the values in a list by the amount of values in the given list.
#All of the values given are numbers.
#All lists will have at least one element.
#Don't forget to return the result.
def MultiplyByLength(arr):
    length=len(arr)
    l=[]
    for i in arr:
        l.append(i*length)
    return l


print(MultiplyByLength([2, 3, 1, 0]))
#➞ [8, 12, 4, 0]
print(MultiplyByLength([4, 1, 1]))
#➞ ([12, 3, 3])
print(MultiplyByLength([1, 0, 3, 3, 7, 2, 1]))
#➞  [7, 0, 21, 21, 49, 14, 7]
print(MultiplyByLength([0]))
#➞ ([0])

#All of the values given are numbers.
#All lists will have at least one element.
#Don't forget to return the result.