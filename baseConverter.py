# -*- coding: utf-8 -*-

from Stack import Stack

def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
        
    baseString = ''
    while not remstack.isEmpty():
        baseString = baseString + digits[remstack.pop()]
    
    return baseString
    
if __name__ == '__main__':
    print(baseConverter(25, 8))
    print(baseConverter(256, 16))
    print(baseConverter(26, 26))
    print(baseConverter(233, 16))
        

