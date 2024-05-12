def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def is_valid_move(grid, row, col, num):
    # Check if num is not repeated in the same row
    if num in grid[row]:
        return False
    
    # Check if num is not repeated in the same column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check if num is not repeated in the same 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    row, col = find_empty_cell(grid)
    if row is None and col is None:
        return True  # Puzzle is solved
    
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack if the current number leads to a contradiction
    
    return False  # No valid number found for the current cell

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Example usage:
# Define the Sudoku grid (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Input Sudoku grid:")
print_grid(sudoku_grid)
print("\nSolving Sudoku...\n")

if solve_sudoku(sudoku_grid):
    print("Sudoku solved successfully:")
    print_grid(sudoku_grid)
else:
    print("No solution exists for the Sudoku puzzle.")
