 import networkx as nx

def add_acronym_node_to_graph(graph, acronym, possible_meanings, context=None, relevance=0.5, related_nodes_weights=None):
    """
    Adds an ambiguous acronym node to the graph with attributes and probabilistic edges.

    Args:
    - graph (networkx.Graph): The graph to modify.
    - acronym (str): The ambiguous acronym (e.g., 'OSA').
    - possible_meanings (list[str]): List of potential interpretations.
    - context (str): Contextual clue or location where the acronym appeared.
    - relevance (float): Overall relevance score of this acronym to the graph's domain.
    - related_nodes_weights (dict): Dictionary of related nodes and their edge weights.
    """
    graph.add_node(acronym,
                   possible_meanings=possible_meanings,
                   context=context,
                   relevance=relevance,
                   type='acronym')

    if related_nodes_weights:
        for node, weight in related_nodes_weights.items():
            if node in graph.nodes:
                graph.add_edge(acronym, node, weight=weight)

    return graph
    # Initialize graph
graph = nx.Graph()
graph.add_nodes_from(["temperature", "humidity", "cloudy"])

# Define OSA possible meanings
osa_meanings = [
    "Optical Spectrum Analyzer",
    "Outside Air",
    "Obstructive Sleep Apnea"
]

# Add OSA node with example relationships
related_weights = {
    "temperature": 0.6,
    "humidity": 0.7,
    "cloudy": 0.3
}

graph = add_acronym_node_to_graph(
    graph,
    acronym="OSA",
    possible_meanings=osa_meanings,
    context="weather app interface",
    relevance=0.8,
    related_nodes_weights=related_weights
)

# Inspect
print(graph.nodes["OSA"])
print(list(graph.edges("OSA", data=True)))
feature_vector = {
    "OSA": 1,
    "OSA_is_outside_air": 1,
    "OSA_is_obstructive_sleep_apnea": 0,
    "temperature": 73,
    "humidity": 45,
    "context_contains": "weather app"
}colors = ['red' if graph.nodes[node].get('type') == 'acronym' else 'skyblue' for node in graph.nodes]

nx.draw(graph, with_labels=True, node_color=colors, node_size=2000, font_weight='bold')
plt.show()
