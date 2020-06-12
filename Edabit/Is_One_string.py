#Is One String in the Other?
#Create a function that takes two strings and returns True if either of the strings appears at the very end of the other string. Return False otherwise. The character * is a wildcard, so it can take the place of any character.
def overlap(str1, str2):
    l_str1=str1.lower()
    l_str2=str2.lower()
    length_Str1=len(l_str1)
    length_Str2=len(l_str2)
    l=''
    if '*' in l_str1 and '*' in l_str2:
        new_list=l_str2[-length_Str1:]
        for i in range(0,len(new_list)):
            if new_list[i]=='*':
                l=l+(l_str2[i])
            else:
                l=l+(new_list[i])
        if l==new_list:
            return True
        else:
            return False
    elif '*' in l_str2:
        new_list=l_str2[-length_Str1:]

        for i in range(0,len(new_list)):
            if new_list[i]=='*':
                l=l+(l_str1[i])
            else:
                l=l+(new_list[i])
        if l==new_list:
            return True
        elif len(set(new_list))==1:
            return True
        else:
            return False
    elif '*' in l_str1:
        new_list=l_str2[-length_Str1:]
        for i in range(0,len(new_list)):
            if new_list[i]=='*':
                l=l+(l_str2[i])
            else:
                l=l+(new_list[i])
        if l==new_list:
            return True
        else:
            return False

    else:
        if l_str2[-length_Str1:]==l_str1:
            return True
        elif l_str1[-length_Str2:]==l_str2:
            return True
        else:
            return False
print((overlap("a*c", "*b*")))# True
print(overlap("*bc", "Ican'tsingmyABC"))#True
print(overlap("hey", "*********"))  # ➞ True
print(overlap("ab", "Ican'tsingmy**c"))#➞ False
print(overlap("ABC", "Ican'tsingmyABC"))#➞ True
print(overlap("abc", "Ican'tsingmyABC"))#➞ True
print(overlap("Ican'tsingmyABC", "abc"))#➞ True
print(overlap("hello world", "hello"))#➞ False
print(overlap("+=", "this should work too +="))#➞ True

#Notes
#Your function should NOT be case sensitive (see example #2).