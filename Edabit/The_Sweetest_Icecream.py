#Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest icecream.
#Sweetness is calculated from the flavor and number of sprinkles. Each sprinkle has a sweetness value of 1, and the sweetness values for the flavors are as follows:
#Flavours	Sweetness Value
#Plain	         0
#Vanilla	     5
#ChocolateChip	 5
#Strawberry	     10
#Chocolate	     10
#You'll be given instance attributes in the order flavor, num_sprinkles.
#Notes
#Remember to only return the sweetness value.
class Icecream:
    def sweetest_icecream(lst):
        flavrs = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}
        list_values = []
        for obj in lst:
            obj_flavor = obj.flavor
            obj_flavor_value = flavrs[obj_flavor]
            total_Value = obj_flavor_value + obj.num_sprinkles
            list_values.append(total_Value)
        return max(list_values)

    #flavrs = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}
    #maxValue = 0
    #for obj in lst:
     #   obj_flavor = obj.flavor
     #   obj_flavor_value = flavrs[obj_flavor]
     #   total_Value = obj_flavor_value + obj.num_sprinkles
     #   if total_Value > maxValue:
      #      maxValue = total_Value
    #return maxValue

ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanillla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8
print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) )
# 23
print(sweetest_icecream([ice3, ice1]) )
# 23
print(sweetest_icecream([ice3, ice5]))
# 17
