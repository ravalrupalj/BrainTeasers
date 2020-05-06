#Find the Odd Integer
#Create a function that takes a list and finds the integer which appears an odd number of times.
#There will always only be one integer that appears an odd number of times.
def find_odd(lst):
    for i in lst:
        for num in lst:
            if lst.count(num) % 2:
                return num

print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
#➞ -1
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
#➞ 5
print(find_odd([10]))
#➞ 10
print(find_odd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))
#10

