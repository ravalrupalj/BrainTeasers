#Return the Index of All Capital Letters
#Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
#Return an empty list if no uppercase letters are found in the string.
#Special characters ($#@%) and numbers will be included in some test cases.
def index_of_caps(word):
    l=[]
    for i in word:
        if i.isupper():
            l.append(word.index(i))
    return l

print(index_of_caps("eDaBiT"))
#➞ [1, 3, 5]
print(index_of_caps("eQuINoX"))
#➞ [1, 3, 4, 6]
print(index_of_caps("determine"))
#➞ []
print(index_of_caps("STRIKE"))
#➞ [0, 1, 2, 3, 4, 5]
print(index_of_caps("sUn"))
#➞ [1]

