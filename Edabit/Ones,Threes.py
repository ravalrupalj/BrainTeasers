#Ones, Threes and Nines (Version #1)
#Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this.
class ones_threes_nines:
    def __init__(self,num):
        self.ones=int(num)
        self.threes=int(num/3)
        self.nines=int(num/9)



n1 = ones_threes_nines(5)
print(n1.nines )
#➞ 0
print(n1.ones )
#➞ 5
print(n1.threes )
#➞ 1
#Notes
#Do not use the math module.
#See version #2 of this series.