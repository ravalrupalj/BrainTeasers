#Max Adjacent Product
#Given a list of integers, find the pair of adjacent elements that have the largest product and return that product.
#Each list has at least two elements.
def adjacent_product(lst):
    l=[]
    for a,b in zip(lst,lst[1:]):
        l.append(a*b)
    return max(l)

print(adjacent_product([3, 6, -2, -5, 7, 3]) )
#➞ 21
print(adjacent_product([5, 6, -4, 2, 3, 2, -23]) )
#➞ 30
print(adjacent_product([0, -1, 1, 24, 1, -4, 8, 10]) )
#➞ 80

