#1470. Shuffle the Array
def shuffle(num,n):
    l=[]
    length=round(len(num)/2)
    for i in range(0,length):
        l.append(num[i])
        t=i+n
        if len(num)>t:
            l.append(num[t])

    return l


print(shuffle([2,5,1,3,4,7],3)) # [2,3,5,4,1,7]
print(shuffle([1,2,3,4,4,3,2,1],4)) #[1,4,2,3,3,2,4,1]
print(shuffle([7,5,9,7,5,8,10,4,3,3,2,5,9,10],7))
# [7,4,5,3,9,3,7,2,5,5,8,9,10,10]