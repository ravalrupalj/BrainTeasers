#Invert Keys and Values
#Write a function that inverts the keys and values of a dictionary.
def invert(dct):
    d={}
    for i,j in dct.items():
        d[j]=i
    return d
print(invert({ "z": "q", "w": "f" }))
#➞ { "q": "z", "f": "w" }

print(invert({ "a": 1, "b": 2, "c": 3 }))
#➞ { 1: "a", 2: "b", 3: "c" }

print(invert({ "zebra": "koala", "horse": "camel" }))
#➞ { "koala": "zebra", "camel": "horse" }
