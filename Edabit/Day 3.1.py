#Given a pH value, return whether that value is 'alkaline', 'acidic', or 'neutral'. Return 'invalid' if the value given is less than 0 or greater than 14.
#Examples
#pH_name(5) ➞ "acidic"
#pH_name(8.7) ➞ "alkaline"
#pH_name(7) ➞ "neutral"
#Notes
#Values such as 6.9999 and 7.00001 should return 'acidic' and 'alkaline' respectively.
def pH_name(pH):
    if pH >=0 and pH<=14:
        if pH>=0 and pH<=6:
            return 'acidic'
        elif pH==7:
            return 'neutral'
        else:
            return 'alkaline'
    else:
        return 'invalid'
print(pH_name(5))
print(pH_name(8.7))
print(pH_name(7))





