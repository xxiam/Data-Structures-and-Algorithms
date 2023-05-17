from DSAHeap import *

#determine length of file
with open("../P7/RandomNames7000.csv", "r") as f:
    for i, l in enumerate(f):
        pass
    length = i + 1

#create heap of length of file
heap = DSAHeap(length)

#read file and insert into heap
with open("../P7/RandomNames7000.csv", "r") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        heap.insert(line[0], line[1])

#remove from heap and print
while not heap.isEmpty():
    print(heap.remove())