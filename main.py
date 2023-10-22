
PiecesDict = {
    "Pawn":'p',
    "Bishop":'b',
    "Knight":'n',
    "Rock":'r',
    "Queen":'q',
    "King":'k'
    

}
colors = {
    "black":'b',
    "white":'w'
}

xWhiteTranslation = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
}

xBlackTranslation = {
    'a':7,
    'b':6,
    'c':5,
    'd':4,
    'e':3,
    'f':2,
    'g':1,
    'h':0,
}

errors = {
    "FieldIsEmpty":"To pole jest puste",
    "ChoosingEnemyFigure":"Figura na tym polu należy do przeciwnika",
    "KingInDanger":"Twój król jest zagrożony",
    "PieceIsDefendingKing":"Dana figura broni króla",
    "BadInput":"Podane pole nie istnieje"
}

def ValidInput():
    while(True):
        w = input("Podaj pole docelowe: a3")
        if(len(w)!=2): 
            print(errors["BadInput"])
        elif((96<ord(w[0])<105) and (47<ord(w[1])<56)):
            return w[0],int(w[1])
        else:print(errors["BadInput"])
    

# choose x,y
# show possible moves
# allow to choose where to go
# check if move is correct
# if move is correct move/attack
# move figure to destination
# check for cheks/mates
# 


class field:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.figure = None
        self.figureColor = None
        self.isDefendingKing = False
        self.isChossen = False
        self.possibleMove = False
        
    def setFieldOcupant(self, fig, figCol):
        self.figure = fig
        self.figureColor = figCol
    
    def removeFieldOcupant(self):
        self.figure = None
        self.figureColor = None

    def getPieceAndColor(self):
        if(self.figure!=None):
            #print(self.figure, " " ,self.figureColor)
            return self.figure+self.figureColor
        elif(self.possibleMove):
            return "oo"
        else:
            return "  "
    
    def setpossibleMove(self): self.possibleMove = True

    def isEmpty(self): 
        if(self.figure == None): return True

    def getFigure(self): return self.figure

    def getColorOfFigure(self): return self.figureColor

    def DefendingKing(self): return self.isDefendingKing

    def isFieldChosen(self): return self.isChossen
    

class chessboard:
    def __init__(self):
        self.board = [[field(row,col) for col in range(8)] for row in range(8)]
        self.tmpBoard = None
        self.move_count = 0
        self.whiteIsInMate = False
        self.whiteIsInChechMate = False
        self.blackIsInMate = False
        self.blackIsInChechMate = False
        self.moves = []
    



    # for now only white oreientation is designed
    def translateMoveTo01(self,x,y):
        col = xWhiteTranslation[x]
        row = 8-y
        return row, col


    def newBoard(self):
        for a in range(8):
            for b in range(8):
                if(a == 1):
                    self.board[a][b].setFieldOcupant(PiecesDict["Pawn"],colors["black"])
                if(a == 6):
                    self.board[a][b].setFieldOcupant(PiecesDict["Pawn"], colors["white"])
                if(a == 0):
                    if(b in [0,7]):
                        self.board[a][b].setFieldOcupant(PiecesDict["Rock"],colors["black"])
                    elif(b in [1,6]):
                        self.board[a][b].setFieldOcupant(PiecesDict["Knight"],colors["black"])
                    elif(b in [2,5]):
                        self.board[a][b].setFieldOcupant(PiecesDict["Bishop"],colors["black"])
                    elif(b == 3):
                        self.board[a][b].setFieldOcupant(PiecesDict["Queen"],colors["black"])
                    elif(b == 4):
                        self.board[a][b].setFieldOcupant(PiecesDict["King"],colors["black"])
                
                if(a == 7):
                    if(b in [0,7]):
                        self.board[a][b].setFieldOcupant(PiecesDict["Rock"],colors["white"])
                    elif(b in [1,6]):
                        self.board[a][b].setFieldOcupant(PiecesDict["Knight"],colors["white"])
                    elif(b in [2,5]):
                        self.board[a][b].setFieldOcupant(PiecesDict["Bishop"],colors["white"])
                    elif(b == 3):
                        self.board[a][b].setFieldOcupant(PiecesDict["Queen"],colors["white"])
                    elif(b == 4):
                        self.board[a][b].setFieldOcupant(PiecesDict["King"],colors["white"])

    #todo
    def CheckForCheckMateOrMate(self):
        pass

    def CheckIfMoveFromFieldIsPossible(self,x,y):
        if(self.board[x][y].isEmpty()):                                      #check if field is empty
            print(errors["FieldIsEmpty"])
            return False
        if(self.move_count%2==0 and self.board[x][y].getColorOfFigure == 'b' #check if field contains current player figure
           or self.move_count%2==1 and self.board[x][y].getColorOfFigure == 'w'):
            print(errors["ChoosingEnemyFigure"])
            return False
        if(self.board[x][y].DefendingKing()):                              #check if current figure is blocking kign from attack
            print(errors["PieceIsDefendingKing"])
            return False
        return True
    
    def RenderPosibleMovesOnTmpBoard(self,x,y):
        figure = self.tmpBoard[x][y].getFigure()
        self.moves = []
        if(figure == PiecesDict["Pawn"]):
            for a in range(2):
                if(self.tmpBoard[x-(a+1)][y].isEmpty()):
                    self.tmpBoard[x-(a+1)][y].setpossibleMove()
                    self.moves.append((x-(1+a),y))
        elif(figure == PiecesDict["Bishop"]):
            pass
        elif(figure == PiecesDict["Knight"]):
            pass
        elif(figure == PiecesDict["Rock"]):
            pass
        elif(figure == PiecesDict["Queen"]):
            pass
        elif(figure == PiecesDict["King"]):
            pass

    def RenderBoardWithPossibleMoves(self,x,y):
        self.tmpBoard = self.board
        self.RenderPosibleMovesOnTmpBoard(x,y)
        self.printBoard(self.tmpBoard)



    def Move(self,x,y):
        chs_move = None
        x_dest = None
        y_dest = None
        p=True
        x,y = self.translateMoveTo01(x,y)
        if(self.CheckIfMoveFromFieldIsPossible(x,y)):
            self.RenderBoardWithPossibleMoves(x,y)
            while(p == True):
                x_dest,y_dest = ValidInput()
                x_dest,y_dest = self.translateMoveTo01(x_dest,y_dest)
                for a in self.moves:
                    if(a[0] == x_dest and a[1] == y_dest): 
                        chs_move = a
                        p = False
            fig = self.board[x][y].getFigure()
            figCol = self.board[x][y].getColorOfFigure()
            self.board[x_dest][y_dest].setFieldOcupant(fig,figCol)
            self.board[x][y].removeFieldOcupant()





    #temp printing method
    def printBoard(self, board = None):
        if(board == None): board = self.board
        dl = len(board)
        print("printing board")
        for a in range(dl):
            for b in range(dl):
                print(board[a][b].getPieceAndColor(), end="")
            print()

        print("end of printing board")




    def readState(self, tab):
        pass
    



    


cb = chessboard()
cb.newBoard()
cb.printBoard()
# cb.AttempAMove('a',4)
# cb.AttempAMove('a',1)

cb.Move('a',2)
cb.printBoard()

