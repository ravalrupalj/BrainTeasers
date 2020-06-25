#You will be given a dictionary with various products and their respective prices. Return a list of the products with a minimum price of 500 in descending order
def pricey_prod(d):
    l=[]
    val=[]
    for i in d.values():
        if i>=500:
            val.append(i)
    for each in sorted(val):
        for i,j in d.items():
            if j==each:
                l.append(i)
    return l[::-1]



print(pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}))
#➞ ["TV", "Computer"]

print(pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}) )
#➞ ["Bike1", "Bike3"]

print(pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}) )
#➞ []