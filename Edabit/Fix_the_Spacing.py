#Fix the Spacing
#Additional spaces have been added to a sentence. Return the correct sentence by removing them. All words should be separated by one space, and there should be no spaces at the beginning or end of the sentence.
def correct_spacing(sentence):
    t=sentence.strip()
    r=t.split()
    return ' '.join(r)
print(correct_spacing("The film   starts       at      midnight. "))
#➞ "The film starts at midnight."

print(correct_spacing("The     waves were crashing  on the     shore.   "))
#➞ "The waves were crashing on the shore."

print(correct_spacing(" Always look on    the bright   side of  life."))
#➞ "Always look on the bright side of life."
