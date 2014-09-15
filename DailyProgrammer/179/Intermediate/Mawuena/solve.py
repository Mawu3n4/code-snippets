
import sys
import curses

from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from random import randint

WIDTH = 60
HEIGHT = 20

def move(world, d):
    player = world['player']
    player['p_x'] = player['x']
    player['p_y'] = player['y']
    player['x'] += (not not d & 4) * (1 if not not d & 1 else -1)
    player['y'] += (not not d & 2) * (-1 if not not d & 1 else 1)

    if (player['y'], player['x']) in world['walls']:
        player['y'] = player['p_y']
        player['x'] = player['p_x']

    return True


def init_curses(width, height):
    curses.initscr()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    return win


def end_game(world, key):
    return False


def init_game():
    world = {
        'walls': [(y, x)
                  for x in range(1, WIDTH-1)
                  for y in range(1, HEIGHT-1)
                  if (x == 1 or x == WIDTH - 2 or
                      y == 1 or y == HEIGHT - 2)],

        'food': [],

        'player': {
            'x' : WIDTH / 2,
            'y' : HEIGHT / 2,
            'p_x': WIDTH / 2,
            'p_y': HEIGHT / 2,
            'score': 0
            }
        }

    return world


def game_loop(win, world):
    key = ''

    actions = {
        KEY_RIGHT: move,
        KEY_LEFT: move,
        KEY_UP: move,
        KEY_DOWN: move,
        ord('q'): end_game
    }

    loop = True
    while loop:
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(world['player']['score']) + ' ')
        event = win.getch()
        for wall in world['walls']:
            win.addch(wall[0], wall[1], 'X')
        for food in world['food']:
            win.addch(wall[0], wall[1], 'o')
        key = key if event == -1 else event
        if key in actions:
            loop = actions[key](world, key)
        key = ''
        win.addch(world['player']['p_y'], world['player']['p_x'], ' ')
        win.addch(world['player']['y'], world['player']['x'], '#')

    curses.endwin()
    print "Score - {0}".format(world['player']['score'])


game_loop(init_curses(width=WIDTH, height=HEIGHT), init_game())

