#How Many "Prime Numbers" Are There?
#Create a function that finds how many prime numbers there are, up to the given integer.
def prime_numbers(num):
    count=0
    i=1
    while num:
        i=i+1
        for j in range(2,i+1):
            if j>num:
                return count
            elif i%j==0 and i!=j:
                break
            elif i==j:
                count=count+1
                break



print(prime_numbers(10))
#➞ 4
# 2, 3, 5 and 7
print(prime_numbers(20))
#➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19

print(prime_numbers(30))
#➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
