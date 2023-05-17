import DSAp3
NUM_TO_BASE = "0123456789ABCDEF" #up to base 16 charset


class FloatingPointError(Exception):
    pass    

class StringInputError(Exception):
    pass

class NegativeNumberError(Exception):
    pass


def displayStack(stack):
    for item in stack.arr:
        if item != 'none':
            print(item, end = ' | ')
    print("\n---")

def iterativeConversion(num, base):
    stack = DSAp3.DSAstack()
    try:
        num, base = int(num), int(base)
    except:
        try:
            num, base = float(num), float(base)
        except:
            raise StringInputError("Error: string input")
        raise FloatingPointError("Error: floating point number")
    
    retVal = ""

    while num != 0:
        retVal += str(NUM_TO_BASE[num % base])
        stack.push(f"iterativeConversion: {retVal[::-1]}")
        displayStack(stack)
        num = int(num/base)

    return ''.join(retVal[::-1])

def recursiveConversion(num,base,retVal,stack):
    if stack is None:
        stack = DSAp3.DSAstack()
    try:
        num, base = int(num), int(base)
    except:
        try:
            num, base = float(num), float(base)
        except:
            raise StringInputError("Error: string input")
        raise FloatingPointError("Error: floating point number")

    if retVal == None:
        retVal = str(NUM_TO_BASE[num % base])
    else:
        retVal += str(NUM_TO_BASE[num % base])
    
    num = int(num/base)

    if num != 0:
        stack.push(f"recursiveConversion: {retVal[::-1]}")
        displayStack(stack)
        recursiveConversion(num,base,retVal,stack)
    else:
        stack.push(f"recursiveConversion: {retVal[::-1]}")
        displayStack(stack)
        retVal = retVal[::-1]
        print(retVal)

def main():
    while True:
        userinput = input("<i/r> n b\n:")
        func, num, base = userinput.split()
        try:
            if func == 'i':
                print(iterativeConversion(num,base))
            if func == 'r':
                recursiveConversion(num,base,None,None)
            else:
                print("please enter a valid choice")
        except FloatingPointError as e:
            print(e)
        except StringInputError as e:
            print(e)
        except NegativeNumberError as e:
            print(e)

main()