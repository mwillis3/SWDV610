# SWDV-610 Week 4 Assignment: Linked Lists with Stacks
# Author: Marcelious Willis

class Node:
    """Node class to maintain nodes of a linked list"""
    def __init__(self,element):
        self.element = element
        self.next = None  
        
class Stack:
    """Stack class to create/modify a linked list. LIFO principle"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    # Method to check if the linked link exists
    def is_empty(self):
        if self.size < 1:
            return True
        else:
            return False
    
    # Method to add a element to the head of the linked list
    def push(self,element):
        newNode = Node(element)  # Create Node instance for the new node
        newNode.next = self.head # Set the new node's next link to the old node.
        self.head = newNode      # Set the current head to the new next link.
        self.size += 1           # Increase the size of the linked list.
        
    # Method to remove the element at the head of the linked list    
    def pop(self):
        if self.is_empty():
            return("Your Linked List is empty. Nothing to pop!")
        self.head = self.head.next # Set the head to the next node
        self.size -= 1             # Decrease the size of the linked list
        
    # Method to display the element at the head of the linked list
    def top(self):
        if self.is_empty():
            return("Your Linked List is empty!")
        return self.head.element
        
    # Method to get the size of the linked list
    def get_size(self):
        return(self.size)
    
    # Method to display the linked list
    def display_list(self):
        displayNode = self.head
        if self.is_empty():
            return("Your linked list is empty!")
        while displayNode != None:
            print(displayNode.element," -> ",end=" ")
            displayNode = displayNode.next
        print('\n')

# Test code:

# Test empty Stack
myStack = Stack()        #Set the Stack instance
print(myStack.pop())     #stack is empty
print(myStack.top())     #stack is empty
print(myStack.get_size())#should be 0
print(myStack.display_list())   #stack is empty

# Add elements to the Stack
myStack.push(111)        #add 111 to the stack
myStack.push(222)        #add 222 to the stack
myStack.push(333)        #add 333 to the stack
myStack.push(444)        #add 444 to the stack
myStack.push(777)        #add 777 to the stack
myStack.push(1111)       #add 1111 to the stack
myStack.display_list()   #show the linked list stack
print(myStack.get_size())#should be 6
print(myStack.top())     #should be 1111

# Remove elements from the Stack
myStack.pop()
myStack.pop()
print(myStack.get_size())#should be 4
print(myStack.top())     #should be 444
myStack.display_list()   #show the linked list stack