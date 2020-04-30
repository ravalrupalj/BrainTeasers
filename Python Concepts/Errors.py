#1]Syntax error or Complie error
#2]Logical error
#3]Run time error
a=5
b=2

try:
    print('resource open')
    print(a/b)
    k = int(input('Enter a number'))
    print(k)
except ZeroDivisionError as e:
    print('Hey, you cannot divide a NUmber by zero',e)
except ValueError as e:
    print('Invalid Input')
except Exception as e:
    print('Somethint went wrong')
finally:
    print('resource closed')





