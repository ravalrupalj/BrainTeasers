#Recursion: Sum
#Write a function that finds the sum of the first n natural numbers. Make your function recursive.
#Check the Resources tab for info on recursion.
def sum_numbers(num):
    return sum(i for i in range(1,num+1))

print(sum_numbers(5) )
#➞ 15
#// 1 + 2 + 3 + 4 + 5 = 15

print(sum_numbers(1) )
#➞ 1

print(sum_numbers(12))
#➞ 78

