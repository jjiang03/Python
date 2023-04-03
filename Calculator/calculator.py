# author: Justin Jiang
# date: March 2, 2023
# file: calculator.py a Python program converts infix expressions to postfix expressions and evaluates the expressions
# input: user expressions
# output: expression evaluation
from stack import Stack
from tree import ExpTree
# a function that converts infix expressions to postfix expressions
def infix_to_postfix(infix):
    print(infix)
    
    if " " in infix:
        infix = infix.replace(" ", "")
    # dictionary that stores the precedence of operators
    prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    postfix = ''
    opstack = Stack()
    token = []
    hold = ''
    count = len(infix)
    # a loop that converts infix expressions to a list
    for i in range(count):
        if (infix[0] not in '(+-*/^)'):
            hold += infix[0]
            infix = infix[1:]
            
        else:
            if (hold):
                token.append(hold)
            token.append(infix[0])
            infix = infix[1:]
            hold = ''
    token.append(hold)
    #converts infix expressions to postfix expressions
    for i in token:
        if (i == ''):
            break
        elif (i[0].isnumeric()):
            postfix += i + ' '
        elif (i == '('):
            opstack.push(i)
        elif (i == ')'):
            while (True):
                if (opstack.peek() == '('):
                    opstack.pop()
                    break
                postfix += opstack.pop() + ' '
        else:
            #compares the precedence of operators
            if (opstack.peek() == None) or (opstack.peek() == '('):
                    opstack.push(i)
            elif i in prec.keys():
                if (prec[i] > prec[opstack.peek()]):
                    opstack.push(i)
                else:
                    postfix += opstack.pop() + ' '
                    opstack.push(i)
    #adds the remaining operators to the postfix expression
    while (opstack.peek() != None):
        postfix += opstack.pop() + ' '
    print("p")
    print(postfix)
    return postfix[:-1]
def calculate(infix):
    input = infix_to_postfix(infix)
    tree = ExpTree.make_tree(input.split())
    return ExpTree.evaluate(tree)
if __name__ == '__main__':
    #test infix_to_postfix function
    
    
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    
   
    print('Welcome to Calculator Program!')
    while(True):
        ex = input('Please enter your expression here. To quit enter \'quit\' or \'q\':\n')
        if (ex == 'q' or ex == "q".upper()) or (ex == 'quit' or ex == 
"quit".upper()):
            print('Goodbye!')
            break
       
        print(calculate(ex))
 