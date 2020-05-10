#Remove Every Vowel from a String
#Create a function that takes a string and returns a new string with all vowels removed.
#"y" is not considered a vowel.
#Expect a valid string for all test cases.
def remove_vowels(string):
    new=[]
    vowels=('aeiouAEIOU')
    for i in string:
        if i not in vowels:
            new.append(i)
    return ''.join(new)
            #l=['a','e','i','o','u']
print(remove_vowels("I have never seen a thin person drinking Diet Coke."))
#➞ " hv nvr sn  thn prsn drnkng Dt Ck."

print(remove_vowels("We're gonna build a wall!"))
#➞ "W'r gnn bld  wll!"

print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!"))
#➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"

