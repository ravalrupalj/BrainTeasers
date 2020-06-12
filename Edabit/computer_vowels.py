#compter_vowels
#the goal of this challenge is simple to create a function which counts the number of vowel in each word of a chain and returns the result in the form of dictionary

#The function takes as input a character string and returns a dictionary containing the word and the number of vowel it contains. -if a word does not contain vowels it does not appear in the dictionary
"Hello how are you ?"
#➞ {'how': 1, 'you': 2, 'Hello': 2, 'are': 2}
def compter_vowels(txt):
    d={}
    s='aeiouAEIOU'
    count=0
    low_txt=txt.split()
    for i in low_txt:
        for t in i:
            if t in s:
                count=count+1
        if count==0:
            continue
        d[i]=count
        count=0
    return d

print(compter_vowels('gggg mmm lol papa yoU knOw'))
#➞ {"knOw'": 1, 'yoU': 2, 'papa': 2, 'lol': 1}
#here mmmm and ggg do not continue vowels

print(compter_vowels('prOgrammIng is a gOod scIencE'))
#➞{'a': 1, 'scIencE': 3, 'is': 1, 'gOod': 2, 'prOgrammIng': 3}
print(compter_vowels('mAthematics, physIcs And chemIstry, computer science, biolOgY ANd medIcinE'))
#➞{'And': 1, 'ANd': 1, 'biolOgY': 3, 'science,': 3, 'chemIstry,': 2, 'computer': 3, 'mAthematics,': 4, 'medIcinE': 4, 'physIcs': 1}
#Notes
#are considered as vowels: a, i, e, u, o