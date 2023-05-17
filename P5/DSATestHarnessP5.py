from DSATree import *
import sys

def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "test":
            binaryTreeTest()
            return
    
    print("\n === DSA BINARY TREE TEST HARNESS === ")
    bt = DSABinarySearchTree()

    while True:
        print(
            " === DSA Binary Search Tree === "
        )
        
        userInput = input(": ")
        if userInput == 'h':
            print(
                "isEmpty\nfind\ninsert\ndelete\ndisplay\nheight\nmin\nmax\nsave\nload\nbalance"
            )
    
        if userInput == "isEmpty":
            print(bt.isEmpty())
        elif userInput == "find":
            print(bt.find(int(input("key: "))))
        elif userInput == 'insert':
            bt.insert(int(input("Key (int): ")), input("value: "))
        elif userInput == 'delete':
            bt.delete(int(input("key (int): ")))
        elif userInput == 'display':
            displayType = input("postorder, inorder, preorder: ")
            if displayType == "postorder":
                bt.printPostorder()
            elif displayType == "inorder":
                bt.printInorder()
            elif displayType == 'preorder':
                bt.printPreorder
            else:
                print("please enter a valid option")
        elif userInput == 'height':
            print(bt.height())
        elif userInput == 'min':
            print(bt.min())
        elif userInput == 'max':
            print(bt.max())
        elif userInput == 'save':
            bt.saveTree(input("filename without extension: "))
        elif userInput == 'load':
            try:
                bt = bt.loadTree(input("filename wihtout extension: "))
            except FileNotFoundError:
                print(f"Error file not found")
        elif userInput == 'balance':
            bt.balance()

def binaryTreeTest():
    print("\n=== RUNNING QUICK BINARY TREE TEST ===")
    bt = DSABinarySearchTree()
    print("checking isEmpty()")
    print(f"isEmpty(): {bt.isEmpty()}\n")
    print("inserting new nodes")
    bt.insert(50, "test1")
    bt.insert(25, "test2")
    bt.insert(70, "test3")
    bt.insert(30, "newNode")
    print("done\n")
    print("checking root")
    print(bt.root)
    print("\ntesting find()")
    print(bt.find(50))
    print(bt.find(25))
    print(bt.find(70))
    print("\nchecking height()")
    print(bt.height())
    print("\ntesting min()")
    print(bt.min())
    print("\ntesting max()")
    print(bt.max())
    print("\ntesting print functions")
    print("---inOrder---")
    bt.printInorder()
    print("---preOrder---")
    bt.printPreorder()
    print("---PostOrder---")
    bt.printPostorder()
    print("\ndeleting nodes")
    bt.delete(25)
    print(bt.root.getLeft())
    print("\nbalance")
    bt.insert(100, "righ")
    print(bt.balance())
    
if __name__ == "__main__":
    main()