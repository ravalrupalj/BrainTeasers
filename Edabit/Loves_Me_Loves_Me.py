#Loves Me, Loves Me Not...
#"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

#Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
def loves_me(num):
    l=['Loves me','Loves me not']
    final_l=[]
    add=l[0]
    for i in range(0,num):
        final_l.append(add)
        if final_l[-1]==l[0]:
            add=l[1]
        else:
            add=l[0]
    final_l[-1]=final_l[-1].upper()
    return ', '.join(final_l)
print(loves_me(3))
#➞ "Loves me, Loves me not, LOVES ME"

print(loves_me(6) )
#➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

print(loves_me(1))
#➞ "LOVES ME"
#Notes
#Remember to return a string.
#he first phrase is always "Loves me".