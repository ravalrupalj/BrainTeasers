#Give Me the Even Numbers
#Create a function that takes two parameters (start, stop), and returns the sum of all even numbers in the range.
#sum_even_nums_in_range(10, 20) ➞ 90
# 10, 12, 14, 16, 18, 20
#sum_even_nums_in_range(51, 150) ➞ 5050
#sum_even_nums_in_range(63, 97) ➞ 1360
#Remember that the start and stop values are inclusive.
def sum_even_nums_in_range(start, stop):
    count=0
    for i in range(start,stop+1):
        if i%2==0:
            count=count+i
    return count
    #return sum(i for i in range(start, stop+1) if not i%2)
print(sum_even_nums_in_range(10, 20) )
    # 10, 12, 14, 16, 18, 20
print(sum_even_nums_in_range(51, 150) )
print(sum_even_nums_in_range(63, 97) )