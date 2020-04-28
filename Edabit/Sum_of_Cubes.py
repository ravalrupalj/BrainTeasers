#Sum of Cubes
#Create a function that takes a list of numbers and returns the sum of its cubes.
#Examples
#sum_of_cubes([1, 5, 9]) ➞ 855
# Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855
#sum_of_cubes([3, 4, 5]) ➞ 216
#sum_of_cubes([2]) ➞ 8
#sum_of_cubes([]) ➞ 0
##If given an empty list, return 0.
def sum_of_cubes(nums):
    count=0
    for i in nums:
        t=i**3
        count=count+t
    return count
print(sum_of_cubes([1, 5, 9]))
# Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855
print(sum_of_cubes([3, 4, 5]) )
print(sum_of_cubes([2]))
print(sum_of_cubes([]))