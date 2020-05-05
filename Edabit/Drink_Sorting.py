#You will be given an list of drinks, with each drink being an dictionary with two properties: name and price. Create a function that has the drinks list as an argument and return the drinks dictionary sorted by price in ascending order.
#Assume that the following array of drink objects needs to be sorted:
from operator import itemgetter
def sort_drinks_by_price(drinks):
    return sorted(drinks, key=itemgetter('price'))
#OR return sorted(drinks, key=lambda x: x['price'])
drinks = [
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10}]
#The output of the sorted drinks object will be:


print(sort_drinks_by_price(drinks))
#➞ [{name: "lime", price: 10}, {name: "lemonade", price: 50}]
