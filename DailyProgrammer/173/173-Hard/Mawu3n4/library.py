# Credit to InkWellIdeas for the striked_pool and missed_pool

import random

striked_pool = {"You pierce the creatures armor/skin/scales.",
                "Your attack rings true.",
                "The creature winces in pain as your attack strikes.",
                "You successfully smash it.",
                "Your attack lands.",
                "You strike it.",
                "It cannot avoid your jab.",
                "Your weapon meets flesh.",
                "You find a soft spot in your foe's armor/skin/chitin.",
                "Your attack slips past your foe's parry and draws blood.",
                "Your strike tears into your opponent's flesh.",
                "You split the creature's hide.",
                "Your weapon bounces off the creatures parry and lands a blow.",
                "You guess the creature's feint and strike flesh.",
                "Your weapon sinks into the creature's flesh.",
                "Your weapon sneaks through the creature's armor/skin/scales.",
                "Your strike glances off your opponents shield but slides into the creature's flesh.",
                "Your weapon lands a heavy blow.",
                "Blood flies as your weapon strikes.",
                "Your opponent dodges-just as you expected and your weapon draws blood.",
                "The creature howls as your weapon leaves its mark.",
                "Your opponent begins to wheeze as your attack hits.",
                "Flesh falls as your attack lands.",
                "The creature stumbles from your latest successful hit.",
                "Your weapon finds flesh and bone."}

missed_pool = {"Your opponent side-steps out of the way.",
               "You strike your opponent but its armor/hide is not pierced.",
               "Your opponent parries your strike.",
               "Abruptly your opponent slides away from where you expect.",
               "Your opponent dodges left, but your attack doesn't catch up to it.",
               "Your weapon flies wildly missing your opponent.",
               "From the corner of your eye, you are distracted by movement and your attack sails wide.",
               "Your attack connects, but glances off your opponent's armor/hide.",
               "You misjudge your opponent's movement and your attack misses.",
               "Your opponent stops your attack with his shield/bracer.",
               "Your weapon seems unbalanced and doesn't move as you expect.",
               "Your opponent raises his weapon and successfully parries.",
               "Your opponent howls, and you flinch throwing your attack off.",
               "You nick your opponent, but the strike is so minor that no damage is done.",
               "A light catches your eye and throws off your attack.",
               "Your opponent changes his stance and you miss.",
               "Your weapon only catches some of your adversary's clothes.",
               "Your attack hits only armor/hide.",
               "Timing your strike, your opponent shifts out of the way.",
               "Your opponent shifts his most heavily armored/protected part to your weapon's path.",
               "The armor/hide of your opponent absorbs the attack.",
               "You change your grip to adjust to your opponent's move, but it is too little and too late.",
               "Your opponent's armor/hide is too strong for your strike.",
               "Your attack hits the most protected part of your opponent, doing no damage.",
               "A call from a party member distracts you and your attack does not connect."}


walked_pool = {"You reached your destination safely.",
               "The path is now free of any obstacles and you walk across.",
               "You firmly grab your weapon and jump across the ditch.",
               "You ponder on how you will walk past the obstacle and find a way.",
               "A shaft of sunlight shine on your way and you find a gap between the rocks.",
               "The crescent moon reflects in the puddle and you notice the way around the fallen trees."}

rested_pool = {"You feel energy flow through your veins.",
               "You could lift a bull right now.",
               "A foe crossing your path right now would be a dead foe.",
               "You never felt so good before."}


def getResultFromPool(pool):
    def getSentenceFromSet():
        return random.sample(globals()[pool], 1)[0]
    return getSentenceFromSet

getStrikedSentence = getResultFromPool('striked_pool')
getMissedSentence = getResultFromPool('missed_pool')
getWalkedSentence = getResultFromPool('walked_pool')
getRestedSentence = getResultFromPool('rested_pool')
