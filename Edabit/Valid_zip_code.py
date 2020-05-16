#Valid Zip Code
#Zip codes consist of 5 consecutive digits. Given a string, write a function to determine whether the input is a valid zip code. A valid zip code is as follows:

#Must only contain numbers (no non-digits allowed).
#Must not contain any spaces.
#Must not be greater than 5 digits in length.
import re
def is_valid(zip_code):
    c=re.findall(r"\D(\d{5})\D\Z", " " + zip_code + " ")
    #c=re.findall('[0-9]{5}',zip_code)
    if (c):
        return True
    else:
        return False
print(is_valid("59001"))
#➞ True
print(is_valid("853a7") )
#➞ False
print(is_valid("732 32") )
#➞ False
print(is_valid("788876"))
#False
print(is_valid("59238aa"))
#False




