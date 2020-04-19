#After N Months...
#Create a function that takes in year and month as input, then return what year it would be after n-months has elapsed.
#after_n_months(2020, 24) ➞ 2022
#after_n_months(1832, 2) ➞ 1832
#after_n_months(1444, 60) ➞ 1449
#Notes
#Assume that adding 12 months will always increment the year by 1.
#If no value is given for year or months, return "year missing" or "month missing".
#At least one value will be present.

def after_n_months(year, month):
    if year is None:
        return 'year missing'
    if month is None:
        return 'month missing'
    return year + month // 12



print(after_n_months(2020, 24))
print(after_n_months(1832, 2))
print(after_n_months(1444, 65))
print(after_n_months(2020, None))
print(after_n_months(None, 2))
