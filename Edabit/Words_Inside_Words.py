#Words Inside Words
#Words can be grouped together when one word can be found within another (e.g. eat is in heat and theater). Given a list of words, return a dictionary that groups together each word with a list of all other words that contain it. Each group of words should be returned in alphabetical order.
def word_groups(lst):
    d = {}
    for i in lst:
        x = [j for j in lst if i in j and i != j]
        if x:
            d[i] = sorted(x)
    return d
#    d={}
#    for i in lst:
#        for j in lst:
#            if i in j and i!=j:
#                d.setdefault(i, []).append(j)
#    d2 = {x: sorted(d[x]) for x in d.keys()}
#    return d2
print(word_groups(['cargo', 'are', 'bar', 'car', 'careful', 'embargo']))
#{'bar': ['embargo'], 'car': ['careful', 'cargo'], 'are': ['careful']})
print(word_groups(["grates", "rat", "rates", "rations"]))
#➞ {
#  "rates": ["grates"],
#  "rat": ["grates", "rates", "rations"]}

print(word_groups(["duct", "produce", "product", "rod"]))
#➞ {
#  "duct": ["product"],
#  "rod": ["produce", "product"]}

print(word_groups(["her", "the", "here", "other", "there"]))
#➞ {
#  "the": ["other", "there"],
#  "here": ["there"],
#  "her": ["here", "other", "there"]}
#Notes
#Words can belong to more than one group.