#Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.
#Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".
#Notes
#Both strings are the same length.
def showdown(p1, p2):
    v1=p1.find('Bang')
    v2=p2.find('Bang')
    if v1>v2:
        return 'p2'
    elif v1<v2:
        return 'p1'
    else:
        return 'tie'
print(showdown( "   Bang!        ",
  "        Bang!   "))
#➞ "p1"
# p1 draws his gun sooner than p2
print(showdown("               Bang! ",
  "             Bang!   "))
#➞ "p2"
print(showdown("     Bang!   ",
  "     Bang!   "))
#➞ "tie"
