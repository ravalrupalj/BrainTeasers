#1389. Create Target Array in the Given Order
def createTargetArray(nums, index):
    l=[]
    for i in range(0,len(index)):
        l.insert(index[i],nums[i])
    return  l


print(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
#Output: [0,4,1,3,2]

print(createTargetArray([1,2,3,4,0],[0,1,2,3,0]))
#Output: [0,1,2,3,4]
