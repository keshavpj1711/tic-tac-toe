# Creating a 2d array to hold the 3x3 matrix
rows, cols = (3, 3)
board = [[0 for i in range(cols)] for j in range(rows)]


def board_layout():
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
  print("-----------")
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
  print("-----------")
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

game_logic()

def main():
  pass

if __name__ == "__main__":
  main()