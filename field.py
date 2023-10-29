from dicts import *
from piece import *



import logging
logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)

class field:
    def __init__(self,x,y) -> None:
        self.x = y
        self.y = x
        self.figure = None
        self.isDefendingKing = False
        self.isChossen = False
        self.possibleMove = False
        self.backGroundColor = None
        
    def setFieldOcupant(self, fig):
        self.figure = fig
        fig.changeCordinates(self.x,self.y)

    def removeFieldOcupant(self):
        self.figure = None
        

    def getPieceAndColor(self):
        if(self.figure!=None):
            return self.figure.getFigAndCol()    

    
    def setBackGroundColor(self, color):
        self.backGroundColor = color

    def getBackGroundColor(self): return self.backGroundColor
        
        

    def setpossibleMove(self): self.possibleMove = True
    def rempossibleMove(self): self.possibleMove = False

    def isEmpty(self): 
        if self.figure is None: return True
        else: return False

    def getFigure(self): return self.figure

    def getColorOfFigure(self): 
        if(self.figure): return self.figure.getFigCol()

    def DefendingKing(self): return self.isDefendingKing

    def isFieldChosen(self): return self.isChossen
    