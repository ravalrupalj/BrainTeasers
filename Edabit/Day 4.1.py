#Volume of a Box
#Create a function that takes a dictionary argument sizes (contains width, length, height keys) and returns the volume of the box.
#volume_of_box({ "width": 2, "length": 5, "height": 1 }) ➞ 10
#volume_of_box({ "width": 4, "length": 2, "height": 2 }) ➞ 16
#volume_of_box({ "width": 2, "length": 3, "height": 5 }) ➞ 30

#Notes
#Don't forget to return the result.
#Remember that the values are in an object.
#Volume is length * width * height.

def volume_of_box(sizes):
    return sizes['width']*sizes['length']*sizes['height']

print(volume_of_box({"width": 2, "length": 5, "height": 1}))
print(volume_of_box({"width": 4, "length": 2, "height": 2}))
print(volume_of_box({"width": 2, "length": 3, "height": 5}))