#Tic Tac Toe
#Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
def tic_tac_toe(board):
    if board[0][0]==board[0][1]==board[0][2] or board[0][0]==board[1][0]==board[2][0] or board[0][0]==board[1][1]==board[2][2] :
        return board[0][0]
    elif board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]
    elif board[2][0]==board[2][1]==board[2][2] or board[2][0]==board[1][1]==board[0][2]:
        return board[2][0]
    elif board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]
    else:
        return 'Draw'
print(tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]))
#➞ "X"
print(tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]))
#➞ "O"

print(tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]))
print(tic_tac_toe([
	["X", "O", "E"],
	["X", "O", "E"],
	["E", "O", "X"]
]))
# "O"
#➞ "Draw"
#Notes
#Make sure that if O wins, you return the letter "O" and not the integer 0 (zero) and if it's a draw, make sure you return the capitalised word "Draw". If you return "X" or "O", make sure they're capitalised too.