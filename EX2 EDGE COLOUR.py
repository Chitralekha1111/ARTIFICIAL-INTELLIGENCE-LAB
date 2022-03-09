class col:
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
 
 
def colourGraph(col):
    result = {}
    
    for u in range(N):
        assigned = set([result.get(i) for i in col.adj[u] if i in result])
 
        colour = 1
        for c in assigned:
            if colour != c:
                break
            colour = colour + 1
 
        result[u] = colour
 
    for v in range(N):
        print("  Colour given to  the edge", v, "is", colours[result[v]])
 

if __name__ == '__main__':
    colours = ["", "red", "gold", "indigo", "purple", "light green", "yellow",
              "blue", "violet", "grey", "white", "orange"]
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
    N = 6
    col = col(edges, N)
    colourGraph(col)
