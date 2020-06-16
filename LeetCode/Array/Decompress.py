#1313. Decompress Run-Length Encoded List

def decompressRLElist(nums):
    l=[]
    count=1
    for i in range(0,len(nums),2):
        for j in range(nums[i]):
            l.append(nums[count])
        count=count+2
    return l

print(decompressRLElist([1,2,3,4]))
print(decompressRLElist([1,1,2,3]))


