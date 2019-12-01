'''
Created on Nov 30, 2019
Marcelious Willis

BinHeap class sourced from: https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
'''

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
        
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    
    def printHeap(self):
        print("Heap List: {}\n".format(self.heapList))
            
# =================== Driver Code =======================
# Question 1
myList = [8, 3, 9, 1, 2, 6, 4, 7, 5]
print("Random List: {}\n".format(myList))
#         8
#      /     \
#     3       9
#    / \     / \
#   1   2   6   4
#  / \
# 7   5

myBinaryHeap1 = BinHeap()
for i in myList:
    myBinaryHeap1.insert(i)
print("Heap List for Question 1:")
myBinaryHeap1.printHeap()
print("         1\n"
      "      /     \ \n"
      "     2       4 \n"
      "    / \     / \ \n"
      "   5   3   6   9 \n"
      "  / \ \n"
      " 8   7 \n"
      "") 

# Question 2
myBinaryHeap2 = BinHeap()
myBinaryHeap2.buildHeap(myList)
print("Heap List for Question 2:")
myBinaryHeap2.printHeap()
print("         1\n"
      "      /     \ \n"
      "     2       4 \n"
      "    / \     / \ \n"
      "   3   8   6   9 \n"
      "  / \ \n"
      " 7   5 \n"
      "")
