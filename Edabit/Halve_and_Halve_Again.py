#Halve and Halve Again
#Given two integers a and b, return how many times a can be halved while still being greater than b.
#Integer a can be halved at least once.
def halve_count(a, b):
    count=0
    while a>b:
        a=a/2
        count=count+1
    return count-1


print(halve_count(1324, 98))
#➞ 3
# (1324 -> 662 -> 331 -> 165.5)
print(halve_count(624, 8))
#➞ 6
# (624 -> 312 -> 156 -> 78 -> 39 -> 19.5 -> 9.75)
print(halve_count(1000, 3))
#➞ 8
# (1000 -> 500 -> 250 -> 125 -> 62.5 -> 31.25 -> 15.625 -> 7.8125 -> 3.90625)


