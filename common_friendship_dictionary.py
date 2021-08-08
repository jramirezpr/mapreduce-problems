from functools import reduce

def concat(list_of_lists):
  """concatenates list of lists into one single list"""
  return reduce(lambda a,b : a+b,list_of_lists,[])

def friend_pairs_and_other_friends(friend_tuple):
    """retursn a list of tuples indexed by all friendship edges,
       where the first element
       of a tuple is a friendship edge of friend_tuple[0], and the second
       element is the friendship list of x (this is the constant value y)""" 
    x=friend_tuple[0]
    y=friend_tuple[1]
    def auxfun(w):
        return (frozenset({x,w}),y)
    return list(map(auxfun,y))#returns [({x,y[0]},y),...]


def intersectiondict(dict_pairs,pairlisttuple):
    """Calculates the intersection between the list of friends pairlisttuple[1]
       and the value for the current list of friends, 
       stored in dict_pairs[pairlisttuple[0]]if it exists.
       If that key doesnt exist,
       then it initializes the value to  pairlisttuple[1]"""
    keygroup = pairlisttuple[0]
    listfriends = pairlisttuple[1]
    if keygroup in dict_pairs:
        dict_pairs[keygroup]= dict_pairs[keygroup].intersection(set(listfriends.copy()))
    else:
        dict_pairs[keygroup] = set(listfriends)
    return dict_pairs


def driver(friend_tuple_list):
  """main program"""
  list_of_edgelists = list(map(friend_pairs_and_other_friends,friend_tuple_list))
  list_of_friend_edges = concat(list_of_edgelists)
  #=[({friend_tuple_list[0][0],friend_tuple_list_[0][1][0]},friend_tuple_list_[0][1])...
  accum = dict()
  dict_common_friends = reduce(intersectiondict,list_of_friend_edges, accum)
  return dict_common_friends
#example usage
friend_tuple_list=[("A",["B","C","D"]),
                   ("B",["A","C","D","E"]),
                   ("C",["A","B","D","E"]),
                   ("D",["A","B","C","E"]),
                   ("E",["B","C","D"])]
  

print(driver(friend_tuple_list))
