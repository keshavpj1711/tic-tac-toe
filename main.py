import sys

# Creating a 2d array to hold the 3x3 matrix
rows, cols = (3, 3)
board = [[0 for i in range(cols)] for j in range(rows)]

# To show the numerical position to all the users
def show_position():
  for i in range(0, 3):
    for j in range(0, 3):
      board[i][j] = (i*3)+(j+1)

  board_layout()

  # after showing we need to wipe all the position to " "
  for i in range(0, 3):
    for j in range(0, 3):
      board[i][j] = " "  


# To show the board 
def board_layout():
  print()
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
  print("-----------")
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
  print("-----------")
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")
  print()


# Checking if the place is available or occupied
def is_place_available(position):
  if board[position[0]][position[1]] != " ":
    return False
  
  return True


def check_win(m, position):
  x = position[0] # getting row info
  y = position[1] # getting column info

  # Checking row
  for i in range(0, 3):
    if board[x][i] != m:
      break
    if i == 2:
      print(f"{m} wins")
      sys.exit()

  # Checking col
  for i in range(0, 3):
    if board[i][y] != m:
      break
    if i == 2:
      print(f"{m} wins")
      sys.exit()

  # Checking diagonal
  if x == y:
    for i in range(0, 3):
      if board[i][i] != m:
        break
      if i == 2:
        print(f"{m} wins")
        sys.exit()

  # Checking anti diagonal
  if x+y == 2:
    for i in range(0, 3):
      if board[i][2-i] != m:
        break
      if i == 2:
        print(f"{m} wins")
        sys.exit()


# This is to place the marker in the required position according to the player
def place_marker(player):
  # Setting up marker for different players
  marker = ''
  if player == 1:
    marker = 'X'
  else:
    marker = 'O'

  user_input = int(input(f"Player {player}({marker}) enter position: "))
  pos = get_location(user_input)

  # until user enters a correct place
  while is_place_available(pos) == False:
    print("Place already occupied")
    user_input = int(input(f"Player {player}({marker}) enter position: "))
    pos = get_location(user_input)

  board[pos[0]][pos[1]] = marker
  board_layout()
  check_win(marker, pos)


def get_location(position):
  row = int((position-1)/3)
  col = (position-1)%3
  
  if position > 9:
    print("Please enter a valid position")
    return 

  return [row, col]


def game_logic():
  for i in range(0, 9):
    if i%2 == 0:
      place_marker(1)
    else:
      place_marker(2)

    if i == 8:
      print("It's a draw!!")


def main():
  print("\n----Tic-Tac-Toe----\n")
  show_position()

  game_logic()
  

if __name__ == "__main__":
  main()