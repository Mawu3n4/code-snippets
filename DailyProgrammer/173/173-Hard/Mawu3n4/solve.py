
import library
import random
#TO-DO
def teleport():
    return ""

#TO-DO
def genNewPath(other_path={'length':0, 'obstacle': False, 'food': 0}):
   return {
       'length': abs(random.randrange(0,50,10) - other_path['length'] + 10),
       'food': (random.randrange(0, 150, 20) if not other_path['food'] and
                random.randrange(0,100,10) < 40 else 0),
       'obstacle': (not random.randrange(0,3) if not other_path['obstacle']
                    else False)
           }




# Peon: Peon
# Warrior: Start with 50 more stamina
# Scout: Can find new paths //CoolDown of 3 turns
# Mage: Can teleport himself forward //CoolDown of 5 turns
# Cleric: Regenerate stamina faster
# Archer: 5 less stamina needed to cross obstacles and attack
class Player(object):
    def __init__(self, *args, **kwargs):
        self.rest_rate = kwargs.get('rest_rate', 4)
        self.stamina = kwargs.get('stamina', 200)
        self.action_cost = kwargs.get('attack_cost', 15)
        self.power = None
        self.spec = kwargs.get('spec', 'Peon')
        self.weapon = kwargs.get('weapon', 'club')
        self.dist = 0
        self.food = 0

class Warrior(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, stamina=250, spec="Warrior", **kwargs)

class Scout(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Scout", **kwargs)
        self.power = genNewPath

class Mage(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Mage", **kwargs)
        self.power = teleport

class Cleric(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Cleric", rest_rate=6, **kwargs)

class Archer(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Archer", action_cost=10, **kwargs)

def initGame():
    options = {}

    for string in library.text['start']:
        if string[:5] == 'INPUT':
            options[string.split(' ')[1]] = raw_input().capitalize()
        else:
            delay = float(string.split('%')[0])
            library.printStrWithDelay(string.split('%')[1], delay)

    player = globals().get(options['spec'].capitalize(), Player)(**options)
    return player


def printPath(path, direction):
    library.printStrWithDelay(
        "The {3} path is {0} units long and {1} obstacles, there is also {2}food.\n".format(
            path['length'], "contains" if path['obstacle'] else "is free of",
            str(path['food']) + "lbs of " if path['food'] else "no ", direction))


# player = initGame()
player = Scout(weapon='dagger')
monster = {
    'pos': 0,
    'speed': 10
    }

while True:
    paths = {}
    paths['R'] = genNewPath()
    paths['L'] = genNewPath(paths['R'])

    printPath(paths['R'], "right")
    printPath(paths['L'], "left")
    library.printStrWithDelay("Which path do you take ?.. [R/L" + "/Power]" if player.power else "]")

    u_input = raw_input()
    u_input = 'R' if not len(u_input) else u_input.capitalize()[0]

    library.printStrWithDelay(
        "You went " + ("right.\n" if u_input == 'R' else "left.\n"))

    player.dist += paths[u_input]['length']
    player.food += paths[u_input]['food']
    player.stamina -= (paths[u_input]['length'] % 10) / 2

    if paths[u_input]['obstacle']:
        library.printStrWithDelay("Something blocks your way.\n"
                                  + library.getWalkedSentence())
        player.stamina -= player.action_cost

    library.printStrWithDelay(library.getPosMonsterSentence(
            player.dist - monster['pos']))

    monster['pos'] += monster['speed']

## TODO
#   Rest
#   Combat
#   Increase speed
#   Powers
