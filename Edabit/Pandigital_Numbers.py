#Pandigital Numbers
#A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.
def is_pandigital(num):
    string=str(num)
    l='0123456789'
    for i in l:
        if i not in string:
            return False
    return True

print(is_pandigital(98140723568910))
#➞ True
print(is_pandigital(90864523148909))
#➞ False
# 7 is missing.
print(is_pandigital(112233445566778899))
#➞ False
#Notes
#Think about the properties of a pandigital number when all duplicates are removed.