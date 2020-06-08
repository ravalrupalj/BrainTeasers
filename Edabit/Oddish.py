#Oddish vs. Evenish
#Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

#For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.
def oddish_or_evenish(num):
    string=str(num)
    count=0
    for i in string:
        count=count+int(i)
    if count%2==0:
        return 'Evenish'
    else:
        return 'Oddish'

print(oddish_or_evenish(43) )
#➞ "Oddish"

print(oddish_or_evenish(373))
#➞ "Oddish"

print(oddish_or_evenish(4433))
#➞ "Evenish"
