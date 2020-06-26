#Encoded String Parse
#Create a function which takes in an encoded string and returns a dictionary according to the following example:
import re
def parse_code(string):
    first, second, _id = re.split('0+', string)
    return {'first_name': first, 'last_name': second, 'id': _id}
print(parse_code("John000Doe000123") )
#➞ { "first_name": "John", "last_name": "Doe","id": "123"}

print(parse_code("michael0smith004331"))
#➞ { "first_name": "michael","last_name": "smith","id": "4331"}

print(parse_code("Thomas00LEE0000043"))
#➞ {"first_name": "Thomas","last_name": "LEE", "id": "43"}
#Notes
#The string will always be in the same format: first name, last name and id with zeros between them.
#id numbers will not contain any zeros.
#Bonus: Try solving this using RegEx.