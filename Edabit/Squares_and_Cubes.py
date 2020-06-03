#Squares and Cubes
#Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.
#Notes
#Remember to return either True or False.
#All lists contain two positive numbers.
import math
def check_square_and_cube(lst):
    root=round(math.sqrt(lst[0]))
    cube=root**3
    return cube==lst[1]
print(check_square_and_cube([4, 8]))
#➞ True

print(check_square_and_cube([16, 48]))
#➞ False

print(check_square_and_cube([9, 27]))
#➞ True
