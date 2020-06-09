#First Before Second Letter
#You are given three inputs: a string, one letter, and a second letter.

#Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.
def first_before_second(s, first, second):
    new_string = ''
    for i in s:
        if i == second:
            place = s.index(i)
            for char in s[place + 1:]:
                new_string = new_string + char
            return first not in new_string




print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#➞ True
# Every instance of "a" occurs before every instance of "j".
print(first_before_second("knaves knew about waterfalls", "k", "w"))
#➞  True
print(first_before_second("happy birthday", "a", "y"))
#➞ False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#➞ False
#Notes
#All strings will be in lower case.
#All strings will contain the first and second letters at least once.