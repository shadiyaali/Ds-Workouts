class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_list:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("it is empty")
        else:
            n =self.head
            while n is not None:
                print(n.data)
                n = n.ref                 
    

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n= self.head
            while n.ref is not None:
                n= n.ref
            n.ref = new_node    

    def update_list(self,data,x):
        n = self.head
        while n is not None:
            if n.data==x:
                n.data=data      

    def delete_start(self):
        if self.head is None:
            print("empty")
        else:
            self.head = self.head.ref                  


LL1 = Linked_list()
LL1.add_begin(100)
LL1.add_end(500)
 
LL1.print_LL()     



        