import numpy as np

def print_sudoku(sudoku):
  """Print sudoku board on standard output"""
  i = 0
  for row in sudoku:
    j = 0
    if i % 3 == 0:
      print("|-------|-------|-------|")
    for number in row:
      if j % 3 == 0:
        print("|", end=" ")
      print(number if number != 0 else ".", end=" ")
      j += 1
    print("|")
    i += 1
  print("|-------|-------|-------|")
  
def solve_sudoku(sudoku, current_col = 0, current_row = 0):
  """Solve sudoku with backtracking"""
  next_col = current_col
  next_row = current_row
  # Success
  if current_col == 8 and current_row == 8:
    if sudoku.sum() == 405:
      return True
  elif current_col == 8:
    next_col = 0
    next_row = current_row + 1
  else:
    next_col = current_col + 1
  
  # Empty cell
  if sudoku[current_row,current_col] == 0:
    # Check numbers
    for number in range(1,10):
      if can_place(sudoku,number,current_col,current_row):
        sudoku[current_row,current_col] = number
        if solve_sudoku(sudoku,next_col,next_row):
          return True
        # Failure
        sudoku[current_row,current_col] = 0
    return False
  else:
    return solve_sudoku(sudoku,next_col,next_row)

def can_place(sudoku,number,pos_x,pos_y):
  """Check if number can be placed"""
  # Check row
  if number in sudoku[pos_y]:
    return False
  # Check column
  if number in sudoku[:,pos_x]:
    return False
  # Top left coordinates of surrounding 3x3 square
  square_x = (pos_x // 3) * 3
  square_y = (pos_y // 3) * 3
  # Check 3x3 square
  if number in sudoku[square_y:square_y+3,square_x:square_x+3]:
    return False
  return True



print("Enter sudoku row by row separated with spaces (Enter 0 for empty spaces):")
sudoku = []
row_num = 0
while row_num < 9:
  row = input().split()
  row = list(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9'], row))
  if len(row) > 9:
    print("Too many numbers in row. Try again.")
    continue  
  if len(row) < 9:
    print("Too few numbers in row. Try again.")
    continue
  row_num += 1
  sudoku.append(list(map(int,row)))

sudoku = np.array(sudoku)

print("---------------------")
print("Your sudoku:")
print_sudoku(sudoku)
print("---------------------")
print("Solving...")
solve_sudoku(sudoku)
print("---------------------")
print("Solution:")
if sudoku.sum() != 405:
  print("ERROR! Possibly a sudoku rule is broken!")
else:
  print_sudoku(sudoku)
