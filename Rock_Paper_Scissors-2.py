#Rock, Paper, Scissors!
#Abigail and Benson are playing Rock, Paper, Scissors.

#Each game is represented by an array of length 2, where the first element represents what Abigail played and the second element represents what Benson played.

#Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".
#R stands for Rock
#P stands for Paper
#S stands for Scissors
def calculate_score(games):
    Abi=0
    Ben=0
    if all(i[0]==i[1] for i in games):
        return 'Tie'
    for i in games:
        if i[0]==i[1]:
            games.remove(i)
    for i in games:
        if i[0]=='R':
            if i[1]=='P':
                Ben=Ben+1
            else:
                Abi=Abi+1
        elif i[0]=='S':
            if i[1]=='R':
                Ben=Ben+1
            else:
                Abi=Abi+1
        elif i[0]=='P':
            if i[1]=='R':
                Abi=Abi+1
            else:
                Ben=Ben+1
    if Abi>Ben:
        return 'Abi'
    elif Abi<Ben:
        return 'Ben'
    else:
        return 'Tie'

print(calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]))
#➞ "Abigail"
# Ben wins the first game (Paper beats Rock).
# Abigail wins the second game (Rock beats Scissors).
# Abigail wins the third game (Scissors beats Paper).
# Abigail wins 2/3.
print(calculate_score([["R", "R"], ["S", "S"]]))
#➞ "Tie"
print(calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]))
#➞ "Tie"
