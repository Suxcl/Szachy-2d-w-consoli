from rich.console import Console
from rich.table import Table, Column
from rich import print,box
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
from rich.pretty import pprint
from rich.align import Align
from rich.padding import Padding
from rich.text import Text


import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

MARKDOWN2 = """
## created by Sak Jakub
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()

md2 = Markdown(MARKDOWN2)
#console.print(md)

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

MainMenu["bottom"].height = console.height - 10


#layout["left"].update(pprint(['Start Game: "start"', 'Continue Game: "con"', '"Exit Aplication: exit']))
#layout["between"].update(Align.center(md))

MainMenu["top"].update(Align.center("\n\n\n░█████╗░██╗░░██╗███████╗░██████╗░██████╗\n██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝\n██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░\n██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗\n╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝\n░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░"))


text = Text(f'1. Start New Game\n2.Continue Saved Game\n3.Credits\n4.Exit Aplication')
text.stylize("bold green", 0,6)


MainMenu["between-middle"].update(text)
MainMenu["bottom"].update("sad")

# do wstawienia figury
MainMenu["between-left"].update(Align.center("XXX\nXXX\nXXX", vertical="middle"))
MainMenu["between-right"].update(Align.center("XXX\nXXX\nXXX", vertical="middle"))


# === GamePanel ===

GamePanel = Layout()



GamePanel.split_row(
    Layout(name="Info"),
    Layout(name="Chess"),
)

GamePanel["Info"].height = console.height - 10
GamePanel["Chess"].height = console.height - 10

GamePanel["Info"].size = 40


table = Table( show_footer=True ,style=None, box=box.MINIMAL)
table.add_column( justify="center",  no_wrap=True)
table.add_column('a', justify="center",  no_wrap=True)
table.add_column('b', justify="center" )
table.add_column("c", justify="center" )
table.add_column("d", justify="center" )
table.add_column("e", justify="center" )
table.add_column("f", justify="center" )
table.add_column("h", justify="center" )
table.add_column("c", justify="center" )



# for a in range(1,9):
    # table.add_row(a, )

table.add_row(x for x in["a","b","c","d","e","f","g","h"])
table.add_row("\n\n7","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)
table.add_row("\n\n6","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)
table.add_row("\n\n5","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)
table.add_row("\n\n4","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)
table.add_row("\n\n3","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)
table.add_row("\n\n2","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)
table.add_row("\n\n1","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########","#########\n#########\n#########\n#########\n#########",)


table = Align.center(table, vertical="middle")

GamePanel["Chess"].update(table)





inp = "What you want do do? - "
przerwa = ""
tmp = console.width/2 - len(inp)/2
for a in range(int(tmp)):
    przerwa = przerwa + " "
promptMainMenu = przerwa + inp


lay = 1
while(True):
    cls()
    if(lay == 0):
        console.print(MainMenu)
        wynik = Prompt.ask(promptMainMenu, show_choices=False, choices=["start", "con", "credits", "exit"])
        if(wynik == "start"): lay = 1
        if(wynik == "con"): lay = 2
        if(wynik == "credits"): lay = 3
        if(wynik == "exit"): lay = 4
    if(lay == 1):
        print(GamePanel)
        wynik = Prompt.ask(promptMainMenu, show_choices=False, choices=["start", "con", "credits", "exit"])
    if(lay == 2):
        pass
    if(lay == 3):
        break

#MainMenu['MainMenuPrompt'].update("")
#while(True):

    #wynik = Prompt.ask("Enter your name", show_choices=False, choices=["Paul", "Jessica", "Duncan"], default="Paul")

# #name = Prompt.ask("Enter your name", show_choices=False, choices=["Paul", "Jessica", "Duncan"], default="Paul")

# header = Column([1,2,3,4,5,6,7,8])
# table = Table( show_footer=True, title="szachy" ,style=None, box=box.MINIMAL)
# table.add_column( justify="center",  no_wrap=True)
# table.add_column('a', justify="center",  no_wrap=True)
# table.add_column('b', justify="center" )
# table.add_column("c", justify="center" )
# table.add_column("d", justify="center" )
# table.add_column("e", justify="center" )
# table.add_column("f", justify="center" )
# table.add_column("h", justify="center" )
# table.add_column("c", justify="center" )

# table.add_row("8","XXX\n X \nXXX")
# table.add_row("7")
# table.add_row("6")
# table.add_row("5")
# table.add_row("4")
# table.add_row("3")
# table.add_row("2")
# table.add_row("1")


# console = Console()
# console.print(table)



