#Letters Only
#Write a function that removes any non-letters from a string, returning a well-known film title.
#See the Resources section for more information on Python string methods.
def letters_only(string):
    l=[]
    for i in string:
        if i.isupper() or i.islower():
            l.append(i)
    return ''.join(l)

print(letters_only("R!=:~0o0./c&}9k`60=y") )
#➞ "Rocky"

print(letters_only("^,]%4B|@56a![0{2m>b1&4i4"))
#➞ "Bambi"

print(letters_only("^U)6$22>8p).") )
#➞ "Up"

