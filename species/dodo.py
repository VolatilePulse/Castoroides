from cls.species import Species
from lib.intervals import Interval
from load_creature import CreatureInput, Status


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


# Wild Level: 1
def create_wild_1() -> CreatureInput:
    dodo = CreatureInput()

    dodo.name = "Wild_Dodo_1"
    dodo.imprint = Interval(0)
    dodo.level = 1
    dodo.stats = [40, 100, 30, 150, 450, 0, 0, 50, 1, 1, 0, 0]
    dodo.status = Status.Wild
    dodo.wild_levels = [0] * 12
    dodo.dom_levels = [0] * 12

    return dodo


# Wild Level: 1
# Tame Level: 1
#
# Taming Effectiveness: 75%
def create_tamed() -> CreatureInput:
    dodo = CreatureInput()

    dodo.name = "Tamed_Dodo_1"
    dodo.imprint = Interval(0)
    dodo.level = 1
    dodo.stats = [40.1, 100, 30.5, 150, 500.6, 0, 0, 50, 1.29, 3, 0, 0]
    dodo.status = Status.Wild
    dodo.wild_levels = [0] * 12
    dodo.dom_levels = [0] * 12

    return dodo


# Wild Level: 1
# Tame Level: 1 + 7
#
# Taming Effectiveness: 75%
def create_tamed_plus_doms() -> CreatureInput:
    dodo = CreatureInput()

    dodo.name = "Tamed_Doms_Dodo_1"
    dodo.imprint = Interval(0)
    dodo.level = 8
    dodo.stats = [42.2, 110, 30.5, 165, 550.7, 0, 0, 52, 1.312, 3.03, 0, 0]
    dodo.status = Status.Wild
    dodo.wild_levels = [0] * 12
    dodo.dom_levels = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]

    return dodo
