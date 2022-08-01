"""
Program Name:           Roll of the Dice
Program Creator:        LunarMusician
Program Purpose:        To understand the basics of Python
Date Created:           19 April, 2022
Date Modified:          19 April, 2022
Project Notes:          
"""
import random

dTwenty = 20
dTwelve = 12
dTen = 10
dEight = 8
dSix = 6
dFour = 4
dTwo = 2


def roll(die):
    dice = random.randrange(1, die)
    return dice


print(roll(dTwenty))
print(roll(dTwelve))
print(roll(dTen))
print(roll(dEight))
print(roll(dSix))
print(roll(dFour))
print(roll(dTwo))
