from field import field
from dicts import *
from piece import *
import time


import logging
logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)

class chessboard:
    def __init__(self):
        self.board = [[field(col,row) for col in range(8)] for row in range(8)]
        self.tmpBoard = None
        self.move_count = 0
        self.whiteIsInMate = False
        self.whiteIsInChechMate = False
        self.blackIsInMate = False
        self.blackIsInChechMate = False
        self.winner = None
        self.moves = []
        self.attacks = []
        self.gameState = 1
        self.move = None
    


    def translateMoveTo01(self,x,y):
        return 8-y, xWhiteTranslation[x] 


        #todo
    def CheckForCheckMateOrMate(self):
        pass


    def checkRequiremtns(self, value):
        if(len(value)!=2): 
                logging.debug("value too long")
                print(errors["BadInput_ToLong"])
                time.sleep(2)
                return False
        if not((96<ord(value[0])<105) and (47<ord(value[1])<57)): 
            print(errors["BadInput_BadChars"])
            time.sleep(2)
            return False
        return True


    def checkForCodes(self, value):
        if(value == 'quit'): return 'q'
        if(value == 'save'): return 's'
        return 


    def ClearAndPrintBoard(self):
        print(f'Player Color: {"black" if self.move_count%2==1 else "white"}')
        

    def InputValue(self, code):
        while(True):
            self.ClearAndPrintBoard()

            inp = input(strings["chosingFigureInput"])
            codes = self.checkForCodes(inp)
            if inp in ['exit, stop, quit, q']:
                self.gameState = 2
                return
            
            
            if(self.checkRequiremtns(inp)): 
                x,y = self.translateMoveTo01(inp[0],int(inp[1]))
                if(code == 1):
                    return x,y
                if(code == 2):
                    if(self.moves):
                        for a in self.moves:
                            if(a[0]==x and a[1]==y): 
                                logging.debug(f'found move {x,y} in {self.moves}')
                                return x,y
                        else:
                            print(errors["BadInput_ToLong"])
                            time.sleep(2)
                            break        
                            logging.debug(f'did not found move {x,y} in {self.moves}')
                    else: print(f'nie ma dostepnych rochów, coś się zepsuło')
                    

    def newBoard(self):
        num = 0
        for a in range(8):
            if(a%2==1): num = 1
            else: num = 0
            for b in range(8):
                self.board[a][b].setBackGroundColor(colors["white"] if num%2==0 else colors["black"]) 
                num+=1
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

        Field = self.board[x][y]
        Figure = self.board[x][y].getFigure()

        logging.debug(f'CheckIfMoveFromFieldIsPossible(): attempting with {x,y} args')
        if(Field.isEmpty()):                                      #check if field is empty
            print(errors["FieldIsEmpty"])
            time.sleep(2)
            logging.debug(f'CheckIfMoveFromFieldIsPossible(): choosen field is empty')
            return False
        if(self.move_count%2==0 and Field.getColorOfFigure() == 'b' #check if field contains current player figure
           or self.move_count%2==1 and Field.getColorOfFigure() == 'w'):
            print(errors["ChoosingEnemyFigure"])
            time.sleep(2)
            logging.debug(f'CheckIfMoveFromFieldIsPossible(): choosen field is enemy color')
            return False
        if(Field.DefendingKing()):                              #check if current figure is blocking kign from attack
            print(errors["PieceIsDefendingKing"])
            time.sleep(2)
            return False

        return True
    

    # returns true if everythink fine, false when there is no move from that possition
    def GetPossibleMoves(self,x,y):
        figure = self.board[x][y].getFigure()
        logging.debug(f'RenderPossibleMoves(): choosen figure: {figure} moves and attacks before: {self.moves, self.attacks}')
        
        self.moves, self.attacks = figure.ReturnPossibleMoves(self.board)
        logging.debug(f'RenderPossibleMoves(): moves and attacks after: {self.moves, self.attacks}')
        return True

    

    def moveFromAtoB(self,x1,y1,x2,y2):
        self.board[x2][y2].setFieldOcupant(self.board[x1][y1].getFigure())
        self.board[x1][y1].removeFieldOcupant()

    def removePosibleMovesFromBoard(self):
        self.moves = []
        self.attacks = []




    

    def CheckForCastling(self, x,y, x_dest, y_dest):
        figure = self.board[x][y].getFigure()
        if(figure.getFigChar() is PiecesDict["Rock"] and figure.hasMoved == False):
            if(self.move_count%2==0):
                xCheck = 7
            else: xCheck = 0
            kingFig = self.board[xCheck][4]
            if(kingFig.getFigure() is PiecesDict["King"] and kingFig.hasMoved == False):
                kingX, kingY = kingFig.getCordinates()
                if(x_dest == xCheck and y_dest in [kingY+1,kingY-1]):
                    kingY2 = 0
                    if(kingY > y): kingY2 -= 2
                    else: kingY2 += 2
                    self.moveFromAtoB(x,y,x_dest,y_dest)
                    self.moveFromAtoB(kingX, kingY, kingX, kingY2)

        return False

    def Move(self):
        x,y = self.move
        logging.debug(f'Move(): attempting move() with {x,y}')

        

        chosen_move = None

        x_dest,y_dest = self.InputValue(2)
        for a in self.moves:
            if(a[0] == x_dest and a[1] == y_dest): 
                chosen_move = a
                break
        
        if not self.CheckForCastling(x,y,x_dest,y_dest):
            if(self.board[x][y].getFigure().getFigChar() in [PiecesDict["King"],PiecesDict["Rock"]]): 
                self.board[x][y].getFigure().setMovedToTrue()

            self.moveFromAtoB(x,y,chosen_move[0],chosen_move[1])
            self.removePosibleMovesFromBoard() 
            self.move_count+=1
        return True
        

    def CheckField(self,x,y):
        logging.debug(f'CheckField(): attempting with {x,y}')

        if not(self.CheckIfMoveFromFieldIsPossible(x,y)): return False
        logging.debug(f'CheckField(): move is possible')

        self.GetPossibleMoves(x,y)
        logging.debug(f'CheckField(): moves and attacks registered')

        if self.moves == None and self.attacks == None: return False
        logging.debug(f'CheckField(): there are possible moves from that location')

        return True

    

    def ChooseFigure(self):
        if(self.gameState == 0):
            print(f'Game Ended Player {self.winner} won!')
            time.sleep(3)
            self.gameState == 2
            return True
        elif(self.gameState == 1):
            
            x,y = self.InputValue(1)
            self.move = (x,y)
            if(self.CheckField(x,y)): return True
            else: return False

    

    # return tuple with figurechar and color and value of background color
    def returnBoard(self):
        result = []
        for a in range(8):
            tmp = []
            for b in range(8):
                Field = self.board[a][b]
                if(Field.isEmpty()): tmp.append((Field.getBackGroundColor()+'B',Field.getBackGroundColor()))
                else: tmp.append((Field.getPieceAndColor(),Field.getBackGroundColor()))
            result.append(tmp)
        return result, self.moves, self.attacks

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
        

        


# do zrobienia
# roszada kurna nie działa
# lista ruchów
# cofanie ruchu
# zapis gry przynajmniej jednej
# interfejs
# błedy 
# te jebany rich
# zakonczenie gry
# 