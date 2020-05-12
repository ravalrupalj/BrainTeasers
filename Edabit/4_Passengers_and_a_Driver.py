#4 Passengers and a Driver
#A typical car can hold 4 passengers and 1 driver, overall allowing 5 people to travel around.
#Given n number of people, return how many cars are needed to seat everyone comfortably.
#It's likely that there'll be a few people left over and that some cars won't be filled to max capacity.
from math import ceil
def cars_needed(people):
    return ceil(people/5)
#OR
    if n == 0 :
        return 0
    elif n % 5 == 0 :
        return (n // 5)
    else :
        return (n // 5) + 1
print(cars_needed(5))
#➞ 1
print(cars_needed(11))
#➞ 3
print(cars_needed(0))
#➞ 0


