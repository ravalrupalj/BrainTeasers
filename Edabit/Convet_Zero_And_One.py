#Convert "Zero" and "One" to "1" and "0"
#Create a function that takes a string as an argument. The function must return a string containing 1s and 0s based on the string argument's words. If any word in the argument is not equal to "zero" or "one" (case insensitive), you should ignore it. The returned string's length should be a multiple of 8, if the string is not a multiple of 8 you should remove the numbers in excess
#Notes
#You must return the result as a string.
def text_to_number_binary(string):
    l = []
    result = ''
    for i in string.split():
        lowercase = i.lower()
        if lowercase == 'zero':
            result = result + '0'
        elif lowercase == 'one':
            result = result + '1'
        elif lowercase!='zero' or lowercase!='one':
            continue
    new_length=len(result)
    if new_length < 8:
        return ''
    elif new_length % 8 == 0:
        return result
    elif new_length % 8 != 0:
        r=len(result)%8
        return result[0:new_length-r]

print(text_to_number_binary('one Zero zero one zero zero one one one one one zero oNe one one zero one zerO'))
 #"1001001111101110"
print(text_to_number_binary("zero one zero one zero one zero one") )
#➞ "01010101"
print(text_to_number_binary("Zero one zero ONE zero one zero one") )
#➞ "01010101"
print(text_to_number_binary("zero one zero one zero one zero one one two") )
#➞ "01010101"
print(text_to_number_binary("zero one zero one zero one zero three") )
#➞ ""
print(text_to_number_binary("one one") )
#➞ ""
