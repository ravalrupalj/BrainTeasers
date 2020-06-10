#Round to Closest N
#Creates a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.
def round_number(num,n):
    step = 0
    while True:
        if not (num + step) % n:
            return num + step
        if not (num - step) % n:
            return num - step
        step += 1
print(round_number(12121212, 144))
#12121200
print(round_number(65, 10))
#➞ 70
print(round_number(46, 7))
#➞ 49
print(round_number(133, 14))
#➞ 140
#Notes
#n will always be a positive number.