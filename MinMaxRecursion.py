# Author: Marcel Willis
# SWDV-620 Week 3: Recursion

def MinRecursive(sequence,sequence_size):
    """Recursion algorithm to find the minimum value of a given sequence."""
    if sequence_size == 1: # Sequence only contains one value
        minvalue = sequence[0]
        return minvalue
    else: # Use recursion to find the minimum value of the sequence.
        minvalue = sequence[0]
        if minvalue < MinRecursive(sequence[1:],sequence_size-1):
            return minvalue
        else:
            return MinRecursive(sequence[1:],sequence_size-1)
        
def MaxRecursive(sequence,sequence_size):
    """Recursion algorithm to find the maximum value of a given sequence."""
    if sequence_size == 1: # Sequence only contains one value
        maxvalue = sequence[0]
        return maxvalue
    else: # Use recursion to find the maximum value of the sequence.
        maxvalue = sequence[0]
        if maxvalue > MaxRecursive(sequence[1:],sequence_size-1):
            return maxvalue
        else:
            return MaxRecursive(sequence[1:],sequence_size-1)

mysequence = [13, 17, 83, -2, 9, 700, 99]
seq_size = len(mysequence)
minvalue = MinRecursive(mysequence,seq_size)
maxvalue = MaxRecursive(mysequence,seq_size)
print("Minimum value: {}".format(minvalue))
print("Maximum value: {}".format(maxvalue))