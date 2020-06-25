#Write a function that returns all orders which cost strictly more than k. The function will look like:

#expensive_orders(d, k)
def expensive_orders(d, k):
    dic={}
    for key,value in d.items():
        if value>k:
            dic[key]=value
    return dic
print(expensive_orders({"a": 3000, "b": 200, "c": 1050}, 1000))
#➞ {"a": 3000, "c": 1050}

print(expensive_orders({"Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000}, 20000))
#➞ {"Gucci Fur": 24600}

print(expensive_orders({"Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5}, 40))
#➞ {}
