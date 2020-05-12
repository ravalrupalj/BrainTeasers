#Return the End Letters of Numbers
#Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th etc.
#Check the Resources tab for more info on ordinal numbers.
def return_end_of_number(num):
    d={1:'ST',2:'ND',3:'RD',4:'TH',5:'TH',6:'TH',7:'TH',8:'TH',9:'TH'}
    st=str(num)
    v=int(st[-1])
    value=d[v]
    final=str(num)+'-'+str(value)
    return final

print(return_end_of_number(553) )
#➞ "553-RD"
print(return_end_of_number(34))
#➞ "34-TH"
print(return_end_of_number(1231))
#➞ "1231-ST"
print(return_end_of_number(22) )
#➞ "22-ND"

