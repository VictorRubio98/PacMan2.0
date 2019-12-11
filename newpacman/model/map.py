import numpy as np
import random

from newpacman.model.pac_man import pac_man
from newpacman.model.ghost import ghost
from newpacman.utilities.constants import constants
from newpacman.view.console import console

class map:
    
    def __init__(self):
        super().__init__()
        self.cons = console()
        self.currentpoints = 0
        self.board = self.create_board()
        self.points, self.MAXPOINTS = self.create_ponints()
        self.pacman = pac_man(constants.INI_X, constants.INI_Y)
        self.ghostarray = [ghost(0, constants.INI_G_X, constants.INI_G_Y)]


    def create_board(self):
        return np.loadtxt("newpacman/model/board.txt", dtype='i', delimiter=',')
    
    def create_ponints(self):
        input = np.loadtxt("newpacman/model/points.txt", dtype='i', delimiter=',')
        maxpoints = 0 
        for row in input:
            for c in row:
                if c == constants.AST_NUM:
                    maxpoints = maxpoints + 1

        self.cons.print_args(constants.MAP_CODE, input)
        return input, (maxpoints -1)

    def move_pacman(self, direction):
        moved = False
        x , y = self.pacman.get_pos()
        newX = x
        newY = y
        if direction == constants.DOWN_CODE and self.board[x + 1][y] == constants.X_NUM:
            self.pacman.move(constants.DOWN_CODE)
            moved = True
            newX = x + 1
            if self.points[x + 1][y] == constants.AST_NUM:
                self.currentpoints = self.currentpoints +1
                self.points[x + 1][y] = constants.SPACE_NUM

        elif direction == constants.UP_CODE and self.board[x - 1][y] == constants.X_NUM:
            self.pacman.move(constants.UP_CODE)
            moved = True
            newX = x - 1
            if self.points[x - 1][y] == constants.AST_NUM:
                self.currentpoints = self.currentpoints +1
                self.points[x - 1][y] = constants.SPACE_NUM

        elif direction == constants.LEFT_CODE and self.board[x][y - 1] == constants.X_NUM:
            self.pacman.move(constants.LEFT_CODE)
            moved = True
            newY = y - 1
            if self.points[x][y - 1] == constants.AST_NUM:
                self.currentpoints = self.currentpoints +1
                self.points[x][y - 1] = constants.SPACE_NUM

        elif direction == constants.RIGHT_CODE and self.board[x][y + 1] == constants.X_NUM:
            self.pacman.move(constants.RIGHT_CODE)
            moved = True
            newY = y + 1
            if self.points[x][y + 1] == constants.AST_NUM:
                self.currentpoints = self.currentpoints +1
                self.points[x][y + 1] = constants.SPACE_NUM

        if moved == True:
            pos = [newX, newY]
            object = [direction, pos, x, y, self.currentpoints]
            self.cons.print_args(constants.PACMAN_CODE, object)
        return self.currentpoints

    def move_ghost(self, id, direction):
        moved = False
        x , y = self.ghostarray[id].get_pos()
        newX = x
        newY = y
        if direction == constants.DOWN_CODE and self.board[x + 1][y] == constants.X_NUM:
            self.ghostarray[id].move(constants.DOWN_CODE)
            moved = True
            newX = x + 1

        elif direction == constants.UP_CODE and self.board[x - 1][y] == constants.X_NUM:
            self.ghostarray[id].move(constants.UP_CODE)
            moved = True
            newX = x - 1

        elif direction == constants.LEFT_CODE and self.board[x][y - 1] == constants.X_NUM:
            self.ghostarray[id].move(constants.LEFT_CODE)
            moved = True
            newY = y - 1

        elif direction == constants.LEFT_CODE and self.board[x][y + 1] == constants.X_NUM:
            self.ghostarray[id].move(constants.RIGHT_CODE)
            moved = True
            newY = y + 1

        pos = [newX, newY]
        object = [direction, id, pos, x, y, self.points]
        self.cons.print_args(constants.GHOST_CODE, object)
        return self.check_death(newX, newY)

    def random_move(self):
        i = 0
        direction = ""
        got_a_kill = False
        while i < 1:
            r = random.randint(0,3)
            if r == 0:
                direction = constants.UP_CODE
            elif r == 1:
                direction = constants.DOWN_CODE
            elif r == 2:
                direction = constants.LEFT_CODE
            elif r == 3:
                direction = constants.RIGHT_CODE
            got_a_kill = self.move_ghost(i,direction)
            i = i + 1
        return got_a_kill     

    def get_pacman_pos(self):
        return self.pacman.get_pos()

    def get_ghost_pos(self, id):
        return self.ghostarray[id].get_pos()
    
    def check_death(self, nextX, nextY):
        p_x, p_y = self.get_pacman_pos()
        if nextX == p_x and nextY == p_y:
            self.pacman.set_start_pos()
            return True
        else:
            return False

    def end_game(self, win):
        object = [win, self.currentpoints]
        self.cons.print_args(constants.ENDGAME_CODE, object)
