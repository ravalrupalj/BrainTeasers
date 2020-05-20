#Capital Split
#Create a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.
#The first letter will stay uncapitalized.
def cap_space(txt):
    t=''
    for i in txt:
        if i.isupper():
            t=t+' '+i.lower()
        else:
            t=t+i
    return t

print(cap_space("helloWorld") )
#➞ "hello world"

print(cap_space("iLoveMyTeapot") )
#➞ "i love my teapot"

print(cap_space("stayIndoors"))
#➞ "stay indoors"

