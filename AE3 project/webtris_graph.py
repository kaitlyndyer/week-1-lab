# AE3 Project
import heapq
from collections import deque

# I started by pasting the pre-fetched data into the file
data = {
  "7-12": [
    {
      "id": 138,
      "site_name": "M25/4546A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1243
    },
    {
      "id": 144,
      "site_name": "M25/4681A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 36,
      "volume": 1510
    },
    {
      "id": 479,
      "site_name": "M25/4806A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 48,
      "volume": 1337
    },
    {
      "id": 544,
      "site_name": "M25/4700A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 23,
      "volume": 1230
    },
    {
      "id": 547,
      "site_name": "M25/4515A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 55,
      "volume": 1091
    },
    {
      "id": 699,
      "site_name": "M25/4479A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 59,
      "volume": 1359
    },
    {
      "id": 752,
      "site_name": "M25/4475A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 60,
      "volume": 1368
    },
    {
      "id": 778,
      "site_name": "M25/4811A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 885,
      "site_name": "M25/4565A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 60,
      "volume": 1204
    },
    {
      "id": 1135,
      "site_name": "M25/4690A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 1221,
      "site_name": "M25/4757A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 1270,
      "site_name": "M25/4534A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1243
    },
    {
      "id": 1442,
      "site_name": "M25/4605A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 51,
      "volume": 1395
    },
    {
      "id": 1990,
      "site_name": "M25/4620A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2005,
      "site_name": "M25/4483A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2089,
      "site_name": "M25/4777A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2097,
      "site_name": "M25/4497A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 61,
      "volume": 1104
    },
    {
      "id": 2149,
      "site_name": "M25/4826A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 54,
      "volume": 1651
    },
    {
      "id": 2419,
      "site_name": "M25/4617J",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2486,
      "site_name": "M25/4509A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 55,
      "volume": 1097
    },
    {
      "id": 2530,
      "site_name": "M25/4752A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2636,
      "site_name": "M25/4787A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 45,
      "volume": 1593
    },
    {
      "id": 3003,
      "site_name": "M25/4696A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 29,
      "volume": 1179
    },
    {
      "id": 3323,
      "site_name": "M25/4583A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 55,
      "volume": 1238
    },
    {
      "id": 3437,
      "site_name": "M25/4490A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1122
    },
    {
      "id": 3714,
      "site_name": "M25/4822A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 53,
      "volume": 1651
    },
    {
      "id": 3835,
      "site_name": "M25/4658A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 30,
      "volume": 1329
    },
    {
      "id": 3897,
      "site_name": "M25/4792A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 51,
      "volume": 1576
    },
    {
      "id": 4000,
      "site_name": "M25/4551A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4092,
      "site_name": "M25/4522A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 58,
      "volume": 1216
    },
    {
      "id": 4145,
      "site_name": "M25/4501A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 57,
      "volume": 1113
    },
    {
      "id": 4202,
      "site_name": "M25/4662A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 47,
      "volume": 1460
    },
    {
      "id": 4223,
      "site_name": "M25/4617A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4714,
      "site_name": "M25/4762A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4719,
      "site_name": "M25/4470A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 59,
      "volume": 1148
    },
    {
      "id": 4761,
      "site_name": "M25/4747A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4894,
      "site_name": "M25/4802A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 47,
      "volume": 1366
    },
    {
      "id": 5107,
      "site_name": "M25/4817A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 50,
      "volume": 1648
    },
    {
      "id": 5118,
      "site_name": "M25/4686A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 30,
      "volume": 1235
    },
    {
      "id": 5138,
      "site_name": "M25/4772A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 5176,
      "site_name": "M25/4767A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 38,
      "volume": 1536
    },
    {
      "id": 5261,
      "site_name": "M25/4742A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 34,
      "volume": 1432
    },
    {
      "id": 5288,
      "site_name": "M25/4592A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 46,
      "volume": 1311
    },
    {
      "id": 5526,
      "site_name": "M25/4637A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 54,
      "volume": 1355
    },
    {
      "id": 5546,
      "site_name": "M25/4783A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 37,
      "volume": 1595
    },
    {
      "id": 5712,
      "site_name": "M25/4653A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 5875,
      "site_name": "M25/4507A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 56,
      "volume": 1085
    },
    {
      "id": 5990,
      "site_name": "M25/4797A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 6156,
      "site_name": "M25/4537A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 65,
      "volume": 1182
    }
  ],
  "12-13": [
    {
      "id": 8,
      "site_name": "M25/4876A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1661
    },
    {
      "id": 1811,
      "site_name": "M25/4848A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1684
    },
    {
      "id": 1910,
      "site_name": "M25/4860A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2952,
      "site_name": "M25/4866A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1647
    },
    {
      "id": 2992,
      "site_name": "M25/4832A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 60,
      "volume": 974
    },
    {
      "id": 3319,
      "site_name": "M25/4854A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 65,
      "volume": 1663
    },
    {
      "id": 5245,
      "site_name": "M25/4879A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 61,
      "volume": 1640
    },
    {
      "id": 5662,
      "site_name": "M25/4843A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 5681,
      "site_name": "M25/4836A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 61,
      "volume": 1035
    }
  ],
  "13-14": [
    {
      "id": 279,
      "site_name": "M25/4909A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 41,
      "volume": 1555
    },
    {
      "id": 737,
      "site_name": "M25/4883A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1341
    },
    {
      "id": 3671,
      "site_name": "M25/4898A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 54,
      "volume": 1601
    },
    {
      "id": 4053,
      "site_name": "M25/4903A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 40,
      "volume": 1527
    },
    {
      "id": 4354,
      "site_name": "M25/4887A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1305
    },
    {
      "id": 5317,
      "site_name": "M25/4892A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 57,
      "volume": 1310
    }
  ],
  "14-Heathrow": [
    {
      "id": 746,
      "site_name": "M25/7106B",
      "time": "2026-01-19T08:59:00",
      "average_mph": 34,
      "volume": 226
    }
  ],
  "A30": [
    {
      "id": 9005,
      "site_name": "6178/1",
      "time": "2026-01-19T08:59:00",
      "average_mph": 57,
      "volume": 330
    }
  ]
}

# GRAPH CONSTRUCTION
# NODES
class Station:
    def __init__(self, name):
        self.name = name
        # this stores the connections to the other stations
        # the key is the Station and the value is the time travel which is the graph weight
        self.connections = {}

    def __eq__(self, other):
        # this is needed so that the stations can be compared
        return isinstance(other, Station) and self.name == other.name
    
    def __hash__(self):
        # here we add this so that the stations can be used as dictionary keys
        return hash(self.name)
    
    def __lt__(self, other):
        # this is used for the priority queue we create (the heapq)
        return self.name < other.name
    
    def __repr__(self):
        return f'Station({self.name})'
    
    def add_connection(self, station, time):
        # add a connection with the travel time, which is the weight of the connection
        self.connections[station] = time

# Create a function to connect the stations
def connect(station_a, station_b, time):
    # the is for an undirected graph which goes both ways in the connection
    station_a.add_connection(station_b, time)
    station_b.add_connection(station_a, time)


# Creating stations
j7 = Station("Junction 7")
j12 = Station("Junction 12")
j13 = Station("Junction 13")
j14 = Station("Junction 14")
heathrow = Station("Heathrow")

# FUNCTIONS
# create an average speed function
def average_speed(sensor_list):
    # collect all valid speeds (ignore None)
    speeds = []
    for sensor in sensor_list:
        if sensor["average_mph"] is not None:
            speeds.append(sensor["average_mph"])

    # return the average speed
    return sum(speeds) / len(speeds)

def travel_time(distance, speed):
    time = (distance / speed) * 60
    return round(time, 1)


# EDGE WIGHTS
# get the average speeds
speed_7_12 = average_speed(data["7-12"])
speed_12_13 = average_speed(data["12-13"])
speed_13_14 = average_speed(data["13-14"])
speed_14_h = average_speed(data["14-Heathrow"])
speed_a30 = average_speed(data["A30"])

# getting the travel time
time_7_12 = travel_time(23, speed_7_12)
time_12_13 = travel_time(3, speed_12_13)
time_13_14 = travel_time(3, speed_13_14)
time_14_h = travel_time(3, speed_14_h)
time_a30 = travel_time(3.8, speed_a30)
time_route_b = 20

# Creating the weighted graph
# main route
connect(j7, j12, time_7_12)
connect(j12, j13, time_12_13)
connect(j13, j14, time_13_14)
connect(j14, heathrow, time_14_h)

# second route
connect(j12, heathrow, time_route_b) 

# third route
connect(j13, heathrow, time_a30)



# ALGORITHMS
# Breadth-First Search (BFS)
# Find the path with the fewest nodes (fewest junctions/stops)
# - return the sequence of nodes in the path
# - return the total cost/weight of the path
def bfs(start, end):
    # queue of the stations to visit
    queue = deque([start])

    # keeping track of the visited stations and adding the starting station
    visited = {start}

    # we store how we reach each station in a dictionary
    previous = {}

    while queue:
        # get the first station
        current = queue.popleft()

        # if we reach the ending station stop
        if current == end:
            break

        # check neighbours of the station
        for neighbour in current.connections:
            if neighbour not in visited:
                visited.add(neighbour)
                previous[neighbour] = current # this is to remember the path we take
                queue.append(neighbour)
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous.get(current)
    
    path.reverse()

    # calculate the total travel time
    total_travel_time = 0

    current = start
    for station in path[1:]:
        total_travel_time += current.connections[station]
        current = station

    print(f'Route: {' - '.join([station.name for station in path])}')
    print(f'Total Travel Time: {total_travel_time} minutes')

bfs(j7, heathrow)


# Depth-First Search (DFS)
# Find a valid path (not necessarily optimal). Discuss how the path found depends on the order in which the neighours are explored
# - return the sequence of nodes in the path
# - return the total cost/weight of the path
def dfs(start, end, visited=None, previous=None):
    if visited is None:
        visited = set()
    if previous is None:
        previous = {}

    visited.add(start)

    if start == end:
        return previous
    
    for neighbour in start.connections:
        if neighbour not in visited:
            previous[neighbour] = start
            result = dfs(neighbour, end, visited, previous)

            if result is not None:
                return result
    return None

def dfs_route(start, end):
    previous = dfs(start, end)

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous.get(current)

    path.reverse()

    total_travel_time = 0
    current = start

    for station in path[1:]:
        total_travel_time += current.connections[station]
        current = station
    
    print(f'Route: {' - '.join([station.name for station in path])}')
    print(f'Total Travel Time: {total_travel_time} minutes')


dfs_route(j7, heathrow)


# Dijkstra's Algorithm
# Find the path with the minimum total weight (shortest distance or fastest time depending on my weighing system, so by fastest time)
# - return the sequence of nodes in the path
# - return the total cost/weight of the path
def dijkstra(start):
    # we create a dictionary to store the cheapest times from the starting station to each station
    shortest_times = {start: 0}
    previous = {}
    visited = set()
    pq = [(0, start)]

    while pq:
        current_time, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
        
        for neighbour, time in current.connections.items():
            if neighbour in visited:
                continue

            new_time = current_time + time

            if neighbour not in shortest_times or new_time < shortest_times[neighbour]:
                shortest_times[neighbour] = new_time
                previous[neighbour] = current
                heapq.heappush(pq, (new_time, neighbour))
    return shortest_times, previous

# function to print the shortest route
def shortest_route(start, end):
    shortest_times, previous = dijkstra(start)

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous.get(current)

    path.reverse()

    total_time = shortest_times.get(end)

    print(f'Route: {' - '.join([station.name for station in path])}')
    print(f'Total Travel Time: {total_time} minutes')

shortest_route(j7, heathrow)








    

