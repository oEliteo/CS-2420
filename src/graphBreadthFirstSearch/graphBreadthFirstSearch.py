from Queue import *

class Graph:
    
    def __init__(self, verticies):
        self.mNeighbors = []
        for i in range(verticies):
            newList = []
            self.mNeighbors.append(newList)

    def addEdge(self, start, end):
        self.mNeighbors[start].append(end)
        
    def findPath(self, start, end):
        q = Queue()
        fromPath = [-1] * len(self.mNeighbors)
        fromPath[start] = start
        q.enqueue(start)
        while not q.isEmpty():
            current = q.dequeue()
            if current == end:
                path = []
                c = end
                for i in range(len(fromPath)):
                    if c in path:
                        break
                    else:
                        path.append(c)
                        c = fromPath[c]
                path.reverse()
                return path
                    
            for i in self.mNeighbors[current]:
                if fromPath[i] == -1:
                    fromPath[i] = current
                    q.enqueue(i)
        return None
        
    def getNeighbors(self):
        return self.mNeighbors
    