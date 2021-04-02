from dataclasses import dataclass, field
from typing import Optional
from model.data import Node

@dataclass
class CalcNode:
    node: Node
    gn: float = 0.0 # 実績コスト
    hn: float = 0.0 # 推定コスト
    parent: Optional['CalcNode'] = field(default=Node, repr=False)

    def x(self):
        return self.node.x


    def y(self):
        return self.node.y