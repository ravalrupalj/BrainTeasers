#Types of Varible:
# Class Varible(outside of init methon and Instance or static Variable(inside of init metnon)
class Car:
    wheels=4
    def __init__(self):
        self.mill=10
        self.com='BMW'

c1=Car()
c2=Car()
Car.wheels=5
print(c1.mill,c1.com,c1.wheels)
print(c2.mill,c2.com,c2.wheels)
