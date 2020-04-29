#Older Than Me
#Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in the following format:
#{other_person} is {older than / younger than / the same age as} me.
#FAILED: 'Samuel is younger than me' should equal 'Joel is older than me.'
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if other.age<self.age:
			return other.name +' is younger than me'
		elif other.age>self.age:
			return other.name+' is older than me'
		elif other.age==self.age:
			return other.name+' the same age as me'
	#OR
		if other.age < self.age:
			s = 'younger than'
		elif other.age > self.age:
			s = 'older than'
		elif other.age == self.age:
			s = 'the same age as'
			return '{} is {} me.'.format(other.name, s)

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))
#"Joel is older than me."
print(p2.compare_age(p1))
#"Samuel is younger than me."
print(p1.compare_age(p3))
#"Lily is the same age as me."

