# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# new_stack = []
# while len(stack) >0:
#     new_stack.append(stack.pop())

    

# print(new_stack)


# class Node:
#     def __init__(self,data):
#         self.data = data
         
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def print_stack(self):
#         if self.head is None:
#             print("empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref  


#     def push(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

#     def pop(self):
#         if self.head is None:
#             return None
#         else:
#             data = self.head.data
#             self.head = self.head.ref 
#             return data

       
#     def reverse(self):
#         new_stack = Stack()
#         while self.head is not None:
#             data = self.pop()
#             new_stack.push(data)
#         self.head = new_stack.head


# ss = Stack()
# ss.push(1)
# ss.push(2)
# ss.push(3)
# ss.push(4)
# ss.push(5)
# ss.pop()
# ss.reverse()

# ss.print_stack()

         
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
# ss = Stack()
# ss.push(12)
# ss.push(22)
# print(ss.items)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None
# class Stack:
#     def __init__(self):
#         self.head = None
#     def print(self):
#         if self.head is None:
#             print("empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def push(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
#     def pop(self):
#         if self.head is None:
#             return None 
#         else:
#             data = self.head.data
#             self.head = self.head.ref
#             return data                               

     
#     def reverse(self):
#         new_stack = Stack()
#         while self.head is not None:
#             data = self.pop()
#             new_stack.push(data)
#         self.head = new_stack.head

# ss = Stack()
# ss.push(1)
# ss.push(2)
# ss.push(3)
# ss.pop()
# ss.reverse()
# ss.print()

# def update(stack, index, new_value):
#     new_stack = []

#     for i in range(index):
#         new_stack.append(stack.pop())

#     stack.pop()
#     stack.append(new_value)

#     while len(new_stack) > 0:
#         stack.append(new_stack.pop())  

# stack = [1, 2, 3, 4]
# update(stack, 2, 10)
# print(stack)          



# def update(stack,old,new):
#      element = old
#      data = new
#      for i in range(len(stack)):
#           if stack[i] == element:
#              stack[i] = data
               
# stack = [1,2,3,4,5,6]
# update(stack, 3,10)
# print(stack)               



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class Stack:
#     def __init__(self):
#         self.head = None

#     def push(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
#     def pop(self):
#         if self.head is  None:
#             return None
        
#         data = self.head.data
#         self.head = self.head.ref
#         return data 
#     def print(self):
#         if self.head is None:
#             print("empyt")
#         else:                                   
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def reverse(self):
#         new_stack  = Stack()
#         while self.head is not None:
#             data = self.pop()
#             new_stack.push(data)
#             self.head = new_stack.head
                        
# ss = Stack()
# ss.push(1)
# ss.push(2)
# ss.push(3)
# ss.push(4)
# ss.pop()
# ss.reverse()
# ss.print()       

# def update_element(stack):
#     element = int(input("enter the number want to update"))
#     data = int(input("enter new element"))

#     for i in range(len(stack)):
#           if stack[i] == element:
#              stack[i] = data 
# stack = [1,2,3,4,5,6,7]
# update_element(stack)
# print(stack)            


# stack = [1,2,3,4,2,3,4,5,6]
# # result = list(set(stack))
# # print(result)

# result = []
# for i in stack:
#     if i not in result:
#         result.append(i)
    
# print(result)      


class Queue:
    def __init__(self):
        self.items = []
    def engueue(self,item):
        self.items.append(item) 
    def dequeue(self):
        return self.items.pop(0)
    
            
qq = Queue()
qq.engueue(1)
qq.engueue(2)
qq.engueue(3)
qq.dequeue()

print(qq.items)



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def print_queue(self):
#         if self.head is None:
#             print("empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def enqueue(self,data):
#         new_node = Node(data)
#         if self.tail is not None:
#             self.tail.ref = new_node
#         else:
#             self.head = new_node    
#         self.tail = new_node

#     def dequeue(self):
#         if self.head is None:
#             return None
#         else:
#             n = self.head
#             self.head = n.ref
#             if not self.head:
#                 self.tail = None
#             return n.data

# qq = Queue()
# qq.enqueue(1)
# qq.enqueue(2)
# qq.enqueue(3)
# qq.dequeue()
# qq.dequeue()

# qq.print_queue() 

# class Hashtable:
#     def __init__(self):
#         self.table ={}

#     def insert(self,key,value):
#         if key in self.table:
#            self.table[key].append(value)
#         else:
#             self.table[key] = [value]   
#     def delete(self,key):
#         if key in self.table:
#             del self.table[key]
#     def get(self,key):
#         if key in self.table:
#             return self.table[key]

# hh = Hashtable()
# hh.insert("1","apple")
# hh.insert("1","orange")
# hh.insert("2","mango")    
# print(hh.get("1"))                    


 



          


                                    

