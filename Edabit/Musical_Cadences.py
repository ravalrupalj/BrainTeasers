#Musical Cadences
#In music, cadences act as punctuation in musical phrases, and help to mark the end of phrases. Cadences are the two chords at the end of a phrase. The different cadences are as follows:
#V followed by I is a Perfect Cadence
#IV followed by I is a Plagal Cadence
#V followed by Any chord other than I is an Interrupted Cadence
#Any chord followed by V is an Imperfect Cadence
#Create a function where given a chord progression as a list, return the type of cadence the phrase ends on.
def find_cadence(lst):
    if lst[-1]=='V':
        return 'imperfect'
    elif lst[-1]=='I' and lst[-2]=='V':
        return 'perfect'
    elif lst[-1]=='I'and lst[-2]=='IV':
        return 'plagal'
    elif lst[-1]=='IV' or lst[-1]=='vi' and lst[-2]=='V':
        return 'interrupted'
    return 'no cadence'

print(find_cadence(["I", "IV", "V"]))
#➞ "imperfect"
print(find_cadence(["ii", "V", "I"]))
#➞ "perfect"
print(find_cadence(["I", "IV", "I", "V", "vi"]))
#➞ "interrupted"
#Notes
#Return strings all in lowercase.
#Only focus on the last two chords of a progression.
#Return "no cadence" if none of the criterea match up.
#I is a capital i not a lowercase L.