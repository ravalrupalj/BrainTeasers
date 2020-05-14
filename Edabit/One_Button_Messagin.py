# One Button Messaging Device
# Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.
# Write a function that takes a string (the message) and returns the total number of times the button is pressed.
# Ignore spaces.
def how_many_times(msg):
    if len(msg)==0:
        return 0

    current=msg[0]
    rest_of_string = msg[1:]

    char_int=ord(current)-96
    return char_int+how_many_times(rest_of_string)

print(how_many_times("abde"))
# ➞ 12
print(how_many_times("azy"))
# ➞ 52
print(how_many_times("qudusayo"))
# ➞ 123
