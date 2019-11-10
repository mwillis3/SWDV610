# Author: Marcel Willis
# SWDV-620 Week 3: Recursion

def reverse_list(sequence):
    """Recursion algorithm to reverse the order of a given sequence."""
    if len(sequence) == 1: # Sequence only contains one value
        return [sequence[0]]
    else: # Use recursion to reverse the sequence.
        return [sequence[-1]] + reverse_list(sequence[:-1])
    
mysequence = [1,2,3,4,5,6,7,8,9,10]
newsequence = reverse_list(mysequence)
print("Reversed sequence is: {}".format(newsequence))