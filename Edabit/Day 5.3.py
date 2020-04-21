#Summing the Squares
#Create a function where given the number n, return the sum of all square numbers up to and including n.
#squares_sum(3) ➞ 14
# 1² + 2² + 3² =
# 1 + 4 + 9 =
# 14
#squares_sum(3) ➞ 14
#squares_sum(12) ➞ 650
#squares_sum(13) ➞ 819
#Notes
#Remember that n is included in the total.
def squares_sum(n):
    count=0
    for i in range(1,n+1):
        count=count+(i**2)
    return count
print(squares_sum(3))
print(squares_sum(12))
print(squares_sum(13))