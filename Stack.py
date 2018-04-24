# -*- coding: utf-8 -*-

class Stack(object):
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     def __repr__(self):
         return(','.join(self.items))
     __str__ = __repr__
    
