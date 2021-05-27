#/usr/bin/env python3

class Element(object):
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, size):
        self.size = size
        self.head = None
        self.hits = 0
        self.miss = 0
        self.evic = 0

    def appendLeft(self, key, value, miss=True):
        if len(self.getKeys()) >= self.size:
            self.popLastElement()
        element = Element(key, value, self.head)
        self.head = element
        if miss:
            self.miss += 1

    def popLastElement(self):
        if self.head == None:
            return
        if self.head.next == None:
            return    
        itr = self.head
        while itr:
            if itr.next == None:
                break
            curr = itr
            itr = itr.next
        curr.next = None
        self.evic += 1

    def popElement(self, key):
        if self.head != None:
            if key == self.head.key:
                self.head = self.head.next
            else:    
                itr = self.head
                while itr:
                    if itr.key == key:
                        break
                    curr = itr
                    itr = itr.next
                curr.next = itr.next
        else:
            return self.head    

    def getElement(self, key):
        if key not in self.getKeys():
            factorial = self.factorial(key)
            self.appendLeft(key, factorial)
            
            return factorial
        else:
            self.hits += 1
            itr = self.head                
            while itr:
                if itr.key == key:
                    self.popElement(key)
                    self.appendLeft(key, itr.value, miss=False)
                    return itr.value
                itr = itr.next

    def getKeys(self):
        elements = []
        itr = self.head
        while itr:
            elements.append(itr.key)
            itr = itr.next
        return elements

    def getValues(self):
        elements = []
        itr = self.head
        while itr:
            elements.append(itr.value)
            itr = itr.next
        return elements

    def factorial(self, element):
        res = 1
        for i in range(2, element + 1):
            res *= i
        return res

    def printElements(self):
        elements = self.getValues()
        
        print("\n### Cache status:\n")
        print("Cache hits: %s" % self.hits)
        print("Cache miss: %s" % self.miss)
        print("Cache evic: %s" % self.evic)
        print("\nCache stack\n")
        for element in elements:
            print("-> " + str(element))
