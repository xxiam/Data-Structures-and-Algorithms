import DSAsorts as sorts

class SortingError(Exception):
    pass 

def main():
    with open("RandomNames7000.csv", "r") as f:
        data = f.read().split("\n")
    
    for i in range(len(data)):
        data[i] = int(data[i][:7]) #removes the name

    sortedData = sorts.bubbleSort(data)

    with open("BubbleSort7k.csv", "w") as f:
        validate(sortedData)
        for entry in sortedData:
            f.write(f"{entry}\n")
    
    selectionSorted = sorts.selectionSort(data)

    with open("SelectionSort7k.csv", "w") as f:
        validate(sortedData)
        for entry in selectionSorted:
            f.write(f"{entry}\n")
    
    insertionSorted = sorts.insertionSort(data)

    with open("InsertionSort7k.csv", "w") as f:
        validate(sortedData)
        for entry in insertionSorted:
            f.write(f"{data}\n")
 
def validate(array):
    '''
    validates if the array is sorted or not
    '''
    for i in range(len(array)):
        try:
            if (array[i] > array[i + 1]):
                raise SortingError("Error: array is not sorted")
        except IndexError:
            pass 
    print("Sorted array")
    
if __name__ == "__main__":
    main()


#this file is redundant, this does not work, it has never been used, and it is not needed for the project