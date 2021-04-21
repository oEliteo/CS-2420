import math

def isPrime(x):
    
    s = int(sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            return False
    return True

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mL = None
        self.mR = None

class UUC:
    def __init__(self, neededSize):
        actualSize = 2 * neededSize + 1
        self.mSize = 0
        while not isPrime(actualSize):
            actualSize += 2
        
        self.mTable = []
        for i in range(actualSize):
            self.mTable.append(None)
            
            
        
    def insert(self, item):
        if self.exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
    
    def delete(self, item):
        if not self.exists(item):
            return False
    
    def retrieve(self, item):
        current = self.mFirst
        if self.exists(item):
            return self.retrieveRecursive(current, item)        
            
    def exists(self, item):
        return self.existsRecursive(item, self.mFirst)
            
    def size(self):
        return self.mSize
    
    def traverse(self, callBackFunction, data):
        