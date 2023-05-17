class NegativeValueError(Exception):
    pass 

def calcNFactorial(n):
    if (n < 0):
        raise NegativeValueError("Error: number cannot be a negative")
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    return nFactorial

def calcNFactorialRecursive(n):
    if (n < 0):
        raise NegativeValueError("Error: number cannot be a negative")
    if (n == 0):
        return 1
    else:
        return n * calcNFactorialRecursive(n - 1)
    
def main():
    choice = input("Would you like to use (r)ecursive or (i)terative: ")
    if (choice == 'r'):
        try:
            print(calcNFactorialRecursive(int(input("Please enter a number: "))))
        except TypeError:
            print("Error: please enter a valid integer")

    if (choice == 'i'):
        try:
            print(calcNFactorial(int(input("Please enter a number: "))))
        except TypeError: #stops negative numbers and strings from being entered
            print("Error: please enter a valid integer")
    else:
        main()
    
if __name__ == "__main__":
    main()