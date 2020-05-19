#Split a String Based on Vowels and Consonants
#Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
import re
def split(string):

    l=['a','e','i','o','u']
    s=''
    t=''
    for i in string:
        if i in l:
            s=s+i
        else:
             t=t+i
    return s+t
            

print(split("abcde"))
#➞ "aebcd"

print(split("Hello!") )
#➞ "eoHll!"

print(split("What's the time?") )
#➞ "aeieWht's th tm?"

#Vowels are a, e, i, o, u.
#Define a separate is_vowel() function for easier to read code (recommendation).