# Hackathon_huawei
# Test



# Notes
Transition states som robot armen?
Greedy algorithm? Minimum spanning tree?

# Game plan
Directed MST with binary elements
Kruskals algorithm for search
Dont rebuild graphs just change cost

# Costs
# Baseline cost is the cost that you have to be under
# Action cost is moving from Cloud to BBU or vice versa
# BBU profile, B is how many board sets we have, rest is resources provided by board and cost of running BBU sets
# CU resource unit is how many things it needs of each 1 CU needs to function
# IO cost CU to DU example





# Breakdown av uppgiften
0 1 3 5 10 
0 2 4 6 10 
+-----------+      +-----------+      +-----------+      +-----------+
| Internet  | ---> | Cloud_cu  | ---> | Cloud_du  | ---> | Cloud_phy |
+-----------+      +-----------+      +-----------+      +-----------+
      |                   |                   |                  |
      v                   v                   v                  v
+-----------+      +-----------+      +-----------+      +-----------+
|  BBU_cu   | ---> |  BBU_du   | ---> |  BBU_phy  | ---> |    UE     |
+-----------+      +-----------+      +-----------+      +-----------+



# Action cost, Service allocation*Actioncost
# IO, Traversal cost for 1 then multiply with how much traffic can take optimal path. IOCost = IOCostLinkedUsed * Traffic

# Breakdown of cloud cost
# CPU required = (amout of acc * X + CPU required)
# 

# Plan av main:
# Sätta alla kostnader
# A*
# OPEX

# Sätt alla kostnader
# Sätt kostnader för cloud
# Sätt kostnader för BBU genom BBU sets funktion
