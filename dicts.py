import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
    "white":'w',
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
strings = {
    "chosingFigureInput":"Proszę wybrać figurę: "
}