#Factor Tractor
#Write a function to find all the prime factors of a given integer. The function must return a list containing all the prime factors, sorted in ascending order. Remember that 1 is neither prime nor composite and should not be included in your output list.
def prime_factorize(num):
    i=1
    l=[]
    while num!=1:
        i = i + 1
        if num%i==0:
            num=num/i
            l.append(i)
            i=1

    return l
print(prime_factorize(25) )
#➞ [5, 5]

print(prime_factorize(19))
#➞ [19]

print(prime_factorize(77) )
#➞ [7, 11]
#Notes
#Output list must be sorted in ascending order.
#The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.

