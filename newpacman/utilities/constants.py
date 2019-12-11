class constants:

    UP_CODE = "UP"
    DOWN_CODE = "DOWN"
    LEFT_CODE = "LEFT"
    RIGHT_CODE = "RIGHT"
    MAP_CODE = "MAP"
    PACMAN_CODE = "PACMAN"
    GHOST_CODE = "GHOST"
    ENDGAME_CODE = "ENDGAME"

    GHOST = "º"
    PACMAN = "C"

    SPACE_NUM = 32
    X_NUM = 88
    AST_NUM = 42
    ONE_NUM = 1
    TWO_NUM = 2
    THREE_NUM = 3
    FOUR_NUM = 4
    FIVE_NUM = 5
    SIX_NUM = 6

    MAX_X = 10
    MAX_Y = 35
    SPEED = 0.5
    INI_X = 1
    INI_Y = 1
    INI_G_X = 3
    INI_G_Y = 9

    ESC_1 = 27
    ESC_2 = 91
    LEFT = 68
    RIGHT = 67
    DOWN = 66
    UP = 65 
    ENTER = 13

    ANSI_RIGHT = "\033[C"
    ANSI_LEFT = "\033[D"
    ANSI_BLUE = "\u001b[34;1m"
    ANSI_BACK_BLUE = "\u001b[44m"
    ANSI_YELLOW = "\u001b[33m"
    ANSI_WHITE = "\u001b[37;1m"
    ANSI_BACK_BLACK = "\u001b[40m"
    ANSI_SUPR = "\033[P"
    ANSI_CLEAR = "\033[H\033[J"
    ANSI_GREEN = "\u001b[32;1m"
    ANSI_RED = "\u001b[31;1m"
    ANSI_BLANK = "\033[@"

    def __init__(self):
        super().__init__()