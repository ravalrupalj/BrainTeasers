#Printer Levels
#Given a dictionary of how many more pages each ink color can print, output the maximum number of pages the printer can print before any of the colors run out.
#Examples
#ink_levels({"cyan": 23,"magenta": 12,"yellow": 10}) ➞ 10
#ink_levels({"cyan": 432,"magenta": 543,"yellow": 777}) ➞ 432
#ink_levels({"cyan": 700,"magenta": 700,"yellow": 0}) ➞ 0
#Notes
#A single printed page uses each color once, so that no prints are possible if there's no more ink in any of the slots (see example #3).
def ink_levels(inks):
    return min(inks.values())
print(ink_levels({ "cyan": 23,"magenta": 12,"yellow": 10}))
print(ink_levels({"cyan": 432,"magenta": 543, "yellow": 777}))
print(ink_levels({ "cyan": 700,"magenta": 700,"yellow": 0}) )