from dataclasses import dataclass


@dataclass
class Actor:
    """This class represents an actor."""

    name: str
    movie_appearance_count: int
