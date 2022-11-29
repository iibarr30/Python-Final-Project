import pygame
from piece import Piece



              #team, type, image
bbish = Piece('b', 'b', 'images/bishopb.png')
wbish = Piece('w', 'b', 'images/bishopw.png')
bqueen = Piece('b', 'q', 'images/queenb.png')
wqueen = Piece('w', 'q', 'images/queenw.png')
bkn = Piece('b', 'kn', 'images/knightb.png')
wkn = Piece('w', 'kn', 'images/knightw.png')
bpawn = Piece('b', 'p', 'images/pawnb.png')
wpawn = Piece('w', 'p', 'images/pawnw.png')
bking = Piece('b', 'k', 'images/kingb.png')
wking = Piece('w', 'k', 'images/kingw.png')
brook = Piece('b', 'r', 'images/rookb.png')
wrook = Piece('w', 'r', 'images/rookw.png')


#order = {(board[0][0]): pyagame.image.load(brook.image), (1,0):
        #pygame.image.load(bkn.image),
        #()
        #}

board = [["  " for i in range(8)] for i in range(8)]


order = {(0, 0): pygame.image.load(brook.image), (1, 0): pygame.image.load(bkn.image),
                  (2, 0): pygame.image.load(bbish.image), (3, 0): pygame.image.load(bking.image),
                  (4, 0): pygame.image.load(bqueen.image), (5, 0): pygame.image.load(bbish.image),
                  (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(brook.image),
                  (0, 1): pygame.image.load(bpawn.image), (1, 1): pygame.image.load(bpawn.image),
                  (2, 1): pygame.image.load(bpawn.image), (3, 1): pygame.image.load(bpawn.image),
                  (4, 1): pygame.image.load(bpawn.image), (5, 1): pygame.image.load(bpawn.image),
                  (6, 1): pygame.image.load(bpawn.image), (7, 1): pygame.image.load(bpawn.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  (0, 6): pygame.image.load(wpawn.image), (1, 6): pygame.image.load(wpawn.image),
                  (2, 6): pygame.image.load(wpawn.image), (3, 6): pygame.image.load(wpawn.image),
                  (4, 6): pygame.image.load(wpawn.image), (5, 6): pygame.image.load(wpawn.image),
                  (6, 6): pygame.image.load(wpawn.image), (7, 6): pygame.image.load(wpawn.image),
                  (0, 7): pygame.image.load(wrook.image), (1, 7): pygame.image.load(wkn.image),
                  (2, 7): pygame.image.load(wbish.image), (3, 7): pygame.image.load(wking.image),
                  (4, 7): pygame.image.load(wqueen.image), (5, 7): pygame.image.load(wbish.image),
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wrook.image),}




def create_board(board):
  
    board[0] = [Piece('b', 'r', 'rookb.png'), Piece('b', 'kn', 'knightb.png'), Piece('b', 'b', 'bishopb.png'), \
               Piece('b', 'q', 'queenb.png'), Piece('b', 'k', 'kingb.png'), Piece('b', 'b', 'bishopb.png'), \
               Piece('b', 'kn', 'knightb.png'), Piece('b', 'r', 'rookb.png')]
    board[7] = [Piece('w', 'r', 'rookw.png'), Piece('w', 'kn', 'knightw.png'), Piece('w', 'b', 'bishopw.png'), \
               Piece('w', 'q', 'queenw.png'), Piece('w', 'k', 'kingw.png'), Piece('w', 'b', 'bishopw.png'), \
               Piece('w', 'kn', 'knightw.png'), Piece('w', 'r', 'rookw.png')]
  
    for i in range(8):
        board[1][i] = Piece('b', 'p', 'pawnb.png')
        board[6][i] = Piece('w', 'p', 'pawnw.png')
    return board





def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x ':
                board[row][column] = '  '
            else:
                try:
                    board[row][column].validP = False
            
                except:
                    pass



      
def highlight(board):
  #will show valid move options for piece
    highlightP = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                highlightP.append((i, j))
            else:
                try:
                    if board[i][j].validP:
                        highlightP.append((i, j))
                except:
                    pass
    return highlightP

def check_team(moves, index):
  #check the piece and see which team is is on
    row, col = index
    if moves%2 == 0:
        if board[row][col].team == 'w':
            return True
    else:
        if board[row][col].team == 'b':
            return True


def select_moves(piece, index, moves):
  #all possible moves for each different pieces
    if check_team(moves, index):
        if piece.type == 'p':
            if piece.team == 'b':
                return highlight(pawn_moves_b(index))
            else:
                return highlight(pawn_moves_w(index))

        if piece.type == 'k':
            return highlight(king_moves(index))

        if piece.type == 'r':
            return highlight(rook_moves(index))

        if piece.type == 'b':
            return highlight(bishop_moves(index))

        if piece.type == 'q':
            return highlight(queen_moves(index))

        if piece.type == 'kn':
            return highlight(knight_moves(index))



def pawn_moves_b(index):
    if index[0] == 1:
        if board[index[0] + 2][index[1]] == '  ' and board[index[0] + 1][index[1]] == '  ':
            board[index[0] + 2][index[1]] = 'x '
    bottom = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

    for positions in bottom:
            if bottom.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'b':
                        board[positions[0]][positions[1]].validP = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

def pawn_moves_w(index):
    if index[0] == 6:
        if board[index[0] - 2][index[1]] == '  ' and board[index[0] - 1][index[1]] == '  ':
            board[index[0] - 2][index[1]] = 'x '
    top = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

    for positions in top:
            if top.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'w':
                        board[positions[0]][positions[1]].validP = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board


def king_moves(index):
    for y in range(3):
        for x in range(3):
                if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                    board[index[0] - 1 + y][index[1] - 1 + x] = "x "
                
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                        board[index[0] - 1 + y][index[1] - 1 + x].validP = True
    return board


def rook_moves(index):
    cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
             [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
             [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
             [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

    for direction in cross:
        for positions in direction:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].validP = True
                    break
    return board

def bishop_moves(index):
    diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                 [[index[0] + i, index[1] - i] for i in range(1, 8)],
                 [[index[0] - i, index[1] + i] for i in range(1, 8)],
                 [[index[0] - i, index[1] - i] for i in range(1, 8)]]

    for direction in diagonals:
        for positions in direction:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].validP = True
                    break
    return board



def knight_moves(index):
    moves = [[2,1], [-2,1], [-2,-1], [2,-1], [1,2], [-1,2], [-1,-2], [1,-2]]
    ok_moves = []
    for x in moves:
        if   index[0] + x[0] >= 0 and   index[0] + x[0] <= 7:
            if  index[1] + x[1] >= 0 and   index[1] + x[1] <= 7:
                ok_moves.append([x[0],x[1]])
    for x in ok_moves:  
        if board[index[0] + x[0]][index[1] + x[1]] == '  ':
            board[index[0] + x[0]][index[1] + x[1]] = 'x '
        else: 
            if board[index[0] + x[0]][index[1] + x[1]].team != board[index[0] + x[0]][index[1] + x[1]].team:    
                board[index[0] + x[0]][index[1] + x[1]].validP = True
    return board



def queen_moves(index):
  #queen move is same as bishop and rook moves
    board = rook_moves(index)
    board = bishop_moves(index)
    return board



possiblemovesw = []
possiblemovesb = []
bkingpos = []
wkingpos = []
def check(board,moves,bkingpos,wkingpos,possiblemovesw,possiblemovesb):
  
  for row in board:
    for col in board:
      if board[bkingpos][wkingpos] != 'x ':
        if Piece.team == 'b' and Piece.type != 'k':
          possiblemovesb.append(select_moves(Piece.type, board[row][col], moves))
        if Piece.team == 'w' and Piece.type != 'k':
          possiblemovesw.append(select_moves(Piece.type, board[row][col], moves))
      if board[row][col] == bking:
        bkingpos = [row,col]
        possiblemovesb.append(select_moves('k',bkingpos,moves))
      elif board[row][col] == wking:
        possiblemovesw.append(select_moves('k',bkingpos,moves))
        wkingpos == [row,col]
  if wkingpos in possiblemovesb:
    return True,bkingpos,wkingpos;
  if bkingpos in possiblemovesw:
    return True,bkingpos,wkingpos;
  else:
    return False

def checkmate(board,moves):
  if check(board,moves,bkingpos,wkingpos,possiblemovesw,possiblemovesb) == True:
    kingmovesw = highlight(wkingpos)
    kingmovesb = highlight(bkingpos)
    if kingmovesw in possiblemovesb:
      return True
    if kingmovesb in possiblemovesw:
      return True
    else:
      return False
      
    #if select_moves('k', bkingpos, moves) in possiblemovesw:
      #return True
    #else:
     # return False
                   
def stalemate(board,moves):
    pass

