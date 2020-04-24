#Overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
s1=Student(40,23)
print(s1.sum(3,7))

#Overridding
class A:
    def show(self):
        print('in A Show')
class B(A):
    def show(self):
        print('in B Show')

a1=B()
a1.show()