#Hiding the Card Number
#Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
#Ensure you return a string.
#The length of the string must remain the same as the input.
def card_hide(card):
    t=str(card[-4:])
    f=card[0:-4]
    st=[]
    for i in f:
        st.append('*')
    return ''.join(st)+t





print(card_hide("1234123456785678") )
#5678➞ "************5678"
print(card_hide("8754456321113213") )
#"************3213"
print(card_hide("35123413355523"))
#"**********5523"

