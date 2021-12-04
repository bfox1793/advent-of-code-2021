## Parse file
my_file = open("input-files/day4.txt", "r")
content = my_file.read()
input_list = content.split("\n\n")

MARKED_CHAR = "X"

## Parse first line as bingo draws
bingo_draws_raw = input_list[0].split(",")
bingo_draws = []
for val in bingo_draws_raw:
  bingo_draws.append(int(val))

## Pop first element, remaining array becomes list of boards
input_list.pop(0)

def generate_bingo_board(input):
  # First split on newline, get rows
  # Next split on whitespace, get cols & append to array
  # Return 2d array
  rows = input.split("\n")
  matrix = []
  for row in rows:
    matrix.append(row.split())
  return matrix

def create_index_string(i,j):
  return "[" + str(i) + "][" + str(j) + "]"

class bingo_board():

  def __init__(self, input_board, board_number):
    self.input_board = input_board
    self.bingo_board = generate_bingo_board(input_board)
    self.board_number = board_number
    self.winning_number = None

  ## Check if the board has a given number
  ## If so, mark the number and return true
  ## Else, return false
  def check_board(self, draw):
    bingo_draw = int(draw)
    for i in range(len(self.bingo_board)):
      for j in range(len(self.bingo_board[i])):
        ## Skip already-marked numbers
        if self.bingo_board[i][j] == MARKED_CHAR:
          continue

        if int(self.bingo_board[i][j]) == bingo_draw:
          print("Board " + str(self.board_number) + " has a hit on number " + str(bingo_draw) + " at " + create_index_string(i,j))
          self.bingo_board[i][j] = MARKED_CHAR
          return True
    return False
      
  ## Loop through bingo_board and see if we've won!
  def is_winner(self, last_number):
    ## If row is entirely X, return true
    for i in range(len(self.bingo_board)):
      values = set()
      for j in range(len(self.bingo_board[i])):
        values.add(self.bingo_board[i][j])
      if len(values) == 1:
        self.winning_number = last_number
        return True
    
    ## If column is entirely X, return true
    for i in range(len(self.bingo_board)):
      ## Assume bingo board is 5x5
      values = set()
      for j in range(len(self.bingo_board[i])):
        values.add(self.bingo_board[j][i])
      if len(values) == 1:
        self.winning_number = last_number
        return True
    ## Else, return false
    return False

  ## Arbitrary AoC being dumb
  def calculate_score(self):
    score = 0
    for i in range(len(self.bingo_board)):
      for j in range(len(self.bingo_board[i])):
        if self.bingo_board[i][j] != MARKED_CHAR:
          score += int(self.bingo_board[i][j])
    return score * self.winning_number

## Set up bingo boards
boards = []
for i in range(len(input_list)):
  boards.append(bingo_board(input_list[i], i))


def part1():
  for draw in bingo_draws:
    for board in boards:
      if board.check_board(draw):
        if board.is_winner(draw):
          print("We found a winner!")
          print("Board " + str(board.board_number) + " has won!!!")
          for row in board.bingo_board:
            print(row)
            print("")
          print("Final score: " + str(board.calculate_score()))
          return

def part2():
  winning_boards = []
  for draw in bingo_draws:
    for board in boards:
      # Skip already-won boards
      if board.is_winner(board.winning_number):
        continue
      if board.check_board(draw):
        if board.is_winner(draw):
          winning_boards.append(board.board_number)

  last_winning_board = winning_boards[len(winning_boards) - 1]
  print("Last winning board: " + str(last_winning_board))
  print("Last winning board score: " + str(boards[last_winning_board].calculate_score()))

part1()
part2()