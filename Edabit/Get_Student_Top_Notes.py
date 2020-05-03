#Create a function that takes an list of student dictionaries and returns a list of their top notes. If student does not have notes then let's assume their top note is equal to 0.
def get_student_top_notes(lst):
    ans=[]
    for i in lst:
        if len(i['notes'])>0:
            ans.append(max(i['notes']))
        elif len(i['notes'])==0:
            ans.append(0)
    return ans         


print(get_student_top_notes([{"id": 1,"name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]},{ "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5] },{"id": 3,
    "name": "Zygmunt","notes": [2, 2, 4, 4, 3, 3]}]))
#➞ [5, 5, 4]
print((get_student_top_notes([{'id': 1, 'name': 'Max', 'notes': [1, 5]}, {'id': 2, 'name': 'Cary', 'notes': [0, 5]}, {'id': 3, 'name': 'Lexi', 'notes': [2, 0]}, {'id': 4, 'name': 'Joshua', 'notes': [1, 2, 2]}, {'id': 5, 'name': 'Hans', 'notes': [3, 4, 0, 5, 1]}, {'id': 6, 'name': 'Alfie', 'notes': [0, 0, 2, 1, 5]}, {'id': 7, 'name': 'Ralph', 'notes': [4, 3, 1, 1, 1]}])) )
#[5, 5, 2, 2, 5, 5, 4]
