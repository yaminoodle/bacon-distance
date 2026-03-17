from dataclasses import dataclass
from enum import Enum


class NodeType(Enum):
    Actor = "Actor"
    Movie = "Movie"


@dataclass
class Node:
    """Represents a node in the bacon-distance graph."""

    type: NodeType
    id: str
    distance: int
