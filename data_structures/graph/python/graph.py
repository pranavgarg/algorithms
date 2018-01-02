class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return "{} node".format(self.value)
class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to
    def __repr__(self):
        return "{} edge-weight from: {} to: {}".format(self.value, self.node_from, self.node_to)

class Graph:
    def __init__(self, nodes = [], edges = []):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def __repr__(self):
        return "Graph with {} node {} edge".format(len(self.nodes), len(self.edges))

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        output = []
        for i in self.edges:
            return_tuple = (i.value, i.node_from.value, i.node_to.value)
            output.append(return_tuple)
        return output

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_node = self.find_max_index()
        output = [None] *(max_node+1)
        for i in self.edges:
            if output[i.node_from.value]:
                output[i.node_from.value].append((i.node_to.value, i.value))
            else:
                output[i.node_from.value] = [(i.node_to.value, i.value)]
        return output

    def get_adjacency_matrix(self):
        max_node = self.find_max_index()
        output = []
        for i in range(max_node+1):
            adj_list = [0] * (max_node+1)
            for j in self.edges:
                if j.node_from.value == i:
                    adj_list[j.node_to.value] = j.value
            output.append(adj_list)
        return output

    def find_max_index(self):
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
assert graph.get_edge_list() == [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
assert graph.get_adjacency_list() == [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
assert graph.get_adjacency_matrix() == [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]