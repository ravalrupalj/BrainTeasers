#Censor Words from List
#Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
def censor_string(txt, lst, char):
    l=[]
    for each in lst:
        l.append(each.lower())
    s=''
    for i in txt.split():
        if i.lower() in l:
            for t in i:
                s=s+char
            s=s+' '
        else:
            s=s+i+' '
    return s.strip()

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
#➞ "----- is - Wednesday!"

print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
#"The *** jumped **** the moon.")

print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
#➞ "Why *** the ******* cross the ****?"
