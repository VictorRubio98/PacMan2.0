import sys, termios, tty
import subprocess
import os

from newpacman.utilities.constants import constants

class console:

    def __init__(self):
        super().__init__()

    def set_raw(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        self.previous_lifes = 3
        print("\u001B[?25l", end = "", flush = True)
    
    def unset_raw(self):
        print("\u001B[?25h", end = "", flush = True)
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

    def print_args(self, id, object):
        if id == constants.MAP_CODE:
            for r in object:
                for c in r:
                    if c == constants.SPACE_NUM:
                        print(constants.ANSI_BACK_BLUE, end = "")
                    if c >0 and c < 7:
                        print(constants.ANSI_YELLOW, end = "")
                    if c == constants.ZERO_CHAR:
                        print(constants.ANSI_BLUE, end = "")
                    print(chr(c), end ="")
                    print(constants.ANSI_BACK_BLACK, end = "")
                    print(constants.ANSI_WHITE, end = "")
                print()
            self.set_raw()
        elif id == constants.PACMAN_CODE:
            direc, pos, x, y , points, lifes= object
            x = x + 2
            y = y + 1
            newX = pos[0] + 2
            newY = pos[1] + 1

            if newX != -1 and newY != -1:
                print("\033[" + str(x) + ";" + str(y) + "H",end="", flush=True)
                print(constants.ANSI_SUPR + constants.ANSI_BLANK, end = "", flush = True)
                print("\033["+ str(newX) + ";" + str(newY) + "H", end = "", flush=True)
                print(constants.ANSI_GREEN + constants.PACMAN + constants.ANSI_WHITE, end = "", flush = True)
                print("\033["+ str(constants.MAX_X + 2) +";1H", end = "", flush=True)
                print("Points: " + str(points) + " *", end = "", flush = True)
                print(" Lives : ", end = "", flush = True)
                i = 0
                if lifes != self.previous_lifes or self.previous_lifes == 3:
                    print(constants.ANSI_SUPR + constants.ANSI_SUPR + constants.ANSI_SUPR, end = "", flush =True)
                    while i < lifes:
                        print("| ", end = "", flush =True)
                        i = i + 1
                    self.previous_lifes = lifes

        elif id == constants.GHOST_CODE:
            direc, num, pos, x, y , points_map, god_mode= object
            x = x + 2
            y = y + 1
            newX = pos[0]+ 2
            newY = pos[1] + 1

            print("\033[" + str(x) + ";" + str(y) + "H",end="", flush=True)
            if points_map[x-2][y-1] == constants.ZERO_CHAR:
                print(constants.ANSI_BLUE, end = "", flush = True)
            print(chr(points_map[x-2][y-1]), end = "", flush = True)
            print(constants.ANSI_WHITE, end = "", flush = True)
            print("\033["+ str(newX) + ";" + str(newY) + "H", end = "", flush=True)
            if god_mode == 0:
                print(constants.ANSI_RED, end = "", flush = True)
            elif god_mode > 0 :
                print(constants.ANSI_BLUE, end = "", flush = True) 
            print(constants.GHOST + constants.ANSI_WHITE, end = "", flush = True)
        elif id == "ENDGAME":
            win, point = object
            print(constants.ANSI_CLEAR, end = "", flush=True)
            print("\033[10;13H", end = "", flush=True)
            if(not win):
                print(constants.ANSI_RED + "YOU LOSE" + constants.ANSI_WHITE, end="", flush = True)
            else:
                print(constants.ANSI_GREEN + "YOU WIN" + constants.ANSI_WHITE, end = "", flush = True)
            print("\033[11;10H", end = "", flush=True)
            print("***Final Points: " + str(point) + "***", end = "", flush = True)
            self.unset_raw()