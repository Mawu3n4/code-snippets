
import sys
import curses

from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from random import randint

curses.initscr()
win_width = 60
win_height = 20
win = curses.newwin(win_height, win_width, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

def check_collisions(player):
    return (player['y'], player['x']) in world['walls']

def move(player, d):
    player['p_x'] = player['x']
    player['p_y'] = player['y']
    player['x'] += (not not d & 4) * (1 if not not d & 1 else -1)
    player['y'] += (not not d & 2) * (-1 if not not d & 1 else 1)

    if check_collisions(player):
        player['y'] = player['p_y']
        player['x'] = player['p_x']

def end_game(player, key):
    print "Score: {0}".format(player.score)
    sys.exit(0)

key = ''

actions = {
    KEY_RIGHT: move,
    KEY_LEFT: move,
    KEY_UP: move,
    KEY_DOWN: move,
    27: end_game
    }

player = {
    'x' : win_width / 2,
    'y' : win_height / 2,
    'p_x': win_width / 2,
    'p_y': win_height / 2,
    'score': 0
    }

world = {
    'walls': [(y, x)
              for x in range(1, win_width-1)
              for y in range(1, win_height-1)
              if (x == 1 or x == win_width - 2 or
                  y == 1 or y == win_height - 2)],

    'food': []
}

while key != 27:
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(player['score']) + ' ')
    event = win.getch()
    for wall in world['walls']:
        win.addch(wall[0], wall[1], 'X')
    for food in world['food']:
        win.addch(wall[0], wall[1], 'o')
    key = key if event == -1 else event
    if key in actions:
        actions[key](player, key)
        key = ''
    win.addch(player['p_y'], player['p_x'], ' ')
    win.addch(player['y'], player['x'], '#')

curses.endwin()
print("\nScore - " + str(score))
