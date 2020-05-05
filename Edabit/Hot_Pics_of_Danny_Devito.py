 #I'm trying to watch some lectures to study for my next exam but I keep getting distracted by meme compilations, vine compilations, anime, and more on my favorite video platform.
#Your job is to help me by creating a function that takes in a string and checks to see if it contains the following words or phrases:
#"anime"
#"meme"
#"vines"
#"roasts"
#"Danny DeVito"
#If it does, return "NO!". Otherwise, return "Safe watching!".
def prevent_distractions(txt):
    l = ["anime", "meme", "vines", "roasts", "Danny DeVito"]
    for i in l:
        if i in txt:
            return 'NO!'
    return 'Safe watching!'
    #if any(x in txt for x in l):
    #    return 'NO!'
    #else:
    #    return 'Safe watching!'

print(prevent_distractions("vines that butter my eggroll"))
#➞ "NO!"
print(prevent_distractions("Hot pictures of Danny DeVito"))
#➞ "NO!"
print(prevent_distractions("How to ace BC Calculus in 5 Easy Steps"))
#➞ "Safe watching!"
