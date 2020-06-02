#Format II: Argument Indeces
#For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can formatted in order to get a certain outcome.
#Write a template string according to the following example:
a = "John"
b = "Joe"
template = "{0} hit {1} and then {0} hit {1}."

template.format(a, b)
#➞ "Joe hit John and then John hit Joe."
#Tips
#Writing a number n inside a place holder will tell .format() to fill in with the nth argument. For example:

"{0} said: Hi, I'm {0}.".format("Monica")
#➞ "Monica said: Hi, I'm Monica."
#Notes
#Sumbit a string, not a function.
#Do not change the name of the variable template.
#You can find all the exercises in this series over here.