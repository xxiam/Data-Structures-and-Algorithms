import sys

class NegativeNumberError(Exception):
    pass

def towers(disks, start, end, auxTower):
    if disks <= 0:
        raise NegativeNumberError("Error: disks cannot be negative")
    if disks == 1:
        moveDisk(start, end)
    else: 
        towers(disks - 1, start, auxTower, end)
        moveDisk(start, end)
        towers(disks - 1, auxTower, end, start)
    
def moveDisk(src, dest):
    print(f"Moved disk from {src} to {dest}")

def main():

    if len(sys.argv) < 4:
        print("hanoi.py <diskAmount> <start> <end>")
    
    else:
        try:
            towers(int(sys.argv[1]), 1, 3, 2)
        except NegativeNumberError as e:
            print(e) 

if __name__ == "__main__":
    main()