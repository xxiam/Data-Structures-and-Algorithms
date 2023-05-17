import DSAp3
import os
'''
Take a string representaing a mathematical equation in infix form and solve it by converting it into postfix and thene evaluating the postfix
'''

class StringInputError(Exception):
    pass    

def solve(equation):
    #error checking
    temp = equation.split()
    for item in temp:
        if item.isalpha() is True:
            raise StringInputError("error: string input recognised")
    #should call parseInfixoPostfix and evaluatePostfix

    parsePostfix = _parseInfixToPostfix(equation).split()
    print("infix equation:\n" + equation)
    print("postfix equation: ")
    for i in parsePostfix:
        print(i, end = ' | ')
    print('')
    postfixQueue = DSAp3.shufflingQueue()
    for i in range(len(parsePostfix)):
        postfixQueue.enqueue(parsePostfix[i])
    print("answer: ")
    print(_evalulatePostfix(postfixQueue))

def _parseInfixToPostfix(equation):
    '''
    Converts infix form equation into postfix.
    Stores the postfix terms into a queue as Objects
    Use Doubles for operands and Characters for operators, but put them all into the queue in postfix order

    Assume that the passed-in equation <equation> has spaces between all operator, operands and brackets, allowing .split() to work
    '''

    equationArr = equation.split()
    opStack = DSAp3.DSAstack()
    termQueue = DSAp3.shufflingQueue()

    #putting all the terms into the queue for parseNextTerm()
    for i in range(len(equationArr)):
        termQueue.enqueue(equationArr[i])

    def parseNextTerm(termQueue):
        '''
        uses DSAqueue to create a shuffling queue to return the next term in the infix equation
        '''
        retVal = termQueue.dequeue()
        return retVal

    postfix = ""

    while len(equationArr) >= len(postfix.split()):

        #exception handling
        try:
            term = parseNextTerm(termQueue) #parseNextTerm extracts the next term (operator or operand) from the infix equation
        except DSAp3.EmptyQueueError as e:
            break

        if term == '(':
            opStack.push('(') # ( gets put straight to the stack

        elif term == ')': 
            while opStack.top()!= '(': #finds the corresponding (
                postfix += opStack.Spop() + " "#remove the remaining operators for the bracketed sub-equation

            opStack.Spop() #discard the ( from the stack

        elif term == '+' or term == '-' or term == '*' or term == '/':
            while opStack.isEmpty() is False and opStack.top() != '(' and _precedenceOf(opStack.top()) >= _precedenceOf(term):
                postfix += opStack.Spop() + " "#move higher/equal precedence ops to postfix equation
            
            opStack.push(term) #always put the new operator onto the stack

        else:
            postfix = postfix + term + " "#term must be an operand if it isnt an operator and add to the postfix equation

    while opStack.isEmpty() is False: #pop the remaining operators from the stack
        if opStack.top() == '(':
            #just remove the (
            opStack.Spop()
        else:
            postfix = postfix + opStack.Spop() + " "

    return postfix

def _evalulatePostfix(postfixQueue):
    '''
    Takes the postfixQueue and evaluates it.
    uses _executeOperation
    '''

    evalStack = DSAp3.DSAstack()

    while postfixQueue.isEmpty() is not True:
        content = postfixQueue.dequeue()

        if content == '+' or content == '-' or content == '*' or content == '/':
            op2, op1 = evalStack.Spop(), evalStack.Spop()

            evalStack.push(str(_executeOperation(content, float(op1), float(op2))))
        else:
            evalStack.push(content)
    
    return evalStack.Spop()

def _precedenceOf(theOp):
    '''
    Helper fuinction for parseInfixToPostfix()
    Returns the precedence (as an integer) of the Operator
    '''
    precedenceDict = {
        '(' : 3,
        ')' : 3,
        '*' : 2,
        '/' : 2,
        '-' : 1,
        '+' : 1
    }

    return precedenceDict[theOp]

def _executeOperation(op, op1, op2):
    '''
    helper function for evaluate Postfix()
    Exeutres the binary operation impied by op:
    '''

    if op == '+':
        ans = op1 + op2
    if op == '-':
        ans = op1 - op2
    if op == '*':
        ans = op1 * op2
    if op == '/':
        ans = op1 / op2

    return ans

def main():
    os.system("clear")
    try:
        solve(input("Please enter equation: "))
    except StringInputError as e:
        print(e)
if __name__ == "__main__":
    main()