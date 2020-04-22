#Count the Capital Letters
#Given a string of letters, how many capital letters are there?
#capital_letters("fvLzpxmgXSDrobbgMVrc") ➞ 6
#capital_letters("JMZWCneOTFLWYwBWxyFw") ➞ 14
#capital_letters("mqeytbbjwqemcdrdsyvq") ➞ 0
def capital_letters(txt):
    count=0
    for i in txt:
        if i.isupper():
            count=count+1
    return count
print(capital_letters("fvLzpxmgXSDrobbgMVrc"))
print(capital_letters("JMZWCneOTFLWYwBWxyFw"))
print(capital_letters("mqeytbbjwqemcdrdsyvq"))