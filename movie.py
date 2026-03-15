from dataclasses import dataclass
from typing import List


@dataclass
class Movie:
    """This class represents a movie."""

    name: str
    starring_actors: List[str]
