import random
from typing import List

import species.dodo as dodo
from cls.server import Server, generate_random_server
from lib.intervals import *
from utils import *


def main():
    # creature
    species = dodo.create_species()
    server = generate_random_server()

    server_IwM: List[float] = server.PerLevelStatsMultiplier_DinoWild
    server_TaM: List[float] = server.PerLevelStatsMultiplier_DinoTamed_Add
    server_TmM: List[float] = server.PerLevelStatsMultiplier_DinoTamed_Affinity
    server_IdM: List[float] = server.PerLevelStatsMultiplier_DinoTamed
    server_bissm: float = server.BabyImprintingStatScaleMultiplier

    for stat_index in range(0, 12):
        if server_IwM[stat_index] == 0.0:
            server_IwM[stat_index] = 1.0
        if server_TaM[stat_index] == 0.0:
            server_TaM[stat_index] = 1.0
        if server_TmM[stat_index] == 0.0:
            server_TmM[stat_index] = 1.0
        if server_IdM[stat_index] == 0.0:
            server_IdM[stat_index] = 1.0


if __name__ == "__main__":
    main()
