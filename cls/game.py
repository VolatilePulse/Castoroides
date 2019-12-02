from enum import Enum
from typing import List


class Stat_Type(Enum):
    Health = 0
    Stamina = 1
    Torpor = 2
    Oxygen = 3
    Food = 4
    Water = 5
    Temperature = 6
    Weight = 7
    Damage = 8
    Speed = 9
    Fortitude = 10
    Crafting_Skill = 11

    def __index__(self):
        return self.value


class Game:
    bIsPercentStat: List[bool]


game = Game()
game.bIsPercentStat = [False, False, False, False, False, False, False, False, True, True, False, True]
