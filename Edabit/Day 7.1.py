#Word Endings
#add_ending(["clever", "meek", "hurried", "nice"], "ly")➞ ["cleverly", "meekly", "hurriedly", "nicely"]
#add_ending(["new", "pander", "scoop"], "er")➞ ["newer", "panderer", "scooper"]
#add_ending(["bend", "sharpen", "mean"], "ing")➞ ["bending", "sharpening", "meaning"]

def add_ending(lst, ending):
    return [i+ending for i in lst]


print(add_ending(["clever", "meek", "hurried", "nice"],"ly"))
print(add_ending(["new", "pander", "scoop"], "er"))
print(add_ending(["bend", "sharpen", "mean"], "ing"))