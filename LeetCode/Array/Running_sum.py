#1480. Running Sum of 1d Array
def running_sum(num):
    l=[]
    count=0
    for i in num:
        count=count+i
        l.append(count)
    return l

print(running_sum([1,2,3,4]))
#[1,3,6,10]