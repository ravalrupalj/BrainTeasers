#Percentage of Box Filled In
#Create a function that calculates what percentage of the box is filled in. Give your answer as a string percentage rounded to the nearest integer.
# Five elements out of sixteen spaces.

#Only "o" will fill the box and also "o" will not be found outside of the box.
#Don't focus on how much physical space an element takes up, pretend that each element occupies one whole unit (which you can judge according to the number of "#" on the sides).
def percent_filled(lst):
    count=0
    t=0
    for i in lst:
        if ' ' in i:
            count=count+i.count(' ')
            t=t+i.count('o')
    if count==0:
        return '100%'

    return str(round(100*t/(count+t)))+'%'
print(percent_filled(["###","#o#","###"]))
print(percent_filled([ "####", "#  #", "#o #", "####"]) )
#➞ "25%"
# One element out of four spaces.

print(percent_filled(["#######","#o oo #", "#######"]))
#➞ "60%"

# Three elements out of five spaces.

print(percent_filled([ "######","#ooo #","#oo  #", "#    #", "#    #","######"]) )
#➞ "31%"

