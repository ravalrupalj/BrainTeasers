#Reverse String Without affecting Special Characters
#Reverse the string without affecting special characters and numbers.
def rev_specstring(string):
    s=''
    for i in string:
        if i.isalpha():
            s=s+i
    posi=list(s[::-1])
    for i in range(0,len(string)):
        if not string[i].isalpha():
            posi.insert(i,string[i])
    return ''.join(posi)
#Examples
print(rev_specstring("AFC#47GH$Ieu"))
#➞ "ueI#47HG$CFA")

print(rev_specstring("guyhiuj1234!@#$%rtyhghu" ))
#➞ "uhghytr1234!@#$%juihyug")

print(rev_specstring("12!@" ))
#➞ "12!@")
#Notes
#Try with for loops.