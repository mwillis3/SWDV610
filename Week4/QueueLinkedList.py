# SWDV-610 Week 4 Assignment: Linked Lists with Queues
# Author: Marcelious Willis

class Node:
    """Node class to maintain nodes of a linked list"""
    def __init__(self,element):
        self.element = element
        self.next = None
        
class Queue:
    """Queue class to create/modify a linked list. FIFO principle"""
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
    def enqueue(self,element):
        newNode = Node(element)  # Create Node instance for the new node
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
            self.size += 1           # Increase the size of the linked list.
            return
        self.tail.next = newNode # Set the new node's next link to the old node.
        self.tail = newNode      # Set the current tail to the new next link.
        self.size += 1           # Increase the size of the linked list.
        
    # Method to remove the element at the head of the linked list    
    def dequeue(self):
        if self.is_empty():
            return("Your Linked List is empty. Nothing to dequeue!")
        self.head = self.head.next # Set the head to the next node
        self.size -= 1             # Decrease the size of the linked list
        
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
        if self.is_empty():
            return("Your linked list is empty!")
        while displayNode != None:
            print(displayNode.element," <- ",end=" ")
            displayNode = displayNode.next
        print('\n')

# Test code:
myQueue = Queue()        #Set the Queue instance

#Test empty list
print(myQueue.dequeue())     #Queue is empty
print("Head is: ",myQueue.top())        #Queue is empty
print("Tail is: ",myQueue.bottom())     #Queue is empty
print(myQueue.get_size())#should be 0
print(myQueue.display_list())   #Queue is empty

#Add values to queue and check values
myQueue.enqueue(111)        #add 111 to the Queue
myQueue.enqueue(222)        #add 222 to the Queue
myQueue.enqueue(333)        #add 333 to the Queue
myQueue.enqueue(444)        #add 444 to the Queue
myQueue.enqueue(777)        #add 777 to the Queue
myQueue.enqueue(1111)       #add 1111 to the Queue
myQueue.display_list()   #show the linked list Queue
print(myQueue.get_size())#should be 6
print("Head is: ",myQueue.top())        #should be 111
print("Tail is: ",myQueue.bottom())     #should be 1111

#Remove values and check values
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.get_size())#should be 4
print("Head is: ",myQueue.top())     #should be 333
print("Tail is: ",myQueue.bottom())  #should be 1111
myQueue.display_list()   #show the linked list stack