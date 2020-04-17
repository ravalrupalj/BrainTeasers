#He tells you that if you multiply the height for the square of the radius and multiply the result for the mathematical constant π (Pi), you will obtain the total volume of the pizza. Implement a function that returns the volume of the pizza as a whole number, rounding it to the nearest integer (and rounding up for numbers with .5 as decimal part).
#vol_pizza(1, 1) ➞ 3
# (radius² x height x π) = 3.14159... rounded to the nearest integer.
#vol_pizza(7, 2) ➞ 308
#vol_pizza(10, 2.5) ➞ 785
import math

def vol_pizza(radius, height):
    t=(radius ** 2) * height *math.pi
    y=round(t,1)
    return round(y)

print(vol_pizza(1, 1))    # (radius² x height x π) = 3.14159... rounded to the nearest integer.
print(vol_pizza(7, 2))
print(vol_pizza(10, 2.5))
print(vol_pizza(15, 1.3))
