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
#         data = self.head.data
#         self.head = self.head.ref
#         return data                               

#     def reverse(self):
#         new_stack =Stack()
#         while self.head is not None:
#             data = self.pop()
#             new_stack.push(data)
#         self.head = new_stack.head       

# ss = Stack()
# ss.push(1)
# ss.push(2)         
# ss.push(3)         
# ss.push(4)   
# ss.pop()
# ss.reverse()
# ss.print()


# stack = [1,2,3,4,5,6]
# new_stack =[]
# for i in range(len(stack)):
#     new_stack.append(stack.pop())
# print(new_stack)  

# def update_stack(stack):
#     element = int(input("enter the number you want to update"))
#     data = int(input("enter new value"))
#     for i in range(len(stack)):
#         if stack[i]==element:
#             stack[i] = data
# stack = [1,2,3,4,5,6,7]
# update_stack(stack)
# print(stack)    

# def rmove_mid(stack):
#     mid = len(stack)//2
#     new_stack = []

#     for i in range(mid):
#         element = stack.pop()
#         new_stack.append(element)

#     # num = int(input("enter number"))
#     stack.pop(mid-1)

#     for i in range(len(new_stack)):
#         stack.append(new_stack.pop())   

# stack = [1,2,3,4,5,6,7,8]

# rmove_mid(stack)
# print(stack)


# def update_mid(stack):
#     mid  =len(stack)//2

 
#     new_value = int(input("enter new_value"))
#     if len(stack) %2 ==1:
#         stack[mid] = new_value
#     else:
#         stack[mid+1] = new_value

# stack = [1,2,3,4,5,6,7]
# update_mid(stack)
# print(stack)      



# stack = [1,2,3,4,5,6]
# queue = []

# for i in range(len(stack)):
#     e = stack.pop()
#     queue.insert(0,e)
# queue.insert(0,10) 
# queue.pop()   

# print(queue)    
def insertionsort(list1):    
  for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
      if list1[i]>list1[j]:
         list1[i],list1[j] = list1[j],list1[i]
list1 = [1,7,4,9,3,10,6]
insertionsort(list1)  
print(list1)       


