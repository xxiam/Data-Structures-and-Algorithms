#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(a):
    passes = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a) - passes - 1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
        passes += 1
    return a
    

def insertionSort(a):
    for n in range(len(a) - 1):
        i = n + 1

        temp = a[i]
        while i > 0 and a[i-1] > temp:
            a[i] = a[i-1]
            i -= 1
        a[i] = temp
    return a

def selectionSort(array):
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        #swap
        array[i], array[minIdx] = array[minIdx], array[i]
    
    return array


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


if __name__ == "__main__":
    import random
    randomList = []
    for i in range(10):
        newNum = random.randint(0,10)
        randomList.append(newNum) 
    bubbleSort(randomList)