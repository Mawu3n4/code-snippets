
import library
import random


def genNewPath(other_path={'length':0, 'obstacle': False, 'food': 0}, player=None):
    if player:
        teleport(genNewPath(other_path), player)
    else:
        return {
            'length': abs(random.randrange(10,60,10) - other_path['length'] + 10),
            'food': (random.randrange(0, 150, 20) if not other_path['food'] and
                     random.randrange(0,100,10) < 40 else 0),
            'obstacle': (not random.randrange(0,3) if not other_path['obstacle']
                         else False)
            }


def teleport(path, player):
    player.dist += path['length']
    player.food += path['food']


# Peon: Peon
# Warrior: Start with 50 more stamina
# Scout: Can find new paths //CoolDown of 3 turns
# Mage: Can teleport himself forward //CoolDown of 5 turns
# Cleric: Regenerate stamina faster
# Archer: 5 less stamina needed to cross obstacles and attack
class Player(object):
    def __init__(self, *args, **kwargs):
        self.rest_rate = kwargs.get('rest_rate', 0.1)
        self.stamina = kwargs.get('stamina', 200)
        self.action_cost = kwargs.get('attack_cost', 15)
        self.power = None
        self.spec = kwargs.get('spec', 'Peon')
        self.weapon = kwargs.get('weapon', 'club')
        self.dist = 0
        self.food = 0
        self.resting = False

    def checkStamina(self):
        if self.stamina <= 0:
            library.printStrWithDelay("You made it as far as {0} miles but yu are exhausted and can't go further.\n Tonight, you will feed the beast.".format(self.dist))
            exit

    def printStatus(self):
        library.printStrWithDelay("Stamina {0}, food left {1}\n".format(
                self.stamina, self.food))

class Warrior(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, stamina=250, spec="Warrior", **kwargs)

class Scout(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Scout", **kwargs)

        self.power = genNewPath
        self.power_up = "Your sharp view notices the way behind the rock on your left and you vault your way through.\n"

class Mage(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Mage", **kwargs)

        self.power = teleport
        self.power_up = "You open up the book from your satchel and you close your eyes as the arcanes surrounds you, you re-open them and are throug the right path.\n"

class Cleric(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, spec="Cleric", rest_rate=0.2, **kwargs)

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


player = initGame()
monster = {
    'pos': 0,
    'speed': 20,
    'attack': 80
    }
paths = {}

while True:

    if not player.resting:
        library.printStrWithDelay(("The branches of the narrow trees slap your \
face as you try to stay alive and two paths emerge before you.\n"))

        paths['R'] = genNewPath()
        paths['L'] = genNewPath(paths['R'])

        printPath(paths['R'], "right")
        printPath(paths['L'], "left")

        library.printStrWithDelay("Which path do you take ?.. [R/L" + "/Power]" if player.power else "]")
        u_input = raw_input()
        u_input = 'R' if not len(u_input) else u_input.capitalize()[0]

        if u_input == 'P':
            library.printStrWithDelay(player.power_up)
            player.power(paths['R'], player)

        else:
            library.printStrWithDelay(
                "You went " + ("right.\n" if u_input == 'R' else "left.\n"))

            # Update ressources
            player.dist += paths[u_input]['length']
            player.food += paths[u_input]['food']
            player.stamina -= paths[u_input]['length']

            # Cross obstacles
            if paths[u_input]['obstacle']:
                library.printStrWithDelay("Something blocks your way.\n"
                                          + library.getWalkedSentence())
                player.stamina -= player.action_cost

    else:
        player.stamina += 10 if player.food >= 10 else player.food
        player.food -= 10 if player.food >= 10 else player.food
        player.stamina += player.stamina * player.rest_rate
        library.printStrWithDelay(library.getRestedSentence())

    # Print msg depending on the pos of the monster
    library.printStrWithDelay(library.getPosMonsterSentence(
            player.dist - monster['pos']))

    # Its coming
    monster['pos'] += monster['speed']
    # increase speed according to player.distance
    monster['speed'] += 20

    if monster['pos'] >= player.dist:
        library.printStrWithDelay("You can't run anymore, take your {0} and fight !\n".format(player.weapon))
        res = random.randrange(0,3)
        while res:
            library.printStrWithDelay(library.getMissedSentence())
            player.stamina -= monster['attack'] + player.atack_cost
            player.checkStamina()

        library.printStrWithDelay(library.getStrikedSentence())
        # Change distance according to player.distance
        monster['pos'] = player.dist - 20
        monster['attack'] += 15
        monster['speed'] = 20

    player.printStatus()
    library.printStrWithDelay("The hollowed tree looks comfortable, do you want to rest a bit ?..[Y/N] ")
    u_input = raw_input()
    player.resting = True if u_input[0] == "Y" else False

    player.checkStamina()

## TODO
#   Combat
#   Increase speed
