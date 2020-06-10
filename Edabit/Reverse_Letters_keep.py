#Reverse Letters, Keep Numbers in Place
#Create a function that reverses letters in a string but keeps digits in their current order.
def reverse(string):
    l=[]
    for i in string:
        if not i.isdigit():
            l.append(i)
    rev=l[::-1]
    s=''
    count=0
    for t in string:
        if not t.isdigit():
            s=s+(t.replace(t,rev[count]))
            count=count+1
        else:
            s=s+t
    return s
print(reverse("ab89c"))
#➞ "cb89a"
print(reverse("jkl5mn923o"))
#➞ "onm5lk923j"
print(reverse("123a45"))
#➞ "123a45"
