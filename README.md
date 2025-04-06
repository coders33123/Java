jaris/
│
├── graph_core.py          # GraphManager: adds nodes, edges, snapshots
├── context_encoder.py     # ContextEncoder: semantic + numeric encoding
├── visualizer.py          # Visualizer: Matplotlib + Pyvis graph views
├── logger.py              # Logger: history, acronym logs, version tracking
├── feedback_loop.py       # FeedbackManager: edge weight learning
│
├── jaris_notebook.ipynb   # Jupyter notebook: interactive brainspace
├── demo_data/             # (Optional) Seed acronyms, example contexts
└── README.md              # Documentation overview
import networkx as nx

class GraphManager:
    def __init__(self):
        self.graph = nx.Graph()

    def add_acronym_node(self, acronym, meanings, context="", relevance=1.0, related_nodes_weights=None):
        if acronym not in self.graph:
            self.graph.add_node(acronym, type='acronym', meanings=meanings, context=context, relevance=relevance)

        if related_nodes_weights:
            for related_node, weight in related_nodes_weights.items():
                self.graph.add_edge(acronym, related_node, weight=weight)

    def add_edge(self, node1, node2, weight=1.0):
        self.graph.add_edge(node1, node2, weight=weight)

    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))

    def get_node_data(self, node):
        return self.graph.nodes.get(node, {})

    def snapshot_graph(self, filename="graph_snapshot.gml"):
        nx.write_gml(self.graph, filename)
