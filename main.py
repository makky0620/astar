from calculator.astar import Astar
from model.data import Node, Edge
import graph.simple_graph as graph

from PIL import Image, ImageDraw
from typing import Dict, List, Tuple
import time


BG_COLOR = (255, 255, 255)

NODE_R = 4
NODE_COLOR = (0, 0, 255)

EDGE_COLOR = (0, 0, 0)

PATH_WIDTH = 3
PATH_COLOR = (255, 0, 0)

def show_baseimage(size: Tuple, bg_color: Tuple, nodes: Dict[str, Node], edges: List[Edge]):
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    for node in nodes.values():
        draw.ellipse((node.x - NODE_R, node.y - NODE_R, node.x + NODE_R, node.y + NODE_R), fill=NODE_COLOR)
    for edge in edges:
            draw.line((edge.start.as_tuple(), edge.end.as_tuple()), fill=EDGE_COLOR)
    return img

def load_graph() -> Tuple[Tuple[int, int], Dict[str, Node], List[Edge], Node, Node]:
    size: Tuple[int, int] = graph.SIZE
    nodes: Dict[str, Node] = graph.NODES
    edges: List[Edge] = graph.EDGES
    start_node: Node = graph.START_NODE
    goal_node: Node = graph.GOAL_NODE

    for node in nodes.values():
        node.edges = [edge for edge in edges if edge.start == node or edge.end == node]

    return size, nodes, edges, start_node, goal_node

def draw_path(filename: str, size: Tuple[int, int], nodes: Dict[str, Node], edges: List[Edge], path: List[Node]) -> None:
    points = [node.as_tuple() for node in path]

    img = show_baseimage(size, BG_COLOR, nodes, edges)
    draw = ImageDraw.Draw(img)
    draw.line(points, fill=PATH_COLOR, width=PATH_WIDTH)
    img.save(filename)

def main() -> None:
    size, nodes, edges, start_node, goal_node = load_graph()
    start = time.time()
    path = Astar(start_node, goal_node).calculate()
    print(f'finish astar searching, time={time.time() - start}')
    draw_path('path.jpg', size, nodes, edges, path)



if __name__ == '__main__':
    main()