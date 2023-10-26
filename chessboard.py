from field import field
from dicts import *
from piece import *
import time


def ValidInput():
    while(True):
        w = input("Podaj pole docelowe: ")
        if(len(w)!=2): 
            print(errors["BadInput"])
        elif((96<ord(w[0])<105) and (47<ord(w[1])<56)):
            return w[0],int(w[1])
        else:print(errors["BadInput"])
    


class chessboard:
    def __init__(self):
        self.board = [[field(col,row) for col in range(8)] for row in range(8)]
        self.tmpBoard = None
        self.move_count = 0
        self.whiteIsInMate = False
        self.whiteIsInChechMate = False
        self.blackIsInMate = False
        self.blackIsInChechMate = False
        self.moves = []
        self.attacks = []
        self.gameState = 0
    



    # for now only white oreientation is designed
    def translateMoveTo01(self,x,y):
        col = xWhiteTranslation[x]
        row = 8-y
        return row, col


        #todo
    def CheckForCheckMateOrMate(self):
        pass

# def ValidInput():
#     while(True):
#         w = input("Podaj pole docelowe: ")
#         if(len(w)!=2): 
#             print(errors["BadInput"])
#         elif((96<ord(w[0])<105) and (47<ord(w[1])<56)):
#             return w[0],int(w[1])
#         else:print(errors["BadInput"])

    def InputValue(self, moves = None):
        # returns transformed value fo user data
            
        inp = None
        while(True):
            
            cls()
            self.printBoard()
            if self.move_count%2 is 0: col = colors["white"]
            else: col = colors["black"]
            
            print(f'Kolor Gracza: {col}')
            inp = input(strings["chosingFigureInput"])
            if(len(inp)!=2): 
                print(errors["BadInput"])
                time.sleep(2)
            elif((96<ord(inp[0])<105) and (47<ord(inp[1])<56)):
                if(moves):
                    x,y = self.translateMoveTo01(inp[0],int(inp[1]))
                    for a in moves:
                        if(a[0]==x and a[1]==y): 
                            return self.translateMoveTo01(inp[0],int(inp[1]))
                else: return self.translateMoveTo01(inp[0],int(inp[1]))
            else:
                print(errors["BadInput"])
                time.sleep(2)
            
        
    #done
    def newBoard(self):
        for a in range(8):
            for b in range(8):
                if(a == 1):
                    self.board[a][b].setFieldOcupant(Pawn(a,b,colors["black"]))
                if(a == 6):
                    self.board[a][b].setFieldOcupant(Pawn(a,b,colors["white"]))
                if(a == 0):
                    if(b in [0,7]):
                        self.board[a][b].setFieldOcupant(Rock(a,b,colors["black"]))
                    elif(b in [1,6]):
                        self.board[a][b].setFieldOcupant(Knight(a,b,colors["black"]))
                    elif(b in [2,5]):
                        self.board[a][b].setFieldOcupant(Bishop(a,b,colors["black"]))
                    elif(b == 3):
                        self.board[a][b].setFieldOcupant(Queen(a,b,colors["black"]))
                    elif(b == 4):
                        self.board[a][b].setFieldOcupant(King(a,b,colors["black"]))
                
                if(a == 7):
                    if(b in [0,7]):
                        self.board[a][b].setFieldOcupant(Rock(a,b,colors["white"]))
                    elif(b in [1,6]):
                        self.board[a][b].setFieldOcupant(Knight(a,b,colors["white"]))
                    elif(b in [2,5]):
                        self.board[a][b].setFieldOcupant(Bishop(a,b,colors["white"]))
                    elif(b == 3):
                        self.board[a][b].setFieldOcupant(Queen(a,b,colors["white"]))
                    elif(b == 4):
                        self.board[a][b].setFieldOcupant(King(a,b,colors["white"]))

    


    #done
    def CheckIfMoveFromFieldIsPossible(self,x,y):
        if(self.board[x][y].isEmpty()):                                      #check if field is empty
            print(errors["FieldIsEmpty"])
            return False
        if(self.move_count%2==0 and self.board[x][y].getColorOfFigure() == 'b' #check if field contains current player figure
           or self.move_count%2==1 and self.board[x][y].getColorOfFigure() == 'w'):
            print(errors["ChoosingEnemyFigure"])
            return False
        if(self.board[x][y].DefendingKing()):                              #check if current figure is blocking kign from attack
            print(errors["PieceIsDefendingKing"])
            return False
        return True
    


    def RenderPossibleMoves(self,x,y):
        figure = self.board[x][y].getFigure()
        self.board , self.moves, self.attacks = figure.ReturnPossibleMoves(self.board)



    def moveFromAtoB(self,x1,y1,x2,y2):
        self.board[x2][y2].setFieldOcupant(self.board[x1][y1].getFigure())
        self.board[x1][y1].removeFieldOcupant()



    def removePosibleMovesFromBoard(self):
        self.moves = []
        self.attacks = []



    def Move(self,x,y):

        chosen_move = None
        x_dest = None
        y_dest = None
        p = True

        if not(self.CheckIfMoveFromFieldIsPossible(x,y)): return 
            
        self.RenderPossibleMoves(x,y)

        while(p):
            cls()
            self.printBoard(self.tmpBoard)
            x_dest,y_dest = ValidInput() # przerobienie na 2 funckjew 1 
            x_dest,y_dest = self.translateMoveTo01(x_dest,y_dest)
            for a in self.moves:
                if(a[0] == x_dest and a[1] == y_dest): 
                    chosen_move = a
                    p = False
        if(self.board[x][y].getFigure().getFigChar() == PiecesDict["King"]): 
            self.board[x][y].setMovesToTrue()
        self.moveFromAtoB(x,y,chosen_move[0],chosen_move[1])
        self.removePosibleMovesFromBoard()
        self.move_count+=1
        


    def startGame(self):
        self.gameState = 1
        while(self.gameState == 1):
            cls()
            x,y = self.InputValue()    
            self.Move(x,y)
        


    #temp printing method
    # dopisanie różnych wartości wypisywania gdy koordynaty pasują do moves[] and attacks[]

    def printBoard(self, board = None):
        if(board == None): board = self.board
        dl = len(board)
        let = ["a","b","c","d","e","f","g","h"]
        num = [8,7,6,5,4,3,2,1]
        
        #test printing


        let.reverse()
        for a in range(dl):
            print(num[a], end="")    
            for b in range(dl):
                if((a,b) in self.moves):
                    print(f'|ooooooooooooooooo|', end="")    
                elif((a,b) in self.attacks):
                    print(f'|xxxxxxxxxxxxxxxxx|', end="")
                else:
                    fig = board[a][b].getFigure()
                    if(fig):
                        print(f'|FC: {fig.getFigAndCol()} xy: {fig.getCordinates()}|', end="")
                    else:
                        print(f'|-----------------|', end="")
            
            print()
        print(f' |aaaaaaaaaaaaaaaaa||bbbbbbbbbbbbbbbbb||ccccccccccccccccc||ddddddddddddddddd||eeeeeeeeeeeeeeeee||fffffffffffffffff||ggggggggggggggggg||hhhhhhhhhhhhhhhhh|')
        

        


    