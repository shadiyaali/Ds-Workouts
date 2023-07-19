class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class stack:
    def __init__(self):
        self.head = None

    def print_stack(self):
        if self.head is None:
            print("it is empty")
        else :
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def push(self,data):
        new_node =  Node(data)
        new_node.ref = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.ref
        return data   
  

SS = stack()
SS.push(1)
SS.push(2)
SS.push(3)
SS.pop()
 
SS.print_stack()



  
def reverse(self):
        
    new_stack = stack()
    while self.head is not None:
        data = self.pop()
        new_stack.push(data)
 
        self.head = new_stack.head