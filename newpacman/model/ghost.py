from newpacman.utilities.constants import constants

class ghost:

    def __init__(self, id, x, y):
        super().__init__()
        self.pos = [x,y]
        self.id = id

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