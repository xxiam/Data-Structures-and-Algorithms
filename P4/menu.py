from headTailLinkedList import *
import os


def main():
    ll = DSALinkedList()
    currentNode = None
    previousNode = None
    nextNode = None

    while True:
        try:
            previousNode = currentNode.getPrevious()
            nextNode = currentNode.getNext()
        except:
            pass

        os.system("clear")
        linkedIter = iter(ll)
        print(
    """
     _ _       _            _ _     _     _
    | (_)_ __ | | _____  __| | |   (_)___| |_   _ __  _   _
    | | | '_ \| |/ / _ \/ _` | |   | / __| __| | '_ \| | | |
    | | | | | |   <  __/ (_| | |___| \__ \ |_ _| |_) | |_| |
    |_|_|_| |_|_|\_\___|\__,_|_____|_|___/\__(_) .__/ \__, |
                                               |_|    |___/
        """
        )
        try:
            print(f"Current node: {currentNode.getValue()}")
            print(f"Previous node: {previousNode.getValue()}")
            print(f"Next node: {nextNode.getValue()}")
            print()
        except:
            pass

        print("1 : insertFirst") #insertFirst
        print("2 : insertLast") #insertLast
        print("3 : removeFirst")
        print("4 : removeLast")
        print("5 : peekFirst")
        print("6 : peekLast")
        print("9 : show all nodes")
        print("98 : save to .npy file")
        print("99 : load .npy file")

        choice = int(input("~$: "))

        if choice == 1:
            currentNode = ll.insertFirst(input("value: "))

        if choice == 2:
            currentNode = ll.insertLast(input("value: "))

        if choice == 3:
            remNode = ll.removeFirst()
            if currentNode == remNode:
                currentNode = currentNode.getNext()
            print(f"removed {remNode}")

        if choice == 4:
            remNode = ll.removeLast()
            if currentNode == remNode:
                currentNode = currentNode.getPrev()
        if choice == 5:
            print(ll.peekFirst())

        if choice == 6:
            print(ll.peekLast())
 
        if choice == 9:
            for i,v in enumerate(linkedIter):
                print(f"{i} : {v}")
            input("press any key to continue")

        if choice == 98:
            ll.savePickle(input("filename (without extension): "))

        if choice == 99:
            file = input("filename (without extension): ")
            ll = ll.loadPickle(file)
            print(f"{file}.pickle is loaded")
            os.system("sleep 2")

            
if __name__ == "__main__":
    main()