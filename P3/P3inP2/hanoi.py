import sys
from DSAp3 import DSAstack

class NegativeNumberError(Exception):
    pass
class OverlapError(Exception):
    pass

def towers(disks, start, end, stack):
    stack.push(f"towers: {disks} {start} {end}")

    if disks < 0 or start < 0 or end < 0:
        raise NegativeNumberError("Error: negative number")

    if disks == 1:
        stack.push(moveDisk(start,end))
    else:
        auxTower = 6 - (start + end)
        towers(disks - 1, start, auxTower, stack)
        moveDisk(start,end)
        towers(disks - 1, auxTower, end, stack)

def moveDisk(src,dest):
    print(f"Moved disk from {src} to {dest}")
    
def display(stack):
    return stack.arr

def main():

    stack = DSAstack()

    if len(sys.argv) < 2:
        print("./hanoi.py <diskAmount>")

    else:
        try:
            towers(int(sys.argv[1]),1,3,stack)
            print(display(stack))
            
        except NegativeNumberError as e:
            print(e)

main()