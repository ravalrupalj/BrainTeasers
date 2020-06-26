#Standard Competition Ranking
#Standard competition ranking (also known as "1224" ranking) assigns the same rank to matching values. Rank numbers are increased each time, so ranks are sometimes skipped. If we have 5 scores (the highest score having a rank of 1):

#No matching values:

#Scores = [99, 98, 97, 96, 95]
#Rank = 1,  2,  3,  4,  5
#With matching values:

#Scores = [99, 98, 98, 96, 95]
#Rank = 1,  2,  2,  4,  5

# Second and third scores are equal, so rank "3" is skipped.
#Given a dictionary containing the names and scores of 5 competitors, and a competitor name, return the rank of that competitor after applying competition ranking.
def competition_rank(results, person):
    sort_orders = sorted(results.items(), key=lambda x: x[1], reverse=True)
    name,grades=[i[0]for i in sort_orders],[i[1] for i in sort_orders]
    l=[]
    for i,j in sort_orders:
        l.append(j)
    new_l=[]
    count = 1
    for i in range(0,len(l)):
        if i==0:
            new_l.append(count)
            continue
        if l[i]==l[i-1]:
            new_l.append(new_l[-1])
            count=count+1
        else:
            count=count+1
            new_l.append(count)
    return new_l[name.index(person)]



    #return new_l
#[('Kate', 92), ('Carol', 92), ('Jess', 87), ('Bruce', 87), ('Scott', 84)]
#[92, 92, 87, 87, 84]
#[1, 1, 3, 3, 5]
print(competition_rank({
  "George": 96,
  "Emily": 95,
  "Susan": 93,
  "Jane": 89,
  "Brett": 82
  }, "Jane") )
#➞ 4



print(competition_rank({
 "Kate": 92,
  "Carol": 92,
 "Jess": 87,
  "Bruce": 87,
  "Scott": 84
  }, "Bruce") )
#➞ 3
#Notes
#The highest score has a rank value of 1.