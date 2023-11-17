import time

filename = "toy_example.txt"

f = open(filename, 'r')

start_time = time.time()

baseline_cost, action_cost = [int(i) for i in f.readline().split()]

cloud_CPU_cost, cloud_MEM_cost = [int(i) for i in f.readline().split()]

B, cpu, mem, acc, cost_per_set = [int(i) for i in f.readline().split()]

N, T, X = [int(i) for i in f.readline().split()]
    
# print(baseline_cost, action_cost)
# print(B, cpu, mem, acc, cost_per_set)




for i in range(N):
    CU =  [int(i) for i in f.readline().split()] # 3 elem cpu, mem, acc
    DU =  [int(i) for i in f.readline().split()] # 3 elem
    PHY = [int(i) for i in f.readline().split()] # 3 elem
    IO = [int(i) for i in f.readline().split()]  # 4 elem LA, LB, LC, LD
    trafficUnits = [int(i) for i in f.readline().split()]   # T elem



###########################################################################################33
#Func ger errors
"""
def rec(BBU : bool, current_state, foo: str):       
    current_state:
    Net = 0, CU = 1, DU = 2, PHY = 3, UE = 4
    if (current_state == 4):
        return 0
    if(BBU):
        print(current_state, 'B')
    else:
        print(current_state, 'C')
    value = 0
    # If in cloud function call to cloud in next state
    if (current_state == 0):
        pass
    elif (current_state == 1):
        pass
    elif (current_state == 2):
        pass
    else:
        pass
    
    if (not BBU):
        # If in Cloud, do function call to Cloud and BBU in next state
        return min(rec(not BBU, current_state+1, foo+'C'), rec(BBU, current_state+1, foo+'C')) + value
        
    # If in cloud or BBU function call to BBU in next state    
    return rec(BBU, current_state+1, foo+'B') + value
"""




"""
states = {"Internet": [2,3], "Cloud_cu": [2,3], "BBU_cu": 2, "Cloud_du": [2,3],           #If cost is a list that tells you how much transition costs
           "BBU_du":2, "Cloud_phy": [2,3], "BBU_phy": 2, "UE": 0}    


transitions = {"Internet": ["BBU_cu","Cloud_cu"],           
               "Cloud_cu": ["BBU_du", "Cloud_du"],
               "BBU_cu": ["BBU_du"],
               "Cloud_du": ["BBU_phy","Cloud_phy"],
               "BBU_du": ["BBU_phy"], 
               "Cloud_phy": ["UE"],
               "BBU_phy" : ["UE"]                                               
}


def transition(current_state, to_BBU: bool):
    next_states = transitions.get(current_state)
    if current_state[0:3] == "BBU":                         #If current_state is BBU then it cannot go to cloud and has to go to BBU or UE
        return next_states[0], states.get(current_state)
    if to_BBU:                                              #If going to BBU not from BBU has to be coming from cloud
        return next_states[0], states.get(current_state)[1]     ####################################################IMPORTANT DONT FORGET TO ADD THE COST OF GOING FROM CLOUD TO BBU OR WHATEVER
    else:                                                   #Lastly from cloud to cloud
        return next_states[1], states.get(current_state)[1]
"""


graph = {
    "0": {"2": 2, "1": 3},
    "1": {"2": 2, "3": 3},
    "2": {"4": 2},
    "3": {"4": 2, "5": 30},
    "4": {"6": 2},
    "5": {"10": 0},
    "6": {"10": 0},
    "10": {}
}

def transition(start, to_BBU: bool):
    next_states = graph.get(start)
    if not int(start)%2:                         #If current_state is BBU then it cannot go to cloud and has to go to BBU or UE
        return graph.get(str(int(start)+2))
        
    if to_BBU:                                              #If going to BBU not from BBU has to be coming from cloud
        return graph.get(str(int(start)+1))     ####################################################IMPORTANT DONT FORGET TO ADD THE COST OF GOING FROM CLOUD TO BBU OR WHATEVER
    else:                                                   #Lastly from cloud to cloud
        return graph.get(str(int(start)+1))


################################################ Attempt to implement Djikstras
def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}
    visited = set()
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = min(priority_queue, key=lambda x: x[0])
        priority_queue.remove((current_distance, current_vertex))

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                priority_queue.append((distance, neighbor))

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return distances[end], path

# Adding the cost of going from cloud to BBU or whatever
for state in graph:
    for neighbor, weight in graph[state].items():
        to_BBU = int(state) % 2 == 1  # Checking if the current state is from the cloud
        graph[state][neighbor] += 1 if to_BBU else 0  # Adding cost if transitioning from the cloud to BBU

# Using Dijkstra's algorithm to find the shortest path from "0" to "10"
start_node = "0"
end_node = "10"
shortest_path_distance, shortest_path = dijkstra(graph, start_node, end_node)

# Print the shortest path from "0" to "10"
print(f"Shortest path from {start_node} to {end_node}: {shortest_path_distance}")
print(f"Shortest path: {' -> '.join(shortest_path)}")

#################################################################################################       A*
def heuristic(node, goal):
    # This is a simple heuristic function for illustrative purposes (Euclidean distance)
    return abs(int(node) - int(goal))

def a_star(graph, start, goal):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}
    visited = set()
    priority_queue = [(0 + heuristic(start, goal), 0, start)]

    while priority_queue:
        priority_queue.sort()  # Sort the queue based on priority
        current_priority, current_distance, current_vertex = priority_queue.pop(0)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        if current_vertex == goal:
            break

        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_vertex
                    priority_queue.append((distance + heuristic(neighbor, goal), distance, neighbor))

    # Reconstruct the path
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return distances[goal], path

# Adding the cost of going from cloud to BBU or whatever
for state in graph:
    for neighbor, weight in graph[state].items():
        to_BBU = int(state) % 2 == 1  # Checking if the current state is from the cloud
        graph[state][neighbor] += 1 if to_BBU else 0  # Adding cost if transitioning from the cloud to BBU

# Using A* algorithm to find the shortest path from "0" to "10"
start_node = "0"
end_node = "10"
shortest_path_distance, shortest_path = a_star(graph, start_node, end_node)

# Print the shortest path from "0" to "10"
print(f"Shortest path from {start_node} to {end_node}: {shortest_path_distance}")
print(f"Shortest path: {' -> '.join(shortest_path)}")


##################################################################################################




end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)






f.close()


