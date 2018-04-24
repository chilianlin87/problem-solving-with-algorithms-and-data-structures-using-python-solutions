# -*- coding: utf-8 -*-
from Node import Node
class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext()) 
                
    def search(self, item):
        count = 0
        found = False
        current = self.head
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                count = count + 1
                current = current.getNext()
        return [found, count]
    def update(self, olditem, newitem):
        current = self.head
        found = False
        while not found:
            if current.getData() == olditem:
                found = True
            else:
                current = current.getNext()
        current.setData(newitem)
    def __repr__(self):
        items = []
        current = self.head
        while current != None:
            items.append(current.getData())
            current = current.getNext()
        return(str(items))
    __str__ = __repr__
    
    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = temp
            temp.setNext(None)
        else:
            previous.setNext(temp)
            temp.setNext(None)
     
if __name__=='__main__':    
    mylist = UnorderedList()
    
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist)
    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
    
    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())
    print(mylist)
    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))
    print(mylist)
    mylist.update(26, 36)
    print(mylist)

    mylist = UnorderedList()
    
    mylist.append(31)
    mylist.append(77)
    mylist.append(17)
    mylist.append(93)
    mylist.append(26)
    mylist.add(54)
    print(mylist)
    

