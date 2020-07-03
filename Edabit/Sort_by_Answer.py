#Sort by Answer
#Given a list of math expressions, create a function which sorts the list by their answer. It should be sorted in ascending order.
def sort_by_answer(lst):
    l=[]
    for i in lst:
        if 'x' in i:
            i=i.replace('x','*')
            l.append(eval(i))
        else:
            l.append(eval(i))
    sort_l=sorted(l)
    final_l=[]
    if len(set(sort_l))==1:
        return lst
    else:
        for j in range(0,len(sort_l)):
            for each in range(0,len(lst)):

                if lst[each] not in final_l:
                    if 'x' in lst[each]:
                        lst[each] = lst[each].replace('x', '*')
                    if eval(lst[each])==sort_l[j]:
                        if sort_l.count(sort_l[j])>1:
                            if '*' in lst[each]:
                                lst[each] = lst[each].replace('*', 'x')
                            final_l.append(lst[each])
                        else:
                            if '*' in lst[each]:
                                lst[each] = lst[each].replace('*', 'x')
                            final_l.append(lst[each])
                        break
                else:
                    continue
        return final_l

#[2, 5, 6, 8]
#[0, 0, 0, 0]
#[0, 2, 4]
print(sort_by_answer(["2 + 2", "2 - 2", "2 x 1"]))
# ["2 - 2", "2 x 1", "2 + 2"]
print(sort_by_answer(["1 x 1", "3 x 3", "-1 x -1", "-3 x -3"] ))
#['1 x 1', '-1 x -1', '3 x 3', '-3 x -3']
print(sort_by_answer(["2 + 2", "2 - 2","2 x 2", "2 / 2"]))
#["2 - 2", "2 / 2", "2 + 2", "2 x 2"])
print(sort_by_answer(["1 + 1", "1 + 7", "1 + 5", "1 + 4"]))
#➞ ["1 + 1", "1 + 4", "1 + 5", "1 + 7"]

print(sort_by_answer(["4 - 4", "2 - 2", "5 - 5", "10 - 10"]))
#➞ ["4 - 4", "2 - 2", "5 - 5", "10 - 10"]

print(sort_by_answer(["2 + 2", "2 - 2", "2 * 1"]))
#➞ ["2 - 2", "2 * 1", "2 + 2"]
#Notes
#If multiple expressions have the same answer, put them in the order of which they appear (see example #2).
#You won't need to worry about divisions by zero.
#The symbol used for multiplication is x instead of *.