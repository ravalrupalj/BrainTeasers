#Upper or Lower Case
#Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case, whichever takes the fewest number of steps. A step consists of changing one character from lower to upper case, or vice versa.
#Return 0 if empty string.
#Return 0 if the string is already entirely in one case.
#Only alphabetic characters.
#Input has no spaces.
def steps_to_convert(txt):
    if txt.islower() or txt.isupper() or len(txt)==0:
        return 0
    else:
        count=0
        t=0
        for i in txt:
            if i.isupper():
                count=count+1
            else:
                t=t+1
        return min(count,t)





print((steps_to_convert('')))
#0
print(steps_to_convert("abC"))
#➞ 1
# "abC" converted to "abc" in 1 step
print(steps_to_convert("abCBA"))
#➞ 2
# "abCBA" converted to "ABCBA" in 2 steps
print(steps_to_convert("aba"))
#➞ 0
print(steps_to_convert("abaCCC"))
#➞ 3

