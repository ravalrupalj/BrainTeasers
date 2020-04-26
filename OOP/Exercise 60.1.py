#Abstract base Classes
#Abstract class will have atleast 1 abstract method
#Abstract method which has only declaration [no body in atleast one method]
from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print('its running')
class Whiteboard():
    def write(self):
        print('its writing')
class Programmer:
    def work(self,com):
        print('Solving Bugs')
        com.process()
#com=Computer()
com1=Laptop()
com2=Whiteboard()

##com.process()
prog1=Programmer()
prog1.work(com1)
#Can not pass com2 in above line bcoz it does not have process method
