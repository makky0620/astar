from dataclasses import dataclass, field
from typing import List, Tuple
import uuid

class Node:
    id: int
    x: int
    y: int
    edges: List['Edge']

    def __init__(self, x, y) -> None:
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.edges = []

    def as_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return NotImplemented
        return self.x == o.x and self.y == o.y

@dataclass
class Edge:
    start: Node
    end: Node

    def get_opposite_node(self,  node: Node) -> Node:
        return self.end if self.start == node else self.start

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Edge):
            return NotImplemented
        return self.start == o.start and self.end == o.end

