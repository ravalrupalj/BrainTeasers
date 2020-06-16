#1108. Defanging an IP Address

def defanging_id(address):
    s=''
    for i in address:
        if i == '.':
            s=s+'[.]'
        else:
            s=s+i
    return s

print(defanging_id('1.1.1.1'))
#"1[.]1[.]1[.]1"