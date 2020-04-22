#Calculate Determinant of a 2x2 Matrix
#Create a function to calculate the determinant of a 2 x 2 matrix. The determinant of the following matrix is: ad - bc:
#calc_determinant([[1, 2],[3, 4]]) ➞ -2
#calc_determinant([ [5, 3],[3, 1]]) ➞ -4
#calc_determinant([[1, 1],[1, 1]]) ➞ 0
import numpy as np
def calc_determinant(matrix):
    a = np.array(matrix)
    return round(np.linalg.det(a))
print(calc_determinant([[1, 2], [3, 4]]))
print(calc_determinant([[5, 3],[3, 1]]))
print(calc_determinant([[1, 1],[1, 1]]))
