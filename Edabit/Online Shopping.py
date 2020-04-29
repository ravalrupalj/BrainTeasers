#Online Shopping
#Create a function that determines whether a shopping order is eligible for free shipping. An order is eligible for free shipping if the total cost of items purchased exceeds $50.00.
#Ignore tax or additional fees when calculating the total order cost.
def free_shipping(order):
    return sum(order.values())>50

print(free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 }) )
#False
print(free_shipping({ "Flatscreen TV": 399.99 }))
#True
print(free_shipping({ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }))
#True