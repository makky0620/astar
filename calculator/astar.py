import math
from dataclasses import dataclass
from typing import List
from model.data import Node, Edge
from model.calc_node import CalcNode
import heapq


@dataclass
class Astar():
    start: Node
    goal: Node

    def calculate(self) -> List[Node]:
        target: CalcNode

        open_list = []
        heapq.heapify(open_list)

        start = CalcNode(self.start)
        start.hn = self.heuristic(start)

        heapq.heappush(open_list, start)

        while True:
            break

    def heuristic(self, node: Node):
        return math.sqrt((node.x - self.goal.x)**2 + (node.y - self.goal.y)**2)
        


