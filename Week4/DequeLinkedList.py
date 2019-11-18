# SWDV-610 Week 4 Assignment: Linked Lists with Deques
# Author: Marcelious Willis

class Node:
    """Node class to maintain nodes of a linked list"""
    def __init__(self,element,nextNode,prevNode):
        self.element = element
        self.prev = prevNode
        self.next = nextNode
        
class Deque:
    """Deque class to create/modify a linked list. """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # Method to check if the linked link exists
    def is_empty(self):
        if self.size < 1:
            return True
        else:
            return False
    
    # Method to add a element to the head of the linked list
    def add_head(self,element):
        headNode = Node(element,self.head,self.tail)  # Create Node instance for the new node        
        if self.is_empty():
            self.head = headNode
            self.tail = headNode
        else:
            self.head.prev = headNode
        self.head = headNode
        self.size += 1          # Increase the size of the linked list.
    
    # Method to add a element to the tail of the linked list
    def add_tail(self,element):
        tailNode = Node(element,self.head,self.tail)  # Create Node instance for the new node        
        if self.is_empty():
            self.head = tailNode
            self.tail = tailNode
        else:
            self.tail.prev = tailNode
        self.tail = tailNode
        self.size += 1           # Increase the size of the linked list.
        
    # Method to remove the element at the head of the linked list    
    def remove_head(self):
        self.head = self.head.next # Set the head to the next node
        self.size -= 1             # Decrease the size of the linked list
        
    def remove_tail(self):
        self.tail = self.tail.prev
        self.size -= 1
        
    # Method to display the element at the head of the linked list
    def top(self):
        if self.is_empty():
            return("empty!")
        return self.head.element
    
    # Method to display the element at the tail of the linked list
    def bottom(self):
        if self.is_empty():
            return("empty!")
        return self.tail.element
        
    # Method to get the size of the linked list
    def get_size(self):
        return(self.size)
    
    # Method to display the linked list
    def display_list(self):
        displayNode = self.head
        finalNode = self.tail
        tempSize = self.get_size()
        while tempSize > 0:
            print(displayNode.element," -> ",end=" ")
            tempSize -= 1
            if tempSize > 1:
                displayNode = displayNode.next
            else:
                displayNode = finalNode
        print('\n')

# Test code:
myDeque = Deque()        #Set the Deque instance

#Add values to Deque and check values
myDeque.add_head(111)        #add 111 to the Deque
myDeque.add_head(222)        #add 222 to the Deque
myDeque.add_head(333)        #add 333 to the Deque
myDeque.add_head(444)        #add 444 to the Deque
myDeque.add_head(777)        #add 777 to the Deque
myDeque.add_tail(1111)       #add 1111 to the Deque
myDeque.display_list()   #show the linked list Deque
print(myDeque.get_size())#should be 6
print("Head is: ",myDeque.top())        #should be 777
print("Tail is: ",myDeque.bottom())     #should be 1111

#Remove values and check values
myDeque.remove_head()
myDeque.remove_tail()
print(myDeque.get_size())#should be 4
print("Head is: ",myDeque.top())     #should be 444
print("Tail is: ",myDeque.bottom())  #should be 111
myDeque.display_list()   #show the linked list stack
