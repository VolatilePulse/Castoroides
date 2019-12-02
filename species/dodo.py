from cls.creature import Creature
from cls.species import Species


def create_species() -> Species:
    dodo = Species()

    dodo.MaxStatusValues = [40, 100, 30, 150, 450, 0, 0, 50, 1, 1, 0, 0]
    dodo.AmountMaxGainedPerLevelUpValue = [0.2, 0.1, 0, 0.1, 0.1, 0, 0, 0.2, 0.05, 0, 0, 0]
    dodo.AmountMaxGainedPerLevelUpValueTamed = [0.27, 0.1, 0, 0.1, 0.1, 0, 0, 0.04, 0.1, 0.01, 0, 0]
    dodo.TamingMaxStatAdditions = [0.5, 0, 0.5, 0, 0, 0, 0, 0, 1, 2, 0, 0]
    dodo.TamingMaxStatMultipliers = [0, 0, 0, 0, 0.15, 0, 0, 0, 0.4, 0, 0, 0]

    dodo.TheMaxTorporIncreasePerBaseLevel = 0.6
    dodo.TamedBaseHealthMultiplier = 1
    dodo.ExtraTamedHealthMultiplier = 1
    dodo.DinoMaxStatAddMultiplierImprinting = [0.2, 0, 0.2, 0, 0.2, 0, 0, 0.2, 0.2, 0.2, 0, 0]
    dodo.MaxGainedPerLevelUpValueIsPercent = [True] * 12
    dodo.MaxTamingEffectivenessBaseLevelMultiplier = 0.5
    dodo.TamingIneffectivenessMultiplier = 1

    return dodo
