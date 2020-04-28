#Total Number of Unique Characters
#Given two strings, create a function that returns the total number of unique characters from the combined string.
#Examples
#count_unique("apple", "play") ➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
#count_unique("sore", "zebra") ➞ 7
#count_unique("a", "soup") ➞ 5
#Notes
#Each word will contain at least one letter.
#All words will be lower cased.
def count_unique(s1, s2):
	t=s1+s2
	return len(set(t))
print(count_unique("apple", "play"))
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
print(count_unique("sore", "zebra"))
print(count_unique("a", "soup"))