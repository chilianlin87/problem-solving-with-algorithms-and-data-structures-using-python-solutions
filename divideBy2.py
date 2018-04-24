# -*- coding: utf-8 -*-

from Stack import Stack
def divideBy2(decNumber):
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
        
    binString = ''
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    
    return binString
    
if __name__ == '__main__':
    print(divideBy2(42))
    print(divideBy2(233))

