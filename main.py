from rich.console import Console
from rich.table import Table, Column
from rich import print
from rich import box
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
from rich.pretty import pprint
from rich.align import Align
from rich.padding import Padding
from rich.text import Text
from rich.markdown import Markdown

from chessboard import chessboard
from dicts import piecesASCII, colors
import os, shutil


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import logging
logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)
logging.debug("Lanuching Main.py")

console = Console()

# cb = chessboard()
# cb.newBoard()
# # logging.debug(cb.translateMoveTo01("a",2))
# # logging.debug(cb.translateMoveTo01("b",2))
# logging.debug(cb.translateMoveTo01("a",8))

# cb.startGame()
# logging.debug("Starting game")

# === MeinManu ===

MainMenu = Layout()

MainMenu.split_column(
    Layout(name="top"),
    Layout(name="between"),
    Layout(name="bottom")
)

MainMenu["between"].split_row(
    Layout(name="between-left"),
    Layout(name="between-middle"),
    Layout(name="between-right"),
)



MainMenu["top"].update(Align.center("\n\n\n░█████╗░██╗░░██╗███████╗░██████╗░██████╗\n██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝\n██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░\n██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗\n╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝\n░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░", vertical="middle"))


text = Text(f' Start New Game    - type "start"\n Credits           - type "credits"\n Exit Aplication   - type "exit"')
text.stylize("bold green")
#text.align("center", width=250)


MainMenu["between-middle"].update(Align.center(text, vertical="middle"))

MainMenu["bottom"].update("")

# do wstawienia figury

konLewy = Text(piecesASCII['w']['nrw'])
konPrawy = Text(piecesASCII['w']['nw'])
konLewy.stylize("bold grey")
#konPrawy.stylize("bold grey")
MainMenu["between-left"].update(Align.center(konLewy, vertical='middle'))
MainMenu["between-right"].update(Align.center(konPrawy, vertical="middle"))


# === GamePanel ===

GamePanel = Layout(name="root")



GamePanel.split_row(
    Layout(name="Info"),
    Layout(name="Chess"),
)

_width, _height = shutil.get_terminal_size()
console.size = (_width-1, _height-4)

GamePanel["root"].height = console.height - 40


GamePanel["Info"].size = 40




#----- creating table for gameboard display -----



def resetTable(board, moves, attacks):
    table = None
    table = Table( show_footer=True ,style=None, box=box.MINIMAL)
    let = ["","a","b","c","d","e","f","g","h"]
    for a in let:
        table.add_column(a, justify="cecnter")
    
    

    for a in range(8):
        rowNumber = "\n\n" + str(8-a)
            
        valueColFig = []
        valueBckCol = []
        asciitab = []
    
        for b in range(8):
            valueColFig.append(board[a][b][0])
            valueBckCol.append(board[a][b][1])
            if((a,b) in moves):
                asciitab.append(piecesASCII[valueBckCol[b]]['move'])
            elif((a,b) in attacks):
                tmp = Text(piecesASCII[valueBckCol[b]][valueColFig[b]])
                tmp.stylize("bold red")
                asciitab.append(tmp)
            else:
                asciitab.append(piecesASCII[valueBckCol[b]][valueColFig[b]])
            
        table.add_row(rowNumber, asciitab[0], asciitab[1], asciitab[2], asciitab[3], asciitab[4], asciitab[5], asciitab[6], asciitab[7])
    table = Align.center(table, vertical="bottom")
    GamePanel["Chess"].update(table)
    







inp = "What you want do do? - "
przerwa = ""
tmp = console.width/2 - len(inp)/2
for a in range(int(tmp)):
    przerwa = przerwa + " "
promptMainMenu = przerwa + inp

lay = 0

chessboards = [chessboard() for x in range(5)]
with console.screen():
    while(True):
        cls()

        if(lay == 0):
            console.print(MainMenu)
            wynik = Prompt.ask(promptMainMenu)
            if(wynik in ['start',"1"]): 
                cb = chessboard()
                cb.newBoard()
                    
                
                lay = 1
            if(wynik in ['con',2]): lay = 2
            if(wynik in ['credits',3]): lay = 3
            if(wynik in ['exit',4]): lay = 4
        if(lay == 1):
            board,moves,attacks = cb.returnBoard()
            resetTable(board,moves,attacks)
            print(GamePanel)
            while(True):
                tmp = cb.ChooseFigure()
                cls()
                board,moves,attacks = cb.returnBoard()
                resetTable(board,moves,attacks)
                print(GamePanel)    
                if(tmp): break
            while not(cb.Move()): 
                cls()
                board,moves,attacks = cb.returnBoard()
                resetTable(board,moves,attacks)
                print(GamePanel)    
                
                    
            lay == 0
            
        if(lay == 2):
            pass
        if(lay == 3):
            exit()




# choose x,y
# show possible moves
# allow to choose where to go
# check if move is correct
# if move is correct move/attack
# move figure to destination
# check for cheks/mates
# 