import sys

def fibIterative(n):
    if ( n < 0 ):
        raise ValueError("Error: n cannot be a negative number")
    elif ( type(n) == float ):
        raise ValueError("Error: n cannot be a floating point number")
    fibVal, lastVal = 0, 0
    currVal = 1

    if ( n == 0 ):
        fibVal = 0
    elif ( n == 1 ):
        fibVal =  1
    
    else:
        for ii in range(1, n):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def fibRecursive(n):
    if ( n < 0 ):
        raise ValueError("Error: n cannot be a negative number")
    elif ( type(n) == float ):
        raise ValueError("Error: n cannot be a floating point number")
    
    fibVal = 0

    if ( n == 0 ):
        fibVal = 0 
    elif ( n == 1 ):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal

def main():
    if (len(sys.argv) < 3):
        print("Usage: fibonnaci.py <i/r> <num>")
    else:
        try:
            if sys.argv[1] == 'i':
                print(fibIterative(int(sys.argv[2])))
            if sys.argv[1] == 'r':
                print(fibRecursive(int(sys.argv[2])))
        except ValueError as e:
            print(e)
main()