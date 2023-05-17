'''
quicksort varaitions:
1. quicksort with first element as pivot
2. quicksort with random element as pivot
3. quicksort with median of three elements as pivot
'''

#quicksort with first element as pivot
def quickSortFirstPivot(array, start, end):
    if start < end:
        pivot = partitionFirstPivot(array, start, end)
        quickSortFirstPivot(array, start, pivot - 1)
        quickSortFirstPivot(array, pivot + 1, end)
    return array

def partitionFirstPivot(array, start, end):
    pivot = array[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

#quicksort with random element as pivot
def quickSortRandomPivot(array, start, end):
    if start < end:
        pivot = partitionRandomPivot(array, start, end)
        quickSortRandomPivot(array, start, pivot - 1)
        quickSortRandomPivot(array, pivot + 1, end)
    return array

def partitionRandomPivot(array, start, end):
    pivot = random.randint(start, end)
    array[start], array[pivot] = array[pivot], array[start]
    pivot = array[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

#quicksort with median of three elements as pivot
def quickSortMedianPivot(array, start, end):
    if start < end:
        pivot = partitionMedianPivot(array, start, end)
        quickSortMedianPivot(array, start, pivot - 1)
        quickSortMedianPivot(array, pivot + 1, end)
    return array

def partitionMedianPivot(array, start, end):
    pivot = medianOfThree(array, start, end)
    array[start], array[pivot] = array[pivot], array[start]
    pivot = array[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def medianOfThree(array, start, end):
    mid = (start + end) // 2
    if array[start] < array[mid]:
        if array[mid] < array[end]:
            return mid
        elif array[start] < array[end]:
            return end
        else:
            return start
    else:
        if array[start] < array[end]:
            return start
        elif array[mid] < array[end]:
            return end
        else:
            return mid
        
#test function
if __name__ == "__main__":
    import random
    randomList = []
    for i in range(10):
        newNum = random.randint(0,10)
        randomList.append(newNum)
    print("Randomly generated list:")
    print(randomList)
    print("Sorted list:")
    print(quickSortFirstPivot(randomList, 0, len(randomList) - 1))
    print(quickSortRandomPivot(randomList, 0, len(randomList) - 1))
    print(quickSortMedianPivot(randomList, 0, len(randomList) - 1))