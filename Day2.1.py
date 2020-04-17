#Spaces Between Each Character
#Create a function that takes a string and returns a string with spaces in between all of the characters.
#space_me_out("space") ➞ "s p a c e"
#space_me_out("far out") ➞ "f a r  o u t"
#space_me_out("elongated musk") ➞ "e l o n g a t e d   m u s k"
#Notes
#Treat a space as its own character (i.e. leave three spaces between words).
def space_me_out(s):
    return ' '.join(s)

print(space_me_out("space") )
print(space_me_out("far out") )
print(space_me_out("elongated musk"))