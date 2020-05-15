#Numbered Alphabet
#Create a function that converts a string of letters to their respective number in the alphabet.
#Make sure the numbers are spaced.
#A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	...
#0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	...
def alph_num(txt):
    l=''
    for i in txt:
        t=ord(i)-65
        l=l+' '+str(t)
    return l.strip()

print(alph_num("XYZ") )
#➞ "23 24 25"

print(alph_num("ABCDEF") )
#➞ "0 1 2 3 4 5"

print(alph_num("JAVASCRIPT"))
#➞ "9 0 21 0 18 2 8 15 10"

