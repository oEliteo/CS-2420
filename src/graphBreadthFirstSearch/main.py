from graphBreadthFirstSearch import *
import random

def main():
    print("Graph 1:")
    file = open("graph0.txt","r")
    verticies = 0
    for line in file:
        verticies += 1
    file.close()
    g = Graph(verticies)
    file = open("graph0.txt", "r")
    for line in file:
        split = line.split()
        for i in range(1, len(split)):
            g.addEdge(int(split[0]), int(split[i]))
    for i in range(verticies):
        random1 = random.randint(0, verticies-1)
        random2 = random.randint(0, verticies-1)
        while(random1 == random2):
            random2 = random.randint(0, verticies-1)
        print("The path found between", str(random1) + ",", str(random2), "in test case", str(i), "graph was:", g.findPath(random1,random2))

def main2():
    print("\n\n")
    print("Graph 2:")
    file = open("graph1.txt","r")
    verticies = 0
    for line in file:
        verticies += 1
    file.close()
    g = Graph(verticies)
    file = open("graph0.txt", "r")
    for line in file:
        split = line.split()
        for i in range(1, len(split)):
            g.addEdge(int(split[0]), int(split[i]))
    for i in range(verticies):
        random1 = random.randint(0, verticies-1)
        random2 = random.randint(0, verticies-1)
        while(random1 == random2):
            random2 = random.randint(0, verticies)
        print("The path found between", str(random1) + ",", str(random2), "in test case", str(i), "graph was:", g.findPath(random1,random2))
    
main()
main2()