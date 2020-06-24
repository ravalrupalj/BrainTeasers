#Words With Duplicate Letters
#Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.
def no_duplicate_letters(phrase):
    for i in phrase.split():
        for j in i:
            if i.count(j)>1:
                return False
    return True


print(no_duplicate_letters("Fortune favours the bold.") )
#➞ True

print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
#➞ True

print(no_duplicate_letters("Look before you leap.") )
#➞ False
# Duplicate letters in "Look" and "before".

print(no_duplicate_letters("An apple a day keeps the doctor away.") )
#➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".
#Notes
#Letter matches are case-insensitive.