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


def rec(BBU : bool, current_state, foo: str):
    """
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
        


states = {"Internet": [2,3], "Cloud_cu": [2,3], "BBU_cu": 2, "Cloud_du": [2,3],           #If cost is a tuple that tells you how much transition costs
           "BBU_du":2, "Cloud_phy": [2,3], "BBU_phy": 2, "UE": 0}    


#Make tuple
transitions = {"Internet": ["BBU_cu","Cloud_cu"],
               "Cloud_cu": ["BBU_du", "Cloud_du"],
               "BBU_cu": ["BBU_du"],
               "Cloud_du": ["BBU_phy","Cloud_phy"],
               "BBU_du": ["BBU_phy"], 
               "Cloud_phy": ["UE"],
               "BBU_phy" : ["UE"] 
}



class states():             #CLOUD -> CU -> DU -> PHY -> BBU
    def __init__(self, BBU : bool, current_state):
        self.in_BBU = BBU
        self.state = current_state 



def transition(current_state, to_BBU):
    next_states = transitions.get(current_state)
    if current_state[0:3] == "BBU":                         #If current_state is BBU then it cannot go to cloud and has to go to BBU or UE
        return next_states[0]
    if to_BBU:                                              #If going to BBU not from BBU has to be coming from cloud
        return next_states[0]
    else:                                                   #Lastly from cloud to cloud
        return next_states[1]


# Example usage: next_states = transition(current_state, False)






end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)






f.close()


