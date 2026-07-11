import random

def roll_dice(dice_str):
    count, sides = map(int, dice_str.split('k'))
    rolls = []
    for _ in range(count):
        rolls.append(random.randint(1, sides))
    return rolls