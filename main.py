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


def game_logic():
  pass


def main():
  print("Welcome!!")
  show_position()

  # Our next goal is to place elements
  

if __name__ == "__main__":
  main()