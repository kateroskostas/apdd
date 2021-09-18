from networkx import Graph
import networkx as nx


def color_dsatur(graph: Graph):
    solution = dict()
    solution = nx.coloring.greedy_color(graph, strategy="DSATUR")
    return solution