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

    @property
    def random_photos(self):
        photos_all = self.photos.all()
        indices = get_random_incides(len(photos_all), 4)
        photos_random = [photos_all[i] for i in indices]
        return photos_random


class Photo(m.Model):
    tripinfo = m.ForeignKey(TripInfo, on_delete=m.CASCADE, related_name="photos")
    url = m.URLField()
