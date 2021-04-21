import random
from model.data import Node, Edge

from typing import List, Dict, Tuple

SIZE: Tuple[int, int] = (1000, 1000)

WIDTH: int = 20
CNT: int = 50
STD: float = 10.0
P: float = 0.15

NODES: Dict[str, Node] = {f'N{i:02}{j:02}': Node(WIDTH * i, WIDTH * j) for i in range(1, CNT) for j in range(1, CNT)}
NODES = {k: Node(int(random.gauss(node.x, STD)), int(random.gauss(node.y, STD))) for k, node in NODES.items()}

row: List[Edge] = [Edge(NODES[f'N{i:02}{j:02}'], NODES[f'N{i:02}{j + 1:02}']) for i in range(1, CNT) for j in range(1, CNT - 1)]
col: List[Edge] = [Edge(NODES[f'N{i:02}{j:02}'], NODES[f'N{i + 1:02}{j:02}']) for i in range(1, CNT - 1) for j in range(1, CNT)]
EDGES: List[Edge] = row + col
EDGES = [edge for edge in EDGES if random.random() > P]

START_NODE = NODES[f'N{1:02}{1:02}']
GOAL_NODE = NODES[f'N{CNT - 1:02}{CNT - 1:02}']
