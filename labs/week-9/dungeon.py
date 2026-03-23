# WEEK 9 LAB
import heapq

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
# Which room is furthest from the Entrance Hall?
# - The Trap Room and Boss Chamber are furthest from the Entrance Hall because the DFS went to the deepest level before backtracking

# Are there any rooms at the same number of hops? What does that tell you about the structure of the dungeon?
# - The Torch Corridor and the Flooded Passage have the same number of hops because and tell us that the Entrance Hall is well connected
# - Similarly the Boss Chamber and the Trap Room are equally the furthest away from the Entrance Hall, showing that there are multiple pathes to in the Dungeon.


class Room:
    def __init__(self, name):
        self.name = name
        self.passages = {}      # {Room: cost}

    def __eq__(self, other):
        return isinstance(other, Room) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"Room({self.name})"

    def add_passage(self, room, cost):
        self.passages[room] = cost


def connect(a, b, cost):
    a.add_passage(b, cost)
    b.add_passage(a, cost)

entrance = Room("Entrance Hall")
torch = Room("Torch Corridor")
map_room = Room("Map Room")
flooded = Room("Flooded Passage")
trap = Room("Trap Room")
crystal = Room("Crystal Chamber")
armoury = Room("Armoury")
boss = Room("Boss Chamber")

connect(entrance, torch, 3)
connect(entrance, map_room, 2)
connect(entrance, flooded, 4)
connect(torch, map_room, 3)
connect(torch, trap, 5)
connect(map_room, crystal, 4)
connect(trap, armoury, 3)
connect(crystal, armoury, 3)
connect(crystal, boss, 5)
connect(armoury, boss, 7)


def dijkstra(start):
    cheapest_cost = {start: 0}
    previous_room = {}
    visited = set()

    pq = [(0, start)]
    while pq:
        current_cost, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        for neighbour, cost in current.passages.items():
            if neighbour in visited:
                continue

            new_cost = current_cost + cost

            if (neighbour not in cheapest_cost or new_cost < cheapest_cost[neighbour]):
                cheapest_cost[neighbour] = new_cost
                previous_room[neighbour] = current
                heapq.heappush(pq, (new_cost, neighbour))
    return cheapest_cost, previous_room


def shortest_route(start, destination):
    cheapest_cost, previous_room = dijkstra(start)

    route = []
    current = destination

    while current is not None:
        route.append(current.name)
        current = previous_room.get(current)
    route.reverse()

    cost = cheapest_cost.get(destination, None)
    print(f"{destination.name}")
    print(f'Route: {' - '.join(route)}')
    print(f'Total tiles: {cost}')


shortest_route(entrance, boss)



