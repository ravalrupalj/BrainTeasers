def numJewelsInStones(J, S):
    unique=set(S)
    count = 0
    for i in unique:
        if i in J:
            count = count + S.count(i)
    return count
print(numJewelsInStones( "aA",  "aAAbbbb"))
