class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4) 
s.push(5)
s.pop() 
  
print(s.items)         