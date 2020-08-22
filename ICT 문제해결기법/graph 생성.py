class Vertex :
    def __init__(self, name) :
        self.name = name
        self.W = {} # 멤버 변수

    def add_neighbor(self, v, w=0) :
        self.W[v] = w

    def get_weight(self, v) :
        return self.W[v]

    def get_neighbors(self) :
        return list(self.W.keys())
    
    # indexing 연산 -- 구글링 필요
    def __getitem__(self, v) :
        return self.get_weight(v)
    # __str__와 유사, repr의 경우 디버깅 용이 -- class 에서 string으로 바꾸어주는 method

    def __repr__(self) :
        return "Vertex('{}', {})".format(self.name, repr(self.W))

class Graph :
    def __init__(self) :
        self.V = {}
    # for i in ~~ : 이거 가능하게 해주는 기능
    def __iter__(self) :
        return iter(self.V.values())
    def add_vertex(self, v) :
        self.V[v] = Vertex(v)

    def add_edge(self, v1,v2, w=0) :
        if v1 not in self.V : self.add_vertex(v1)
        if v2 not in self.V : self.add_vertex(v2)
        self.V[v1].add_neighbor(v2, w)
        self.V[v2].add_neighbor(v1, w)

    def get_vertex(self, v) :
        return self.V[v] if v in self.V else None

    def get_vertices(self) :
        return list(self.V.keys())

    def __getitem__(self, v) :
        return self.get_vertex(v)

    def __repr__(self) :
        return repr(self.V)

class DiGraph(Graph) :
    def add_edge(self, v1, v2, w=0) :
        if v1 not in self.V : self.add_vertex(v1)
        if v2 not in self.V : self.add_vertex(v2)
        self.V[v1].add_neighbor(v2, w)

g = Graph()
g.add_edge('a', 'b', 5)
g.add_edge('a', 'c', 10)
g.add_edge('b', 'd', 3)
for v in g :
    print(v)
print(g.get_vertices())
print(g['a'].get_neighbors())
print(g['a']['b'],g['c']['a'])
