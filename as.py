class Node:
    def __init__(self,data):
        self.data = data
        self.ref =None

class Linke_List:
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

    def add(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node                            