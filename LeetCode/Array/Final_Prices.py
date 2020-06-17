#1475. Final Prices With a Special Discount in a Shop
def finalPrices( prices):
    l=[]
    for i in range(0,len(prices)-1):
        if prices[i]>=prices[i+1]:
            discount=prices[i]-prices[i+1]
            l.append(discount)
        else:
            for j in range(i+2,len(prices)):
                if prices[i]>=prices[j]:
                    discount=prices[i]-prices[j]
                    l.append(discount)
                    break
            else:
                l.append(prices[i])

    l.append(prices[-1])
    return l
print(finalPrices([8,7,4,2,8,1,7,7,10,1]))
#[1,3,2,1,7,0,0,6,9,1]
print(finalPrices([8,4,6,2,3]))
#[4,2,4,2,3]
print(finalPrices([1,2,3,4,5]))
#[1,2,3,4,5]
print(finalPrices([10,1,1,6]))
#[9,0,1,6]

