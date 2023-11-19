import time
import math
filename = "One test case.txt"

f = open(filename, 'r')



baseline_cost, action_cost = [int(i) for i in f.readline().split()]
cloud_CPU_cost, cloud_MEM_cost = [int(i) for i in f.readline().split()]
BBU_limit, cpu_per_set, mem_per_set, acc_per_set, cost_per_set = [int(i) for i in f.readline().split()]
N, T, X = [int(i) for i in f.readline().split()]




#################################################################################################       

def calBBUCost(cpu, mem, acc, traffic_unit):
    cpu_allo = cpu * traffic_unit
    mem_allo = mem * traffic_unit
    acc_allo = acc * traffic_unit
    BBUsetsRequired = max(math.ceil(cpu_allo/cpu_per_set), math.ceil(mem_allo/mem_per_set), math.ceil(acc_allo/acc_per_set))
    if (BBUsetsRequired <= BBU_limit):
        return BBUsetsRequired * cost_per_set
    # if BBUsetsRequired exceeds limit then return invalid cost
    #return -1
    return -1
# Example usage for CU: calBBUCost(CU[0], CU[1], CU[2], cpu_per_set, mem_per_set, acc_per_set, B, cost_per_set, traffic


def cloud_costs(node: list, trafficUnits: int):     
    total_cpu_cost = cloud_CPU_cost*(node[0]+ node[2]*X)
    total_mem_cost = cloud_MEM_cost * node[1]
    return trafficUnits*(total_cpu_cost+total_mem_cost)

################################################ Attempt to implement Djikstras


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
        if (int(current)%2):
            # Cloud
            path.insert(0, 'C')
        else:
            path.insert(0, 'B')
        current = previous_nodes[current]
    path.pop()
    path.pop(0)
    return distances[goal], path
##############################################################################################################################
def main():
    previous = ["B", "B", "B"]
    for _ in range(N):
        CU =  [int(i) for i in f.readline().split()] # 3 elem cpu, mem, acc
        DU =  [int(i) for i in f.readline().split()] # 3 elem
        PHY = [int(i) for i in f.readline().split()] # 3 elem
        IO = [int(i) for i in f.readline().split()]  # 4 elem LA, LB, LC, LD
        trafficUnits = [int(i) for i in f.readline().split()]   # T elem
        for traffic in trafficUnits:
            cuBBUCost = calBBUCost(CU[0], CU[1], CU[2], traffic)
            duBBUCost = calBBUCost(DU[0], DU[1], DU[2], traffic)
            phyBBUCost = calBBUCost(PHY[0], PHY[1], PHY[2], traffic)
            BBUCost = (0 if cuBBUCost == -1 else cuBBUCost) + (0 if duBBUCost == -1 else duBBUCost) + (0 if phyBBUCost == -1 else phyBBUCost)

            cuCcost = cloud_costs(CU, traffic)+ action_cost * (not previous[0] == "B")
            duCcost = cloud_costs(DU, traffic)+ action_cost * (not previous[1] == "B")
            phyCcost = cloud_costs(PHY, traffic)+ action_cost * (not previous[2] == "B")
            
            graph = {
                "0": {"1": cuCcost, "2": (float("inf") if cuBBUCost == -1 else IO[0] + cuBBUCost)},
                "1": {"3": duCcost, "4": (float("inf") if duBBUCost == -1 else IO[1] + duBBUCost)},
                "2": {"4": duBBUCost},
                "3": {"5": phyCcost, "6": (float("inf") if phyBBUCost == -1 else IO[2] + phyBBUCost)},
                "4": {"6": phyBBUCost},
                "5": {"10": IO[3]},
                "6": {"10": 0},
                "10": {}
            }
            start_node = "0"
            end_node = "10"
            shortest_path_distance, shortest_path = a_star(graph, start_node, end_node)
            previous = shortest_path
            total_cloud_cost = (shortest_path[0]=="C") * cuCcost+ (shortest_path[1]=="C") * duCcost + (shortest_path[2]=="C") * phyCcost
            print(f"Shortest path from {start_node} to {end_node}: {shortest_path_distance}")
            print(f"Shortest path: {''.join(shortest_path)}")
            print(f"BBU costs: {BBUCost}")
            print(f"Cloud cost: {total_cloud_cost}:")

# Adding the cost of going from cloud to BBU or whatever
    


##################################################################################################
start_time = time.time()
main()
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)






f.close()
