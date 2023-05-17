import pickle 
class DSAListNode:

    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.previousNode = None

    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.nextNode
    
    def getPrevious(self):
        return self.previousNode
    
    def setNext(self,next):
        self.nextNode = next

    def setPrev(self,prev):
        self.previousNode = prev

    def setValue(self,value):
        self.value = value

    def __iter__(self):
        self.cursor = self.head
        return self

    def __next__(self):
        cursorValue = None
        if self.cursor is None:
            raise StopIteration
        else:
            cursorValue = self.cursor.getValue()
            self.cursor = self.cursor.getNext()
        return cursorValue

class DSALinkedList(DSAListNode):
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False
        
    def insertFirst(self,value):
        newNode=DSAListNode(value)
        if (self.isEmpty() is True):
            self.head=newNode
            self.tail=newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head=newNode
        return newNode
    
    def insertLast(self,value): #insert a new value in the right side, tail
        newNode = DSAListNode(value)
        if self.isEmpty() is True:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
        return newNode

    def peekFirst(self):
        if (self.isEmpty() is True):
            return None
        else:
            return self.head.getValue()
        
    def peekLast(self):
        if (self.isEmpty() is True):
            return None
        else:
            return self.tail.getValue()
    
    def removeFirst(self):
        if (self.isEmpty() is True):
            raise ListError("Error: empty linked list")
        else:
            nodeValue = self.head.getValue()
            if self.head.getNext() is None: #last node
                self.head, self.tail = None, None
            else:
                self.head = self.head.getNext()
                self.head.setPrev(None)
            return nodeValue

    def removeLast(self):
        if (self.isEmpty() is True):
            raise ListError("Error: empty linked list")
        else:
            nodeValue = self.tail.getValue()
            if self.tail.getPrevious() is None: #last node 
                self.head, self.tail = None, None
            else:
                self.tail = self.tail.getPrevious()
                self.tail.setNext(None)
            return nodeValue

    def savePickle(self, filename):
        with open(filename + ".pickle", "wb") as f:
            pickle.dump(self, f)

    def loadPickle(self, filename):
        with open(filename + ".pickle", "rb") as f:
            return (pickle.load(f))
        
    #new addition for P6
    def removeNode(self, node):
        '''
        removes any node from any index
        '''
        #traverse the linked list
        currentNode = self.head
        while currentNode.getNext() is not None:
            
            if (currentNode == node):
                #grab pervious node and next node and link them together
                previousNode = currentNode.getPrevious()
                nextNode = currentNode.getNext()

                previousNode.setNext(nextNode)
                nextNode.setPrev(previousNode)

            #traverse the linked list
            currentNode = currentNode.getNext()
            
            



    
class ListError(Exception):
    pass

if __name__ == "__main__":
    ...