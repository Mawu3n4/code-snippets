
import sys
import curses
import random

from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from random import randint

WIDTH = 60
HEIGHT = 20

WALL = '#'
PLAYER = '@'
EMPTY = ' '
FOOD = 'O'

SEED = 15

OBSTACLES = WIDTH * HEIGHT / SEED
FOODS = WIDTH * HEIGHT / (SEED * 2)

def move(world, d):
    player = world['player']
    player['p_x'] = player['x']
    player['p_y'] = player['y']
    player['x'] += (not not d & 4) * (1 if not not d & 1 else -1)
    player['y'] += (not not d & 2) * (-1 if not not d & 1 else 1)

    if (player['y'], player['x']) in world['walls']:
        player['y'] = player['p_y']
        player['x'] = player['p_x']

    else:
        player['life'] -= 1

    if (player['y'], player['x']) in world['food']:
        world['food'].remove((player['y'], player['x']))
        player['score'] += 1

    return not not player['life']


def init_curses(width, height):
    curses.initscr()
    curses.start_color()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    return win


def end_game(world, key):
    return False


def init_game():

    def get_rand_pos():
        return (random.randrange(2, HEIGHT - 1),
                random.randrange(2, WIDTH - 1))

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
            'score': 0,
            'life': 101
            }
        }

    for i in range(OBSTACLES):
        obstacle = get_rand_pos()
        while obstacle in world['walls']:
            obstacle = get_rand_pos()
        world['walls'].append(obstacle)

    for i in range(FOODS):
        food = get_rand_pos()
        while food in world['walls']:
            food = get_rand_pos()
        world['food'].append(food)

    return world


def print_world(win, world):
    win.border(0)
    win.addstr(0, 2, 'Score : {0} - Life : {1}'.format(
            world['player']['score'], world['player']['life']-1))

    for y in range(1, HEIGHT-1):
        for x in range(1, WIDTH-1):
            win.addch(y, x, (WALL if (y, x) in world['walls'] else
                             FOOD if (y, x) in world['food'] else
                             EMPTY),
                      (RED if (y, x) in world['walls'] else
                       BLUE if (y, x) in world['food'] else
                       GREEN)
                      )

    win.addch(world['player']['p_y'], world['player']['p_x'], EMPTY)
    win.addch(world['player']['y'], world['player']['x'], PLAYER, GREEN)


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
        event = win.getch()
        key = key if event == -1 else event
        if key in actions:
            loop = actions[key](world, key)
        key = ''
        print_world(win, world)

    curses.endwin()
    print "Score - {0}".format(world['player']['score'])


_win = init_curses(width=WIDTH, height=HEIGHT)

RED = curses.color_pair(1)
GREEN = curses.color_pair(2)
BLUE = curses.color_pair(4)

game_loop(_win, init_game())
