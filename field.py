from dicts import *
from piece import *

class field:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.figure = None
        self.isDefendingKing = False
        self.isChossen = False
        self.possibleMove = False
        
    def setFieldOcupant(self, fig):
        self.figure = fig
        fig.changeCordinates(self.x,self.y)

    def removeFieldOcupant(self):
        self.figure = None
        

    def getPieceAndColor(self):
        if(self.figure!=None):
            return self.figure.getFigAndCol()    
        else:
            return "  "
    
    def setpossibleMove(self): self.possibleMove = True
    def rempossibleMove(self): self.possibleMove = False

    def isEmpty(self): 
        if(self.figure == None): return True

    def getFigure(self): return self.figure

    def getColorOfFigure(self): 
        if(self.figure): return self.figure.getFigCol()

    def DefendingKing(self): return self.isDefendingKing

    def isFieldChosen(self): return self.isChossen
    