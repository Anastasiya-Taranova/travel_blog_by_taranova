import itertools
import random
from typing import Tuple

from django.db import models as m


def get_random_incides(length, plex) -> Tuple[int]:
    indices = range(length)
    combinations = tuple(itertools.combinations(indices, plex))
    combination = random.choice(combinations)
    shuffled = tuple(sorted(combination, key=lambda i: random.random()))
    return shuffled


class TripInfo(m.Model):
    country = m.TextField(unique=True)
    descr = m.TextField(null=True, blank=True)
    number = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Trip Info"



