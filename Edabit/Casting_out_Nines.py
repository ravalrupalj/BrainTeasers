#This is a method commonly taught in primary schools, used to verify the correctness of an operation; usually (as in this exercise) the multiplication.

#Every number involved in the multiplication is replaced by its digital root (reiterated sum of its digits until a single-digit number is obtained). After this, the digital roots of factors are multiplied, and again this result is reduced to the digital root. If the digit obtained is different from the result's digital root the operation is surely wrong, if it is equal the operation can be correct with a possibility out of nine to be a false positive.

#Given two factors and a result, implement a function that returns a string in the format:

#"x, x, x, x = Result!", with x being the digital roots (a, b, r, and a*b in the order).
#Result! being "Correct!" if the last two digits are the same and the result is correct.
#"False Positive!" if the last two digits are the same but the result is wrong.
#"Wrong!" if the last two digits are different.
# D.R. is for Digital Root
def cast_out_nines(a, b, r):
    string_a=getSingleLetter(a)
    string_b=getSingleLetter(b)
    string_r=getSingleLetter(r)
    new_num=string_a,string_b,string_r
    multiplication=string_a*string_b
    new_multi=getSingleLetter(multiplication)
    if string_r!=new_multi:
        return 'wrong'
    else:
        return 'correct'

def getSingleLetter(num):
    string_a=str(num)
    count=0
    while len(string_a)>1:
        count=0
        for i in string_a:
            count=count+int(i)
        string_a=str(count)
    return count


print(cast_out_nines(467, 78, 36426))
#➞ "8,6,3,3 = Correct!"
# D.R. 467 = 4 + 6 + 7 = 17 = 1 + 7 = 8
# D.R. 78 = 7 + 8 = 15 = 1 + 5 = 6
# D.R. 36426 = 3 + 6 + 4 + 2 + 6 = 21 = 2 + 1 = 3
# D.R. 8 * 6 = D.R. 48 = 4 + 8 = 12 = 1 + 2 = 3
# Last two digits are the same and result is correct: Correct!

print(cast_out_nines(467, 78, 36425))
#➞ "8,6,2,3 = Wrong!"
# D.R. 467 = 8
# D.R. 78 = 6
# D.R. 36425 = 3 + 6 + 4 + 2 + 5 = 20 = 2 + 0 = 2
# D.R. 8 * 6 = 3
# Last two digits are different and result is wrong: Wrong!

print(cast_out_nines(467, 78, 129))
#➞ "8,6,3,3 = False Positive!"
# D.R. 467 = 8
# D.R. 78 = 6
# D.R. 129 = 1 + 2 + 9 = 12 = 1 + 2 = 3
# D.R. 8 * 6 = 3
# Last two digits are equals but result is wrong: False Positive!