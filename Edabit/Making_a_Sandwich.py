#Making a Sandwich
#Given a list of ingredients i and a flavour f as input, create a function that returns the list, but with the elements bread around the selected ingredient.
def make_sandwich(i,f):
    total=i.count(f)
    place = i.index(f)
    if total==1:
        i.insert(place,'bread')
        i.insert(place+2,'bread')
        return i
    else:
        l=[]
        if len(set(i))==1:
            i.insert(place,'bread')
            i.insert(place + 2, 'bread')
            i.insert(place + 2, 'bread')
            i.append('bread')
        return i
#print(make_sandwich(["tuna", "ham", "tomato"], "ham") )
#➞ ["tuna", "bread", "ham", "bread", "tomato"]
#print(make_sandwich(["cheese", "lettuce"], "cheese") )
#➞ ["bread", "cheese", "bread", "lettuce"]
print(make_sandwich(["ham", "ham"], "ham") )
#➞ ["bread", "ham", "bread", "bread", "ham", "bread"]
#Notes
#You will always get valid inputs.
#Make two separate sandwiches if two of the same elements are next to each other (see example #3).