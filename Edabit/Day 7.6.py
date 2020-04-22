#Hitting the Jackpot
#Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.
#test_jackpot(["@", "@", "@", "@"]) ➞ True
#test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
#test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
#test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
#test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False
def test_jackpot(result):
    return len(set(result)) == 1
print(test_jackpot(["@", "@", "@", "@"]))
print(test_jackpot(["abc", "abc", "abc", "abc"]))
print(test_jackpot(["SS", "SS", "SS", "SS"]))
print(test_jackpot(["&&", "&", "&&&", "&&&&"]))
print(test_jackpot(["SS", "SS", "SS", "Ss"]))