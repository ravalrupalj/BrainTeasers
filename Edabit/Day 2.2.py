#Say "Hello" Say "Bye"
#Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.
#say_hello_bye("alon", 1) ➞ "Hello Alon"
#say_hello_bye("Tomi", 0) ➞ "Bye Tomi"
#say_hello_bye("jose", 0) ➞ "Bye Jose"
#Notes
#The name you return must be capitalized.

def say_hello_bye(name, num):
    if num==1:
        return 'Hello '+name.capitalize()
    else:
        return 'Bye '+name.capitalize()



print(say_hello_bye("alon", 1) )
print(say_hello_bye("Tomi", 0) )
print(say_hello_bye("jose", 0))