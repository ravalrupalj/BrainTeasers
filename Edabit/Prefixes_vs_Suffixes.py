#Prefixes vs. Suffixes
#Create two functions: is_prefix(word, prefix-) and is_suffix(word, -suffix).
#is_prefix should return True if it begins with the prefix argument.
#is_suffix should return True if it ends with the suffix argument.
#Otherwise return False.
#Notes
#The prefix and suffix arguments have dashes - in them.
import re
def is_prefix(word, prefix):
    e=len(prefix)
    t=re.findall(r'(\w{5})',word)
    new=''.join(t)
    new_condition= new[0:e-1]+'-'
    return  new_condition==prefix
def is_suffix(word, suffix):
    e=len(suffix)
    t=re.findall(r'(\w+)',word)
    new=''.join(t)
    new_condition= '-'+new[-e+1:]
    return new_condition==suffix
print(is_prefix("automation", "auto-") )
#➞ True
print(is_suffix("arachnophobia", "-phobia"))
#➞ True
print(is_prefix("retrospect", "sub-"))
#➞ False
print(is_suffix("vocation", "-logy"))
#➞ False
