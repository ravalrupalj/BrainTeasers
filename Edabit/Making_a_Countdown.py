#Making a Countdown
#Create a function where given the number n to count down from, and some words txt, return a countdown sequence as a string leading up to the words at the end.
#Put a full stop after each number and capitalize and add an exclamation mark to the word. See the examples below for clarification!
#n will be a number greater than 0.
#txt won't already include an exclamation mark.
#Don't include 0 in the countdown.
def countdown(n,txt):
    s=''
    for i in range(n,0,-1):
        s=s+str(i)+'. '
    return s+txt.upper()+'!'

print(countdown(10, "Blast Off") )
#➞ "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"
print(countdown(3, "go") )
#➞ "3. 2. 1. GO!"
print(countdown(5, "FIRE"))
#➞ "5. 4. 3. 2. 1. FIRE!"

