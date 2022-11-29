#create chess piece
class Piece:
  def __init__(self, team, type, image, validP=False):
    #team - which side is piece on
    #type - what kind of piece is it
    #image = to load image of piece
    #validP - to move is valid
    self.validP = validP
    self.image = image
    self.team = team
    self.type = type