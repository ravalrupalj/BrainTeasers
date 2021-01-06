def add_name(obj, name, value):
    obj[name]=value
    return obj

print(add_name({}, "Brutus", 300) )
#➞ { "Brutus": 300 }
print(add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440))
#{ "piano": 500, "stereo": 300, "Caligula": 440 }
