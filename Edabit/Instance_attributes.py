#Fullname and Email
#Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
#Form the fullname by simply joining the first and last name together, separated by a space.
#Form the email by joining the first and last name together with a "." in between, and follow it with '@company.com' at the end. Make sure everything is in lowercase.
#The attributes firstname and lastname are already made for you.
class Employee:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.fullname='{} {}'.format(firstname,lastname)
        self.email=('{}.{}@company.com'.format(firstname,lastname).lower())

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)
#➞ "John Smith"
print(emp_2.email)
#"mary.sue@company.com"
print(emp_3.firstname)
#"Antony"

