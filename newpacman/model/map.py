import numpy as np
import random, math

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
        self.ghostarray = self.create_ghosts()
        self.god_mode = 0


    def create_board(self):
        return np.loadtxt(constants.LAYOUT, dtype='i', delimiter=',')

    def create_ghosts(self):
        return [ghost(0, constants.INI_G_X[0], constants.INI_G_Y[0]), ghost(1, constants.INI_G_X[1], constants.INI_G_Y[1]), 
        ghost(2, constants.INI_G_X[2], constants.INI_G_Y[2]), ghost(3, constants.INI_G_X[3], constants.INI_G_Y[3])]
        
    
    def create_ponints(self):
        input = np.loadtxt(constants.POINTS, dtype='i', delimiter=',')
        maxpoints = 0 
        for row in input:
            for c in row:
                if c == constants.AST_NUM:
                    maxpoints = maxpoints + 1

        self.cons.print_args(constants.MAP_CODE, input)
        return input, (maxpoints -1)

    def move_pacman(self, direction, lifes):
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

        elif direction == constants.LEFT_CODE and y == 1:
            moved = True
            newY = y - 1
            newY = constants.MAX_Y - 2
            self.pacman.set_pos(newX,newY)

            if self.points[x][y - 1] == constants.AST_NUM:
                self.currentpoints = self.currentpoints +1
                self.points[x][y - 1] = constants.SPACE_NUM

        elif direction == constants.RIGHT_CODE and y == constants.MAX_Y - 2:
            moved = True
            newY = y + 1
            newY = 1
            self.pacman.set_pos(newX,newY)
            if self.points[x][y + 1] == constants.AST_NUM:
                self.currentpoints = self.currentpoints +1
                self.points[x][y + 1] = constants.SPACE_NUM
        
        if self.points[newX][newY] == constants.ZERO_CHAR:
            if self.god_mode == 0:
                self.sum_godmode()
            self.points[newX][newY] = constants.SPACE_NUM
        elif self.god_mode > 0 and self.god_mode < constants.MAX_GOD_MODE:
            self.sum_godmode()
        if self.god_mode >= constants.MAX_GOD_MODE:
            self.god_mode = 0
        
        if moved == True:
            pos = [newX, newY]
            object = [direction, pos, x, y, self.currentpoints, lifes]
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
        elif direction == constants.LEFT_CODE and y == 1:
            moved = True
            newY = y - 1
            newY = constants.MAX_Y - 2
            self.ghostarray[id].set_pos(newX,newY)

        elif direction == constants.RIGHT_CODE and y == constants.MAX_Y - 2:
            moved = True
            newY = y + 1
            newY = 1
            self.ghostarray[id].set_pos(newX,newY)

        pos = [newX, newY]
        object = [direction, id, pos, x, y, self.points, self.god_mode]
        self.cons.print_args(constants.GHOST_CODE, object)
        return self.check_death(newX, newY, id), moved

    def random_move(self):
        i = 0
        direction = ""
        got_a_kill = [False, False, False, False]
        moved = False
        while i < 4:
            r = random.randint(0,3)
            if r == 0:
                direction = constants.UP_CODE
            elif r == 1:
                direction = constants.DOWN_CODE
            elif r == 2:
                direction = constants.LEFT_CODE
            elif r == 3:
                direction = constants.RIGHT_CODE
            got_a_kill[i], moved = self.move_ghost(i,direction)
            if moved == True:    
                i = i + 1
        return (got_a_kill[0] or got_a_kill[1] or got_a_kill[2] or got_a_kill[3])

    def almost_smart_move(self):
        i = 0
        tired = 0
        direction = ""
        got_a_kill = [False, False, False, False]
        moved = False
        p_x, p_y = self.get_pacman_pos()
        while i < 4:
            if tired < 2:
                g_x, g_y = self.get_ghost_pos(i)
                v_x = p_x - g_x
                v_y = p_y - g_y
                angle = (math.atan2(v_y,v_x)*(180/math.pi))%360
                r = random.randint(0,1)
                if angle >= 45 and angle < 135:
                    if tired == 0:
                        direction = constants.RIGHT_CODE

                    if tired == 1:
                        if r == 0:
                            direction = constants.UP_CODE
                        elif r == 1:
                            direction = constants.DOWN_CODE

                elif angle >= 135 and angle < 225:
                    if tired == 0:
                        direction = constants.UP_CODE

                    if tired == 1:
                        if r == 0:
                            direction = constants.LEFT_CODE
                        elif r == 1:
                            direction = constants.RIGHT_CODE

                elif angle >= 225 and angle < 315:
                    if tired == 0:
                        direction = constants.LEFT_CODE
                    elif tired == 1:
                        if r == 0:
                            direction = constants.UP_CODE
                        elif r == 1:
                            direction = constants.DOWN_CODE
                else: 
                    if tired == 0:
                        direction = constants.DOWN_CODE
                    elif tired == 1:
                        if r == 0:
                            direction = constants.LEFT_CODE
                        elif r == 1:
                            direction = constants.RIGHT_CODE
                            
            else:
                r = random.randint(0,3)
                if r == 0:
                    direction = constants.UP_CODE
                elif r == 1:
                    direction = constants.DOWN_CODE
                elif r == 2:
                    direction = constants.LEFT_CODE
                elif r == 3:
                    direction = constants.RIGHT_CODE
            got_a_kill[i], moved = self.move_ghost(i,direction)
            tired = tired + 1
            if moved == True:    
                i = i + 1
                tired = 0
        return (got_a_kill[0] or got_a_kill[1] or got_a_kill[2] or got_a_kill[3])

    def get_pacman_pos(self):
        return self.pacman.get_pos()

    def get_ghost_pos(self, id):
        return self.ghostarray[id].get_pos()
    
    def check_death(self, nextX, nextY, id):
        p_x, p_y = self.get_pacman_pos()
        if self.god_mode == 0:
            if nextX == p_x and nextY == p_y:
                self.pacman.set_start_pos()
                return True
            else:
                return False
        elif self.god_mode > 0  and nextX == p_x and nextY == p_y:
            self.ghostarray[id].set_start_pos(id)
            return False

    def end_game(self, win):
        object = [win, self.currentpoints]
        self.cons.print_args(constants.ENDGAME_CODE, object)
    
    def sum_godmode(self):
        self.god_mode = self.god_mode + 1
