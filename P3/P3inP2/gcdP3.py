from DSAp3 import DSAstack

class FloatingPointError(Exception):
    pass    

class StringInputError(Exception):
    pass

class NegativeNumberError(Exception):
    pass


def displayStack(stack):
    for item in stack.arr:
        if item != 'none':
            print(item, end = ' ')
    print("\n---")

def gcdIterative(a, b):
    stack = DSAstack()

    try:
        a, b = int(a), int(b)
    except:
        try:
            a, b = float(a), float(b)
        except:
            raise StringInputError("Error: string input")
        raise FloatingPointError("Error: floating point number")

    while b != 0:
        stack.push(f"gcdIterative: {a}, {b}")
        displayStack(stack)
        (a, b) = (b, a%b)
    return a

def gcdRecursive(a, b, stack):
    if stack is None:
        stack = DSAstack()

    try:
        a, b = int(a), int(b)
    except:
        try:
            a, b = float(a), float(b)
        except:
            raise StringInputError("Error: string input")
        raise FloatingPointError("Error: floating point number")

    if b == 0:
        stack.push(f"gcdRecursive: {a}, {b}")    
        displayStack(stack)
        return a
    else:
        stack.pusn(f"gcdRecursive: {a}, {b}")
        displayStack(stack)
        return gcdRecursive(b, a % b, stack)