#Regex Series: String Contains at Least One Digit
#Write a regular expression that matches a string if it contains at least one digit.
#This challenge is designed to use RegEx only.
import re
def has_digit(string):
    match=re.search(r'\d',string)
    if match:
        return True
    else:
        return False

print(has_digit("c8") )
#➞ True
print(has_digit("23cc4"))
#➞ True
print(has_digit("abwekz") )
#➞ False
print(has_digit("sdfkxi"))
#➞ False

