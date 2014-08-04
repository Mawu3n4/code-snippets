
import library
import random
#TO-DO
def teleport():
    return ""

#TO-DO
def genNewPath(other_path={'length':0, 'obstacle': False, 'food': 0}):
   return {
       'length': abs(random.randrange(0,50,10) - other_path['length']),
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
# Archer: 5 less stamina needed to cross obstacles
class Player(object):
    def __init__(self, *args, **kwargs):
        self.rest_rate = kwargs.get('rest_rate', 4)
        self.stamina = kwargs.get('stamina', 200)
        self.attack_cost = kwargs.get('attack_cost', 15)
        self.power = None
        self.spec = kwargs.get('spec', 'Peon')
        self.weapon = kwargs.get('weapon', 'club')

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
        Player.__init__(self, spec="Archer", attack_cost=10, **kwargs)

def initGame():
    options = {}

    for string in library.text['start']:
        if string[:5] == 'INPUT':
            options[string.split(' ')[1]] = raw_input().capitalize()
        else:
            delay = float(string.split('%')[0])
            library.printStrWithDelay(string.split('%')[1], delay)

    player = globals().get(options['spec'].capitalize(), Player)(**options)
    print player.spec
    print player.weapon


def printPath(path, direction):
    library.printStrWithDelay(
        "The {3} path is {0} units long and {1} obstacles, there is also {2}food.\n".format(
            path['length'], "contains" if path['obstacle'] else "is free of",
            "" if path['food'] else "no ", direction))

while True:
    right = genNewPath()
    left = genNewPath(right)

    printPath(right, "right")
    printPath(left, "left")
    library.printStrWithDelay("Which path do you take ?.. [R/L]")

    u_input = raw_input()
    u_input = 'R' if not len(u_input) else u_input.capitalize()[0]

    library.printStrWithDelay("You went " + ("right.\n" if u_input == 'R'
                                             else "left.\n"))
