## minesweeper.py




grid1 = [[True ,False,False],
           [False,False,False],
           [False,False,True]]

board2 = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

board1 = [[' ', '1', '0'],
          ['1', '2', '1'],
          ['0', '1', ' ']]


def game_lost(board):
    mined_rows = len(list(filter(lambda row: '*' in row, board)))
    return mined_rows != 0


def row_won(grid,board,row,col):
    width = len(grid[0])
    if col == width:
        return True
    else:
         
        cell = (grid[row][col]and board[row][col] == ' ')\
            or(not grid[row][col] and board[row][col] != ' ')
        return cell and row_won(grid,board,row,col+1)
    
    
def all_won(grid,board,row) :
    height= len(grid)
    if(row==height):
        return True
    else:
        return row_won(grid,board,row,0)and all_won(grid,board,row+1) 




def game_won(grid,board):
    if game_lost(board):
        return False
    else:
        return all_won(grid,board,0)


# reveal(grid,board, row, col) reveals the tile at the given row and col(umn)
#   in board, using the mine positions from grid
# reveal: MineGrid MineBoard -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# effects: board is mutated

def reveal(grid,board,row,col):
    if grid[row][col]:
        board[row][col] = '*'
    else:
        board[row][col] = str(count_mines(grid,row,col))


def has_mine(grid,row,col):
    h = len(grid)
    w = len(grid[0])
    if row >= 0 and row < h and col >= 0 and col < w and grid[row][col]:
        return 1
    else:
        return 0    
    

def count_mines(grid,row,col):
    return has_mine(grid,row-1,col-1) +\
           has_mine(grid,row-1,col) +\
           has_mine(grid,row-1,col+1) +\
           has_mine(grid,row,col-1) +\
           has_mine(grid,row,col+1) +\
           has_mine(grid,row+1,col-1) +\
           has_mine(grid,row+1,col) +\
           has_mine(grid,row+1,col+1)













# reveal(grid,board, row, col) reveals the tile at the given row and col(umn)
#   in board, using the mine positions from grid
# reveal: MineGrid MineBoard -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# effects: board is mutated



def reveal(grid,board,row,col):
    if grid[row][col]:
        board[row][col] = '*'
    else:
        board[row][col] = str(count_mines(grid,row,col))

# game_lost(board) returns true if board contains one or more revealed mines,
#   false otherwise
# game_lost: GameBoard -> Bool

def game_lost(board):
    mined_rows = len(list(filter(lambda row: '*' in row, board)))
    return mined_rows != 0

row_prompt = "Please enter a row number: "
col_prompt = "Please enter a column number: "
range_error = "Value out of range!"

# read_pos(limit,prompt) prompts the user using the given prompt, and then 
#   reads an int.  If int is not in range 0 .. limit-1 then prompt and read
#   are repeated, otherwise the read value is returned
# read_pos: Nat Str -> Nat
# requires: limit > 0
# effects: input and output

def read_pos(limit,prompt):
    n = int(input(prompt))
    if n < 0 or n >= limit:
        print(range_error)
        return read_pos(limit,prompt)
    else:
        return n

# draw_board(board) prints the board to the screen
# draw_board: MineBoard -> None
# effects: prints to screen

def draw_board(board):
    print("\n".join(map(lambda row: "".join(row),board)))

# make_board(width,height) returns a MineBoard with all tiles hidden, 
#   the board has "height" rows and "width" columns
# make_board: Nat Nat -> MineBoard
# requires: width, height are positive

def make_board(width,height):
    
    return list(map(lambda i: [' '] * width, range(height)))

# play_minesweeper(grid) plays a game of minesweeper, using grid for the mine
#   positions
# play_minesweeper: MineGrid -> None
# effects: reads input, prints to the screen

def play_minesweeper(grid):
    height = len(grid)
    width = len(grid[0])
    board = make_board(width,height)
    play_game(grid,board)

# play_game(grid,board) plays a game of minesweeper, using grid for the mine 
#   positions, and board as the current visible tiles
# play_game: MineGrid MineBoard -> None
# requires: grid and board are consistent
# effects: reads input, prints to the screen
    
def play_game(grid,board):
    height = len(grid)
    width = len(grid[0])
    print("="*width)
    draw_board(board)
    print("="*width)
    win = game_won(grid,board)
    lose = game_lost(board)
    if win:
        print("Game over, you win!")
    elif lose:
        print("Game over, you lose!")
    else:
        row = read_pos(height,row_prompt)
        col = read_pos(width,col_prompt)        
        reveal(grid,board,row,col)
        play_game(grid,board)
import random
def new_game(size, n):
    if n > size * size:
        print("You cannot put more mines than available spaces!")
        return
    
    # Randomly choose n mines
    mines = []
    i = 0
    while i < n:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in mines:
            mines.append((row, col))
            i += 1
    
    # Generate game grid
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[i].append((i, j) in mines)
    
    # Start a new game
    play_minesweeper(grid)
    print("Mines are at", mines)
    
    
    
    
    
