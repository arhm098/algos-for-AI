#muhammad arham
#roll 2314 53689

from xml.etree.ElementTree import TreeBuilder


class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {}  # dictionary of edges NODE: NEIGHBOURS

        # add a dictionary to store heuristics for nodes
        self.heuristics = {}

    def get_n(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.

        :params node: (string) a node in the graph

        :return: (list) neighbouring nodes
        """

        return self.edges[node]


    def get_h(self, node):
        """
        This function will give our the heuristic from the node to goal.

        :params node: (String) current node / any node

        :return: (int) heuristic to the goal
        """

        # write your code below
        return self.heuristics[node]

def hill_climb_search(graph,start,end):
    cur = start
    goal_state = end
    edges = graph.get_n(cur)
    print(cur)
    while True:
        edges = graph.get_n(cur)
        if edges == []:
            return -1
        if goal_state in edges:
            print(goal_state)
            return
        maximum = graph.get_h(cur)
        best = ''
        for i in edges:
            if maximum < graph.get_h(i):
                maximum = graph.get_h(i)
                best = i
        cur = best
        print(best)
        



def main():
    # testing out the graph class
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {"A": ["B", "C", "D"],
                   "B": ["E", "F"],
                   "C": ["G", "H"],
                   "D": ["I", "J"],
                   "H": ["K"],
                   }

    # setting up heuristics
    graph.heuristics = {"A": 3,
                        "B": 4,
                        "C": 6,
                        "D": 5,
                        "E": 3,
                        "F": 2,
                        "G": 7, 
                        "H": 8,
                        "I": 6,
                        "J": 7,
                        "K": 9,
                        }

    hill_climb_search(graph,"A","K")

main()

