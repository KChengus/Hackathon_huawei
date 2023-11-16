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
    Net = 0, CU = 1, DU = 2, PHY = 3, UE = 4
    """
    if (current_state == 4):
        return 0
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
    
    path1 = -1
    if (not BBU):
        # If in Cloud, do function call to Cloud and BBU in next state
        return min(rec(not BBU, current_state+1, foo.append("b")), rec(BBU, current_state+1, foo.append("c"))) + value
        
    # If in cloud or BBU function call to BBU in next state    
    return min(rec(BBU, current_state+1, foo.append("c")), path1)
        

states = {"In_Cloud": True, "Internet": 2, "Cloud_cu": 2, "BBU_cu": [2,3], "Cloud_du": 2,           #If cost is a list then it depends on if coming from cloud or BBU
           "BBU_du":[2,3], "Cloud_phy": 2, "BBU_phy": [2,3], "UE": [2,3]}    


transitions = {"Internet": ["Cloud_cu", "BBU_cu"],
               "Cloud_cu": ["Cloud_du", "BBU_du"],
               "BBU_cu": ["BBU_du"],
               "Cloud_du": ["Cloud_phy", "BBU_phy"],
               "BBU_du": ["BBU_phy"], 
               "Cloud_phy": ["UE"],
               "BBU_phy" : ["UE"] 
}



class states():             #CLOUD -> CU -> DU -> PHY -> BBU
    def __init__(self, BBU : bool, current_state):
        self.in_BBU = BBU
        self.state = current_state 

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)






f.close()


