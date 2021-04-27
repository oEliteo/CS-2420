class Queue:
    
    def __init__(self):
        self.mSize = 0
        self.mQueue = []
    
    def last(self):
        return self.mQueue[len(self.mQueue - 1)]
    
    def first(self):
        return self.mQueue[self.mQueue - 1]
    
    def enqueue(self, item):
        self.mQueue.append(item)
        self.mSize += 1
        
    def dequeue(self):
        returnVal = self.mQueue[len(self.mQueue) - 1]
        self.mQueue.remove(self.mQueue[len(self.mQueue) - 1])
        self.mSize -= 1
        return returnVal
        
        
                                
    def exists(self, item):
        for i in range(len(self.mQueue)):
            if self.mQueue[i] == item:
                return True
        return False
    
    def isEmpty(self):
        if self.mSize > 0:
            return False
        else:
            return True
        
