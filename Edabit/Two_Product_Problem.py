#Two Product Problem
#Create a function that takes an array arr and a number N and returns an array of two integers whose product is that of the number N.
def two_product(arr,n):
    for i in arr:
        for j in arr[1:]:
            if i*j==n:
                return [i,j]




print(two_product([1, 2, -1, 4, 5], 20))
#➞ [4, 5]

print(two_product([1, 2, 3, 4, 5], 10))
#➞ [2, 5]

print(two_product([100, 12, 4, 1, 2], 15))
#➞ None
#Note:
#Try doing this with 0(N) time complexity.
#No duplicates.
#In the array there can be multiple solutions so return the first match that you have found.
#If any doubts please refer to the comments section.