from graphics import *
from Stack import *
import math

"""
Instructions:

Create a Graphing calculator.
As part of the assignment, you must implement your own Stack class.
Your program should let the user enter an expression of their choice.
Convert their expression with a function InfixToPostfix
Plot their expression with a function EvaluatePostfix
Use graphics.py or pygame.py.
You may need to do coordinate transformations from world to pixel coordinates.

Assume the user enters valid expressions, so you do not need error checking.
Valid expressions consists of single digit integers, the variable x, the operators +, -, /, and *, and parenthesis.
You can choose to not allow any spaces, though it's not hard to allow them.
(Be sure to make your limitations clear when you prompt the user to enter an expression.)
Test your program on several expressions, such as "x*x*x/(2*5)".
"""

def main():
    
    #setup window defaults
    lowerBound = -10
    upperBound = 10
    winSize = 800
    increment = .1
    epsilon = .0001
    pointList = []
    window = GraphWin("Graphing Calculator", winSize, winSize)
    window.setCoords(lowerBound, lowerBound, upperBound, upperBound)
    #end window setup
    
    #User defined graph
    printInstructions()
    infix = input("Enter an expression to graph following the outline above: ")
    postfix = infixToPostFix(infix)
    print(postfix)
    generatePoints(pointList, lowerBound, upperBound, increment, epsilon, postfix)
    #End User Defined Graph
    
    
    for i in range(len(pointList) - 1):
        line = Line(Point(pointList[i][0],pointList[i][1]), Point(pointList[i+1][0],pointList[i+1][1]))
        line.draw(window)
    window.getMouse()
    window.close()
    
def generatePoints(xlist, lowerBound, upperBound, increment, epsilon, postfix):
    x = lowerBound
    while x < upperBound + epsilon:
        y = evaluatePostFix(postfix, x)
        xlist.append((x, y))
        x += increment

def infixToPostFix(infix):
    stack = Stack()
    postfix = ""
    for i in infix:
        if i >= "0" and i <= "9":
            postfix += i
        elif i.lower() == 'x':
            postfix += i
        elif i in "+-":
            while not stack.isEmpty() and stack.peek() in "+-*/":
                postfix += stack.pop()
            stack.push(i)
        elif i in "*/":
            while not stack.isEmpty() and stack.peek() in "*/":
                postfix += stack.pop()
            stack.push(i)
        elif i in "(":
            stack.push(i)
        elif i in ")":
            while not stack.isEmpty() and stack.peek() in ")":
                postfix += stack.pop()
            stack.pop()
    while not stack.isEmpty():
        postfix += stack.pop()

    return postfix

def evaluatePostFix(postfix, x):
    stack = Stack()
    for i in postfix:
        if i >= "0" and i <= "9":
            stack.push(float(i))
        elif i.lower() == 'x':
            stack.push(x)
        elif i == "+":
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs + rhs
            stack.push(result)
        elif i == "-":
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs - rhs
            stack.push(result)
        elif i == "*":
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs * rhs
            stack.push(result)
        elif i == "/":
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs / rhs
            stack.push(result)
        elif i == "(":
            stack.pop()
    
    return stack.pop()
        
    
def printInstructions():
    return "The graphing calculator does not yet support multiple digit numbers, keep it between 0 and 9 \n operators supported are +, -, *, /, parentheses can be used. No spaces"
main()