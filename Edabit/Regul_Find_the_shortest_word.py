#Find the Shortest Word(s) in a Sentence
#Create a function that accepts a string as an argument. Find its shortest word(s) and return them as a list sorted alphabetically (if there are multiple shortest words).
import re
def find_shortest_words(txt):
    #txt = re.sub(r"[^a-zA-Z ]", "", txt)
    #mLen = min([len(word) for word in txt.split()])
    #return sorted([word.lower() for word in txt.split() if len(word) == mLen])
    #OR
    normal_l=[]
    l=[]
    for i in txt.split():
        a=''.join(re.findall(r'[a-zA-Z]+',i))
        normal_l.append(a.lower())
        if len(a)>0:
            l.append(len(a))
    minimum_lenght=min(l)
    final_l=[]
    for j in normal_l:
       if len(j)==minimum_lenght:
           final_l.append(j)
    return sorted(final_l)
print((find_shortest_words("You miss 100% of the shots you don't take.")))
#['of']
print(find_shortest_words("The only person you are destined to become is the person you decide to be."))
#['be', 'is', 'to', 'to']
print(find_shortest_words("There is only one way to avoid criticism: do nothing, say nothing, and be nothing."))
#['be', 'do', 'is', 'to' ])
print(find_shortest_words("I think the solution is fairly obvious."))
#➞ ["i"]
print(find_shortest_words("Chase two rabbits, catch none."))
#➞ ["two"]

print(find_shortest_words("We become what we think about."))
#➞ ["we", "we"]

print(find_shortest_words("The quick brown fox jumped over the lazy dogs back."))
#➞ ["fox", "the", "the"]
#Notes
#Periods, commas and other special characters don't count as part of a word's length.
#Remember to sort the list of words alphabetically before returning your result.
#Return words in lowercase only.