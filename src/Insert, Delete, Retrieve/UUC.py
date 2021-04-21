class Node:
    def __init__(self, item):
        self.mItem = item
        self.mL = None
        self.mR = None

class UUC:
    def __init__(self):
        self.mFirst = None
        self.mSize = 0
        
    def insert(self, item):
        if self.exists(item):
            return False
        n = Node(item)
        self.mFirst = self.insertRecursive(n, self.mFirst)
        self.mSize += 1
        return True
    
    def insertRecursive(self, node, current):
        if current==None:
            current = node
        elif node.mItem < current.mItem:
            current.mL = self.insertRecursive(node, current.mL)
        
        else:
            current.mR = self.insertRecursive(node, current.mR)
        
        return current
    
    def delete(self, item):
        if not self.exists(item):
            return False
        self.deleteRecursive(item, self.mFirst)
        self.mSize -= 1
        return True
        
    
    def deleteRecursive(self, item, current):
        if item < current.mItem:
            self.deleteRecursive(item, current.mL)
        elif item > current.mItem:
            self.deleteRecursive(item, current.mR)
        else:
            if current.mL is None and current.mR is None:
                current = None
            elif current.mL is None and current.mR is not None:
                current = current.mR
            elif current.mL is not None and current.mR is None:
                current = current.mL
            else:
                successor = current.mR
                while successor.mL is not None:
                    successor = successor.mL
                current.mItem = successor.mItem
                current.mR = self.deleteRecursive(successor.mItem, current.mR)
        return current
    
    def retrieve(self, item):
        current = self.mFirst
        if self.exists(item):
            return self.retrieveRecursive(current, item)
    
    def retrieveRecursive(self, current, item):
        if item == current.mItem and current.mItem is not None:
            return current.mItem
        else:
            if item < current.mItem:
                return self.retrieveRecursive(current.mL, item)
            else:
                return self.retrieveRecursive(current.mR, item)
            
            
    def exists(self, item):
        return self.existsRecursive(item, self.mFirst)
    
    def existsRecursive(self, item, current):
        if current is None:
            return False
        elif current.mItem == item:
            return True
        elif item < current.mItem:
            return self.existsRecursive(item, current.mL)
        else:
            return self.existsRecursive(item, current.mR)
            
    def size(self):
        return self.mSize
    
    def traverse(self, callBackFunction, data):
        self.traverseRecursive(callBackFunction, self.mFirst, data)
    
    def traverseRecursive(self, callBackFunction, current, data):
        if current is None:
            return
        callBackFunction(current.mItem, data)
        self.traverseRecursive(callBackFunction, current.mL, data)
        self.traverseRecursive(callBackFunction, current.mR, data)
        
        