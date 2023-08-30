stack= []

stack.append(1) 
stack.append(2)
stack.append(3)
 

additional_stack =[]

while len(stack)>0:
    additional_stack.append(stack.pop())
# stack = additional_stack   

# top_element = stack.pop()
# print(top_element)
print(additional_stack)