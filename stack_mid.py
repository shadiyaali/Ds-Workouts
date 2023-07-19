# def add_middle():
#     mid = len(stack)//2
    
#     for i in range(mid):
#         e = stack.pop()
#         new_stack.append(e)
    
#     num = int(input("Enter the number you want to insert :"))
#     stack.append(num)
    
#     for i in range(len(new_stack)):
#         stack.append(new_stack[i])
        
#     print(stack)

# stack = [1,2,3,34,5,6,7,84]
# new_stack=[]  
# add_middle()
# print(new_stack)  


# def add_middle(stack):
#     new_stack = []
#     mid = len(stack) //2

#     for i in range(mid):
#         element = stack.pop()
#         new_stack.append(element)

#     num = int(input("enter the num"))
#     stack.append(num)

#     for i in range(len(new_stack)):
#         stack.append(new_stack[i])
         
           
# stack = [1,2,3,5,7,3,4]
# add_middle(stack)
# print(stack)
        

# def update(stack):
#     element = int(input("enter the elemnet you want to update")) 
#     data = int(input("enter new value"))     

#     for i in range(len(stack)):
#         if stack[i] == element:
#             stack[i] = data

# stack = [1,2,3,4,5,6,7,8]
# update(stack)
# print(stack)        


class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
                          