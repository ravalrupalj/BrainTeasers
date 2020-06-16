#1281. Subtract the Product and Sum of Digits of an Integer

def subtractProductAndSum(n):
    multi=1
    count=0
    for i in str(n):
        multi=multi*int(i)
        count=count+int(i)
    return multi-count


print(subtractProductAndSum(234))
#15