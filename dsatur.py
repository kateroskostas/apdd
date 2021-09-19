from networkx import Graph
import networkx as nx

# Δημιουργώ μια συνάρτηση για να κάνω το χρωματισμό γράφου
def color_dsatur(graph: Graph):
    # δημιουργώ ενα κενό λεξικό για να καταχωρίσω μετα την λύση μου
    solution = dict()
    # Κάνω τον χρωματισμό του γράφου μου επιλέγοντας την τεχνική DSATUR
    solution = nx.coloring.greedy_color(graph, strategy="DSATUR")
    return solution
