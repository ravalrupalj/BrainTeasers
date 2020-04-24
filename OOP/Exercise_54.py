#Inner Class
#You can create object of inner class inside the outer class
#OR Your can creat object of inner class outside the ourter class provided you use outer class name to call it

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        #self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        lap1.show()
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student('Navin',2)
s2=student('Jenny',3)
lap1=student.Laptop()
s1.show()
