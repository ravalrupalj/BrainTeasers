#Sum of all Evens in a Matrix
#Create a function that returns the sum of all even elements in a 2D matrix.
#Submatrices will be of equal length.
#Return 0 if the 2D matrix only consists of empty submatrices.
def sum_of_evens(lst):
    y=[]
    for i in lst:
        for num in i:
            if num%2==0:
                y.append(num)
    return sum(y)
print(sum_of_evens([[1, 0, 2],[5, 5, 7],[9, 4, 3]]) )
#➞ 6
#// 2 + 4 = 6
print(sum_of_evens([[1, 1],[1, 1]]))
#➞ 0
print(sum_of_evens([[42, 9],[16, 8]]) )
#➞ 66
print(sum_of_evens([[],[],[]]))
#➞ 0
