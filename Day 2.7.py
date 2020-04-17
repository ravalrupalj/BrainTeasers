#Sum of the Odd Numbers
#Create a function which returns the total of all odd numbers up to and including n. n will be given as an odd number
#add_odd_to_n(5) ➞ 9  # 1 + 3 + 5 = 9
#add_odd_to_n(13) ➞ 49
#add_odd_to_n(47) ➞ 576
#Notes
#Curiously, the answers are all square numbers

def add_odd_to_n(n):
    dum=0
    for i in range(1,n+1):
        if i%2!=0:
            dum=dum+i
    return dum


print(add_odd_to_n(5))
print(add_odd_to_n(13))
print(add_odd_to_n(47) )
