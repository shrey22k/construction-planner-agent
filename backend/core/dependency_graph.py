import networkx as nx

class DependencyGraph:

    def build(self, tasks):
        G = nx.DiGraph()

        for t in tasks:
            G.add_node(t["task"])
            for d in t["depends_on"]:
                G.add_edge(d, t["task"])

        if not nx.is_directed_acyclic_graph(G):
            raise Exception("Dependency Cycle Found")

        return G
