import random
from pprint import pformat
from typing import List

from cls.game import Stat_Type
from cls.species import Species, generate_random_species
from load_creature import Status


class Creature:
    BaseCharacterLevel: int
    ExtraCharacterLevel: int
    Species: Species
    Status: Status

    NumberOfLevelUpPointsApplied: List[int]
    NumberOfLevelUpPointsAppliedTamed: List[int]
    DinoImprintingQuality: float
    TamedIneffectivenessModifier: float
    MaxStatusValues: List[float]

    def __init__(self, species=generate_random_species()):
        self.BaseCharacterLevel = 1
        self.ExtraCharacterLevel = 0
        self.Species = species
        self.Status = Status.Wild

        self.NumberOfLevelUpPointsApplied = [0] * 12
        self.NumberOfLevelUpPointsAppliedTamed = [0] * 12

        self.DinoImprintingQuality = 0
        self.TamedIneffectivenessModifier = 0
        self.MaxStatusValues = list(species.MaxStatusValues)

    def Get_Creature_Level(self):
        return self.BaseCharacterLevel + self.ExtraCharacterLevel

    def __repr__(self):
        return pformat(vars(self), width=200)


def generate_random_creature(pretame_level: int = 0, total_level: int = 0, status: Status = None) -> Creature:
    creature = Creature()
    creature.Status = status if status else random.choice(list([Status.Wild, Status.Tamed, Status.Bred]))
    if not pretame_level:
        pretame_level = random.randint(1, 1000)

    while creature.NumberOfLevelUpPointsApplied < pretame_level:
        stat_index = random.randint(0, 11)
        if stat_index == Stat_Type.Torpor:
            continue

        if not creature.Species.DontUseValue[stat_index] and creature.NumberOfLevelUpPointsApplied[stat_index] < 255:
            creature.NumberOfLevelUpPointsApplied[stat_index] += 1
            creature.BaseCharacterLevel += creature.NumberOfLevelUpPointsApplied[stat_index]

    if creature.Status != Status.Wild:
        creature.NumberOfLevelUpPointsAppliedTamed[stat_index] = random.randint(0, 255)
        creature.ExtraCharacterLevel += creature.NumberOfLevelUpPointsAppliedTamed[stat_index]
    if creature.Status == Status.Tamed:
        creature.TamedIneffectivenessModifier = random.random()
    elif creature.Status == Status.Bred:
        creature.TamedIneffectivenessModifier = 1
        creature.DinoImprintingQuality = random.random()

    return creature
