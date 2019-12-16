from newpacman.utilities.constants  import constants
class pac_man:

    def __init__(self, x , y):
        super().__init__()
        self.pos = [x, y]

    def move(self, direction):
        if direction == constants.UP_CODE:
            self.pos[0] = self.pos[0] - 1
        elif direction == constants.DOWN_CODE:
            self.pos[0] = self.pos[0] + 1
        elif direction == constants.LEFT_CODE:
            self.pos[1] = self.pos[1] - 1
        elif direction == constants.RIGHT_CODE:
            self.pos[1] = self.pos[1] + 1
    
    def get_pos(self):
        return self.pos
    
    def set_start_pos(self):
        self.pos = [constants.INI_X, constants.INI_Y]
    def set_pos(self, x, y):
        self.pos = [x, y]