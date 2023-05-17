from DSAHeap import *

def TestHarness():
    #creating heap
    heap = DSAHeap(10)

    #adding in 10 items, the priority is in reverse (first item has priority of 10)
    for i in range(10):
        heap.insert((i - 10) * -1  , i)

    heap.display()
    print("--")
    heap.remove()
    heap.display()
    print("start removing")
    print("priority, value")
    while not heap.isEmpty():
        priority, value = heap.remove()
        print(priority, value)

 
 #

    #testing if items actually get removed from the heap array
    heap.insert(1, "a")

TestHarness()