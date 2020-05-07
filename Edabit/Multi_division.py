#Create a function, that will for a given a, b, c, do the following:
#1]Add a to itself b times.
#2]Check if the result is divisible by c.
#In the first step of the function, a doesn't always refer to the original a.
#"if the result is divisible by c", means that if you divide the result and c, you will get an integer (5, and not 4.5314).
#The second test is correct.
def abcmath(a, b, c):
    t=a
    for i in range(b):
        t=t+t
    if t%c==0:
        return True
    else:
        return False





print(abcmath(42, 5, 10))
#➞ False
# 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
# 1344 is not divisible by 10
print(abcmath(5, 2, 1))
#➞ True
print(abcmath(1, 2, 3))
#➞ False

