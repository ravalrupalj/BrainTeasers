#Censor Words Longer Than Four Characters
#Create a function that takes a string and censors words over four characters with *.
#Don't censor words with exactly four characters.
#If all words have four characters or less, return the original string.
#The amount of * is the same as the length of the word.
def censor(string):
    t=''
    for i in string.split():
       if len(i)>4:
           t=t+('*'*len(i))+' '
       else:
           t=t+i+' '
    return t.rstrip()

print(censor("The code is fourty"))
#➞ "The code is ******"
print(censor("Two plus three is five"))
#➞ "Two plus ***** is five"
print(censor("aaaa aaaaa 1234 12345"))
#➞ "aaaa ***** 1234 *****"

