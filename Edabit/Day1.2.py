#Is it true?
#In this challenge you will be given a relation between two numbers, written as a string.
#Here are some example inputs: '2 = 2', '8 < 7', '5 = 13', '15 > 4'.
#Write a function that determines if the relation is True or False.
#'2 = 2' ➞ True

#'8 < 7' ➞ False

#'5 = 13' ➞ False

#'15 > 4' ➞ True

#Notes
#the tests will only have three types of relations: '=' relations, '>' relations, '<' relations.
#there are many approaches that work here, but the eval() function is particularly useful!



def is_it_true(relation):
    return eval(relation.replace('=','=='))


print(is_it_true('2 = 2'))

print(is_it_true('8 < 7'))

print(is_it_true('5 = 13'))

print(is_it_true('15 > 4'))


