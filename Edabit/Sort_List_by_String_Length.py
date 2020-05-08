#Sort a List by String Length
#Create a function that takes a list of strings and return a list, sorted from shortest to longest.
#All test cases contain lists with strings of different lengths, so you won't have to deal with multiple strings of the same length.
def sort_by_length(lst):
    t= sorted(lst,key=len)
    return t
print(sort_by_length(["Google", "Apple", "Microsoft"]))
#➞ ["Apple", "Google", "Microsoft"]
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
#➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
print(sort_by_length(["Turing", "Einstein", "Jung"]))
#➞ ["Jung", "Turing", "Einstein"]

