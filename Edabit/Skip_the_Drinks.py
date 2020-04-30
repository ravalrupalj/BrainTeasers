#Skip the Drinks with Too Much Sugar
#The function skip_the_sugar() takes in a list of drinks. Make sure the function only returns a list of drinks with no sugar in it or a little bit of sugar.
#Drinks that contain too much sugar (in this challenge) are:
#Cola
#Fanta
#The skip_the_sugar() function returns a list of strings. All drink names are in lowercase.
def skip_the_sugar(drinks):
    return [i for i in drinks if i!='cola'and i!='fanta']

print(skip_the_sugar(["fanta", "cola", "water"]) )
#[water]
print(skip_the_sugar(["fanta", "cola"]) )
#[]
print(skip_the_sugar(["lemonade", "beer", "water"]))
# ["lemonade", "beer", "water"]