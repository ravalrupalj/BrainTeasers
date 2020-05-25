#Flash Cards
#Create a function that outputs the results of a flashcard. A flashcard is a list of three elements: a number, an operator symbol, and another number. Return the mathematical result of that expression.

#There are 4 operators: + (addition), - (subtraction), x (multiplication), and / (division). If the flashcard displays a number being divided by zero, e.g. [3, "/", 0], then return None. For division, round to the hundredths place. So [10, "/", 3] should return 3.33.
#Notes
#Flash cards contain only zero or positive numbers.
import operator

def flash(flash):
    ops={'+':operator.add,'-':operator.sub,'x':operator.mul,'/':operator.truediv}
    t=flash[1]
    if flash[1]=='/' and flash[2]==0:
        return None
    result=ops[t](int(flash[0]),int(flash[2]))
    return round(result,2)
#OR
# #card =  (' '.join([str(i) for i in flashcard]))
#	card = card.replace('x', '*')
#	if '/ 0' in card:
#		return None
#	return round(eval(card), 2)
print(flash([3, "x", 7]))
#➞ 21
print(flash([5, "+", 7]))
#➞ 12
print(flash([10, "-", 9]))
#➞ 1
print(flash([10, "/", 0]))
#➞ None
print(flash([10, "/", 3]))
#➞ 3.33
