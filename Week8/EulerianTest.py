'''
Created on Dec 12, 2019

@author: Marcelious Willis

SWDV-610 Week 8 Project

Algorithm to test input graphs for Eulerian characteristics
'''
from collections import defaultdict

class EulerianGraph:
    '''
    Class to create an undirected graph and analyze the graph.
    '''
    
    def __init__(self,num_of_vertices):
        ''' 
        Eulerian graph constructor to initialize the graph.
        '''
        self._graph = defaultdict(list)
        self._num_of_vertices = num_of_vertices
    
       
    def insert_edge(self, u, v):
        '''
        Method to insert an edge between vertices u and v for an undirected graph.
        '''
        self._graph[u].append(v)
        self._graph[v].append(u)
        
    def get_edges(self):
        '''
        Method to get the list of edges in the graph.
        '''
        edges = []
        for vertex in self._graph:
            for neighbor in self._graph[vertex]:
                if [neighbor, vertex] not in edges:
                    edges.append([vertex, neighbor])
        return edges
        
    def dfs(self, v):
        '''
        Depth First Search helper method to mark vertex v as visited
        utilizing recursion.
        '''
        self.visited[v] = True
        
        # Use recursion to mark all vertices adjacent to vertex v as visited.     
        for i in self._graph[v]:
            if self.visited[i] == False:
                self.dfs(i)
                
    @property
    def is_connected(self):
        '''
        Property to check new non-zero degree vertices are connected. 
        '''  
        self.visited = [False]*(self._num_of_vertices)
        
        # Find a vertex with non-zero degree (at least 1 edge connecting the vertex)
        for i in range(self._num_of_vertices):
            if len(self._graph[i]) > 1:
                break
        
        # Return that the vertices are connected   
        if i == self._num_of_vertices - 1:
            return True
        
        # Use depth first search traversal to find the next non-zero degree vertex.
        self.dfs(i)
        
        # Check all vertices to verify everyone is visited
        for i in range(self._num_of_vertices):
            if self.visited[i] == False and len(self._graph[i]) > 0:
                return False
        return True
    
    @property    
    def is_eulerian(self):
        '''
        Method to determine if a graph is Eulerian or not.
        '''
        if self.is_connected == False: 
            return 0
        else: #Count vertices with odd degree 
            odd = 0
            for i in range(self._num_of_vertices): 
                if len(self._graph[i]) % 2 !=0: 
                    odd +=1
            if odd == 0: # If the odd count is 0, the graph is Eulerian
                return 2
            elif odd == 2: # If the odd count is 2, the graph is semi-Eulerian  
                return 1
            elif odd > 2: # If the odd count is more than 2, the graph is not Eulerian
                return 0
            
    def eulerian_test(self, graph_name): 
        '''
        Method to determine if a graph is Eulerian or not. Print the results to the user.
        '''       
        res = self.is_eulerian
        if res == 0:
            print(self.get_edges())
            print("{} is not Eulerian.".format(graph_name))
        elif res == 1:
            print(self.get_edges())
            print("{} has an Eulerian Path.".format(graph_name))
        else:
            print(self.get_edges())
            print("{} has an Eulerian Cycle.".format(graph_name))
                
def main():
    '''
    Test Code
    '''    
    # Test Case 1
    # 0-------1
    # |\     /|
    # | \   / |
    # |  \ /  |
    # |   4   |
    # |       |
    # 3-------2
    
    graph1 = EulerianGraph(5)
    graph1.insert_edge(0, 1)
    graph1.insert_edge(1, 2)
    graph1.insert_edge(2, 3)
    graph1.insert_edge(3, 0)
    graph1.insert_edge(0, 4)
    graph1.insert_edge(4, 1)
    graph1.eulerian_test('Graph for Test Case 1')
    print("")
    
    # Test Case 2
    # 0-------1
    # |\     /|
    # | \   / |
    # |  \ /  |
    # |   \   |
    # |  / \  |
    # | /   \ |
    # |/     \|
    # 3-------2
    graph1 = EulerianGraph(4)
    graph1.insert_edge(0, 1)
    graph1.insert_edge(1, 2)
    graph1.insert_edge(2, 3)
    graph1.insert_edge(3, 0)
    graph1.insert_edge(0, 2)
    graph1.insert_edge(3, 1)
    graph1.eulerian_test('Graph for Test Case 2')
    print("")
    
    # Test Case 3
    # 0-------1
    # |       |
    # |       |
    # 3-------2
    graph1 = EulerianGraph(4)
    graph1.insert_edge(0, 1)
    graph1.insert_edge(1, 2)
    graph1.insert_edge(2, 3)
    graph1.insert_edge(3, 0)
    graph1.eulerian_test('Graph for Test Case 3')
    print("")
        
if __name__ == '__main__':
    '''
    Run Test Code
    '''
    main()