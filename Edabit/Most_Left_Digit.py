#Most Left Digit
#Write a function that takes a string as an argument and returns the left most digit in the string.
#Each string will have at least two numbers.
def left_digit(string):
    for i in string:
        if i.isdigit():
            return int(i)

print(left_digit("TrAdE2W1n95!"))
#➞ 2
print(left_digit("V3r1ta$"))
#➞ 3
print(left_digit("U//DertHe1nflu3nC3"))
#➞ 1
print(left_digit("J@v@5cR1PT") )
#➞ 5
