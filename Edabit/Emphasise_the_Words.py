#Emphasise the Words
#The challenge is to recreate the functionality of the title() method into a function called emphasise(). The title() method capitalises the first letter of every word.
#You won't run into any issues when dealing with numbers in strings.
#Please don't use the title() method directly :(
def emphasise(string):
    r=''
    for i in string.split():
        t=(i[0].upper())+(i[1:].lower())+' '
        r=r+t
    return r.rstrip()
print(emphasise("hello world"))
#➞ "Hello World"
print(emphasise("GOOD MORNING") )
#➞ "Good Morning"
print(emphasise("99 red balloons!"))
#➞ "99 Red Balloons!"

