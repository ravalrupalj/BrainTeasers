#Find the falsehoods
#By default, python will interpret empty values, such as 0, (), {}, [], "" as the boolean False. For example, the code "cat" if () else "dog" returns "dog" since "() is False".
#On the other hand, non-empty values are interpreted as True. For example, "cat" if (3,2) else "dog" returns "cat" since "(3,2) is True".
#Write a function which, given a list of values, return the list of the values that are False
#["", "a", "ab"] ➞ [""]
#[None, 1, [], [0], 0] ➞ [None, [], 0]
#[] ➞ []
#[[]] ➞ [[]]
#[[[]]] ➞ []
def find_the_falsehoods(lst):
    return [i for i in lst if bool(i) is False]

print(find_the_falsehoods([0, 1, 2, 3]))
print(find_the_falsehoods(["", "a", "ab"] ))
print(find_the_falsehoods([None, 1, [], [0], 0]))
print(find_the_falsehoods([]))
print(find_the_falsehoods([[[]]]))