# Creating a 2d array to hold the 3x3 matrix
rows, cols = (3, 3)
board = [[0 for i in range(cols)] for j in range(rows)]


def show_position():
  for i in range(0, 3):
    for j in range(0, 3):
      board[i][j] = (i*3)+(j+1)

  board_layout()

  # after showing we need to wipe all the position to " "
  for i in range(0, 3):
    for j in range(0, 3):
      board[i][j] = " "  

def board_layout():
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
  print("-----------")
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
  print("-----------")
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


def is_place_available(position):
  pass


def check_win(position):
  pass


def place_marker(player, chances):
  # Setting up marker for different players
  marker = ''
  if player == 1:
    marker = 'X'
  else:
    marker = 'O'

  input = int(input(f"Player {player}({marker}) enter position: "))
  pos = get_location(input)
  board[pos[0]][pos[1]] = 'X'
  if chances > 4:
    check_win(pos)


def game_logic():
  for i in range(0, 9):
    if i%2 == 0:
      place_marker(1, i)
    else:
      place_marker(2, i)
      
    board_layout()

def get_location(position):

  row = int((position-1)/3)
  col = (position-1)%3
  
  if position > 9:
    print("Please enter a valid position")
    return None

  return [row, col]


def main():
  print("Welcome!!")
  show_position()

  game_logic()

  # Our next goal is to place elements
  

if __name__ == "__main__":
  main()