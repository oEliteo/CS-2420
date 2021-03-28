class Node:
    def __init__(self, item, nxt):
        self.mItem = item
        self.mNext = nxt

class UUC:
    def __init__(self):
        self.mFirst = None
        
    def insert(self, item):
        if self.exists(item):
            return False
        n = Node(item, self.mFirst)
        self.mFirst = n
        return True
    
    def delete(self, item):
        if not self.Exists(item):
            return False
        
        if self.mFirst.mItem == item:
            self.mFirst = self.mFirst.mNext
            return True
        
        current = self.mFirst
        while current.mNext.mItem != item:
            current = current.mNext
        current.mNext = current.mNext.mNext
        
    def retrieve(self, item):
        current = self.mFirst
        while current != None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
            
    def exists(self, item):
        current = self.mFirst
        while current != None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False
            
    def size(self):
        count = 0
        current = self.mFirst
        while current != None:
            current = current.mNext
            count += 1
        return count
    
    def traverse(self, callBackFunction):
        current = self.mFirst
        while current != None:
            callBackFunction(current.mItem)
            current = current.mNext
        