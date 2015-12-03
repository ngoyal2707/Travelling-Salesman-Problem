This is the README file for TSP solver program.

The procedure to run the program is as following:

1) On console type following command:
	python TSPSolver.python

The command line argument to be passed are as following:

-alg BnB|Approx|Heur|LS1|LS2
-inst burma14.tsp
-time 600
-seed 10


Where the algorithm argument are as following:
BnB: 	Branch and Bound
Approx: MST 2 Approximation
Heur:	Furthest insertion Greedy Heuristic
LS1:	Simulated Annealing
LS2:	Hill Climbing

The structure of the code is as following:
Approximation.py: 		Code for MST 2 approximation
furthest_insertion.py:	Code for furthest insertion greedy heuristic
BranchAndBound.py:		Code for branch and bound solution
two_opt.py:				Code for two opt / three opt hill climbing 
SA.py:					Code for simulated annealing
readData.py:			Code for reading the graph file and creating graph
prim.py:				Code for return mst weight and mst path
pqdict:					Library for priority queue with faster decrease key opertaion
TSPSolver:				Starting point of the code


Note: The true optimal cost is not passed to the local search approaches and
they keep on trying to find the optimal cost until the cutoff even if they find 
the optimal solution for smaller graph. The reason is too mimic the real world 
scenario when, the algorithm doesn't know true optimal cost of the tour.