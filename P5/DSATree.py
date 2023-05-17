'''
p5
'''
import pickle
import numpy as np
import csv

class NoNodeError(Exception):
    pass

class DSATreeNode():
    
    def __init__(self, key, value):
        self.key = int(key)
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Key: {self.key} | Value: {self.value}" 
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setKey(self, key):
        self.key = key

    def setValue(self, val):
        self.key = val

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class DSABinarySearchTree(DSATreeNode):
    
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def isEmpty(self):
        if self.root is None and self.nodeCount == 0:
            return True
        else:
            return False
        
    def find(self, key):
        
        def __findRec(key, currentNode):
            value = None
            if currentNode is None:
                raise NoNodeError(f"Error: {key} does not exist  ")
            
            elif key == currentNode.getKey(): #if the node is the root
                value = currentNode.getValue()
            
            elif key < currentNode.getKey():
                value = __findRec(key, currentNode.getLeft())
            else:
                value = __findRec(key, currentNode.getRight())

            return value

        return __findRec(key, self.root)
    
    def insert(self, key, value):

        def __insertRec(key, value, currentNode):
            updateNode = currentNode

            if updateNode is None:
                updateNode = DSATreeNode(key, value)
            
            elif key < updateNode.getKey():
                updateNode.setLeft(__insertRec(key, value, updateNode.getLeft()))

            elif key > updateNode.getKey():
                updateNode.setRight(__insertRec(key, value, updateNode.getRight()))

            return updateNode

        if self.isEmpty() is True:
            newNode = DSATreeNode(key, value)
            self.root = newNode
        
        else:
            __insertRec(key, value, self.root)
        
        self.nodeCount += 1

    def delete(self, key):
        
        def __promoteSuccessor(node):
            successor = node
            if node.getLeft() is None:
                successor = node
            else:
                if node.getLeft() is not None:
                    successor = __promoteSuccessor(node.getLeft())
                    if successor == node.getLeft():
                        node.setLeft(successor.getRight())
            return successor

        def __deleteNode(node):
            
            if  node.getLeft() is None and node.getRight() is None:
                updateNode = None
            elif node.getLeft() is not None and node.getRight() is None:
                updateNode = node.getLeft()
            elif node.getRight() is not None and node.getLeft() is None:
                updateNode = node.getRight()
            else:
                updateNode = __promoteSuccessor(node.getRight())
                if updateNode is not node.getRight():
                    updateNode = node.getRight()
                updateNode.setLeft(node.getLeft())
            return updateNode

        def __deleteRec(key, curNode):
            updateNode = curNode
            if curNode is None:
                return None
            
            elif key == curNode.getKey():
                updateNode =  __deleteNode(curNode)
            elif key < curNode.getKey():
                curNode.setLeft(__deleteRec(key, curNode.getLeft()))
            else:
                curNode.setRight(__deleteRec(key, curNode.getRight()))
            return updateNode

        self.root = __deleteRec(key, self.root)

    def height(self):

        if self.isEmpty() is True:
            return 0

        def __height(level, nodeCount, currentCount):
            if currentCount >= nodeCount:
                return level
                #the counter has reached a level where the max nodes per level is greater or equal to the node count
            elif nodeCount > currentCount:
                level += 1
                currentCount = currentCount + currentCount * 2
                    
                return __height(level, nodeCount, currentCount)
        
        return __height(1, self.nodeCount, 1) #1 because height 1 will always be 1, unless the tree is empty
    
    def min(self):
        
        def __min(currentNode):
            if currentNode.getLeft() is None:
                return currentNode
            else:
                return __min(currentNode.getLeft())

        return __min(self.root).getKey()
    
    def max(self):

        def __max(currentNode):
            if currentNode.getRight() is None:
                return currentNode
            else:
                return __max(currentNode.getRight())
        
        return __max(self.root).getKey()

    def printInorder(self):

        def __printIndorder(cur):
            if cur is not None:
                __printIndorder(cur.getLeft())
                print(cur)
                __printIndorder(cur.getRight())
        __printIndorder(self.root)

    def printPostorder(self):

        def __printPostorder(cur):
            if cur is not None:
                __printPostorder(cur.getLeft())
                __printPostorder(cur.getRight())
                print(cur)
        __printPostorder(self.root)

    def printPreorder(self):

        def __printPreorder(cur):
            if cur is not None:
                print(cur)
                __printPreorder(cur.getLeft())
                __printPreorder(cur.getRight())
        __printPreorder(self.root)

    def balance(self):

        def __balance(cur, ndCount):
            ndCount = 0
            if cur is not None:
                ndCount += 1
                __balance(cur.getLeft(), ndCount)
                __balance(cur.getRight(), ndCount)
            return ndCount

        leftcount = __balance(self.root.getLeft(), 0)
        rightcount = __balance(self.root.getRight(), 0)
        return leftcount, rightcount
    
    def treeToArray(self):

        def __treeToArrPreOrder(cur, array, index):
            if cur is not None:
                array[index] = cur
                __treeToArrPreOrder(cur.getLeft(), array, index + 1)
                __treeToArrPreOrder(cur.getRight(), array, index + 1)
            return array

        emptyArray = np.empty(self.nodeCount, dtype = "object")
        retArray = np.empty(self.nodeCount, dtype = "object")
        c = 0
        index = 0
        keyVal = __treeToArrPreOrder(self.root, emptyArray, index)
        for i in keyVal:
            value = i.getValue()
            key = str(i.getKey())
            retArray[c] = (key, value)
            c += 1
        return retArray
        

    def saveTree(self, filename):
        with open(filename + ".pickle", "wb") as f:
            pickle.dump(self, f)
        print("Saved to " + filename)

    def loadTree(self, filename):
        with open(filename + ".pickle", "rb") as f:
            return pickle.load(f)
        
    def saveCSV(self, filename):
        data = self.treeToArray()
        header = np.array(('key','value'))

        with open(filename + '.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for v in data:
                writer.writerow(v)

    def readCSV(self, filename):
        ...

if __name__ == "__main__":
    bt = DSABinarySearchTree()
    bt.insert(50, 'hello')
    bt.insert(78, "asdfasdfas")
    bt.insert(25, "2")
    bt.saveCSV("csvtest")
