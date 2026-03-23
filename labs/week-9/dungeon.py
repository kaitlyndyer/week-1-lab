# WEEK 9 LAB

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)
        vertex.adjacent_vertices.append(self)


entrance = Vertex("Entrance Hall")
torch = Vertex("Torch Corridor")
map_room = Vertex("Map Room")
flooded = Vertex("Flooded Passage")
trap = Vertex("Trap Room")
crystal = Vertex("Crystal Chamber")
armoury = Vertex("Armoury")
boss = Vertex("Boss Chamber")

entrance.add_adjacent_vertex(torch)
entrance.add_adjacent_vertex(map_room)
entrance.add_adjacent_vertex(flooded)
torch.add_adjacent_vertex(map_room)
torch.add_adjacent_vertex(trap)
map_room.add_adjacent_vertex(crystal)
trap.add_adjacent_vertex(armoury)
crystal.add_adjacent_vertex(armoury)
crystal.add_adjacent_vertex(boss)
armoury.add_adjacent_vertex(boss)

def dfs_traverse(vertex, visited=None, hops=0):
    if visited == None:
        visited = set()
    visited.add(vertex)
    print(f'{vertex.value}: {hops} hops')
    for neighbour in vertex.adjacent_vertices:
        if neighbour not in visited:
            dfs_traverse(neighbour, visited, hops + 1)

dfs_traverse(entrance)
