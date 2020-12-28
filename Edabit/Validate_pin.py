def valid(word):
    if len(word)==4 or len(word)==6:
        for i in word:
            if i.isnumeric():
                pass
            else:
                return False
        return True
    return False

print(valid("1234"))
print(valid("89abc1"))
print(valid(" 4983"))