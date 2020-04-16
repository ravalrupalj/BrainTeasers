#Burrrrrrrp
#Create a function that returns Burp with num "r"s in it.
#long_burp(3) ➞ "Burrrp"
#long_burp(5) ➞ "Burrrrrp"
#long_burp(9) ➞ "Burrrrrrrrrp"
#Notes
#Remember to use a capital B.
#Don't forget to return the result.

def long_burp(num):
    return 'Bu'+('r'*num)+'p'



print(long_burp(3))
print(long_burp(5))
print(long_burp(9))