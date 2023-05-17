def selectionSort(array):
    
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        #swap
        array[i], array[minIdx] = array[minIdx], array[i]
    
    print(array)
    return array

sampleArray = [1,5,4,0,7,2,3,9,6,8,7]


selectionSort(sampleArray)