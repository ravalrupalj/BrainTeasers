#Complete the Square (Matrix)
#Sadly, the mathematical world is biased in favor of square matrices. As such, this challenge will help rectangular matrices by making them square.

#For example, for the matrix:
#Notes
#Matrices should be padded on the right or at the bottom, but not both simultaneously (i.e. the size of the biggest direction shouldn't change).
#If the input is already a square matrix, just return that matrix.
#[
#  [1, 2],
#  [3, 4],
#  [5, 6]
#]
#This can be done by padding it with a column of zeroes on the right to get:

#[
#  [1, 2, 0],
#  [3, 4, 0],
#  [5, 6, 0]
#]
#While for the matrix:

#[
#  [1, 2, 3, 4],
#  [5, 6, 7, 8]
#]
#One can pad it with two rows of zeros at the bottom to get:

#[
 # [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]
#]
#Write a function that pads a rectangular matrix with zeros on the right or at the bottom to make it square.
def complete_square(lst):
    new_length=len(lst[0])
    l=[0]*new_length
    left_l=new_length-len(lst)
    right_l=len(lst)-new_length

    if len(lst)!=len(lst[0]):
        if len(lst)>len(lst[0]):
            for i in lst:
                for t in range(right_l):
                    i.append(0)
        else:
            for value in range(0, left_l):
                lst.append(l)
    return lst
print(complete_square(
[[1, 8, 9],
 [3, 6, 7],
 [5, 4, 5],
[7, 2, 3],
[9, 0, 1]]))
#[[1, 8, 9, 0, 0],
# [3, 6, 7, 0, 0],
 #[5, 4, 5, 0, 0],
# [7, 2, 3, 0, 0],
# [9, 0, 1, 0, 0]])
print(complete_square([[1, 2, 3, 4],
 [5, 6, 7, 8]]))
#[[1, 2, 3, 4],
# [5, 6, 7, 8],
# [0, 0, 0, 0],
# [0, 0, 0, 0]])

print(complete_square([[2, 5]]))
#➞ [ [2, 5],
# [0, 0]]

print(complete_square([[2, 5],
  [1, 7]]))
#➞ [ [2, 5],
#  [1, 7]]

print(complete_square([
  [1, 2],
  [3, 4],
  [5, 6]]))
#➞ [
 # [1, 2, 0],
#  [3, 4, 0],
#  [5, 6, 0]]
