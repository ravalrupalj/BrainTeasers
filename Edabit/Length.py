def number_length(num):
    count=0
    s=str(num)
    for i in s:
        count=count+1
    return count

print(number_length(10))