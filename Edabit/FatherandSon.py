def age_difference(a,b):
    diff=a-b
    count=1
    for i in range(diff+1,100):
        if i/count==2:
            if i>a:
                return i-a
            else:
                return a-i
            break
        count = count + 1


print(age_difference(36,7))
print(age_difference(55,30))
print(age_difference(42, 21))