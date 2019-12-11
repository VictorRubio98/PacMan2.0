from newpacman.model.map import map
import time

m = map()
i = 0
while True:
    m.random_move()
    i = i + 1
    time.sleep(0.5)