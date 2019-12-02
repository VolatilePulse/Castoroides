from configparser import ConfigParser
from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional

from lib.intervals import Float, Interval


class Status(IntEnum):
    Wild = 1
    Tamed = 2
    Bred = 3


@dataclass(init=False)
class CreatureInput:
    name: str
    species_bp: str
    status: Status
    level: int
    imprint: Interval
    stats: List[Float]
    wild_levels: Optional[List[int]]
    dom_levels: Optional[List[int]]


def load_export_init(filename: str):
    parser = ConfigParser(inline_comment_prefixes='#;')
    parser.optionxform = lambda v: v  # keep exact case of mod names, please
    parser.read(filename)

    creature = CreatureInput()

    creature.name = parser['Dino Data']['DinoNameTag']
    creature.species_bp = parser['Dino Data']['DinoClass']
    creature.status = Status.Tamed
    if parser['Dino Data'].get('ImprinterName', '').strip():
        creature.status = Status.Bred
    if parser['Dino Data']['BabyAge'] != '1.000000':
        raise ValueError("Not fully grown")
    creature.level = int(parser['Dino Data']['CharacterLevel'])
    creature.imprint = Interval(parser['Dino Data']['DinoImprintingQuality'])

    creature.stats = [Float(txt) for txt in parser['Max Character Status Values'].values()]

    return creature
