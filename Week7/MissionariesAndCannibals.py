'''
Created on Dec 7, 2019

@author: Marcelious Willis
'''
from collections import deque

class CurrentState:
    '''
    Current State class for the Missionaries and Cannibals problem
    
    Three missionaries and three cannibals come to a river and find a boat that 
    holds two people. Everyone must get across the river to continue on the 
    journey. However, if the cannibals ever outnumber the missionaries on either
    bank, the missionaries will be eaten. Find a series of crossings that will 
    get everyone safely to the other side of the river.
    '''
    
    def __init__(self, missionaries, cannibals, boat=1):
        ''' 
        Constructor for the current state class
        '''
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        
    def __repr__(self):
        '''
        Representation method for the current state of the unsafe bank.
        '''
        return "Current state of unsafe bank: " + str(self.missionaries) + " missionaries, " + str(self.cannibals) + " cannibals, and " + str(self.boat) + " boats."
    
    @property
    def is_valid(self):
        '''
        Check for valid inputs based on common sense and the problem statement
        '''
        if self.missionaries < 0 or self.cannibals < 0 or self.boat < 0 or self.missionaries > 3 or self.cannibals > 3: # Negative values or values larger than actual, not a valid state
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0: # More cannibals than missionaries on unsafe bank, not a valid state.
            return False
        if self.missionaries > self.cannibals and self.missionaries < 3: # More cannibals than missionaries on safe bank, not a valid state.
            return False
        else: # Otherwise, this is a valid state.
            return True
    
    @property    
    def is_solution(self):
        '''
        Check if the solution is found.
        '''
        if self.missionaries == 0 and self.cannibals == 0: # If no more travelers are left on the unsafe bank, solution is found.
            return True
        else: # solution was not found
            return False
    
    @property    
    def travel(self):
        '''
        Method to determine how to move the travelers using the boat.
        '''
        if self.boat == 1: # Check if the boat is on the unsafe bank
            direction = -1
            direction_str = 'from the unsafe bank to the safe bank'
        else: # The boat is on the safe bank
            direction = 1
            direction_str = 'from the safe bank to the unsafe bank'
        for m in range(3): # Loop through travelers and update the current state of the unsafe bank
            for c in range(3):
                new_state = CurrentState(self.missionaries+direction*m, self.cannibals+direction*c, self.boat+direction*1)
                if m + c >= 1 and m + c <= 2 and new_state.is_valid: # The attempted travel action is valid so update the travel action and new state.
                    action = "Moving {} missionaries and {} cannibals {}. {}".format(m,c,direction_str,new_state)
                    yield action, new_state
                    
class Node:  
    '''
    Node class to maintain nodes within the graph.
    '''
    def __init__(self, parent_node, state, action, graph_level):
        self.parent_node = parent_node
        self.state = state
        self.action = action
        self.graph_level = graph_level
    
    @property
    def expand(self):
        # For the given action and next state of the travelers, get the next node of the graph.
        for (action, next_state) in self.state.travel:
            next_node = Node(parent_node=self, state=next_state, action=action, graph_level=self.graph_level + 1)
            yield next_node
    
    @property
    def get_solution(self):
        # While the parent node of the current node is not the root node, get the solution.
        solution = []
        node = self
        while node.parent_node != None:
            solution.append(node.action)
            node = node.parent_node
        solution.reverse()
        return solution
    
def bfs(initial_state):
    # Breadth First Search method 
    initial_node = Node(parent_node=None, state=initial_state, action=None, graph_level=0)
    fifo = deque([initial_node]) # Create a double-ended queue for moving travelers on the boat
    num_expansions = 0
    max_graph_level = -1
    while True:
        if not fifo: # Check if the deque exists
            print("{} expansions".format(num_expansions))
            return None
        node = fifo.popleft() # Pop the left value out of the deque
        if node.graph_level > max_graph_level: # Update the level of the graph
            max_graph_level = node.graph_level
            print("[graph_level = {}]".format(max_graph_level))
        if node.state.is_solution: # Determine if the solution was found
            print("{} expansions".format(num_expansions))
            solution = node.get_solution
            return solution
        num_expansions += 1
        fifo.extend(node.expand)
    
    
# Driver Code
init_state = CurrentState(3,3)
solution = bfs(init_state)
if solution == None:
    print("No Solution. Stopping")
else:
    for i in solution:
        print(i)
    print("Solution found. Stopping")
            