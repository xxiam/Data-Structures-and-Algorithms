import sys

class NegativeNumberError(Exception):
    pass

def gcdRec(a, b):
    if a < 0 or b < 0:
        raise NegativeNumberError("Error: values must be a positive integer")
    
    if b == 0:
        return a
    else:
        return gcdRec(b, a % b)

def gcdIterative(a, b):

    if a < 0 or b < 0:
        raise NegativeNumberError("Error: values must be a positive integer")
    
    while b != 0:
        (a,b) = (b, a%b)
    return a

def main():
    if len(sys.argv) < 4:
        print("gcd.py <i/r> a, b")
    else:
        try:
            if (sys.argv[1] == "i"): #iterative
                print(gcdIterative(int(sys.argv[2]), int(sys.argv[3])))
            if (sys.argv[1] == "r"):
                print(gcdRec(int(sys.argv[2]), int(sys.argv[3])))
        except NegativeNumberError as e:
            print(e)

if __name__ == "__main__":
    main()