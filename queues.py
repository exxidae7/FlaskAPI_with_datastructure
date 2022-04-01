class Node:
    def __init__(self , data, next_node):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.items = []
        self.head =None
        self.tail = None
        
    def enqueue(self ,data):
        if self.head is None and self.tail is None:
            self.tail = self.head = Node(data , None)
            return 
        
        self.tail.next_node =Node(data , None) 
        self.tail = self.tail.next_node
        self.items.append(self.tail)
    
    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed
    def print(self):
        for e in self.items:
            return(e)

q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print()