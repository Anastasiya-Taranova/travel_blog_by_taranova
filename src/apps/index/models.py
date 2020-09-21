import itertools
import random
from typing import Tuple




def get_random_incides(length, plex) -> Tuple[int]:
    indices = range(length)
    combinations = tuple(itertools.combinations(indices, plex))
    combination = random.choice(combinations)
    shuffled = tuple(sorted(combination, key=lambda i: random.random()))
    return shuffled

