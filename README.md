# Map-Reduce problems

 Python applications using map and reduce (in this case, using itertools)
 
 common_friendship_dictionary.py calculates the dictionary that returns the list of common friends between each pair of nodes in the network using a map-reduce framework.
 The controlling function `driver` takes a list of tuples. Each tuple represents a person in the friendship network tpl[0], and the list of friends they have tpl[1].
 It returns a dictionary where the keys are frozensets representing every pair of nodes, and the value of the key {x,y} is the set of friends that x and y have in common.
 
 E.g.
 ```
  driver([("A",["B","C","D"]),
         ("B",["A","C","D","E"]),
         ("C",["A","B","D","E"]),
         ("D",["A","B","C","E"]),
         ("E",["B","C","D"])])
 
 
 
 ```

returns
```
{frozenset({'A', 'B'}): {'C', 'D'},
frozenset({'C', 'A'}): {'D', 'B'},
frozenset({'D', 'A'}): {'C', 'B'},
frozenset({'C', 'B'}): {'D', 'A', 'E'},
frozenset({'D', 'B'}): {'C', 'A', 'E'},
frozenset({'E', 'B'}): {'C', 'D'}, 
frozenset({'D', 'C'}): {'A', 'E', 'B'},
frozenset({'E', 'C'}): {'D', 'B'}, 
frozenset({'E', 'D'}): {'C', 'B'}}
```
 
