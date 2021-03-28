from UUC import *

def printName(item):
    print(item)
    
def main():
    uuc  = UUC()
    
    uuc.insert("John")
    uuc.insert("Bob")
    uuc.insert("Mary")
    uuc.insert("Bob")
    print(uuc.exists("John"))
    print(uuc.exists("Sally"))
    print(uuc.size())
    uuc.traverse(printName)
    
main()