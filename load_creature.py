from configparser import ConfigParser
from dataclasses import dataclass
from enum import IntEnum
from typing import List

from mpmath import mpf, mpi


class Status(IntEnum):
    Wild = 1
    Tamed = 2
    Bred = 3


@dataclass(init=False)
class Creature:
    name: str
    species_bp: str
    status: Status
    level: int
    imprint: mpi
    stats: List[mpf]


def load_export_init(filename: str):
    parser = ConfigParser(inline_comment_prefixes='#;')
    parser.optionxform = lambda v: v  # keep exact case of mod names, please
    parser.read(filename)

    creature = Creature()

    creature.name = parser['Dino Data']['DinoNameTag']
    creature.species_bp = parser['Dino Data']['DinoClass']
    creature.status = Status.Tamed
    if parser['Dino Data'].get('ImprinterName', '').strip():
        creature.status = Status.Bred
    if parser['Dino Data']['BabyAge'] != '1.000000':
        raise ValueError("Not fully grown")
    creature.level = int(parser['Dino Data']['CharacterLevel'])
    creature.imprint = mpi(parser['Dino Data']['DinoImprintingQuality'])

    creature.stats = [
        mpf(txt) for txt in parser['Max Character Status Values'].values()
    ]

    return creature
