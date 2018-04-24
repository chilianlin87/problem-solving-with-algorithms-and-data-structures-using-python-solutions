# -*- coding: utf-8 -*-

from Deque import Deque
def palchecker(aString):
    chardeque = Deque()
    for char in aString:
        chardeque.addFront(char)
        
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeRear()
        last = chardeque.removeFront()
        if first != last:
            stillEqual = False
    return stillEqual
    
if __name__ == '__main__':
    print(palchecker('radar'))
    print(palchecker('abcdcba'))
    print(palchecker("lsdkjfskf"))
