#Pronouncing the Xs
#Create a function which replaces all the x's in the string in the following ways:

#Replace all x's with "cks" UNLESS:

#The word begins with "x", therefore replace it with "z".
#The word is just the letter "x", therefore replace it with "ecks".
#Notes
#All x's are lowercase.
#I know that not all words with x's follow this rule, but there are too many edge cases to count!
def x_pronounce(string):
    result=''
    for i in string.split():
        if i=='x':
            result=result+' '+i.replace('x','ecks')
        elif len(i)>1 and i[0]=='x':
            result=result+' '+i.replace('x','z')
        elif 'x' in i:
            result=result+' '+i.replace('x','cks')
        else:
            result=result+' '+i
    return result.strip()

#print(x_pronounce("Inside the box was a xylophone") )
#➞ "Inside the bocks was a zylophone"

print(x_pronounce("The x ray is excellent") )
#➞ "The ecks ray is eckscellent"

print(x_pronounce("OMG x box unboxing video x D") )
#➞ "OMG ecks bocks unbocksing video ecks D"
