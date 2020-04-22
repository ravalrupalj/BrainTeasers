#The Full Length of a Google
#Google's logo can be stretched depending on how many pages it lets you skip forward to.
#Google's logo can be stretched depending on how many pages it lets you skip forward to.
#googlify(10) ➞ "Goooooooooogle"
#googlify(23) ➞ "Gooooooooooooooooooooooooogle"
#googlify(2) ➞ "Google"
#googlify(-2) ➞ "invalid"
#If n is equal to or less than 1, return invalid.
def googlify(n):
    if n > 1: 
        return 'G'+('o'*n)+'gle'
    else:
        return 'invalid'

print(googlify(10))
print(googlify(23) )
print(googlify(2) )
print(googlify(-2) )