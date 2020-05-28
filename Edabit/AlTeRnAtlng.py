#AlTeRnAtInG cApS
#Create a function that alternates the case of the letters in a string (known as Spongecase).
#Notes
#The first letter should always be UPPERCASE.
#Ignore spaces.
def alternating_caps(txt):
    first_letter=txt[0].upper()
    s = first_letter + ''
    for i in range(1, len(txt)):
        if txt[i] == ' ':
            s = s + ' '
            if (s[i - 1]).islower():
                s = s + (txt[i+1]).upper()
            elif (s[i - 1]).isupper():
                s = s + (txt[i+1]).lower()

        else:
            if txt[i-1]!=' ':
                if (s[i-1]).islower():
                    s = s + (txt[i]).upper()
                elif(s[i-1]).isupper():
                    s = s + (txt[i]).lower()
    return s


print((alternating_caps("alternating caps")))
#"AlTeRnAtInG cApS"
#print(alternating_caps("Hello") )
#➞ "HeLlO"
print(alternating_caps("How are you?") )
#➞ "HoW aRe YoU?"
print(alternating_caps("OMG this website is awesome!") )
#➞ "OmG tHiS wEbSiTe Is AwEsOmE!"
