#Basic E-Mail Validation
#Create a function that accepts a string, checks if it's a valid email address and returns either True or False, depending on the evaluation.
#The string must contain an @ character.
#The string must contain a . character.
#The @ must have at least one character in front of it.
#e.g. "e@edabit.com" is valid while "@edabit.com" is invalid.
#The . and the @ must be in the appropriate places.
#e.g. "hello.email@com" is invalid while "john.smith@email.com" is valid.
#If the string passes these tests, it's considered a valid email address.
#Notes
#Check the Tests tab to see exactly what's being evaluated.
#You can solve this challenge with RegEx, but it's intended to be solved with logic.
#Solutions using RegEx will be accepted but frowned upon :(
import re
def validate_email(txt):
    if re.match(r'.+\@.+(\.com)$',txt):
        return True
    else:
        return False
#OR
# if (re.search(r'[\w.-]+@[\w.-]+[.]+.\w+', st)) : return True
 # return False
#OR
 #   if '.com' in txt:
 #       if '@' in txt:
 #           if not txt.startswith('@'):
 #               return True

 #   return False

print(validate_email('www.email.com'))
#False
print(validate_email("@gmail.com"))
#➞ False
print(validate_email("hello.gmail@com"))
#➞ False
print(validate_email("gmail"))
#➞ False
print(validate_email("hello@gmail"))
#➞ False
print(validate_email("hello@edabit.com"))
#➞ True
