#Triangular Number Sequence
#This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are: 1, 3, 6, 10, 15. Write a function that converts n number of places with its corresponding number.
def triangle(num):
    count=0
    for i in range(1,num+1):
        count=count+i
    return count


print(triangle(1) )
#➞ 1
print(triangle(6) )
#➞ 21
print(triangle(215))
#➞ 23220
