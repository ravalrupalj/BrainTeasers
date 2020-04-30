#Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
#Notes
#All of the letters in the input list will always be lowercase.
def mapping(letters):
    return {str(i): i.capitalize() for i in letters}


print(mapping(["p", "s"]))
#{ "p": "P", "s": "S" }

print(mapping(["a", "b", "c"]))
#{ "a": "A", "b": "B", "c": "C" }

print(mapping(["a", "v", "y", "z"]))
#{ "a": "A", "v": "V", "y": "Y", "z": "Z"}