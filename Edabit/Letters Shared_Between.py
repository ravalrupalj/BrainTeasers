#Letters Shared Between Two Words
#Create a function that returns the number of characters shared between two words.
def shared_letters(a,b):
    count=0
    for i in set(a):
       if i in b:
           count=count+b.count(i)
    return count
print(shared_letters("class", "last"))
 # 3
print(shared_letters("apple", "meaty"))
#➞ 2
# Since "ea" is shared between "apple" and "meaty".

print(shared_letters("fan", "forsook") )
#➞ 1

print(shared_letters("spout", "shout") )
#➞ 4
