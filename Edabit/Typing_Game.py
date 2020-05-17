#Typing Game
#You're in the midst of creating a typing game.
#Create a function that takes in two lists: the list of user-typed words, and the list of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words).
# Inputs:
#User-typed: ["cat", "blue", "skt", "umbrells", "paddy"]
#Correct: ["cat", "blue", "sky", "umbrella", "paddy"]
# Output: [1, 1, -1, -1, 1]
#The input list lengths will always be the same.
def correct_stream(user, correct):
    l = []
    for i, j in zip(user, correct):
        if i == j:
            l.append(1)
        else:
            l.append(-1)
    return l
#OR
#outArr = []
#    for i in range(len(user)):
 #       if user[i] == correct[i]:
 #           outArr.append(1)
 #       else:
 #           outArr.append(-1)

 #   return outArr

print(correct_stream(["it", "is", "find"], ["it", "is", "fine"]) )
#➞ [1, 1, -1]

print(correct_stream(["april", "showrs", "bring", "may", "flowers"],["april", "showers", "bring", "may", "flowers"]) )
#➞ [1, -1, 1, 1, 1]

