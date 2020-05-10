#Folding a Piece of Paper
#Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
#There are 1000mm in a single meter.
#Don't round answers.
def num_layers(n):
    start = 0.0005
    for i in range(n):
        start *= 2
    return str(start) + "m"
print(num_layers(0))
#"0.0005m
print(num_layers(3))
#➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)
print(num_layers(4))
#➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)
print(num_layers(21))
#➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
