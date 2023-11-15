import time

filename = "toy_example.txt"

f = open(filename, 'r')

start_time = time.time()

baseline_cost, action_cost = [int(i) for i in f.readline().split()]

cloud_CPU_cost, cloud_MEM_cost = [int(i) for i in f.readline().split()]

B, cpu, mem, acc, cost_per_set = [int(i) for i in f.readline().split()]

N, T, X = [int(i) for i in f.readline().split()]
    


for i in range(N):
    CU =  [int(i) for i in f.readline().split()] # 3 elem cpu, mem, acc
    DU =  [int(i) for i in f.readline().split()] # 3 elem
    PHY = [int(i) for i in f.readline().split()] # 3 elem
    IO = [int(i) for i in f.readline().split()]  # 4 elem LA, LB, LC, LD
    trafficUnits = [int(i) for i in f.readline().split()]   # T elem



"""
def rec(BBU : bool, current_state, foo: string:
    
    current_state:
    Net = 0 CU = 1, DU = 2, PHY = 3, UE = 4

    if (current_state == 4):
        return 0
    
    if (not BBU):
        # If in cloud function call to cloud in next state
        if (current_state == 0):
            pass
        elif (current_state == 1):
            pass
        elif (current_state == 2):
            pass
        else:
            pass
    
        rec(not BBU, current_state+1, foo.append("b"))
    else:

        if (current_state == 0):
            pass
        elif (current_state == 1):
            pass
        elif (current_state == 2):
            pass
        else:
            pass

        # If in cloud or BBU function call to BBU in next state
        rec(BBU, current_state+1, foo.append("c"))
    return 0"""
        

###########################################################################################################################################

#Make into class?


for i in range(N):
    CU =  [int(i) for i in f.readline().split()] # 3 elem cpu, mem, acc
    DU =  [int(i) for i in f.readline().split()] # 3 elem
    PHY = [int(i) for i in f.readline().split()] # 3 elem
    IO = [int(i) for i in f.readline().split()]  # 4 elem LA, LB, LC, LD
    trafficUnits = [int(i) for i in f.readline().split()]   # T elem







def Calculate_BBU_sets():       #Returns the required amount of BBU sets
    return 0



#Cost Idea: we can add all and multiply with traffic at the end
def BBU_cost():
    return cost_per_set*Calculate_BBU_sets()




##########################################################################################################################################




class StateMachine():             #CLOUD -> CU -> DU -> PHY -> BBU    
    def __init__(self):
        self.states = {"Internet": 0, "Cloud_cu": 2, "BBU_cu": 2, "Cloud_du": 2,           #If cost is a list then it depends on if coming from cloud or BBU
           "BBU_du":[2,3], "Cloud_phy": 2, "BBU_phy": [2,3], "UE": [2,3]}                   #Shit way of storing costs.
        

        self.transitions = {"Internet": ["Cloud_cu", "BBU_cu"],          #Key is node and value is all nodes it can transition into
                    "Cloud_cu": ["Cloud_du", "BBU_du"],
                    "BBU_cu": ["BBU_du"],
                    "Cloud_du": ["Cloud_phy", "BBU_phy"],
                    "BBU_du": ["BBU_phy"], 
                    "Cloud_phy": ["UE"],
                    "BBU_phy" : ["UE"] 
        }
        self.current_state = "Internet"             #Sets starting state at internet

    def transition(self, next_state):                       #Transitions into new state
            if next_state in self.transitions[self.current_state]:
                self.current_state = next_state

    def get_cost(self, state, source):
        if source == "cloud":
            return self.cost_from_cloud[state]
        elif source == "BBU":
            return self.cost_from_BBU[state]




for i in range(T):      #Iterating over traffic
    pass



end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)






f.close()


