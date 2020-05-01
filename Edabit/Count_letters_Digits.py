def count_all(str):
    letters=0
    digit=0
    for i in str:
        if i.isalpha()==True:
            letters=letters+1
        elif i.isdigit()==True:
            digit=digit+1
    return {'LETTERS':letters,'DIGITS':digit}


print(count_all("Hello World") )
#➞ { "LETTERS":  10, "DIGITS": 0 }

print(count_all("H3ll0 Wor1d"))
# { "LETTERS":  7, "DIGITS": 3 }

print(count_all("149990"))
# { "LETTERS": 0, "DIGITS": 6 }