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
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
  print("-----------")
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
  print("-----------")
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


# Checking if the place is available or occupied
def is_place_available(position):
  if board[position[0]][position[1]] != " ":
    return False
  
  return True


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


def get_location(position):
  row = int((position-1)/3)
  col = (position-1)%3
  
  if position > 9:
    print("Please enter a valid position")
    return 

  return [row, col]


def main():
  print("Welcome!!")
  show_position()

  # Our next goal is to place elements
  

if __name__ == "__main__":
  main()