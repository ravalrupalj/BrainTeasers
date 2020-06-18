#1299. Replace Elements with Greatest Element on Right Side

def replaceElements(arr):
    final_l=[]
    for i in range(0,len(arr)-1):
        posi=arr[i]
        l=[]
        for j in range(i+1,len(arr)):
            l.append(arr[j])
        maximum=max(l)
        final_l.append(maximum)
    final_l.append(-1)
    return final_l



print(replaceElements([17,18,5,4,6,1]))