from model.data import Node, Edge
import graph.simple_graph as graph

from PIL import Image, ImageDraw
from typing import Dict, List, Tuple


BG_COLOR = (255, 255, 255)

NODE_R = 4
NODE_COLOR = (0, 0, 255)

EDGE_COLOR = (0, 0, 0)


def show_baseimage(size: Tuple, bg_color: Tuple, nodes: Dict[str, Node], edges: List[Edge]):
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    for node in nodes.values():
        draw.ellipse((node.x - NODE_R, node.y - NODE_R, node.x + NODE_R, node.y + NODE_R), fill=NODE_COLOR)
    for edge in edges:
            draw.line((edge.start.as_tuple(), edge.end.as_tuple()), fill=EDGE_COLOR)
    img.save('maze.png')

def load_graph() -> Tuple[Tuple[int, int], Dict[str, Node], List[Edge], Node, Node]:
    size: Tuple[int, int] = graph.SIZE
    nodes: Dict[str, Node] = graph.NODES
    edges: List[Edge] = graph.EDGES
    start_node: Node = graph.START_NODE
    goal_node: Node = graph.GOAL_NODE

    for node in nodes.values():
        node.edge = [edge for edge in edges if edge.start == node or edge.end == node]

    return size, nodes, edges, start_node, goal_node

def main() -> None:
    size, nodes, edges, start_node, goal_node = load_graph()
    show_baseimage(size, BG_COLOR, nodes, edges)
    
    

if __name__ == '__main__':
    main()