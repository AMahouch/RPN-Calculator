# Ameen Mahouch
# 1001920240
# 5 April 2023
# macOS Big Sur 11.4

import os

file = open("input_RPN.txt", "r")
lines = file.read().splitlines()

for line in lines:
    stack = []
    for i in line.split():
        if (i.isdigit()) :
            stack.append(int(i))
        elif i == '+':
            op2 = stack.pop()
            op1 = stack.pop()
            intermediate = op1 + op2
            stack.append(intermediate)
        elif i == '-':
            op2 = stack.pop()
            op1 = stack.pop()
            intermediate = op1 - op2
            stack.append(intermediate)
        elif i == '*':
            op2 = stack.pop()
            op1 = stack.pop()
            intermediate = op1 * op2
            stack.append(intermediate)
        elif i == '/':
            op2 = stack.pop()
            op1 = stack.pop()
            intermediate = float(op1) / op2
            stack.append(intermediate)
        else:
            print("unexpected token. error with " + i)
            break        
    print(stack.pop())

