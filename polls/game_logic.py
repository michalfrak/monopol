import random


def dice_throw():
    return random.randint(1, 6)


def dice_go(current_position):
    forward_go = dice_throw()
    return current_position + forward_go

