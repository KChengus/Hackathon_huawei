filename = ""

f = open(filename, 'r')

baseline_cost, action_cost = [int(i) for i in f.readline().split()]

cloud_CPU_cost, cloud_MEM_cost = [int(i) for i in f.readline().split()]

B, cpu, mem, acc, cost_per_set = [int(i) for i in f.readline().split()]

N, T, X = [int(i) for i in f.readline().split()]
    

for _ in range(N):
    CU =  [int(i) for i in f.readline().split()] # 3 elem cpu, mem, acc
    DU =  [int(i) for i in f.readline().split()] # 3 elem
    PHY = [int(i) for i in f.readline().split()] # 3 elem
    IO = [int(i) for i in f.readline().split()]  # 4 elem LA, LB, LC, LD
    traficUnits = [int(i) for i in f.readline().split()]   # T elem


def rec(BBU : bool, current_state, foo: string):
    """ 
    current_state:
    Net = 0, CU = 1, DU = 2, PHY = 3, UE = 4
    """
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
    return 0
        

class states():             #CLOUD -> CU -> DU -> PHY -> BBU
    def __init__(self, BBU : bool, current_state):
        self.in_BBU = BBU
        self.state = current_state 


f.close()