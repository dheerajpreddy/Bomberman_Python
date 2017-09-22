"""Main program."""

from board import Board
from walls import Walls
from bomberman import Bomberman
import os
import sys
from enemy import Enemy
from bricks import Bricks
from bombs import Bomb
from input import Get, input_to

brd = Board(34, 68)
wlls = Walls(2, 4)
wlls.placeWalls(brd)
bombman = Bomberman(2, 4, 'bomberman')
bombman.setNewPosition(brd, 2, 4)


enemies = []
for i in range(0, 10):
    enemies.append(Enemy(2, 4, 'enemy'))
    enemies[i].random(brd)

# enemies = []
# enemies.append(Enemy(2, 4, 'enemy'))
# enemies.append(Enemy(2, 4, 'enemy'))
# enemies.append(Enemy(2, 4, 'enemy'))

# enemies[0].setNewPosition(brd, 14, 20)
# enemies[1].setNewPosition(brd, 22, 34)
# enemies[2].setNewPosition(brd, 26, 10)

#
bricks = []
for i in range(0, 10):
    bricks.append(Bricks(2, 4))
    bricks[i].random(brd)
# bricks = []
# bricks.append(Bricks(2, 4))
# bricks.append(Bricks(2, 4))
# bricks.append(Bricks(2, 4))
#
# bricks[0].setNewPosition(brd, 6, 20)
# bricks[1].setNewPosition(brd, 14, 12)
# bricks[2].setNewPosition(brd, 22, 8)

os.system('clear')
print(brd.returnStringBoard())

getch = Get()
bomb = Bomb(2, 4)

while True:
    input = input_to(getch)
    os.system('clear')
    print(brd.returnStringBoard())
    if input is not None:
        bombman.move(input, brd)

    if input == 'q':
        os.system('clear')
        sys.exit()

    if input == 'b':
        bomb.placeBomb(brd, bombman)

    bomb.update(brd, enemies, bricks, bombman)
    for i in range(0, 10):
        enemies[i].randomMove(brd)
