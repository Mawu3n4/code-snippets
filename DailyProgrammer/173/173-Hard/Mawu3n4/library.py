# Credit to InkWellIdeas for the striked_pool and missed_pool

import random
import sys
import time

# Ressources
text = {
    'start': [
        # Float%String
        # Delay%Text to print
        '0.06%You wake up in a cold grove, hungry but rested, where the dim light of the second moon reveals an hazardous path between the trees.\n',
        '0.06%As you gather your strength to stand up, you lean on your rigth to pick up your ..',
        # INPUT var_name
        # Will get user input on stdin and send it to
        # the class ctor with the name var_name
        'INPUT weapon',
        '0.06%A fine weapon that followed you everywhere, no other Mage, Cleric, Warrior, Scout, or Archer can weild it like you do, you are the most talented ..',
        'INPUT spec',
        "0.048%You start walking at a slow pace towards the breach between nature's fingers when you realize the growing noise behind you.\n",
        '0.08%The lull suddenly come back and fills the air, a sore iron smell sting your nose and you feel eyes on you.\n',
        '0.04%The mightiest roar ripps the silence open and a beast of vaguely anthropoid outline, prodigious claws on hind and fore feet, and long, narrow wings behind, comes running at you.\n',
        '0.05%After a brief moment of sheer terror, your senses come back and you start running for your life through the breach you spotted before.\n']
        }

striked_pool = {"You pierce the creatures armor/skin/scales.\n",
                "Your attack rings true.\n",
                "The creature winces in pain as your attack strikes.\n",
                "You successfully smash it.\n",
                "Your attack lands.\n",
                "You strike it.\n",
                "It cannot avoid your jab.\n",
                "Your weapon meets flesh.\n",
                "You find a soft spot in your foe's armor/skin/chitin.\n",
                "Your attack slips past your foe's parry and draws blood.\n",
                "Your strike tears into your opponent's flesh.\n",
                "You split the creature's hide.\n",
                "Your weapon bounces off the creatures parry and lands a blow.\n",
                "You guess the creature's feint and strike flesh.\n",
                "Your weapon sinks into the creature's flesh.\n",
                "Your weapon sneaks through the creature's armor/skin/scales.\n",
                "Your strike glances off your opponents shield but slides into the creature's flesh.\n",
                "Your weapon lands a heavy blow.\n",
                "Blood flies as your weapon strikes.\n",
                "Your opponent dodges-just as you expected and your weapon draws blood.\n",
                "The creature howls as your weapon leaves its mark.\n",
                "Your opponent begins to wheeze as your attack hits.\n",
                "Flesh falls as your attack lands.\n",
                "The creature stumbles from your latest successful hit.\n",
                "Your weapon finds flesh and bone.\n"}

missed_pool = {"Your opponent side-steps out of the way.\n",
               "You strike your opponent but its armor/hide is not pierced.\n",
               "Your opponent parries your strike.\n",
               "Abruptly your opponent slides away from where you expect.\n",
               "Your opponent dodges left, but your attack doesn't catch up to it.\n",
               "Your weapon flies wildly missing your opponent.\n",
               "From the corner of your eye, you are distracted by movement and your attack sails wide.\n",
               "Your attack connects, but glances off your opponent's armor/hide.\n",
               "You misjudge your opponent's movement and your attack misses.\n",
               "Your opponent stops your attack with his shield/bracer.\n",
               "Your weapon seems unbalanced and doesn't move as you expect.\n",
               "Your opponent raises his weapon and successfully parries.\n",
               "Your opponent howls, and you flinch throwing your attack off.\n",
               "You nick your opponent, but the strike is so minor that no damage is done.\n",
               "A light catches your eye and throws off your attack.\n",
               "Your opponent changes his stance and you miss.\n",
               "Your weapon only catches some of your adversary's clothes.\n",
               "Your attack hits only armor/hide.\n",
               "Timing your strike, your opponent shifts out of the way.\n",
               "Your opponent shifts his most heavily armored/protected part to your weapon's path.\n",
               "The armor/hide of your opponent absorbs the attack.\n",
               "You change your grip to adjust to your opponent's move, but it is too little and too late.\n",
               "Your opponent's armor/hide is too strong for your strike.\n",
               "Your attack hits the most protected part of your opponent, doing no damage.\n",
               "A call from a party member distracts you and your attack does not connect."}


walked_pool = {"You reached your destination safely.\n",
               "The path is now free of any obstacles and you walk across.\n",
               "You firmly grab your weapon and jump across the ditch.\n",
               "You ponder on how you will walk past the obstacle and find a way.\n",
               "A shaft of sunlight shine on your way and you find a gap between the rocks.\n",
               "The crescent moon reflects in the puddle and you notice the way around the fallen trees.\n"}

rested_pool = {"You feel energy flow through your veins.\n",
               "You could lift a bull right now.\n",
               "A foe crossing your path right now would be a dead foe.\n",
               "You never felt so good before.\n"}

monster_pos_pool = [
    "You can't hear the growling of the beast anymore, it is not a good thing.\n",
    "Leafs from shaking trees are paving your ways, it's coming for you.\n",
    "You hear the spine of an animal getting crushed under its footsteps, run.\n",
    "The smell of your fear and its breath is making you sick of terror, may the gods have mercy.\n"
    ]
# Misc Func

def getPosMonsterSentence(distance):
    distance = 0 if distance > 200 else 1 if distance > 100 else 2 if distance > 50 else 3
    return monster_pos_pool[distance]

# Polymorphic function using a closure
def getResultFromPool(pool):
    def getSentenceFromSet():
        # access the global scope
        return random.sample(globals()[pool], 1)[0]
    return getSentenceFromSet


# Templates in Python
getStrikedSentence = getResultFromPool('striked_pool')
getMissedSentence = getResultFromPool('missed_pool')
getWalkedSentence = getResultFromPool('walked_pool')
getRestedSentence = getResultFromPool('rested_pool')


def printStrWithDelay(string, delay=0.06):
    for char in string:
        # print displays a ugly space after single char prints
        sys.stdout.write(char)
        # flush the buffer
        sys.stdout.flush()
        # Delay longer for punctuation, helps set the ambiance
        time.sleep(0.3 if char == ','
                   else 0.5 if char in {',', '.', '?', '!'}
                   else delay)
