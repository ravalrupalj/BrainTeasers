#One Button Messaging Device
#Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.
#Write a function that takes a string (the message) and returns the total number of times the button is pressed.
#Notes
#Ignore spaces.
def how_many_times(string):
    count=0
    for i in string:
        count=count+ord(i)-96
    return count

print(how_many_times("abde"))
#➞ 12
print(how_many_times("azy"))
#➞ 52
print(how_many_times("qudusayo") )
#➞ 123


