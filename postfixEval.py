# -*- coding: utf-8 -*-

from Stack import Stack

def postfixEval(postfixExp):
    postfixList = postfixExp.split()
    value = Stack()
    
    for operator in postfixList:
        if operator in '0123456789':
            value.push(int(operator))
        else:
            operand2 = value.pop()
            operand1 = value.pop()
            result = doMath(operator, operand1, operand2)
            value.push(result)
            
    return value.pop()
            
def doMath(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    else:
        return operand1 / operand2

if __name__ == '__main__':
    print(postfixEval('7 8 + 3 2 + /'))
    print(postfixEval('3 5 * 6 8 * +'))
    print(postfixEval('3 5 + 6 * 8 5 - 8 2 + * -'))
