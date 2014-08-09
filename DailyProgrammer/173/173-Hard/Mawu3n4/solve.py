
import library
import random


class Monster(object):
    def __init__(self, *args, **kwargs):
        super(Monster, self).__init__()
        self.pos = kwargs.get('pos', 0)
        self.speed = kwargs.get('speed', 20)
        self.attack = kwargs.get('attack', 80)
        self.acceleration = kwargs.get('acceleration', 20)

    def update(self, player_dist):
        # Print msg depending on the pos of the monster
        library.printStrWithDelay(library.getPosMonsterSentence(
                player_dist - self.pos))

        # Its coming
        self.pos += self.speed
        # increase speed according to player.distance
        self.speed += self.acceleration

    def enrage(self, **kwargs):
        self.pos = kwargs.get('pos', 0)
        self.attack += kwargs.get('factor', 15)
        self.speed = kwargs.get('reseted_speed', 20)

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
            library.printStrWithDelay("You made it as far as {0}".format(self.dist))
            library.printStrWithDelay(" miles but you are exhausted and can't go")
            library.printStrWithDelay(" further.\nTonight, you will feed the beast.")
            return False

        return True


    def printStatus(self):
        library.printStrWithDelay("Stamina {0}, food left {1}\n".format(
                self.stamina, self.food))


    def rest(self):
        library.printStrWithDelay("The hollowed tree looks comfortable, ")
        library.printStrWithDelay("do you want to rest a bit ?..[Y/N] ")

        u_input = raw_input()
        self.resting = True if u_input[0] == "Y" else False

        if self.resting:
            self.stamina += 10 if self.food >= 10 else self.food
            self.food -= 10 if self.food >= 10 else self.food
            self.stamina += self.stamina * self.rest_rate
            library.printStrWithDelay(library.getRestedSentence())


    def move(self, choice, path):
        library.printStrWithDelay(
            "You went " + ("right.\n" if choice == 'R' else "left.\n"))

        # Update ressources
        self.dist += path['length']
        self.food += path['food']
        self.stamina -= path['length']

        # Cross obstacles
        if path['obstacle']:
            library.printStrWithDelay("Something blocks your way.\n"
                                      + library.getWalkedSentence())
            self.stamina -= self.action_cost


    def combat(self, opponent):
        library.printStrWithDelay(
            "You can't run anymore, take your {0} and fight !\n".format(
                self.weapon))

        difficulty = 4
        res = random.randrange(0,difficulty)
        while not res:
            library.printStrWithDelay(library.getMissedSentence())
            self.stamina -= opponent.attack + self.action_cost
            library.printStrWithDelay(library.getHitSentence())
            if not self.checkStamina(): return False
            difficulty -= 1
            res = random.randrange(0,difficulty)

        return True


class Warrior(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, stamina=300, **kwargs)

class Scout(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, **kwargs)

        self.power = genNewPath
        self.power_up = "Your sharp view notices the way behind the rock "
        self.power_up += "on your left and you vault your way through.\n"

class Mage(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, **kwargs)

        self.power = teleport
        self.power_up = "You open up the book from your satchel and you close "
        self.power_up += "your eyes as the arcanes surrounds you, you re-open "
        self.power_up += "them and are through the right path.\n"

class Cleric(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, rest_rate=0.2, **kwargs)

class Archer(Player):
    def __init__(self, **kwargs):
        Player.__init__(self, action_cost=10, **kwargs)


def getNewPaths():
    paths = {}

    library.printStrWithDelay(("The branches of the narrow trees slap your \
    face as you try to stay alive and two paths emerge before you.\n"))

    paths['R'] = genNewPath()
    paths['L'] = genNewPath(paths['R'])

    printPath(paths['R'], "right")
    printPath(paths['L'], "left")

    return paths


def genNewPath(other_path={'length':0, 'obstacle': False, 'food': 0},
               player=None):
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


def gameLoop(player, monster):
    while player.checkStamina():

        if not player.resting:
            paths = getNewPaths()

            library.printStrWithDelay("Which path do you take ?.. [R/L" +
                                   ("/Power]" if player.power else "]"))
            u_input = raw_input()
            u_input = 'R' if not len(u_input) else u_input.capitalize()[0]

            if u_input == 'P':
                library.printStrWithDelay(player.power_up)
                player.power(paths['R'], player)

            else:
                player.move(u_input, paths[u_input])

        monster.update(player.dist)

        if monster.pos >= player.dist:
            if not player.combat(monster):
                return

            library.printStrWithDelay(library.getStrikedSentence())
            library.printStrWithDelay("You managed to make it flee but it will")
            library.printStrWithDelay(" come back, more adamant to feast on you.")
            monster.enrage(factor=15, reseted_speed=20, pos=player.dist-20)

        player.printStatus()
        player.rest()
        player.checkStamina()


gameLoop(initGame(), Monster())
