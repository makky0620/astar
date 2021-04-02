from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Node:
    x: int
    y: int
    edges: List['Edge'] = field(default_factory=list, repr=False)

    def as_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

@dataclass
class Edge:
    start: Node
    end: Node

