def count_uppercase(lst):
	return sum(char.isupper() for letter in lst for char in letter)
print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]) )
#➞ 6

print(count_uppercase(["little", "lower", "down"]))
#➞ 0

print(count_uppercase(["EDAbit", "Educate", "Coding"]) )
#➞ 5