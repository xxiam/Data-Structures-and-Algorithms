
NUM_TO_BASE = "0123456789ABCDEF" #up to base 16 charset

def iterativeConversion(num,base):
    
    try:
        num = int(num)
    except ValueError as e:
        print("Error: number cannot be a floating point number")

    retVal = ""

    while num != 0:
        retVal += str(NUM_TO_BASE[num % base])
        num = int(num/base)
    
    return ''.join(retVal[::-1])

def recursiveConversion(num,base,val):
    try:
        num = int(num)
    except ValueError as e:
        print("Error: number cannot be a floating point number")

    if val == "":
        val = str(NUM_TO_BASE[num % base])
    else:
        val += str(NUM_TO_BASE[num % base])

    num = int(num/base)

    if num != 0:
        recursiveConversion(num,base,val)
    else:
        retVal = val[::-1]
        print(retVal)
        
    

def main():
    while True:
        print(
            "Usage: <[i]terative/[r]ecursive> <n> <base>\n",
            "type 'quit' to quit"
        )

        choice = input("~$ ").split()
        
        iR, n, base = choice[0], choice[1], choice[2]

        if iR == 'i':
            try:
                print(iterativeConversion(int(n),int(base)))
            except ValueError as e:
                print(e)
        if iR == 'r':
            try:
                print(recursiveConversion(int(n),int(base),""))
            except ValueError as e:
                print(e)

        if choice == 'quit':
            return

class FloatingPointError(Exception):
    pass

if __name__ == "__main__":
    main()