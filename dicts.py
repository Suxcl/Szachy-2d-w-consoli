import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



piecesASCII = {
    'w' : {
        'wB'  : "         \n         \n         \n         \n         ",
        'pw' : "         \n   ( )   \n   / \   \n  /   \  \n         ",
        'pb' : "         \n   (|)   \n   /|\   \n  /|||\  \n         ",
        'rw' : "         \n [ ''' ] \n  |   |  \n  |   |  \n         ",
        'rb' : "         \n [ ''' ] \n  | | |  \n  | | |  \n         ",
        'bw' : "    .    \n   / \   \n   / \   \n  /_ _\  \n         ",
        'bb' : "    .    \n   /|\   \n   /|\   \n  /_|_\  \n         ",
        'nw' : "    __   \n   /  \  \n    / /  \n   /_ _\ \n         ",
        'nb' : "    __   \n   //\\  \n    ///  \n   /_|_\ \n         ",
        'qw' : '         \n \/\ /\/ \n  \   /  \n  /_ _\  \n         ',
        'qb' : '         \n \/\|/\/ \n  \ | /  \n  /_|_\  \n         ',
        'kw' : '    +    \n  /\|/\  \n  \   /  \n  |_ _|  \n         ',
        'kb' : '    +    \n  /\|/\  \n  \ | /  \n  |_|_|  \n         ',
        'nrw': "    __   \n   /  \  \n   \ \   \n  /_ _\  \n         ",
        'move':"         \n         \n  {   }  \n         \n         ",
    }

    ,
    'b' : {
        'bB'  : "---------\n---------\n---------\n---------\n---------",
        'pw' : "---------\n---( )---\n---/ \---\n--/   \--\n---------",
        'pb' : "---------\n---(|)---\n---/|\---\n--/|||\--\n---------",
        'rw' : "---------\n-[ ''' ]-\n--|   |--\n--|   |--\n---------",
        'rb' : "---------\n-[ ''' ]-\n--| | |--\n--| | |--\n---------",
        'bw' : "----.----\n---/ \---\n---/ \---\n--/_ _\--\n---------",
        'bb' : "----.----\n---/|\---\n---/|\---\n--/_|_\--\n---------",
        'nw' : "----__---\n---/  \--\n----/ /--\n---/_ _\-\n---------",
        'nb' : "----__---\n---//\\--\n----///--\n---/_|_\-\n---------",
        'qw' : '---------\n-\/\ /\/-\n--\   /--\n--/_ _\--\n---------',
        'qb' : '---------\n-\/\|/\/-\n--\ | /--\n--/_|_\--\n---------',
        'kw' : '----+----\n--/\|/\--\n--\   /--\n--|_ _|--\n---------',
        'kb' : '----+----\n--/\|/\--\n--\ | /--\n--|_|_|--\n---------',
        'move':"---------\n---------\n--{   }--\n---------\n---------",
    },
}

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
    "BadInput_ToLong":"Podana wartość jest jest za długa i nie odnosi się do żadnego pola",
    "BadInput_BadChars":"Podana wartość nie odnosi się do żadnego pola",

}
strings = {
    "chosingFigureInput":"Proszę wybrać figurę: "
}