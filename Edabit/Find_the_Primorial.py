#Find the Primorial
#A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.

#Create a function that returns the Primorial of a number.
def primorial(num):
    total = 1
    count=0
    i=1
    while count<num:
        i=i+1
        for j in range(2,i+1):
            if i%j==0 and i!=j:
                break
            elif i==j:
                total=total*i
                count=count+1
    return total

#print(primorial(1) )
#➞ 2
#print(primorial(2) )
#➞ 6
print(primorial(8) )
#➞ 9699690
print(primorial(3))
#30

