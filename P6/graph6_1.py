import DSAgraph
import DSALinkedList
import numpy as np

graph = DSAgraph.DSAGraph()
ll = DSALinkedList.DSALinkedList()

with open("prac6_1.al", 'r') as f: #also works with prac6_2.al
    data = f.read()

for row in data.split('\n'):
    array = np.empty(2, dtype = 'str')
    array[0] = row[0]
    array[1] = row[-1]

    ll.insertLast(array) #would be array([A, B])

#start creating objects and pass duplicates
itemCount = 0
for item in iter(ll):
    itemCount += 1

completedVertices = np.empty(itemCount, dtype = "str")
i = 0
for item in iter(ll):
    if item[0] not in completedVertices:
        graph.addVertex(item[0], None)
        completedVertices[i] = item[0]
        i += 1
    elif item[1] not in completedVertices:
        graph.addVertex(item[1], None)
        completedVertices[i] = item[1]
        i += 1

for item in iter(ll):
    graph.addOneWay(item[0], item[1])

graph.displayAsList()
