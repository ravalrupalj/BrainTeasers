#Simple OOP Calculator
#Create methods for the Calculator class that can do the following:
#Add two numbers.
#Subtract two numbers.
#Multiply two numbers.
#Divide two numbers.
#Notes
#The methods should return the result of the calculation.
class Calculator:

    def add(self,n1,n2):
        return n1+n2
    def subtract(self,n1,n2):
        return n1-n2
    def multiply(self,n1,n2):
        return n1*n2
    def divide(self,n1,n2):
        return n1/n2
calculator = Calculator()
print(calculator.add(10, 5))
# 15
print(calculator.subtract(10, 5))
# 5
print(calculator.multiply(10, 5))
#50
print(calculator.divide(10, 5))
# 2
