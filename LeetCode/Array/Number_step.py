#1342. Number of Steps to Reduce a Number to Zero
def numberOfSteps (num):
    count=0
    while num>0:
        if num%2==0:
            num=num/2
            count=count+1
        else:
            num=num-1
            count=count+1
    return count


print(numberOfSteps(14))
print(numberOfSteps(123))