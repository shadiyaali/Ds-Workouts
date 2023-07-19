class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_Queue(self):
        n = self.head
        while n is not None:
            print(n.data)
            n=n.ref

    def enqueue(self,data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.ref = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            self.head = n.ref
            if not self.head:
                self.tail = None
                return n.data    

QQ =  Queue()
QQ.enqueue(1)
QQ.enqueue(2)
QQ.enqueue(3)
QQ.dequeue()


QQ.print_Queue()                                    