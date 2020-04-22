#Add, Subtract, Multiply or Divide?
#Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24. If none of the operations can give 24, return None.
#operation(15, 9) ➞ "added"
#operation(26, 2) ➞ "subtracted"
#operation(11, 11) ➞ None
#Notes
#Only integers are used as test input.
#Numbers should be added, subtracted, divided or multiplied in the order they appear in the parameters.
def operation(num1, num2):
    if num1+num2==24:
        return 'added'
    elif num1-num2==24:
        return 'subtracted'
    elif num1*num2==24:
        return 'multiplied'
    elif num1/num2==24:
        return 'divided'
    else:
        return None
#2nd solution return {a + b: "added", a - b: "subtracted", a * b: "multiplied", a / b: "divided"}.get(24)


print(operation(15, 9))
print(operation(26, 2) )
print(operation(11, 11))