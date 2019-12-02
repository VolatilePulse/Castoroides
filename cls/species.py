import random
from pprint import pformat
from typing import List

from cls.game import Stat_Type, game


class Species:
    DontUseValue: List[bool]
    CanLevelUpValue: List[bool]

    MaxStatusValues: List[float]

    MaxGainedPerLevelUpValueIsPercent: List[bool]
    AmountMaxGainedPerLevelUpValue: List[float]
    AmountMaxGainedPerLevelUpValueTamed: List[float]
    TamingMaxStatAdditions: List[float]
    TamingMaxStatMultipliers: List[float]
    DinoMaxStatAddMultiplierImprinting: List[float]

    TheMaxTorporIncreasePerBaseLevel: float
    TamedBaseHealthMultiplier: float
    TamingIneffectivenessMultiplier: float
    ExtraTamedHealthMultiplier: float
    MaxTamingEffectivenessBaseLevelMultiplier: float

    def __init__(self):
        self.DontUseValue = [False] * 12
        self.CanLevelUpValue = [False] * 12

        self.MaxStatusValues = [100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0]

        self.MaxGainedPerLevelUpValueIsPercent = [True] * 12
        self.AmountMaxGainedPerLevelUpValue = [0] * 12
        self.AmountMaxGainedPerLevelUpValueTamed = [0] * 12
        self.TamingMaxStatAdditions = [0] * 12
        self.TamingMaxStatMultipliers = [0] * 12
        self.DinoMaxStatAddMultiplierImprinting = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0.2, 0, 0]

        self.TheMaxTorporIncreasePerBaseLevel = 0.06
        self.TamedBaseHealthMultiplier = 1
        self.TamingIneffectivenessMultiplier = 1
        self.ExtraTamedHealthMultiplier = 1
        self.MaxTamingEffectivenessBaseLevelMultiplier = 0.5

    def __repr__(self):
        return pformat(vars(self), width=180)


def generate_random_species() -> Species:
    species = Species()

    for stat_index in range(12):
        species.DontUseValue[stat_index] = bool(random.getrandbits(1))
        if not species.DontUseValue[stat_index]:
            species.CanLevelUpValue[stat_index] = bool(random.getrandbits(1))

    species.DontUseValue[Stat_Type.Health] = False
    species.DontUseValue[Stat_Type.Torpor] = False
    species.CanLevelUpValue[Stat_Type.Health] = True
    species.CanLevelUpValue[Stat_Type.Torpor] = False

    for stat_index in range(12):
        if not species.DontUseValue[stat_index]:
            if game.bIsPercentStat[stat_index]:
                species.MaxStatusValues[stat_index] = 1
            else:
                species.MaxStatusValues[stat_index] = int(random.random() * 10_000)

            if species.MaxGainedPerLevelUpValueIsPercent[stat_index] and not game.bIsPercentStat[stat_index]:
                species.AmountMaxGainedPerLevelUpValue[stat_index] = int(random.random() * 1_000)
                if species.CanLevelUpValue[stat_index]:
                    species.AmountMaxGainedPerLevelUpValueTamed[stat_index] = int(random.random() * 1_000)
            else:
                species.AmountMaxGainedPerLevelUpValue[stat_index] = random.random()
                if species.CanLevelUpValue[stat_index]:
                    species.AmountMaxGainedPerLevelUpValueTamed[stat_index] = random.random()

            species.TamingMaxStatAdditions[stat_index] = random.random()
            species.TamingMaxStatMultipliers[stat_index] = random.random()
            species.DinoMaxStatAddMultiplierImprinting[stat_index] = random.random()

    species.MaxGainedPerLevelUpValueIsPercent = [True] * 12
    species.TheMaxTorporIncreasePerBaseLevel = random.random() or 1
    species.TamedBaseHealthMultiplier = random.random() or 1
    species.ExtraTamedHealthMultiplier = random.random() or 1

    return species
