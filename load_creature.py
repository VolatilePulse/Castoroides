from configparser import ConfigParser
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional

from lib.intervals import Float, I
from utils import possible_inputs_from_rounded


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
    imprint: I
    stats: List[I]
    wild_levels: Optional[List[int]] = None
    dom_levels: Optional[List[int]] = None


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
    creature.imprint = I(parser['Dino Data']['DinoImprintingQuality'])

    creature.stats = [
        possible_inputs_from_rounded(Float(txt), digits=6) for txt in parser['Max Character Status Values'].values()
    ]

    return creature
