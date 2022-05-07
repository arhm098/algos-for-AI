#muhammad arham
#231453689

#using prority Queue

import heapq

class PriorityQueue:

    """
    The class provides an implementation of priority queses via min heaps. This class has basic functions of a priority queue.
    """

    def __init__(self):
        self.__queue = []
        self.__index = 0

    def insert(self, item, priority):
        """
        The function takes in the item and its priority, wraps it up in a tuple and 
        inserts it in the heap.

        :params item: item to be inserted into the queue
        :params priority: the priority of the item to be inserted

        :return: None
        """

        heapq.heappush(self.__queue, (priority, self.__index, item))
        self.__index += 1

    def remove(self):
        """
        The functions removes the lowest priority item from the priority queue (via heaps)
        and returns the item along with the cost of it.

        :return : the item with the lowest priority
        """

        temp = heapq.heappop(self.__queue)
        
        cost = temp[0]
        item = temp[-1]

        return cost, item

    def is_empty(self):
        """
        Checks whether the queue is empty or not.

        :returns: (Boolean)
        """
        return len(self.__queue) == 0
"""
Lab Task: 

For this lab you will be implementing A* (A Star Search) on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable 
with the functions

MAIN TASKS:

    1- Modify graph.py to have the ability to store heuristics
    2- Create a funciton 'get_h' in graph.py to get heuristic for a node : input will be a Node and output will be heuristic 
    3- Create the graph in graph.py to and check all the functions
    4- Replicate the graph in 'lab4.py'
    5- Implement A* function 

Your function should print the shortest path along with the cost of that path. 
A sample output is provided in the assests directory.
"""


class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {}  # dictionary of edges NODE: NEIGHBOURS
        self.weights = {}  # dictionary of NODES and their COSTS

        # add a dictionary to store heuristics for nodes
        self.heuristics = {}

    def neighbours(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.

        :params node: (string) a node in the graph

        :return: (list) neighbouring nodes
        """

        return self.edges[node]

    def get_cost(self, from_node, to_node):
        """
        Gets the cost of a connection between adjacent nodes.

        :params from_node: (string) starting node
        :params to_node: (string) ending node

        :return: (int) 
        """

        return self.weights[(from_node + to_node)]

    def get_h(self, node):
        """
        This function will give our the heuristic from the node to goal.

        :params node: (String) current node / any node

        :return: (int) heuristic to the goal
        """

        # write your code below
        return self.heuristics[node]

def a_star_search(graph, start_node, goal_node):
        """
        The function should take in the graph defined along with the
        start and goal nodes and print out the shorted path according 
        to the A* Search Algorithm.

        :params graph: (Graph) defined graph
        :params start_node: (String) starting node from graph
        :params goal_node: (String) goal node from the graph

        :return : None
        """

        # write your code below

        pq = PriorityQueue()

        visited = {}

        pq.insert(start_node, graph.get_h(start_node))

        lowest_cost = 10**8
        shortest_path = ""

        while not pq.is_empty():
            cost, item = pq.remove()
            path = item
            item = item[-1]
            cost = cost - graph.get_h(item)

            if item == goal_node:
                if lowest_cost > cost:
                    lowest_cost = cost
                    shortest_path = path

            if item not in visited:
                for neighbour in graph.neighbours(item):
                    pq.insert(path + neighbour,
                              (cost + graph.get_cost(item, neighbour)+graph.get_h(neighbour)))

                visited[item] = 1

        print(f"Shortest Path: {list(shortest_path)}\nCost: {lowest_cost}")

if __name__ == "__main__":
    # testing out the graph class
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {'A': set(['B', 'C']),
                   'B': set(['C', 'E']),
                   'C': set(['G']),
                   'D': set(['B', 'E']),
                   'E': set(['G']),
                   'S': set(['A', 'D']),
                   'G': set([])
                   }

    # setting up connection costs
    graph.weights = {'AB': 5, 'AC': 10,
                     'BC': 2, 'BE': 1, 'CG': 4,
                     'DB': 1, 'DE': 4,
                     'EG': 3,
                     'SA': 3, 'SD': 2}

    # setting up heuristics
    graph.heuristics = {'A': 9,
                        'B': 4,
                        'C': 2,
                        'D': 5,
                        'E': 3,
                        'S': 7,
                        'G': 0}

    # test functions from the class
    #print(graph.get_h('A'))
    a_star_search(graph, 'S', 'G')# To Test get_h
