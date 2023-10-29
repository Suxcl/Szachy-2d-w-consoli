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
from dicts import piecesASCII, colors, asciiChars
import os, shutil

import pickle


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import logging
logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)
logging.debug("Lanuching Main.py")

console = Console()
side = 'w'
oneTime = True
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


GamePanel["Info"].size = 35



# ------------------------------------------------
# ----- creating table for gameboard display -----
# ------------------------------------------------


def resetTable(chessboard):
    board,moves,attacks,position = chessboard.returnBoard()
    table = None
    table = Table( show_footer=True ,style=None, box=box.MINIMAL)
    let = ["","a","b","c","d","e","f","g","h"]
    for a in let:
        table.add_column(a, justify="center", width=9, footer=a)
    
    ran = range(8)
    if(side == 'b'):
        ran = range(7, -1, -1)
    


    for a in ran:
        rowNumber = "\n\n" + str(8-a)
            
        valueColFig = []
        valueBckCol = []
        asciitab = []
    
        for b in range(8):
            valueColFig.append(board[a][b][0])
            valueBckCol.append(board[a][b][1])
            if((a,b) == position):
                tmp = Text(piecesASCII[valueBckCol[b]][valueColFig[b]])
                tmp.stylize("bold blue")
                asciitab.append(tmp)
            elif((a,b) in moves):
                tmp = Text(piecesASCII[valueBckCol[b]]['move'])
                tmp.stylize("bold blue")
                asciitab.append(tmp)
            elif((a,b) in attacks):
                tmp = Text(piecesASCII[valueBckCol[b]][valueColFig[b]])
                tmp.stylize("bold red")
                asciitab.append(tmp)
            else:
                asciitab.append(piecesASCII[valueBckCol[b]][valueColFig[b]])
            
        table.add_row(rowNumber, asciitab[0], asciitab[1], asciitab[2], asciitab[3], asciitab[4], asciitab[5], asciitab[6], asciitab[7],)
    table = Align.center(table, vertical="bottom")
    GamePanel["Chess"].update(table)
    

    moveList = chessboard.getMoveList()
    move_count = chessboard.move_count


    info = None
    info = Table( show_footer=True ,style=None, box=box.MINIMAL)

    # figuremoved, x1,y1,x2,y2, None or Figure Destoyed 
    info.add_column("Move", justify="center", width=8)
    info.add_column("piece", justify="center", width=8)
    info.add_column("orig", justify="center", width=8)
    info.add_column("dest", justify="center", width=8)
    info.add_column("target", justify="center", width=10)

    if(oneTime == True):
        oneTime==False
    else:
        for a in moveList:
            fig1 = a[0][0]
            col1 = a[0][1]
            fig2,col2
            if(a[5]!=None):
                fig2 = a[5][0]
                col2 = a[5][1]
            info.add_row(asciiChars[col1][fig1], a[1]+a[2], a[3]+a[4], "--" if fig2 == None else asciiChars[col2][fig2])

        
    info = Align.center(info, vertical="middle")
    
    GamePanel["Info"].update(info)






inp1 = "What you want do do? - "
inp2 = "Chose Side w/b - "
przerwa = ""
tmp = console.width/2 - len(inp1)/2
for a in range(int(tmp)):
    przerwa = przerwa + " "
promptMainMenu = przerwa + inp1
promptChoseSide = przerwa + inp2

lay = 0


with console.screen():
    while(True):
        
        if(lay == 0):
            cls()
            console.print(MainMenu)
            wynik = Prompt.ask(promptMainMenu)
            if(wynik in ['start',"1"]): 
                cb = chessboard()

                side = Prompt.ask(promptChoseSide, choices=['w',"W","b","B"], show_choices=False)
                if(side in ['w',"W"]):
                    cb.newBoard()
                else: 
                    cb.newBoard(1)
                    side = 'b'

                lay = 1
            if(wynik in ['con',2]): lay = 2
            if(wynik in ['credits',3]): lay = 3
            if(wynik in ['exit',4]): lay = 4
        if(lay == 1):
            
            resetTable(cb)
        
            cls()
            print(GamePanel)
            while(True):
                tmp = cb.ChooseFigure()
                
                resetTable(cb)
                cls()
                print(GamePanel)    
                if(tmp): break
            while(True):
                tmp = cb.Move()
                resetTable(cb)
                cls()
                print(GamePanel)    
                if(tmp == True): break
                
                    
            #lay == 0
            
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