#Reverse Titling
#The normal title() function in Python capitalises the first letter of every word in a given sentence, leaving all the other letters as lowercase.
#The goal of this challenge is to create a reverse_title() function, which achieves the complete opposite! Make the first letter of every word lowercase, and the rest uppercase!
#reverse_title('this is a title') ➞ 'tHIS iS a tITLE'
#reverse_title('BOLD AND BRASH!') ➞ 'bOLD aND bRASH!'
#reverse_title('Elephants dance about bravely in Thailand') ➞ 'eLEPHANTS dANCE aBOUT bRAVELY iN tHAILAND'
def reverse_title(txt):
    t=txt.title()
    return t.swapcase()

print(reverse_title('this is a title'))
print(reverse_title('BOLD AND BRASH!'))
print(reverse_title('Elephants dance about bravely in Thailand'))