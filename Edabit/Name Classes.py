#Name Classes
#Write a class called Name and create the following attributes given a first name and last name (as fname and lname):
#An attribute called fullname which returns the first and last names.
#A attribute called initials which returns the first letters of the first and last name. Put a '.' between the two letters.
#Remember to allow the attributes fname and lname to be accessed individually as well.
#Notes
#Make sure only the first letter of each name is capitalised.
#Check the Resources tab for some helpful tutorials on Python classes.
class Name:
    def __init__(self,fname,lname):
        self.fname=fname.title()
        self.lname=lname.title()
        self.fullname=('{} {}'.format(fname,lname)).title()
        self.initials=(fname[0]+'.'+lname[0]).title()
a1 = Name('john', 'SMITH')
print(a1.fname)
#'John'
print(a1.lname )
#'Smith'
print(a1.fullname)
#'John Smith'
print(a1.initials)
#'J.S'