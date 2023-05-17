from DSAp3 import *

class FloatingPointError(Exception):
    pass    

class StringInputError(Exception):
    pass


def displayStack(stack):
    '''
    prints stack without the 'none' placeholder entries in the array
    '''

    for item in stack.arr:
        if (item != 'none'):
            print(item, end = ' ')
    print("\n---")

def iterFactorial(n):
    stack = DSAstack()

    try:
        n = int(n)
    except ValueError:
        try:
            n = float(n)
        except:
            raise StringInputError("Error: string inputted")
        raise FloatingPointError("Error: floating point number")
    
    stack.push(f"iterFactorial: {n}")
    for i in range(n-1, 1, -1):
        n *= i
        stack.push(f"iterFactorial: {n}")
        displayStack(stack)
        
    return n

def recFactorial(n, stack):
    if stack is None:
        stack = DSAstack()

    try:
        n = int(n)
    except ValueError:
        try:
            n = float(n)
        except:
            raise StringInputError("Error: string inputted")
        raise FloatingPointError("Error: floating point number")
    
    displayStack(stack)
    if ( n == 1 or n == 0 ):
        return 1
    else:
        stack.push(f"recFactorial: {n}")
        val = n * recFactorial(n-1, stack)
        return val 

def main():
    while True:
        print("<i/r> n | q to quit")
        a = input(": ")

        try:
            if ( a[0] == 'i'):
                print(iterFactorial(a[1::]))
            if ( a[0] == 'r'):
                print(recFactorial(a[1::]))
        except StringInputError as e:
            print(e)
        except FloatingPointError as e:
            print(e)
        except StackOverflowError as e:
            print(e)
            return 0
        
        if ( a[0] == 'q'):
            return 0

main()