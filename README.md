# Map-Reduce problems
 Python applications using map and reduce (in this case, using itertools)
 common_friendship_dictionary.py calculates the dictionary that returns the list of common friends between each pair of nodes in the network using a map-reduce framework.
 The controlling function `driver` takes a list of tuples. Each tuple represents a person in the friendship network tpl[0], and the list of friends they have tpl[1].
 It returns a dictionary where the keys are frozensets representing every pair of nodes, and the value of the key {x,y} is the set of friends that x and y have in common.
 
