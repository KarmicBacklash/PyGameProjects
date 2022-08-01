"""
Program Name:           Roll of the Dice
Program Creator:        LunarMusician
Modified By:            KarmicBackash
Program Purpose:        To understand the basics of Python (Modifed to be more pythonic)
Date Created:           19 April, 2022
Date Modified:          19 April, 2022
Project Notes:          
"""
import random


class die:
    def roll(x):
        x = random.randint(1, x)
        print(x)


class roll:
    def dTwenty():
        x = 20
        die.roll(x)

    def dTwelve():
        x = 12
        die.roll(x)

    def dTen():
        x = 10
        die.roll(x)

    def dEight():
        x = 8
        die.roll(x)

    def dSix():
        x = 6
        die.roll(x)

    def dFour():
        x = 4
        die.roll(x)

    def dTwo():
        x = 2
        die.roll(x)


roll.dTwenty()
roll.dTwelve()
roll.dTen()
roll.dEight()
roll.dSix()
roll.dFour()
roll.dTwo()
