#Reverse the Odd Length Words
#Given a string, reverse all the words which have odd length. The even length words are not changed.
def reverse_odd(string):
    new_lst=string.split()
    s=''
    for i in new_lst:
        if len(i)%2!=0:
            t=i[::-1]
            s=s+t+' '
        else:
            s=s+i+' '
    return s.strip()
print(reverse_odd("Bananas"))
#➞ "sananaB"

print(reverse_odd("One two three four"))
#➞ "enO owt eerht four"

print(reverse_odd("Make sure uoy only esrever sdrow of ddo length"))
#➞ "Make sure you only reverse words of odd length"
#Notes
#There is exactly one space between each word and no punctuation is used.