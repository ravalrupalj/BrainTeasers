#Types of Methods:
#Instance methods,Class methods,Static methods
#1]Instance methond[work with Inst Variable]: Get and Set
#2]Class methods[work with Class Var]:
#3]Static[Nothing to do with Inst method or Class method]
class Student:
    school='Telusko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def rup():
        print('This is Student clss..in avc module')
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
s1=Student(34,43,54)
s2=Student(85,12,35)

print(s1.avg())
print(s2.avg())
print(Student.info())
print(Student.rup())

