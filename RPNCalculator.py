# Import libraries
import numpy as np

def RPNCalculator(commands):
    # RPNCalculator takes in a string of number and commands then 
    # executes the commands in the string and uses the numbers as variables
    # 
    #
    # Usage:  RPNCalculator(a string og text)
    #           
    # Input:  commands (A string)
    #
    # Output: stack (A string)
    #
    # Author: Vitale Jorgensen, s184846
    
    # Starts by creating an empty list then a list of posible
    # occured operations +,- as lambda expressions
    stack=[]
    ops={"+":(lambda a,b: a+b),
         "-":(lambda a,b: a-b) }
    # Splits the input string into list of items then loop
    # in the items to see if ops is in there or 's'. when the operations are
    # found the variables are poped and passed to the lambda expression
    items=commands.split()
    for item in items:
        if item in ops:
            b=stack.pop()
            a=stack.pop()
            result=ops[item](a,b)
            stack.append(result)
        elif item == "s":
            b=stack.pop()
            a=stack.pop()
            a,b=b,a
            stack.append(a)
            stack.append(b)
        else:
            stack.append(int(item))
            print("test change in github")
    return stack

