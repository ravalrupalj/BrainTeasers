#Creating a Picture Frame
#Create a function that takes the width, height and character and returns a picture frame as a 2D list.
def get_frame(w, h, ch):
    final_l=[]
    if w<=2 or h<=2:
        return 'invalid'
    else:
        for i in range(0,h):
            s = ''
            for j in range(0,w):
                if i==0 or i==(h-1):
                    s=s+ch
                else:
                    if j==0 or j==(w-1):
                        s=s+ch
                    else:
                        s=s+' '
            final_l.append([s])

        return final_l
print(get_frame(3, 3, "0"))
#[
#	["000"],
#	["0 0"],
#	["000"]
#])


print(get_frame(4, 5, "#") )
#➞ [
#  ["####"],
#  ["#  #"],
#  ["#  #"],
#  ["#  #"],
#  ["####"]
#]
# Frame is 4 characters wide and 5 characters tall.

print(get_frame(10, 3, "*") )
#➞ [
#  ["**********"],
#  ["*        *"],
#  ["**********"]
#]
# Frame is 10 characters and wide and 3 characters tall.

print(get_frame(2, 5, "0") )
#➞ "invalid"
# Frame"s width is not more than 2.
#Notes
#Remember the gap.
#Return "invalid" if width and height is 2 or less (can't put anything inside).