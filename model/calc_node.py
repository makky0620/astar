from dataclasses import dataclass, field
from typing import Any, List, Optional
from model.data import Node

@dataclass
class CalcNode:
    node: Node
    gn: float = 0.0 # 実績コスト
    hn: float = 0.0 # 推定コスト
    parent: Optional['CalcNode'] = field(default=None, repr=False)
    _nexts: Optional[List['CalcNode']] = field(default=None, repr=False)

    @property
    def x(self):
        return self.node.x

    @property
    def y(self):
        return self.node.y

    @property
    def nexts(self) -> List['CalcNode']:
        if self._nexts is None:
            self._nexts = [CalcNode(edge.get_opposite_node(self.node)) for edge in self.node.edges]
        return self._nexts

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, CalcNode):
            return NotImplemented
        return self.total < other.total

    def __eq__(self, o: Any) -> bool:
        if not isinstance(o, CalcNode):
            return NotImplemented
        return self.node.id == o.node.id

    def __iter__(self):
        current = self
        while current is not None:
            yield current
            current = current.parent

