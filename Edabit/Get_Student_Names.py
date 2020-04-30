#Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

def get_student_names(dict):
    return sorted(dict.values())


print(get_student_names({
    "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"}))
#["Becky", "John", "Steve"]
