#Card Counting (BlackJack)
#In BlackJack, cards are counted with -1, 0, 1 values:
#2, 3, 4, 5, 6 are counted as +1
#7, 8, 9 are counted as 0
#10, J, Q, K, A are counted as -1
#Create a function that counts the number and returns it from the list of cards provided.
#Notes
#String inputs will always be upper case.
#You do not need to consider case sensitivity.
#If the argument is empty, return 0.
#No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
#2, 3, 4, 5, 6 are counted as +1
#7, 8, 9 are counted as 0
#10, J, Q, K, A are counted as -1
def count(deck):
    total=0
    for i in deck:
        if i==2 or i==3 or i==4 or i==5 or i==6:
            total=total+1
        elif i==7or i==8 or i==9:
            total=total+0
        else:
            total=total-1
    return total
print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
#➞ 1
print(count(["A", "A", "K", "Q", "Q", "J"]))
#➞ -6
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))
#➞ 5
