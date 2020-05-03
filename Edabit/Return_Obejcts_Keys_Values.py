#Create a function that takes a dictionary and returns the keys and values as separate lists.
def keys_and_values(d):
    keys=sorted(list(d.keys()))
    values=sorted(list(d.values()))
    return [keys,values]

print(keys_and_values({ "a": 1, "b": 2, "c": 3 }))
# [["a", "b", "c"], [1, 2, 3]]
print(keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" }))
# [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
print(keys_and_values({ "key1": True, "key2": False, "key3": True }))
# [["key1", "key2", "key3"], [True, False, True]]
