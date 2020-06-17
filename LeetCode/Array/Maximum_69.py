#1323. Maximum 69 Number
def maximum69Number(num):
    string=list(str(num))
    l=[num]
    for i in range(0,len(string)):
        string = list(str(num))
        if string[i]=='9':
            string[i]='6'
            t=''.join(string)
            l.append(int(t))
        elif string[i]=='6':
            string[i]='9'
            t=''.join(string)
            l.append(int(t))
    return max(l)
print(maximum69Number(9669))
#9969
print(maximum69Number(9996))
#9999
print(maximum69Number(9999))
#9999