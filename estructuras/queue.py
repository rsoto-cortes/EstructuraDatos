from estructuras.lineales.nodo import Node

class Queue(object):
    def __init__(self):
        self.first=None
        self.last=None
    
    def is_empty(self):
        return self.first == None  
    
    
    def enqueue(self,data):
        new_node =Node(data) 
        
        if self.first:
            self.last.next=new_node
            self.last=new_node
        else:
            self.first=new_node
            self.last=new_node
    
    def dequeue(self):
        temp= self.first
        if self.is_empty():
            return None
        
        elif self.first != self.last:
            self.first=self.first.next
        else:
            self.first= None
            self.last=None

        
    def firstQueue(self):
        if self.is_empty():
            return None
        elif self.first != None:
            return self.first.data
        
    def lastQueue(self):
        if self.is_empty():
            return None
        elif self.last != None:
            return self.last.data
    
    def printQueue(self):
        temp = self.first
        print("First -> ", end="")
        while temp is not None:
            print(temp.data,"->", end="")
            temp = temp.next
        print("<- Last")