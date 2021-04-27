import math

def isPrime(x):
    
    s = int(math.sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            return False
    return True

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mL = None
        self.mR = None

class UUCH:
    def __init__(self, neededSize):
        actualSize = 2 * neededSize + 1
        self.mSize = 0
        while not isPrime(actualSize):
            actualSize += 2
        
        self.mTable = [None] * actualSize     
        
    def insert(self, item):
        if self.exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while self.mTable[index]:
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)
        self.mSize += 1
        self.mTable[index] = item
        return True
                
                
    
    def delete(self, item):
        if not self.exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while not (self.mTable[index] and self.mTable[index] == item):
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)
        self.mTable[index] = False
        self.mSize -= 1
        return True
    
    def retrieve(self, item):
        if not self.exists(item):
            return None
        key = int(item)
        index = key % len(self.mTable)
        while not (self.mTable[index] and self.mTable[index] == item):
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)
        return self.mTable[index]
            
    def exists(self, item):
        key = int(item)
        index = key % len(self.mTable)
        while True:
            if self.mTable[index] is None:
                return False
            if self.mTable[index] and self.mTable[index] == item:
                return True
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)
            
    def size(self):
        return self.mSize
    
    def traverse(self, callBackFunction, data):
        for i in range(len(self.mTable)):
            if self.mTable[i]:
                callBackFunction(self.mTable[i], data)
        