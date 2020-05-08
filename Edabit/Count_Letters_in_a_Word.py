#Count Letters in a Word Search
#Create a function that counts the number of times a particular letter shows up in the word search.
#You will always be given a list with five sub-lists.
def letter_counter(lst,letter):
    count=0
    for i in lst:
        count=count+i.count(letter)
    return count

print(letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]], "D"))
#➞ 3

# "D" shows up 3 times: twice in the first row, once in the third row.

print(letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]], "H"))
#➞ 2
