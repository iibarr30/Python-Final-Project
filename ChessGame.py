import pygame, sys
from pygame.locals import QUIT

from piece import Piece
from pieceMoves import *
from pieceMoves import select_moves
from pieceMoves import order
#from board import Board
#from board import *
 


WIDTH = 500
HEIGHT = 500
TILESIZE = 400/8
ROWS = 8
COLS = 8
BOARD_POS = (0,0)

#RGB COLORS
GREEN = (0,255,0)
BROWNL = (186, 140, 99)
BROWND = (102, 51, 0)

DISPLAY_SURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")



class Board:
      def __init__(self, row, col, width):
        self.color = BROWNL
        self.col = col
        self.row = row
        self.x = int(row * width)
        self.y = int(col * width)
        

  
      def draw(self, DISPLAY_SURF):
        pygame.draw.rect(DISPLAY_SURF, self.color, (self.x, self.y, WIDTH/8, WIDTH/8))

  
      def setup(self, DISPLAY_SURF):
        if order[(self.row, self.col)]:
            if order[(self.row, self.col)] == None:
                pass
            else:
                DISPLAY_SURF.blit(order[(self.row, self.col)], (self.x, self.y))

def make_grid(rows, width):
    grid = []
    space = WIDTH//rows
    print(space)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            board1 = Board(j, i, space)
            grid[i].append(board1)
            if (i+j)%2 == 1:
                grid[i][j].color = BROWND
    return grid


def draw_grid(DISPLAY_SURF, rows, width):
    space = width//8
    for i in range(rows):
        pygame.draw.line(DISPLAY_SURF, BROWND, (0, i * space), (width, i * space))
        for j in range(rows):
            pygame.draw.line(DISPLAY_SURF, BROWND, (j * space, 0), (j * space, width))




def update_display(win, grid, rows, width):
    for row in grid:
        for area in row:
            area.draw(win)
            area.setup(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def Find_Board(pos, WIDTH):
    interval = WIDTH / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    return int(rows), int(columns)


def display_potential_moves(positions, grid):
    for i in positions:
        x, y = i
        grid[x][y].color = GREEN



def Do_Move(OriginalPos, FinalPosition, DISPLAY_SURF):
    order[FinalPosition] = order[OriginalPos]
    order[OriginalPos] = None


def remove_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].color = BROWNL
            else:
                grid[i][j].color = BROWND
    return grid

  


create_board(board)



def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILESIZE) for v in mouse_pos]
    try: 
        if (x >= 0) and (y >= 0): 
          return (board[y][x], x, y)
    except IndexError: 
      pass
    return None, None, None

  
def draw_selector(screen, piece, x, y):
    if piece != None:
        rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)


def draw_drag(screen, board, selected_piece):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x != None:
            rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)

        s1 = selected_piece[0]
        s2 = selected_piece[0]
        pos = pygame.Vector2(pygame.mouse.get_pos())
        screen.blit(s2, s2.get_rect(center=pos + (1, 1)))
        screen.blit(s1, s1.get_rect(center=pos))
        selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.line(screen, pygame.Color('red'), selected_rect.center, pos)
        return (x, y)




def main():
    pieceToMove=[]
    moves = 0
    selected_piece = None
    selected = False
    grid = make_grid(8, WIDTH)
    #clock = pygame.time.Clock()

  
    while True:
        piece, x, y = get_square_under_mouse(board)
        events = pygame.event.get()
        for e in events:
        #for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
                #pygame.quit()
                #sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
              #if piece != None:
                selected_piece = piece, x, y
                pos = pygame.mouse.get_pos()
                draw_selector(DISPLAY_SURF, piece, x, y)
                y, x = Find_Board(pos, WIDTH)
                if selected == False:
                    try:
                        possibleP = select_moves((board[x][y]), (x,y), moves)
                        for positions in possibleP:
                            row, col = positions
                            grid[row][col].color = GREEN
                        pieceToMove = x,y
                        selected = True
                    except:
                        pieceToMove = []
                else:
                    try:
                        if board[x][y].validP == True:
                            row, col = pieceToMove 
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), DISPLAY_SURF)
                            moves = moves+1
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                    except:
                        if board[x][y] == 'x ':
                            row, col = pieceToMove
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), DISPLAY_SURF)
                            moves = moves+1
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                    selected = False
            #if e.type == pygame.MOUSEBUTTONUP:
                #if drop_pos:
                    #piece, old_x, old_y = selected_piece
                    #board[old_y][old_x] = 0
                    #new_x, new_y = drop_pos
                    #board[new_y][new_x] = piece
                #selected_piece = None
                #drop_pos = None

            update_display(DISPLAY_SURF, grid, 8, WIDTH)
            #check(board, moves, bkingpos, wkingpos, possiblemovesw, possiblemovesb)
            #checkmate(board, moves)
            #drop_pos = draw_drag(DISPLAY_SURF, board, selected_piece)
            #clock.tick(60)

if __name__ == '__main__':
    main()
