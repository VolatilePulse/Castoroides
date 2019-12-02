import random
from typing import List


class Server:
    PerLevelStatsMultiplier_DinoWild: List[float]
    PerLevelStatsMultiplier_DinoTamed_Add: List[float]
    PerLevelStatsMultiplier_DinoTamed_Affinity: List[float]
    PerLevelStatsMultiplier_DinoTamed: List[float]
    BabyImprintingStatScaleMultiplier: float


def generate_random_server() -> Server:
    generated_server = Server()

    for stat_index in range(0, 12):
        generated_server.PerLevelStatsMultiplier_DinoWild[stat_index] = random.uniform(0, 100)
        generated_server.PerLevelStatsMultiplier_DinoTamed_Add[stat_index] = random.uniform(0, 100)
        generated_server.PerLevelStatsMultiplier_DinoTamed_Affinity[stat_index] = random.uniform(0, 100)
        generated_server.PerLevelStatsMultiplier_DinoTamed[stat_index] = random.uniform(0, 100)

    generated_server.BabyImprintingStatScaleMultiplier = random.uniform(0, 100)
    return generated_server
