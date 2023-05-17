
import numpy as np

class QueueOverflowError(Exception):
    pass
class StackOverflowError(Exception):
    pass
class EmptyStackError(Exception):
    pass
class EmptyQueueError(Exception):
    pass


class DSAstack:

    def __init__(self):
        a = []
        for _ in range(100):
            a.append("none")

        self.arr = np.array(a, dtype = 'object')
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.count == len(self.arr):
            return True
        else:
            return False

    def push(self,value):
        try:
            if self.isFull():
                raise StackOverflowError("Error: stack is already full")
        except StackOverflowError as e:
            print(e)

        else:
            self.arr[self.count] = value
            self.count += 1
        return value

    def top(self): #this should be fixed soon
        if self.isEmpty() is False:
            return self.arr[self.count - 1]
        else:
            print("Error: empty stack ")
         

    def Spop(self): #because pop already exists

        if self.isEmpty() is True:
            return None

        topVal = self.arr[self.count - 1]
        self.arr[self.count - 1] = 'none'
        self.count -= 1
        return topVal


class DSAQueue():

    def __init__(self):
        a = []
        for _ in range(100):
            a.append("none")
        
        self.arr = np.array(a, dtype = 'object')
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False
        
    def isFull(self):
        if self.count == len(self.arr):
            return True
        else:
            return False

class circularQueue(DSAQueue):
    
    def __init__(self):
        DSAQueue.__init__(self)
        self.head = self.tail = -1

    def enqueue(self,var):
        if (self.tail + 1) % len(self.arr) == self.head:
            raise QueueOverflowError("Error: queue is full")
        self.count += 1

        if self.head == -1:
            self.head = self.tail = 0
            self.arr[self.tail] = var

        else:
            self.tail = (self.tail + 1) % len(self.arr)
            self.arr[self.tail] = var
        
    def dequeue(self):
        self.count -= 1
        if self.head == -1:
            raise EmptyQueueError("Error: Empty queue")
        
        elif self.head == self.tail:
            temp = self.arr[self.head]
            self.head = -1
            self.tail = -1
            return temp
        
        else:
            temp = self.arr[self.head]
            self.head = (self.head + 1) % len(self.arr)
            return temp
        
class shufflingQueue(DSAQueue):

    def __init__(self):
        DSAQueue.__init__(self)
     

    def enqueue(self, var):
        if self.count >= len(self.arr):
            raise QueueOverflowError("The queue is full")
        
        else:        
            self.arr[self.count] = var
            self.count += 1
    
    def dequeue(self):

        if self.isEmpty() is True:
            raise EmptyQueueError("Error: empty queue")

        temp = self.arr[0]

        for i in range(1,self.count):
            self.arr[i - 1] = self.arr[i]

        self.arr[self.count] = 'none'

        self.count -= 1

        return temp