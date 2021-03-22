class Stack:
    
    def __init__(self):
        self.mItems = []
        
    def isEmpty(self):
        return self.mItems == []
    
    def push(self, item):
        self.mItems.append(item)
        
    def pop(self,):
        return self.mItems.pop()
    
    def peek(self):
        return self.mItems[len(self.mItems)-1]
    
    def size(self):
        return len(self.mItems)
        