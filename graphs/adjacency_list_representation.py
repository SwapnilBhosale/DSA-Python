class Vertex:
    def __init__(self, v):
        self.vertex = v
        self.adjacent = {}
        self.visited = False

    def is_visited(self):
        return self.visited

    def add_neighbour(self, v, w):
        self.adjacent[v] = w

    def get_neighbours(self):
        return self.adjacent.keys()

    def get_neighbour_weight(self, n):
        return self.adjacent[n]

class Graph:

    def __init__(self, directed=False):
        self.vertices = {}
        self.num_of_vertices = 0
        self.directed = directed

    def add_vertex(self, v):
        vertex = Vertex(v)
        self.vertices[v] = vertex
        self.num_of_vertices += 1
        return vertex

    def add_edge(self, frm, to, weight=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbour(self.vertices[to], weight)

        if not self.directed:
            self.vertices[to].add_neighbour(self.vertices[frm], weight)

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()


    def get_edges(self):
        edges = []
        for v in self.vertices:
            edge_from_vertex = []

            for w in self.vertices[v].get_neighbours():
                frm = self.vertices[v].vertex
                to = w.vertex
                weight = self.vertices[v].adjacent[w]
                edge_from_vertex.append((frm, to, weight))

            if len(edge_from_vertex) != 0:
                edges.append(edge_from_vertex)

        return edges


g = Graph(directed=True)
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')

g.add_edge('a', 'b', 2)
g.add_edge('a','c', 5)
g.add_edge('c', 'e', 3)
g.add_edge('e', 'b', 10)

for e in g.get_edges():
    print("edge from {} ".format(e[0][0]), end=' ')
    print(e)