from DSAp3 import *

class NegativeValueError(Exception):
    pass
class StringInputError(Exception):
    pass
class FloatingPointError(Exception):
    pass

def displayStack(stack):
    for item in stack.arr:
        if item != 'none':
            print(item, end = ' ')
    print("\n---")

def iterFibonacci(n):
    stack = DSAstack()

    a, b = 0, 1

    try:
        n = int(n)
    except:
        try:
            n = float(n)
        except:
            raise StringInputError("Error: string inputted")
        raise FloatingPointError("Error: floating point number")

    if (n < 0):
        raise NegativeValueError("Error: please enter a positive integer")
    
    elif (n == 0):
        displayStack(stack)
        stack.push(f"iterFibonacci: 0")
        return 0
    
    elif (n == 1):
        displayStack(stack)
        stack.push(f"iterFibonacci: 1")
        return 1
    
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            displayStack(stack)
            stack.push(f"iterFibonacci: {b}")

    return b

def recursiveFibonacci(n, stack):
    if stack is None:
        stack = DSAstack()
    
    try:
        n = int(n)
    except:
        try:
            n = float(n)
        except:
            raise StringInputError("Error: string inputted")
        raise FloatingPointError("Error: floating point number")

    if n < 0:
        raise NegativeValueError("Error: please enter a positive number")

    fibVal = 0
    if n == 0:
        stack.push(f"recursiveFibonacci: {fibVal}")
        return fibVal
    if n == 1:
        fibVal = 1
        stack.push(f"recursiveFibonacci: {fibVal}")
        return fibVal
    else:
        displayStack(stack)
        fibVal = recursiveFibonacci(n-1, stack) + recursiveFibonacci(n-2, stack)
        stack.push(f"recursiveFibonacci: {fibVal}")
        return fibVal
    
def main():
    while True:
        func, num = input("<i/r> num\n:").split()
        try:
            if func == 'i':
                print(iterFibonacci(num))
            if func == 'r':
                print(recursiveFibonacci(num,None))
            else:
                print("please enter a valid choice")
        except FloatingPointError as e:
            print(e)
        except StringInputError as e:
            print(e)
        except NegativeValueError as e:
            print(e)

main()