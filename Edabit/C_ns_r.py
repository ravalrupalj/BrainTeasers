#C*ns*r*d Str*ngs
#Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

#Given a censored string and a string of the censored vowels, return the original uncensored string.
def uncensor(txt, vowels):
    s=''
    count=0
    for word in txt:
        if word=='*':
            count=count+1
            s=s+word.replace('*',vowels[count-1])
        else:
            s=s+word
    return s


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") )
#➞ "Where did my vowels go?"

print(uncensor("abcd", "") )
#➞ "abcd"

print(uncensor("*PP*RC*S*", "UEAE") )
#➞ "UPPERCASE"
#Notes
#The vowels are given in the correct order.
#The number of vowels will match the number of * characters in the censored string.