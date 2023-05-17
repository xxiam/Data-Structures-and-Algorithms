from DSAp3 import *
def main():

    def circularTest():
        circ = circularQueue()
        while True:
            try:
                metholdList = [q for q in dir(circularQueue) if callable(getattr(circularQueue, q)) and not q.startswith("__")]
                print('\n')
                for i,v in enumerate(metholdList):
                    print(f"{i} : {v}")
                print('111: display')

                choice = int(input('~$ '))

                if choice == 111:
                    print(circ.arr)
                if choice == 0:
                    print(circ.dequeue())
                if choice == 1:
                    circ.enqueue(input("value: "))
                if choice == 2:
                    print(circ.getCount())
                if choice == 3:
                    print(circ.isEmpty())
                if choice == 4:
                    print(circ.isFull())
            except QueueOverflowError as e:
                print(e)
            except EmptyQueueError as e:
                print(e)

    def shufflingTest():
        shuffle = shufflingQueue()
        while True:
            try:
                metholdList = [q for q in dir(shufflingQueue) if callable(getattr(shufflingQueue, q)) and not q.startswith("__")]
                print('\n')
                for i,v in enumerate(metholdList):
                    print(f"{i} : {v}")
                print('111: display')

                choice = int(input("~$ "))

                if choice == 111:
                    print(shuffle.arr)
                if choice == 0:
                    print(shuffle.dequeue())
                if choice == 1:
                    shuffle.enqueue(input("val: "))
                if choice == 2:
                    print(shuffle.getCount())
                if choice == 3:
                    print(shuffle.isEmpty())
                if choice == 4:
                    print(shuffle.isFull())
            except QueueOverflowError as e:
                print(e)
            except EmptyQueueError as e:
                print(e)

    def stackTest():
        stack = DSAstack()
        while True:
            try:
                methodList = [stack for stack in dir(DSAstack) if callable(getattr(DSAstack, stack)) and not stack.startswith("__")]
                print('\n')
                for i,v in enumerate(methodList):
                    print(f"{i} : {v}")
                print("111 : display")

                choice = int(input("~$ "))

                if choice == 0:
                    print(stack.Spop())
                if choice == 1:
                    print(stack.getCount())
                if choice == 2:
                    print(stack.isFull())
                if choice == 3:
                    print(stack.isFull())
                if choice == 4:
                    print(stack.push(input("val: ")))
                if choice == 5:
                    print(stack.top())
                if choice == 111:
                    print(stack.arr)
            except StackOverflowError as e:
                print(e)
            except EmptyStackError as e:
                print(e)

    print(
        " 0 : circularTest\n",
        "1 : shufflingTest\n",
        "2 : stackTest\n"
    )

    choice = int(input("~$ "))

    if choice == 0:
        circularTest()
    if choice == 1:
        shufflingTest()
    if choice == 2: 
        stackTest()

if __name__ == '__main__':
    main()