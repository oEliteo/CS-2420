class Count:
    def __init__(self):
        self.mCompares = 0
        self.mSwaps = 0
        
    def incrementCompares(self):
        self.mCompares += 1
    
    def incrementSwaps(self):
        self.mSwaps += 1
    
    def getCompares(self):
        return self.mCompares
    
    def getSwaps(self):
        return self.mSwaps