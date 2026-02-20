import networkx as nx

class SchedulerAgent:

    def schedule(self, graph, valid_tasks):
        order = list(nx.topological_sort(graph))
        return [t for t in order if t in valid_tasks]
