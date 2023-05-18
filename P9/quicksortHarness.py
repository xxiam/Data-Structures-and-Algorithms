import sys
import quickSortVariants
import random
import numpy as np

arraylen = int(input("enter array size: "))

randomArray = np.random.rand(arraylen)

sortType = input("quicksort type: ")

if (sortType == 'random'):
    quickSortVariants.quickSortRandomPivot(randomArray, 0, len(randomArray) - 1)

elif (sortType == 'first'):
    quickSortVariants.quickSortFirstPivot(randomArray, 0, len(randomArray) - 1)

elif (sortType == 'median'):
    quickSortVariants.quickSortMedianPivot(randomArray, 0, len(randomArray) - 1)

print(randomArray)