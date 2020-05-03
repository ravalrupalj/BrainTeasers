#Calculate the Total Price of Groceries
#Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. A grocery dictionary has a product, a quantity and a price, for example:
#Notes
#There might be a floating point precision problem in here...
def get_total_price(groceries):
    t=[]
    for i in groceries:
        values=i['quantity']*i['price']
        t.append(values)
    return round(sum(t),1)
#OR
#sum = 0
	#for obj in groceries:
	#	sum = sum +(obj["price"] * obj["quantity"])
	#return round(sum,1)


#{"product": "Milk","quantity": 1,"price": 1.50}
# 1 bottle of milk:
print(get_total_price([{ "product": "Milk", "quantity": 1, "price": 1.50 }]))
#➞ 1.5
# 1 bottle of milk & 1 box of cereals:
print(get_total_price([{ "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }]))
#➞ 4
# 3 bottles of milk:
print(get_total_price([{ "product": "Milk", "quantity": 3, "price": 1.50 }]))
#➞ 4.5
# Several groceries:
print(get_total_price([{"product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }]))
#➞ 10.4
# Some cheap candy:
print(get_total_price([{ "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }]))
#➞ 0.3
