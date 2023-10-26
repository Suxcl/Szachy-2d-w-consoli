from dicts import *

class Piece:
    def __init__(self,x,y,figCol):
        self.x = x
        self.y = y
        self.color = figCol
        self.figure = None
        self.isDefKing = False

    
    def getFigAndCol(self):
        return self.figure + self.color

    def getFigChar(self): return self.figure

    def getFigCol(self): return self.color

    def changeCordinates(self,x,y):
        self.x = x
        self.y = y

    def getCordinates(self):
        return self.x, self.y

    def ReturnPossibleMoves(self,board): return 
        
    
#   0 1 2 3 4 5 6 7
# 0 
# 1
# 2
# 3
# 4
# 5
# 6
# 7

class Pawn(Piece):
    def __init__(self,x, y, figCol):
        super().__init__(x,y, figCol)
        self.figure = PiecesDict["Pawn"]

    def leftAttack(self, board): 
        yy = self.y-1
        if(self.color == colors["white"]):
            xx = self.x-1
        else:
            xx = self.x+1
        col = board[xx][yy].getColorOfFigure()
        if(board[xx][yy].isEmpty() or col == self.color): return None
        return xx,yy
        
    def rightAttack(self, board): 
        yy = self.y+1
        if(self.color == colors["white"]):
            xx = self.x-1
        else:
            xx = self.x+1
        col = board[xx][yy].getColorOfFigure()
        if(board[xx][yy].isEmpty() or col == self.color): return None
        return xx,yy
        
    ###### #pawn tranformation to do       
    def ReturnPossibleMoves(self,board):
        moves = []
        attacks = []
        if(self.color == colors["white"]):
            for a in range(1,3):
                if(board[self.x-a][self.y].isEmpty()):
                    moves.append((self.x-a,self.y))
        else:
            for a in range(1,3):
                if(board[self.x+a][self.y].isEmpty()):
                    moves.append((self.x+a,self.y))
        if(self.y==0):
            t = self.rightAttack(board)
            if(t): moves.append(t)
        elif(self.y==7):
            t = self.leftAttack(board)
            if(t): moves.append(t)
        else:
            t = self.rightAttack(board)
            if(t): moves.append(t)
            t = self.leftAttack(board)
            if(t): moves.append(t)

        
        return board, moves, attacks



class Bishop(Piece):
    def __init__(self, x, y, figCol):
        super().__init__(x, y, figCol)
        self.figure = PiecesDict["Bishop"]




    def ReturnPossibleMove(self,board):
        moves = []
        attacks = []
        
        x , y  = self.x,self.y
        while(x >= 0 or y >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x-=1
            y-=1
        
        x , y  = self.x,self.y
        while(x <= 7 or y <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x+=1
            y+=1

        x , y  = self.x,self.y
        while(x >= 0 or y <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x-=1
            y+=1
        
        x , y  = self.x,self.y
        while(x <= 7 or y >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x+=1
            y-=1
        
        return board, moves, attacks




class Knight(Piece):
    def __init__(self, x, y, figCol):
        super().__init__(x, y, figCol)
        self.figure = PiecesDict["Knight"]

class Rock(Piece):
    def __init__(self, x, y, figCol):
        super().__init__(x, y, figCol)
        self.figure = PiecesDict["Rock"]
    
    def ReturnPossibleMoves(self, board):
        moves = []
        attacks = []
        x , y  = self.x,self.y
        while(x >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x-=1
        x = self.x
        while(x <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x+=1
        y = self.y
        while(y >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            y-=1
        y = self.y
        while(y <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            y+=1
        return board, moves, attacks

class Queen(Piece):
    def __init__(self, x, y, figCol):
        super().__init__(x, y, figCol)
        self.figure = PiecesDict["Queen"]

    def ReturnPossibleMoves(self, board):
        moves = []
        attacks = []
        #horizontal
        x , y  = self.x,self.y
        while(x >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x-=1
        x = self.x
        while(x <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x+=1
        y = self.y
        while(y >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            y-=1
        y = self.y
        while(y <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            y+=1
        
        # diagonal 

        x , y  = self.x,self.y
        while(x >= 0 or y >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x-=1
            y-=1
        
        x , y  = self.x,self.y
        while(x <= 7 or y <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x+=1
            y+=1

        x , y  = self.x,self.y
        while(x >= 0 or y <= 7):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x-=1
            y+=1
        
        x , y  = self.x,self.y
        while(x <= 7 or y >= 0):
            if(board[x][y].isEmpty()): moves.append((x,y))
            if(board[x][y].getColorOfFigure() != self.color): 
                attacks.append((x,y))
                break 
            x+=1
            y-=1

        return board, moves, attacks

class King(Piece):
    def __init__(self, x, y, figCol):
        super().__init__(x, y, figCol)
        self.figure = PiecesDict["King"]
        self.hasMoved = False

    def setMovesToTrue(self):
        self.hasMoved = True

    def ReturnPossibleMoves(self, board):
        moves = []
        attacks = []
        x, y = self.x, self.y
        possiblities = [
            (x-1,y-1),(x-1,y),(x-1,y+1),
            (x,y-1),(x,y+1),
            (x+1,y-1),(x+1,y),(x+1,y+1),
        ]
        for a in possiblities:
            x, y = a
            if not(x < 0 or x > 7 or y < 0 or y > 7):
                if(board[x,y].isEmpty()): moves.append((x,y))       
                elif(board[x][y].getColorOfFigure() != self.getFigCol()): attacks.append((x,y))
    
        
        return super().ReturnPossibleMoves(board)