#Find the Mean of All Digits
#Create a function that returns the mean of all digits.
#The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
#The mean will always be a integer.
def mean(num):
    count=0
    for i in str(num):
        count=count+int(i)
    return round(count/len(str(num)))
print(mean(42) )
#➞ 3
print(mean(12345))
#➞ 3
print(mean(666) )
#➞ 6

