class Graph:
    def _init_(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def colorGraph(graph, n):

    result = {}

    for u in range(n):

        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])

        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        result[u] = color
 
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')
 

if __name__ == '__main__':

    colors = ['', 'RED', 'YELLOW', 'BLUE', 'GREEN', 'PURPLE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'ORANGE', 'VOILET']

    edges = [(0, 1), (0, 2), (1, 5), (2, 5), (2, 4), (2, 3), (0, 3), (1, 4)]

    n = 6
    graph = Graph(edges, n)

    colorGraph(graph, n)
