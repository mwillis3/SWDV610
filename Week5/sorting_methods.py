def bubble_sort(alist):
    """Method to sort a list using the bubble approach."""
    for passnum in range(len(alist)-1,0,-1): # Loop through the list starting at the location ahead of the last value.
        for i in range(passnum): # Loop through the leftover values in the list
            if alist[i]>alist[i+1]: # Check if the current value is greater than the value on the right 
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist
                    
def selection_sort(alist):
    """Method to sort a list using the selection approach."""
    for fillslot in range(len(alist)-1,0,-1): # Loop through the list starting at the location ahead of the last value.
        positionOfMax=0 # Set the default location of the max value to 0.
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]: # Check if the current value is greater than the value of the default max value
                positionOfMax = location # If so, update the location of the max value
        temp = alist[fillslot] # Store the current value in a temporary value
        alist[fillslot] = alist[positionOfMax] # Update the current value with the max value
        alist[positionOfMax] = temp # Update the max value with the temporary value
    return alist
        
def insertion_sort(alist):
    """Method to sort a list using the insertion approach."""
    for index in range(1,len(alist)): # Loop through the list starting at the location ahead of the last value.
        currentvalue = alist[index] # Store the current value
        position = index # Store the location of the current value
        while position>0 and alist[position-1]>currentvalue: # Loop through until the position reaches the first location and the current value is less than the value at the previous location.
            alist[position]=alist[position-1] # Update the value at the current location with the value to the left of it.
            position = position-1 # Move the location to the left.
        alist[position]=currentvalue # Update this new location with the current value.
    return alist

print("Bubble Sort")
myList = [5, 10, 8, 2, 4, 1, 6, 7, 9, 3]
print(myList)
newList = bubble_sort(myList)
print(newList)
print("")

print("Selection Sort")
myList = [5, 10, 8, 2, 4, 1, 6, 7, 9, 3]
print(myList)
newList = selection_sort(myList)
print(newList)
print("")

print("Insertion Sort")
myList = [5, 10, 8, 2, 4, 1, 6, 7, 9, 3]
print(myList)
newList = insertion_sort(myList)
print(newList)  