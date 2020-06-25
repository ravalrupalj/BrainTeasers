def check(d1, d2, k):
    d1=  { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
    d2 = { "people": 12, "sun": "star", "book": "bad" }
    if k in d1.keys() and k in d2.keys():
        if d1[k]==d2[k]:
            return True
        elif d1[k]!=d2[k]:
            return 'Not the same'
    else:
         return 'One\'s empty'
print(check('dict_first', 'dict_second', "horde") )
#➞ "One"s empty"

print(check('dict_first', 'dict_second', "people") )
#➞ True

print(check('dict_first', 'dict_second', "sun") )
#➞ "Not the same"