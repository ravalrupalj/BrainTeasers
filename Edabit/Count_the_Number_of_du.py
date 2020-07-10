#Count the Number of Duplicate Characters
#Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.
def duplicates(string):
    unique_string=set(string)
    total_space=string.count(' ')
    count=0
    for i in unique_string:
        if string.count(i)>1:
            count=count+1
    return count+total_space
print(duplicates("donald trump"))
 #1)
print(duplicates("The Quick Brown Fox Jumps Over the Lazy Dog"))
#14
print(duplicates("Hello World!") )
#➞ 3

print(duplicates("foobar"))
#➞ 1

print(duplicates("helicopter"))
#➞ 1

print(duplicates("birthday") )
#➞ 0
# If there are no duplicates, return 0
#Notes
#Make sure to only start counting the second time a character appears.