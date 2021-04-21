import math
from dataclasses import dataclass
from typing import List, Optional
from model.data import Node
from model.calc_node import CalcNode
import heapq


@dataclass
class Astar():
    start: Node
    goal: Node

    def calculate(self) -> List[Node]:
        target: CalcNode
        open_list: List[CalcNode] = []
        close_list: List[CalcNode] = []
        heapq.heapify(open_list)

        start = CalcNode(self.start)
        start.total = self.__heuristic(start)

        heapq.heappush(open_list, start)

        while True:
            if len(open_list) == 0:
                print('No route found')
                return []

            target = heapq.heappop(open_list)
            if target.node == self.goal:
                break

            close_list.append(target)

            target.real = target.total - self.__heuristic(target)            
            for candidate in target.nexts:
                total = target.real  + self.__cost(target, candidate) + self.__heuristic(candidate)
                opened_candidate = self.__find_candidate(open_list, candidate)
                if opened_candidate is not None:
                    if total < opened_candidate.total:
                        open_list.remove(opened_candidate)
                        opened_candidate.total = total
                        opened_candidate.parent = target
                        heapq.heappush(open_list, opened_candidate)
                else:
                    closed_candidate = self.__find_candidate(close_list, candidate)
                    if closed_candidate is not None:
                        if total < closed_candidate.total:
                            close_list.remove(closed_candidate)
                            closed_candidate.total = total
                            closed_candidate.parent = target
                            heapq.heappush(open_list, closed_candidate)
                    else:
                        candidate.total = total
                        candidate.parent = target
                        heapq.heappush(open_list, candidate)    

        return [li.node for li in reversed(list(target))]

    def __heuristic(self, node: CalcNode) -> float:
        return math.sqrt((node.x - self.goal.x)**2 + (node.y - self.goal.y)**2)
        
    def __cost(self, target: CalcNode, candidate: CalcNode) -> float:
        return math.sqrt((candidate.x - target.x)**2 + (candidate.y - target.y)**2)

    def __find_candidate(self, li: List[CalcNode], candidate: CalcNode) -> Optional[CalcNode]:
        for idx, node in enumerate(li):
            if node == candidate:
                return li[idx]
        return None

        

