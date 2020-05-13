#Count Palindrome Numbers in a Range
#Create a function that returns the number of palindrome numbers in a specified range (inclusive).
#For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.
#Single-digit numbers are trivially palindrome numbers.
def count_palindromes(num1, num2):
    l=[]
    for i in range(num1,num2+1):
        a=str(i)
        b=a[::-1]
        if a==b:
            l.append(i)
    return len(l)



print(count_palindromes(1, 10))
#➞ 9
print(count_palindromes(555, 556))
#➞ 1
print(count_palindromes(878, 898))
#➞ 3
