#Odd Up, Even Down — N Times
#Create a function that performs an even-odd transform to a list, n times. Each even-odd transformation:

#Adds two (+2) to each odd integer.
#Subtracts two (-2) to each even integer.
def even_odd_transform(lst,n):
    final_lst=[lst]
    for i in range(0,n):
        new_lst=[]
        for digit in final_lst[-1]:
            if digit%2==0:
               new_lst.append(digit-2)
            else:
                new_lst.append(digit+2)
        final_lst.append(new_lst)
    return new_lst
print(even_odd_transform([3, 4, 9], 3) )
#➞ [9, -2, 15]
# Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

print(even_odd_transform([0, 0, 0], 10))
#➞ [-20, -20, -20]

print(even_odd_transform([1, 2, 3], 1) )
#➞ [3, 0, 5]
