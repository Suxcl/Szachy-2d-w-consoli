from chessboard import chessboard
import os

from pytermgui import *


import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# choose x,y
# show possible moves
# allow to choose where to go
# check if move is correct
# if move is correct move/attack
# move figure to destination
# check for cheks/mates
# 

cb = chessboard()
cb.newBoard()
cb.startGame()
#cb.printBoard()
# cb.AttempAMove('a',4)
# cb.AttempAMove('a',1)

#cb.Move('a',2)
#cb.printBoard()

# while(True):
#     cls()
#     x,y = cb.InputValue()    
#     cb.Move(x,y)
