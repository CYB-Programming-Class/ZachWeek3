import random

rawInput = input("Enter a list of names seperated by commas.")
list = rawInput.split(",")



stories1 = [
    " walked into a bar, and then",
    " was strolling down the beach when",
    " found a peach and then",
    " opened a portal, then",
    " was a very grumpy man. then",
    " had a shiny ferarri when",
    " jumped out of a plane when",
    " was searching for treasure when",
    " had a heart attack when",
    " fantasised that"
]

stories2 = [
    " they were attacked by ",
    " their tummy felt funny after eating ",
    " they found ",
    " they suddenly realised that the world was inside ",
    " they called their parents to ask for ",
    " they wrote a song about ",
    " they dreamed of becoming ",
    " they became ",
    " they were the first human to come into contact with ",
    " they overturned the nefarious dictatorship of "
]

stories3 = [
    "a peanut.",
    "Kim Jong-un.",
    "a server farm.",
    "seven bald men.",
    "deep fried mac'n'cheese.",
    "the president.",
    "the national treasure.",
    "a superb owl.",
    "too many onion rings.",
    list[random.randint(0,len(list)-1)] + "."
]

stories4 = [
    " That is how they died.",
    " That is how they became president.",
    " They were never seen again.",
    " That was their awful no good very bad day.",
    " That was their origin story.",
    " Kids, this story has a lot of lessons to be learned.",
    " Buckle up, every time.",
    " Never again.",
    " This kills the " + list[0],
    " The world changed that day..."
]

for name in list:
    print("")
    print (name + stories1[random.randint(0,9)]+ stories2[random.randint(0,9)]+ stories3[random.randint(0,9)]+ stories4[random.randint(0,9)])
