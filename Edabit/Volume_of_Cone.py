#Volume of a Cone
#Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone. See the resources tab for the formula.
#Volume of a Cone Image
#Return approximate answer by rounding the answer to the nearest hundredth.
#Use Python's math.pi constant or equivalent, don't fall for 3.14 ;-)
#If the cone has no volume, return 0.
import math
def cone_volume(h,r):
    return round((math.pi * (r ** 2) * h) / 3, 2)

print(cone_volume(3, 2) )
#➞ 12.57
print(cone_volume(15, 6) )
#➞ 565.49
print(cone_volume(18, 0) )
#➞ 0

