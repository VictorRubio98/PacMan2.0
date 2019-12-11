from newpacman.model.map import map
from newpacman.utilities.constants import constants

import sys, threading, time, os

class moderator:
    def __init__(self):
        super().__init__()
        self.m = map()
        self.previously_read = ""
        self.direction = ""
        self.lifes = 3
        
    def read(self):
        try:
            ch = sys.stdin.read(1)
            if ord(ch) == constants.ESC_1:
                ch = sys.stdin.read(1)
                if ord(ch) == constants.ESC_2:
                    ch = sys.stdin.read(1)
                    if ord(ch) == constants.LEFT:
                        self.previously_read = constants.LEFT_CODE
                        return constants.LEFT_CODE
                    elif ord(ch) == constants.RIGHT:
                        self.previously_read = constants.RIGHT_CODE
                        return constants.RIGHT_CODE
                    elif ord(ch) == constants.UP:
                        self.previously_read = constants.UP_CODE
                        return constants.UP_CODE
                    elif ord(ch) == constants.DOWN:
                        self.previously_read = constants.DOWN_CODE
                        return constants.DOWN_CODE
            elif ord(ch) == constants.ENTER:
                    return -1
        except:
            return self.previously_read

    def read_event(self):
        while self.direction != -1:
            self.direction = self.read()

    def engine(self):
        th = threading.Thread(target = self.read_event)
        th.start()
        got_a_kill = False
        while(self.direction != -1):
            points = self.m.move_pacman(self.direction)
            got_a_kill = self.m.random_move()
            time.sleep(constants.SPEED)
            if (got_a_kill == True):
                self.lifes = self.lifes - 1
                if self.lifes == 0:
                    self.end_game(False)
                    return
            
            if points == self.m.MAXPOINTS:
                self.end_game(True)

    def end_game(self, win):
        self.direction = -1
        self.m.end_game(win) 

        
