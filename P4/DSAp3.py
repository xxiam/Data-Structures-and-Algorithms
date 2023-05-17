


from headTailLinkedList import *

class DSAstack:

    def __init__(self):
        self.ll = DSALinkedList()
        self.count = 0
    
    def __iter__(self):
        return iter(self.ll)

    def getCount(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def push(self,value):
        self.ll.insertLast(value)
        self.count += 1

    def top(self): 
        return self.ll.peekLast()
         
    def Spop(self): #because pop already exists
        self.count -= 1
        return self.ll.removeLast()

class DSAQueue():

    def __init__(self):
        self.ll = DSALinkedList()
        self.count = 0
    
    def __iter__(self):
        return iter(self.ll)

    def getCount(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def enqueue(self, val):
        self.count += 1
        self.ll.insertFirst(val)
    
    def dequeue(self):
        self.count -= 1
        return self.ll.removeLast()
    
if __name__ == "__main__":
    stack = DSAQueue()
    stack.enqueue(1)
    stack.enqueue(2)
    stack.enqueue(3)
    
    for item in stack:
        print(item)