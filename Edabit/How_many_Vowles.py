#How Many Vowels?
#Create a function that takes a string and returns the number (count) of vowels contained within it.
#a, e, i, o, u are considered vowels (not y).
#All test cases are one word and only contain letters.
def count_vowels(txt):
    count=0
    t=txt.lower()
    for i in txt:
        if i in ['a','e','o','i','u']:
            count=count+1
    return count


print(count_vowels("Celebration"))
#➞ 5
print(count_vowels("Palm"))
#➞ 1
print(count_vowels("Prediction"))
#➞ 4
