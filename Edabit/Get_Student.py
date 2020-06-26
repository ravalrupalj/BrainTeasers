#Get Student with Best Test Avg.
#Given a dictionary with students and the grades that they made on the tests that they took, determine which student has the best Test Average. The key will be the student's name and the value will be a list of their grades. You will only have to return the student's name. You do not need to return their Test Average.
def get_best_student(grades):
    d={}
    for i,j in grades.items():
        count = 0
        for value in j:
            count=count+value
        d[i]=count/len(j)
    max_avg=max(d.values())
    for name,avg in d.items():
        if avg==max_avg:
            return name


print(get_best_student({ "John": [100, 90, 80],"Bob": [100, 70, 80]}))
#➞ "John"

# John's avg = 90
# Bob's avg = 83.33

print(get_best_student({
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]}))
#➞ "Mike"
#Notes
#All students in a dictionary will have the same amount of test scores. So no student will have taken more tests than another.