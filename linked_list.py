class Node:
    def __init__(self,data):
        self.data=data
        self.ref =None

class Linked_list:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("it is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

LL1 =  Linked_list()
LL1.print_LL()               
