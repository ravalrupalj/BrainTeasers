#Is It a Triangle?
#Create a function that takes three numbers as arguments and returns True if it's a triangle and False if not.
#is_triangle(2, 3, 4) ➞ True
#is_triangle(3, 4, 5) ➞ True
#is_triangle(4, 3, 8) ➞ False
#Notes
#a, b and, c are the side lengths of the triangles.
#Test input will always be three positive numbers.

def is_triangle(a, b, c):
    return a+b>c and a+c>b and b+c>a

print(is_triangle(2, 3, 4))
print(is_triangle(3, 4, 5))
print(is_triangle(4, 3, 8))
print(is_triangle(2, 9, 5))