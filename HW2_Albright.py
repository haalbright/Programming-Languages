import copy

theboard = [
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_","_"]
]

# print each of the rows one by one
def showTheBoard(board):
  for i in [0,1,2,3,4,5,6,7]:
    print(" ".join(board[i]))

# the board is solved when there are 8 queens on it
def isSolved(board):
  queens = 0
  for i in [0,1,2,3,4,5,6,7]:
    if "1" in board[i]:
      queens = queens + 1
  if queens == 8: #solved if 8 queens are placed
    return True
  return False

# if ANY row is crossed out then you can't solve it
def impossible(board):
  for i in [0,1,2,3,4,5,6,7]:
    if ["0","0","0","0","0","0","0","0"] == board[i]:#if there is a row w/o a queen, then the board can't be solved
      return True
  return False

def addQueen(board, row, column):
  # straight lines
  for i in [0,1,2,3,4,5,6,7]:
    board[i][column] = "0" #mark with 0 so no queen is placed there
  for j in [0,1,2,3,4,5,6,7]:
    board[row][j] = "0"

  # diagonals
  i = row
  j = column
  while i < 8 and j < 8:
    board[i][j] = "0"
    i = i + 1
    j = j + 1

  i = row
  j = column
  while i < 8 and 0 <= j:
    board[i][j] = "0"
    i = i + 1
    j = j - 1

  i = row
  j = column
  while 0 <= i and j < 8:
    board[i][j] = "0"
    i = i - 1
    j = j + 1

  i = row
  j = column
  while 0 <= i and 0 <= j:
    board[i][j] = "0"
    i = i - 1
    j = j - 1


  board[row][column] = "1" #add the queen

def recursivelySolve(startBoard, column):
  if isSolved(startBoard):
    print "\nFound a solution!"
    showTheBoard(startBoard)
    return True

  if impossible(startBoard):
    return False

  for row in [0,1,2,3,4,5,6,7]: #test rows 0-7
    if startBoard[row][column] == "_":
      newBoard = copy.deepcopy(startBoard) #create a new board
      addQueen(newBoard, row, column)
      if recursivelySolve(newBoard, column+1):#go the next column
        return True
  return False


recursivelySolve(theboard, 0) #start at column 0
