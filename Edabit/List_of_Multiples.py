#List of Multiples
#Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
#Notes
#Notice that num is also included in the returned list.
def list_of_multiples(num, length):
    l=[num]
    for i in range(length-1):
        t=l[-1]+num
        l.append(t)
    return l
print(list_of_multiples(7, 5) )
#➞ [7, 14, 21, 28, 35]

print(list_of_multiples(12, 10) )
#➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

print(list_of_multiples(17, 6) )
#➞ [17, 34, 51, 68, 85, 102]
