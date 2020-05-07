#Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
#There will be exactly one space between the first and last name.
#If you get stuck on a challenge, find help in the Resources tab.
#If you're really stuck, unlock solutions in the Solutions tab.
def name_shuffle(txt):
    t=txt.split()
    e=list(reversed(t))
    value=' '.join(e)
    return value
print(name_shuffle("Donald Trump") )
#➞ "Trump Donald"

print(name_shuffle("Rosie O'Donnell"))
#➞ "O'Donnell Rosie"

print(name_shuffle("Seymour Butts") )
#➞ "Butts Seymour"
